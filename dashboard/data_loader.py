"""
data_loader.py
==============
Data ingestion and validation layer for the Friction-Compliance Explorer.

This module handles loading all four data sources:
  1. Core 30-week friction/compliance index dataset (CSV)
  2. Historical backfill 2017-2024 event pairs (CSV)
  3. Negative (non-response) windows (CSV)
  4. Federal Register Executive Order spider output (JSON)

All load functions are cached with @st.cache_data so each file is read
exactly once per Streamlit session, regardless of reruns.

IMPORTANT: See Section 1 below for file path configuration.
"""

import json
from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


# =========================================================================
# =========================================================================
#
#   ██████╗  █████╗ ████████╗██╗  ██╗    ███████╗███████╗████████╗██╗   ██╗██████╗
#   ██╔══██╗██╔══██╗╚══██╔══╝██║  ██║    ██╔════╝██╔════╝╚══██╔══╝██║   ██║██╔══██╗
#   ██████╔╝███████║   ██║   ███████║    ███████╗█████╗     ██║   ██║   ██║██████╔╝
#   ██╔═══╝ ██╔══██║   ██║   ██╔══██║    ╚════██║██╔══╝     ██║   ██║   ██║██╔═══╝
#   ██║     ██║  ██║   ██║   ██║  ██║    ███████║███████╗   ██║   ╚██████╔╝██║
#   ╚═╝     ╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝    ╚══════╝╚══════╝   ╚═╝    ╚═════╝ ╚═╝
#
# =========================================================================
#  SECTION 1: FILE PATH CONFIGURATION
# =========================================================================
#
#  HOW THIS WORKS:
#  ---------------
#  By default, this file auto-resolves paths relative to the repository
#  root. The dashboard/ folder sits one level below the repo root, so:
#
#       REPO_ROOT = <parent of the directory containing this file>
#
#  If you cloned the repo with its standard structure, everything will
#  work automatically. But if you moved your CSV/JSON files to a
#  different location, you MUST update the four paths below.
#
#
#  ┌─────────────────────────────────────────────────────────────────────┐
#  │                                                                     │
#  │   TO USE CUSTOM FILE PATHS:                                         │
#  │                                                                     │
#  │   1. Comment out the REPO_ROOT line below                           │
#  │   2. Replace each _XXXX_CSV / _EO_JSON path with your              │
#  │      absolute local path (e.g., Path("/home/user/data/file.csv"))   │
#  │                                                                     │
#  │   EXAMPLE:                                                          │
#  │     _CORE_CSV = Path("/Users/yourname/Desktop/data/master.csv")     │
#  │     _BACKFILL_CSV = Path("/Users/yourname/Desktop/data/backfill.csv")│
#  │                                                                     │
#  └─────────────────────────────────────────────────────────────────────┘
#
# =========================================================================

# ── Auto-resolved repo root (works if you kept the standard repo structure) ──
REPO_ROOT = Path(__file__).resolve().parent.parent

# =========================================================================
# FILE 1: CORE 30-WEEK DATASET
# =========================================================================
# Source: Control_Proof/master_reflexive_correlation_data.csv
# Schema: Week_Index, Epstein_Friction_Index, Institutional_Compliance_Index, Correlation_Note
# Rows:   30 (one per week)
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>  INSERT YOUR LOCAL PATH HERE IF NOT USING STANDARD REPO LAYOUT  <<<
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
_CORE_CSV = REPO_ROOT / "Control_Proof" / "master_reflexive_correlation_data.csv"


# =========================================================================
# FILE 2: HISTORICAL BACKFILL (2017-2024)
# =========================================================================
# Source: Run_Correlations_Yourself/historical_backfill_2017_2024.csv
# Schema: Year, Friction_Event, Friction_Date, Compliance_Event, Compliance_Date, Lag_Days, Source_URL
# Rows:   66 event pairs
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>  INSERT YOUR LOCAL PATH HERE IF NOT USING STANDARD REPO LAYOUT  <<<
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
_BACKFILL_CSV = REPO_ROOT / "Run_Correlations_Yourself" / "historical_backfill_2017_2024.csv"


# =========================================================================
# FILE 3: NEGATIVE WINDOWS (5 NON-RESPONSE EVENTS)
# =========================================================================
# Source: Run_Correlations_Yourself/negative_windows.csv
# Schema: Year, Friction_Event, Friction_Date, Window_Start, Window_End, Notes
# Rows:   5 (friction events with no compliance response within 14 days)
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>  INSERT YOUR LOCAL PATH HERE IF NOT USING STANDARD REPO LAYOUT  <<<
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
_NEGATIVE_CSV = REPO_ROOT / "Run_Correlations_Yourself" / "negative_windows.csv"


# =========================================================================
# FILE 4: FEDERAL REGISTER EO SPIDER OUTPUT (JSON)
# =========================================================================
# Source: federal_register/Spider Output Files/items_federal_register_eo_1.json
# Schema: Array of objects with Title, Date, Document_Number, URL (+ spider metadata)
# Generated by: federal_register/spiders/federal_register_eo.py (Scrapy/Zyte)
#
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# >>>  INSERT YOUR LOCAL PATH HERE IF NOT USING STANDARD REPO LAYOUT  <<<
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
_EO_JSON = REPO_ROOT / "federal_register" / "Spider Output Files" / "items_federal_register_eo_1.json"


# =========================================================================
# =========================================================================
#  END OF PATH CONFIGURATION — Do not modify anything below this line
#  unless you are changing the data loading logic itself.
# =========================================================================
# =========================================================================


# ── Helper: parse Lag_Days values ────────────────────────────────────────
def _parse_lag(val) -> int | float:
    """Parse Lag_Days values like '+3', '-2', '0' into integers.

    The backfill CSV stores lag days as strings with optional '+' prefix.
    This function strips whitespace and the '+' sign, then converts to int.
    Returns np.nan for unparseable values.
    """
    try:
        return int(str(val).strip().replace("+", ""))
    except (ValueError, TypeError):
        return np.nan


# =========================================================================
#  LOADER 1A: Core 30-Week Dataset
# =========================================================================
@st.cache_data
def load_core_dataset() -> pd.DataFrame | None:
    """Load and validate the 30-observation friction/compliance index dataset.

    This is the primary dataset for computing the core Pearson r = 0.6196.
    Each row represents one week with a friction index (1-10) and a
    compliance index (1-10), pre-aligned with a 2-week lag.

    Returns
    -------
    pd.DataFrame or None
        DataFrame with columns: Week_Index, Epstein_Friction_Index,
        Institutional_Compliance_Index, Correlation_Note.
        Returns None if the file is missing or schema validation fails.
    """
    if not _CORE_CSV.exists():
        st.error(
            f"**Core dataset not found.**\n\n"
            f"Expected path: `{_CORE_CSV}`\n\n"
            f"Open `data_loader.py` and update the `_CORE_CSV` path variable "
            f"in Section 1 (line ~80) to point to your local copy of "
            f"`master_reflexive_correlation_data.csv`."
        )
        return None

    df = pd.read_csv(_CORE_CSV)

    # ── Schema validation ──
    expected_cols = {"Week_Index", "Epstein_Friction_Index", "Institutional_Compliance_Index"}
    if not expected_cols.issubset(df.columns):
        st.error(
            f"Core dataset schema mismatch.\n\n"
            f"Expected columns: {sorted(expected_cols)}\n\n"
            f"Found columns: {sorted(df.columns.tolist())}"
        )
        return None

    # ── Row count validation ──
    if len(df) != 30:
        st.warning(
            f"Core dataset has {len(df)} rows (expected 30). "
            f"Statistical outputs may differ from published values."
        )

    # ── Range validation (indices should be 1-10) ──
    for col in ["Epstein_Friction_Index", "Institutional_Compliance_Index"]:
        if not df[col].between(1, 10).all():
            st.warning(
                f"Core dataset: `{col}` contains values outside the 1-10 range. "
                f"Range found: [{df[col].min()}, {df[col].max()}]"
            )

    return df


# =========================================================================
#  LOADER 1B: Historical Backfill (2017-2024)
# =========================================================================
@st.cache_data
def load_backfill() -> pd.DataFrame | None:
    """Load and validate the 66-pair historical backfill dataset.

    Each row is a friction-event → compliance-event pair with the observed
    lag in days. Dates are parsed to datetime; Lag_Days is parsed from
    string (e.g., '+3') to integer and stored in a new 'lag_parsed' column.

    Returns
    -------
    pd.DataFrame or None
        DataFrame with original columns plus 'lag_parsed' (int).
        Returns None if the file is missing.
    """
    if not _BACKFILL_CSV.exists():
        st.error(
            f"**Backfill dataset not found.**\n\n"
            f"Expected path: `{_BACKFILL_CSV}`\n\n"
            f"Open `data_loader.py` and update the `_BACKFILL_CSV` path variable "
            f"in Section 1 (line ~93) to point to your local copy of "
            f"`historical_backfill_2017_2024.csv`."
        )
        return None

    df = pd.read_csv(_BACKFILL_CSV)

    # ── Parse date columns ──
    df["Friction_Date"] = pd.to_datetime(df["Friction_Date"], errors="coerce")
    df["Compliance_Date"] = pd.to_datetime(df["Compliance_Date"], errors="coerce")

    # ── Parse lag days from string to integer ──
    df["lag_parsed"] = df["Lag_Days"].apply(_parse_lag)

    n_bad = df["lag_parsed"].isna().sum()
    if n_bad > 0:
        st.warning(
            f"Backfill: {n_bad} row(s) with unparseable Lag_Days values. "
            f"These rows will be excluded from lag distribution analysis."
        )

    return df


# =========================================================================
#  LOADER 1C: Negative Windows (5 Non-Response Events)
# =========================================================================
@st.cache_data
def load_negative_windows() -> pd.DataFrame | None:
    """Load and validate the 5 negative-window events.

    These are friction events where NO compliance response was found in
    the 14-day Federal Register search window. They are essential to the
    outlier framing strategy: 5 of 71 events (7%) is within expected
    variance for a model with r^2 = 0.384.

    Returns
    -------
    pd.DataFrame or None
        DataFrame with columns: Year, Friction_Event, Friction_Date,
        Window_Start, Window_End, Notes.
        Returns None if the file is missing.
    """
    if not _NEGATIVE_CSV.exists():
        st.error(
            f"**Negative windows file not found.**\n\n"
            f"Expected path: `{_NEGATIVE_CSV}`\n\n"
            f"Open `data_loader.py` and update the `_NEGATIVE_CSV` path variable "
            f"in Section 1 (line ~106) to point to your local copy of "
            f"`negative_windows.csv`."
        )
        return None

    df = pd.read_csv(_NEGATIVE_CSV)

    # ── Parse date columns ──
    for col in ["Friction_Date", "Window_Start", "Window_End"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce")

    # ── Row count validation ──
    if len(df) != 5:
        st.warning(
            f"Negative windows has {len(df)} rows (expected 5). "
            f"Outlier framing statistics will be recalculated accordingly."
        )

    return df


# =========================================================================
#  LOADER 1D: Federal Register EO Spider Output (JSON)
# =========================================================================
@st.cache_data
def load_eo_spider() -> pd.DataFrame | None:
    """Load Executive Orders from the Zyte/Scrapy spider JSON output.

    The JSON file is an array of objects scraped from the Federal Register.
    This loader extracts the relevant columns (Title, Date, Document_Number,
    URL), parses dates, and returns a sorted DataFrame (newest first).

    Returns
    -------
    pd.DataFrame or None
        DataFrame with available columns from [Title, Date, Document_Number, URL].
        Returns None if the file is missing.
    """
    if not _EO_JSON.exists():
        st.error(
            f"**EO spider JSON not found.**\n\n"
            f"Expected path: `{_EO_JSON}`\n\n"
            f"Open `data_loader.py` and update the `_EO_JSON` path variable "
            f"in Section 1 (line ~119) to point to your local copy of "
            f"`items_federal_register_eo_1.json`."
        )
        return None

    with open(_EO_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    df = pd.DataFrame(data)

    # ── Keep only the columns relevant to the dashboard ──
    keep_cols = ["Title", "Date", "Document_Number", "URL"]
    available = [c for c in keep_cols if c in df.columns]
    df = df[available]

    # ── Parse and sort by date (newest first) ──
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df = df.sort_values("Date", ascending=False).reset_index(drop=True)

    return df


# =========================================================================
#  CONVENIENCE: Load all datasets at once
# =========================================================================
def load_all_datasets() -> dict:
    """Load all four datasets and return them as a dictionary.

    This is a convenience wrapper for app.py to call once at startup.
    Individual datasets that fail to load will be None in the dict.

    Returns
    -------
    dict
        Keys: 'core', 'backfill', 'negative', 'eo'
        Values: pd.DataFrame or None
    """
    return {
        "core": load_core_dataset(),
        "backfill": load_backfill(),
        "negative": load_negative_windows(),
        "eo": load_eo_spider(),
    }
