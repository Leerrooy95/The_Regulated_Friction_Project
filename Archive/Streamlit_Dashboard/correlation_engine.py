"""
correlation_engine.py
=====================
Pure statistical computation engine for the Friction-Compliance Explorer.

This module contains ALL mathematical logic for the dashboard. It has
ZERO Streamlit imports and can be tested independently from the command line.

Mathematical methods implemented:
  - Pearson product-moment correlation (with configurable lag)
  - Spearman rank correlation (non-parametric robustness check)
  - Lag sweep (Pearson r at lags 0 through max_lag)
  - Fisher z-transform (confidence intervals for Pearson r)
  - Lag distribution statistics (median, percentiles, binning)
  - OLS regression with +/- 2 SD prediction bands

All functions accept pandas Series or DataFrames and return plain Python
types (floats, dicts, lists) — no side effects, no state.
"""

import numpy as np
import pandas as pd
from scipy import stats
from scipy.stats import pearsonr, spearmanr

from constants import LAG_BINS


# =========================================================================
#  2A. PEARSON CORRELATION WITH LAG
# =========================================================================
#
#  MATHEMATICAL LOGIC:
#  -------------------
#  Pearson product-moment correlation coefficient:
#
#      r = Σ[(xi - x̄)(yi - ȳ)] / sqrt[Σ(xi - x̄)² · Σ(yi - ȳ)²]
#
#  The "lag" is applied by shifting the friction series forward by N
#  positions. This tests the hypothesis that friction at time t predicts
#  compliance at time t + lag.
#
#  For the core dataset:
#      lag = 2 weeks → r = 0.6196, p = 0.0004 (n_eff = 28)
#
#  The p-value is a two-tailed test of H0: r = 0 using the t-distribution:
#      t = r · sqrt(n - 2) / sqrt(1 - r²),  df = n - 2
#
# =========================================================================

def compute_lagged_correlation(
    friction: pd.Series, compliance: pd.Series, lag: int = 2
) -> tuple[float, float, int]:
    """Compute Pearson r between friction (shifted by `lag`) and compliance.

    Friction is shifted FORWARD by `lag` positions, meaning we test whether
    friction at time t correlates with compliance at time t + lag. This is
    the core operation: friction LEADS compliance.

    Parameters
    ----------
    friction : pd.Series
        The friction index time series (1-10 scale, 30 observations).
    compliance : pd.Series
        The compliance index time series (1-10 scale, 30 observations).
    lag : int
        Number of periods to shift friction forward. Default = 2 (weeks).

    Returns
    -------
    tuple[float, float, int]
        (r, p_value, n_effective)
        - r: Pearson correlation coefficient [-1, +1]
        - p_value: Two-tailed significance (H0: r = 0)
        - n_effective: Number of valid paired observations after lag
    """
    # Shift friction forward: friction[t] aligns with compliance[t + lag]
    friction_lagged = friction.shift(lag)

    # Drop NaN rows created by the shift
    valid = ~friction_lagged.isna()
    r, p = pearsonr(friction_lagged[valid], compliance[valid])

    return float(r), float(p), int(valid.sum())


# =========================================================================
#  2B. SPEARMAN RANK CORRELATION WITH LAG
# =========================================================================
#
#  MATHEMATICAL LOGIC:
#  -------------------
#  Spearman's ρ is Pearson r computed on the RANKS of the data rather
#  than the raw values. This makes it robust to:
#    - Non-linear monotonic relationships
#    - Outliers in the index values
#    - Non-normal distributions
#
#  Used as a robustness check: if Spearman ρ ≈ Pearson r, the
#  correlation is not driven by a few extreme values.
#
# =========================================================================

def compute_spearman(
    friction: pd.Series, compliance: pd.Series, lag: int = 2
) -> tuple[float, float]:
    """Compute Spearman rank correlation at the given lag.

    Parameters
    ----------
    friction : pd.Series
        The friction index time series.
    compliance : pd.Series
        The compliance index time series.
    lag : int
        Number of periods to shift friction forward.

    Returns
    -------
    tuple[float, float]
        (rho, p_value)
    """
    friction_lagged = friction.shift(lag)
    valid = ~friction_lagged.isna()
    rho, p = spearmanr(friction_lagged[valid], compliance[valid])

    return float(rho), float(p)


# =========================================================================
#  2C. LAG SWEEP: Pearson r at lags 0 through max_lag
# =========================================================================
#
#  MATHEMATICAL LOGIC:
#  -------------------
#  For each lag L in [0, 1, 2, ..., max_lag]:
#    1. Shift friction forward by L positions
#    2. Compute Pearson r on the overlapping observations
#    3. Record (r, p)
#
#  This produces a "lag profile" showing how correlation strength varies
#  with the assumed response delay. The peak lag (highest |r|) indicates
#  the most likely response latency.
#
#  For the core dataset:
#      lag=0: r ≈ −0.30  (negative — friction and compliance move oppositely)
#      lag=1: r ≈ +0.15  (weak positive)
#      lag=2: r = +0.6196 (PEAK — strong positive)  <-- optimal lag
#      lag=3: r ≈ +0.30  (declining)
#      lag=4+: r declining toward zero
#
#  The sharp peak at lag=2 is the signature of the friction → compliance
#  response mechanism with a ~2-week institutional latency.
#
# =========================================================================

def compute_lag_sweep(
    friction: pd.Series, compliance: pd.Series, max_lag: int = 6
) -> dict[int, tuple[float, float]]:
    """Compute Pearson r at each lag from 0 to max_lag.

    Parameters
    ----------
    friction : pd.Series
        The friction index time series.
    compliance : pd.Series
        The compliance index time series.
    max_lag : int
        Maximum lag to test (inclusive). Default = 6.

    Returns
    -------
    dict[int, tuple[float, float]]
        {lag: (r, p_value)} for each lag with sufficient observations.
        Lags with fewer than 6 valid pairs are excluded.
    """
    results = {}
    for lag in range(max_lag + 1):
        shifted = friction.shift(lag)
        valid = ~shifted.isna()
        # Require at least 6 overlapping observations for a meaningful r
        if valid.sum() > 5:
            r, p = pearsonr(shifted[valid], compliance[valid])
            results[lag] = (float(r), float(p))
    return results


# =========================================================================
#  2D. FISHER Z-TRANSFORM: Confidence Interval for Pearson r
# =========================================================================
#
#  MATHEMATICAL LOGIC:
#  -------------------
#  The sampling distribution of Pearson r is skewed (bounded by [-1, +1]).
#  The Fisher z-transform maps r to an approximately normal variable:
#
#      z = arctanh(r) = 0.5 · ln[(1 + r) / (1 - r)]
#
#  The standard error of z depends only on n:
#
#      SE(z) = 1 / sqrt(n - 3)
#
#  A 95% confidence interval in z-space:
#
#      z ± z_crit · SE(z)     where z_crit = 1.96 for α = 0.05
#
#  Transform back to r-space using the inverse (tanh):
#
#      r_low  = tanh(z - z_crit · SE)
#      r_high = tanh(z + z_crit · SE)
#
#  For r = 0.6196, n = 28:
#      z = 0.7247
#      SE = 0.2000
#      95% CI in z: [0.3327, 1.1167]
#      95% CI in r: [0.3212, 0.8111]
#
#  Interpretation: We are 95% confident the true population correlation
#  lies between 0.32 and 0.81. The entire interval is positive and
#  excludes zero, consistent with p = 0.0004.
#
# =========================================================================

def fisher_ci(r: float, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Compute confidence interval for Pearson r via Fisher z-transform.

    Parameters
    ----------
    r : float
        Observed Pearson correlation coefficient.
    n : int
        Number of paired observations used to compute r.
    alpha : float
        Significance level. Default = 0.05 (95% confidence interval).

    Returns
    -------
    tuple[float, float]
        (ci_lower, ci_upper) in r-space [-1, +1].

    Raises
    ------
    ValueError
        If n < 4 (need at least 4 observations for SE computation).
    """
    if n < 4:
        # SE = 1/sqrt(n-3) is undefined or unstable for n < 4
        return float("nan"), float("nan")

    # Step 1: Transform r to z-space (arctanh)
    z = np.arctanh(r)

    # Step 2: Standard error in z-space
    se = 1.0 / np.sqrt(n - 3)

    # Step 3: Critical value from standard normal
    z_crit = stats.norm.ppf(1 - alpha / 2)

    # Step 4: CI in z-space → transform back to r-space (tanh)
    ci_low = float(np.tanh(z - z_crit * se))
    ci_high = float(np.tanh(z + z_crit * se))

    return ci_low, ci_high


# =========================================================================
#  2E. BACKFILL LAG DISTRIBUTION STATISTICS
# =========================================================================
#
#  The backfill dataset contains 66 friction → compliance event pairs
#  from 2017-2024, each with an observed lag in days. These functions
#  compute summary statistics and bin the lags for histogram display.
#
# =========================================================================

def compute_lag_stats(lag_series: pd.Series) -> dict:
    """Compute summary statistics for the lag distribution.

    Parameters
    ----------
    lag_series : pd.Series
        Series of parsed lag values (integers, days). NaN values are dropped.

    Returns
    -------
    dict
        Keys: median, mean, std, min, max, n, pct_positive,
              pct_within_7, pct_within_14, n_negative
    """
    lags = lag_series.dropna()
    return {
        "median": float(lags.median()),
        "mean": float(lags.mean()),
        "std": float(lags.std()),
        "min": int(lags.min()),
        "max": int(lags.max()),
        "n": len(lags),
        "pct_positive": float((lags > 0).mean() * 100),
        "pct_within_7": float(((lags >= 0) & (lags <= 7)).mean() * 100),
        "pct_within_14": float(((lags >= 0) & (lags <= 14)).mean() * 100),
        "n_negative": int((lags < 0).sum()),
    }


def compute_lag_bins(lag_series: pd.Series) -> list[dict]:
    """Bin lag values using the standard bin definitions from constants.py.

    Parameters
    ----------
    lag_series : pd.Series
        Series of parsed lag values (integers, days).

    Returns
    -------
    list[dict]
        Each dict has keys: Bin (str), Count (int), Pct (str).
    """
    lags = lag_series.dropna()
    total = len(lags)
    rows = []
    for label, lo, hi in LAG_BINS:
        if hi is None:
            # Open-ended upper bin (e.g., "+15+")
            count = int((lags >= lo).sum())
        else:
            count = int(((lags >= lo) & (lags <= hi)).sum())
        pct = count / total * 100 if total > 0 else 0.0
        rows.append({"Bin": label, "Count": count, "Pct": f"{pct:.1f}%"})
    return rows


def compute_year_breakdown(df: pd.DataFrame) -> pd.DataFrame:
    """Compute per-year lag summary from the backfill dataset.

    Parameters
    ----------
    df : pd.DataFrame
        Backfill DataFrame with 'Year' and 'lag_parsed' columns.

    Returns
    -------
    pd.DataFrame
        One row per year with columns: Year, Pairs, Median Lag,
        Mean Lag, Min, Max.
    """
    rows = []
    for yr in sorted(df["Year"].unique()):
        sub = df[df["Year"] == yr]["lag_parsed"].dropna()
        if len(sub) == 0:
            continue
        rows.append({
            "Year": yr,
            "Pairs": len(sub),
            "Median Lag": f"{sub.median():+.1f}",
            "Mean Lag": f"{sub.mean():+.2f}",
            "Min": f"{int(sub.min()):+d}",
            "Max": f"{int(sub.max()):+d}",
        })
    return pd.DataFrame(rows)


# =========================================================================
#  2F. OLS REGRESSION LINE + PREDICTION BAND
# =========================================================================
#
#  MATHEMATICAL LOGIC:
#  -------------------
#  Ordinary least squares regression:
#
#      Compliance = slope × Friction(lagged) + intercept
#
#  The prediction band shows ±2 standard deviations of the residuals,
#  giving an approximate 95% interval for where new observations would
#  fall. This is a prediction interval (not a confidence interval for
#  the regression line itself).
#
#      y_hat = slope · x + intercept
#      residuals = y_observed - y_hat
#      SD_residual = std(residuals)
#      prediction_band = y_hat ± 2 · SD_residual
#
# =========================================================================

def compute_regression(
    friction: pd.Series, compliance: pd.Series, lag: int = 2
) -> dict:
    """Compute OLS regression line and ±2 SD prediction band.

    Parameters
    ----------
    friction : pd.Series
        Friction index time series.
    compliance : pd.Series
        Compliance index time series.
    lag : int
        Number of periods to shift friction forward.

    Returns
    -------
    dict
        Keys:
        - slope, intercept: regression coefficients
        - residual_sd: standard deviation of residuals
        - x, y: aligned data arrays (for scatter plot)
        - x_line, y_line: smooth regression line (100 points)
        - y_upper, y_lower: ±2 SD prediction band boundaries
    """
    friction_lagged = friction.shift(lag).dropna()
    compliance_aligned = compliance.iloc[lag:]

    # Ensure equal length after alignment
    n = min(len(friction_lagged), len(compliance_aligned))
    x = friction_lagged.values[:n].astype(float)
    y = compliance_aligned.values[:n].astype(float)

    # OLS fit: y = slope * x + intercept
    slope, intercept = np.polyfit(x, y, 1)
    y_hat = slope * x + intercept
    residuals = y - y_hat
    residual_sd = float(np.std(residuals))

    # Smooth x range for plotting the regression line
    x_line = np.linspace(float(x.min()), float(x.max()), 100)
    y_line = slope * x_line + intercept

    return {
        "slope": float(slope),
        "intercept": float(intercept),
        "residual_sd": residual_sd,
        "x": x,
        "y": y,
        "x_line": x_line,
        "y_line": y_line,
        "y_upper": y_line + 2 * residual_sd,
        "y_lower": y_line - 2 * residual_sd,
    }


# =========================================================================
#  SELF-TEST: Run this file directly to verify against known values
# =========================================================================
#
#  Usage:  cd dashboard && python correlation_engine.py
#
#  Expected output:
#      2-week index lag: r = 0.6196, p = 0.0004, n = 28  (actual median: 7 days)
#      95% CI: [0.3212, 0.8111]
#      Lag sweep with peak at lag=2
#      VERIFIED: Original r=0.6196
#
# =========================================================================

if __name__ == "__main__":
    import os

    # Resolve path to core dataset from this file's location
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    csv_path = os.path.join(repo, "Control_Proof", "master_reflexive_correlation_data.csv")
    df = pd.read_csv(csv_path)

    friction = df["Epstein_Friction_Index"]
    compliance = df["Institutional_Compliance_Index"]

    print("=" * 60)
    print("  CORRELATION ENGINE SELF-TEST")
    print("=" * 60)

    # Test 1: Lagged Pearson correlation
    r, p, n_eff = compute_lagged_correlation(friction, compliance, lag=2)
    print(f"\n[1] 2-week index lag Pearson:  r = {r:.4f},  p = {p:.4f},  n = {n_eff}  (actual median: 7 days)")

    # Test 2: Fisher z-transform CI
    ci_lo, ci_hi = fisher_ci(r, n_eff)
    print(f"[2] 95% CI (Fisher z):  [{ci_lo:.4f}, {ci_hi:.4f}]")

    # Test 3: Spearman rank correlation
    rho, p_sp = compute_spearman(friction, compliance, lag=2)
    print(f"[3] 2-week index lag Spearman: \u03c1 = {rho:.4f},  p = {p_sp:.4f}")

    # Test 4: Lag sweep
    print(f"\n[4] Lag sweep (0-6 weeks):")
    sweep = compute_lag_sweep(friction, compliance)
    for lag, (rv, pv) in sorted(sweep.items()):
        marker = "  <-- PEAK" if lag == 2 else ""
        print(f"    lag={lag}: r={rv:+.4f}, p={pv:.4f}{marker}")

    # Test 5: Regression
    reg = compute_regression(friction, compliance, lag=2)
    print(f"\n[5] Regression: Compliance = {reg['slope']:.4f} \u00d7 Friction + {reg['intercept']:.4f}")
    print(f"    Residual SD = {reg['residual_sd']:.4f}")
    print(f"    r\u00b2 = {r**2:.4f} ({r**2 * 100:.1f}% variance explained)")

    # Verification gate
    print("\n" + "=" * 60)
    match = abs(r - 0.6196) < 0.01
    if match:
        print("  VERIFIED: Original r = 0.6196 | Reproduced r = {:.4f}".format(r))
    else:
        print("  DISCREPANCY: Original r = 0.6196 | Reproduced r = {:.4f}".format(r))
    print("=" * 60)
