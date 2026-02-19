#!/usr/bin/env python3
"""
Backfill Lag Distribution Analysis
Purpose: Analyze the lag distribution across all friction→compliance pairs
         in the historical backfill dataset (2017-2024).

Reads: Run_Correlations_Yourself/historical_backfill_2017_2024.csv
Reports: bin counts, summary statistics, year breakdown, text histogram.

Datasets used: historical_backfill_2017_2024.csv (66 event pairs)
"""

import os
import warnings
import pandas as pd
import numpy as np
from scipy.stats import mode as scipy_mode

from original_data_loader import REPO_ROOT

warnings.filterwarnings('ignore', category=FutureWarning)

# ── Lag bins ─────────────────────────────────────────────────────────────
BINS = [
    ('[-3 to  0]', -3, 0),
    ('[+1 to +3]',  1, 3),
    ('[+4 to +7]',  4, 7),
    ('[+8 to +10]', 8, 10),
    ('[+11 to +14]', 11, 14),
    ('[+15+]',      15, None),
]


def parse_lag(val):
    """Parse Lag_Days values like '+3', '-2', '0' into integers."""
    try:
        return int(str(val).strip().replace('+', ''))
    except (ValueError, TypeError):
        return np.nan


def bin_label(lag):
    """Return the bin label for a given lag value."""
    for label, lo, hi in BINS:
        if hi is None:
            if lag >= lo:
                return label
        elif lo <= lag <= hi:
            return label
    return 'out of range'


def text_histogram(lags, width=50):
    """Return a simple text histogram of lag values."""
    counts = {}
    for lag in sorted(lags.unique()):
        counts[lag] = (lags == lag).sum()
    max_count = max(counts.values()) if counts else 1
    lines = []
    for lag in sorted(counts):
        bar_len = int(counts[lag] / max_count * width)
        bar = '█' * max(bar_len, 1)
        lines.append(f"  {lag:>+4d} │ {bar} ({counts[lag]})")
    return '\n'.join(lines)


# ── Load data ────────────────────────────────────────────────────────────
csv_path = os.path.join(REPO_ROOT, 'Run_Correlations_Yourself',
                        'historical_backfill_2017_2024.csv')

df = pd.read_csv(csv_path)
df['lag'] = df['Lag_Days'].apply(parse_lag)
df = df.dropna(subset=['lag'])
df['lag'] = df['lag'].astype(int)

print("=" * 70)
print("BACKFILL LAG DISTRIBUTION ANALYSIS")
print("=" * 70)
print(f"\nDataset : historical_backfill_2017_2024.csv")
print(f"Total pairs: {len(df)}")

# ── Step 1: Lag bins ─────────────────────────────────────────────────────
print(f"\n{'═' * 70}")
print(f"  STEP 1: LAG DISTRIBUTION BY BIN")
print(f"{'═' * 70}")

df['bin'] = df['lag'].apply(bin_label)

print(f"\n  {'Bin':>16}  {'Count':>6}  {'Pct':>7}")
print(f"  {'─' * 33}")
for label, lo, hi in BINS:
    n = (df['bin'] == label).sum()
    pct = n / len(df) * 100
    print(f"  {label:>16}  {n:>6}  {pct:>6.1f}%")

# ── Step 2: Summary statistics ───────────────────────────────────────────
print(f"\n{'═' * 70}")
print(f"  STEP 2: SUMMARY STATISTICS")
print(f"{'═' * 70}")

lags = df['lag']
median_lag = lags.median()
mean_lag = lags.mean()
mode_result = scipy_mode(lags, keepdims=True)
mode_val = mode_result.mode[0]
mode_count = mode_result.count[0]

print(f"\n  Median lag      : {median_lag:+.1f} days")
print(f"  Mean lag        : {mean_lag:+.2f} days")
print(f"  Mode            : {mode_val:+d} days (appeared {mode_count} times)")
print(f"  Std dev         : {lags.std():.2f} days")
print(f"  Min             : {lags.min():+d} days")
print(f"  Max             : {lags.max():+d} days")
print(f"  Positive lags   : {(lags > 0).sum()} / {len(lags)} "
      f"({(lags > 0).sum() / len(lags) * 100:.1f}%)")
print(f"  Zero lags       : {(lags == 0).sum()} / {len(lags)}")
print(f"  Negative lags   : {(lags < 0).sum()} / {len(lags)}")

# ── Step 3: By year ─────────────────────────────────────────────────────
print(f"\n{'═' * 70}")
print(f"  STEP 3: LAG DISTRIBUTION BY YEAR")
print(f"{'═' * 70}")

print(f"\n  {'Year':>6}  {'Pairs':>6}  {'Median':>8}  {'Mean':>8}  {'Min':>5}  {'Max':>5}")
print(f"  {'─' * 46}")
for yr in sorted(df['Year'].unique()):
    sub = df[df['Year'] == yr]['lag']
    print(f"  {yr:>6}  {len(sub):>6}  {sub.median():>+8.1f}  {sub.mean():>+8.2f}"
          f"  {sub.min():>+5d}  {sub.max():>+5d}")

# ── Step 4: Text histogram ──────────────────────────────────────────────
print(f"\n{'═' * 70}")
print(f"  STEP 4: TEXT HISTOGRAM (lag in days)")
print(f"{'═' * 70}\n")

print(text_histogram(lags))

# ── Bottom line ──────────────────────────────────────────────────────────
within_week = ((lags >= 0) & (lags <= 7)).sum()
within_two_weeks = ((lags >= 0) & (lags <= 14)).sum()

print(f"\n{'═' * 70}")
print(f"  BOTTOM LINE")
print(f"{'═' * 70}")
print(f"""
  Across {len(df)} friction→compliance pairs (2017-2024):
    • Median lag: {median_lag:+.1f} days  |  Mean lag: {mean_lag:+.2f} days
    • {within_week}/{len(df)} pairs ({within_week/len(df)*100:.0f}%) saw compliance within 0-7 days
    • {within_two_weeks}/{len(df)} pairs ({within_two_weeks/len(df)*100:.0f}%) saw compliance within 0-14 days
    • Only {(lags < 0).sum()} pair(s) showed compliance BEFORE friction (negative lag)

  The distribution is right-skewed with a strong concentration in the
  +1 to +7 day range, consistent with a short institutional response
  window following friction events.
""")
print("=" * 70)
