#!/usr/bin/env python3
"""
Granger Causality Test — Excluding December 2025
Purpose: Re-run Granger causality tests with December 2025 removed to check
         whether the directional findings are robust or driven by the densest
         month in the dataset.

Future Recommendation item:
    "Re-run Granger causality excluding December 2025 to test robustness"

December 2025 is the densest month in the timeline.  If removing it changes
the Granger direction or destroys significance, the directional conclusions
are fragile and driven by one anomalous month.

Datasets used: original pre-2026 datasets via original_data_loader.py
"""

import os
import warnings
import pandas as pd
import numpy as np
from scipy.stats import pearsonr

from original_data_loader import (
    load_friction_events, load_compliance_events, build_weekly_counts, REPO_ROOT
)

warnings.filterwarnings('ignore', category=FutureWarning)
from statsmodels.tsa.stattools import grangercausalitytests

MAX_LAG = 8


def run_granger(data, direction_label, max_lag=MAX_LAG):
    """Run Granger causality and return results list."""
    results = []
    try:
        gc = grangercausalitytests(data, maxlag=max_lag, verbose=False)
        for lag in range(1, max_lag + 1):
            f_stat = gc[lag][0]['ssr_ftest'][0]
            p_val = gc[lag][0]['ssr_ftest'][1]
            results.append({'lag': lag, 'f_stat': f_stat, 'p': p_val})
    except Exception as exc:
        print(f"  Error ({direction_label}): {exc}")
    return results


def print_results(results, label):
    """Print a Granger results table."""
    print(f"\n  ── {label} ──")
    print(f"  {'Lag':>6} {'F-stat':>10} {'p-value':>10} {'Sig?':>8}")
    print(f"  {'─' * 36}")
    for r in results:
        sig = "✓" if r['p'] < 0.05 else "✗"
        print(f"  {r['lag']:>6} {r['f_stat']:>10.4f} {r['p']:>10.4f} {sig:>8}")


def summarize(fc, cf, label):
    """Print interpretation for a pair of Granger results."""
    fc_sig = [r for r in fc if r['p'] < 0.05]
    cf_sig = [r for r in cf if r['p'] < 0.05]
    print(f"\n  ── Interpretation ({label}) ──")
    if fc_sig and not cf_sig:
        print(f"  ✓ UNIDIRECTIONAL: Friction → Compliance")
        print(f"    Significant at lags: {', '.join(str(r['lag']) for r in fc_sig)}")
    elif cf_sig and not fc_sig:
        print(f"  ✓ UNIDIRECTIONAL: Compliance → Friction (REVERSE)")
        print(f"    Significant at lags: {', '.join(str(r['lag']) for r in cf_sig)}")
    elif fc_sig and cf_sig:
        print(f"  ⚠ BIDIRECTIONAL")
        print(f"    F→C lags: {', '.join(str(r['lag']) for r in fc_sig)}")
        print(f"    C→F lags: {', '.join(str(r['lag']) for r in cf_sig)}")
    else:
        print(f"  ✗ NO GRANGER CAUSALITY in either direction")


# ── Load data ────────────────────────────────────────────────────────────
print("=" * 70)
print("GRANGER CAUSALITY — EXCLUDING DECEMBER 2025")
print("=" * 70)
print("\nRobustness check: does Granger direction survive without Dec 2025?")
print("Datasets: original pre-2026 via original_data_loader.py\n")

friction_events = load_friction_events()
compliance_events = load_compliance_events()
weekly_full = build_weekly_counts(friction_events, compliance_events)

# ── Full dataset (baseline) ──────────────────────────────────────────────
print(f"\n{'═' * 70}")
print(f"  FULL DATASET (baseline)")
print(f"{'═' * 70}")
f_full = weekly_full['friction'].values.astype(float)
c_full = weekly_full['compliance'].values.astype(float)
n_full = len(f_full)
print(f"  Weeks: {n_full}")

data_fc = pd.DataFrame({'compliance': c_full, 'friction': f_full})
data_cf = pd.DataFrame({'friction': f_full, 'compliance': c_full})

fc_full = run_granger(data_fc[['compliance', 'friction']], 'F→C full')
cf_full = run_granger(data_cf[['friction', 'compliance']], 'C→F full')
print_results(fc_full, 'Friction → Compliance (FULL)')
print_results(cf_full, 'Compliance → Friction (FULL)')
summarize(fc_full, cf_full, 'FULL')

# ── Exclusion windows ────────────────────────────────────────────────────
exclusions = {
    'Dec 2025 excluded': lambda w: not (w.start_time.year == 2025 and w.start_time.month == 12),
    'Nov-Dec 2025 excluded': lambda w: not (w.start_time.year == 2025 and w.start_time.month in [11, 12]),
    'All 2025 excluded': lambda w: w.start_time.year != 2025,
    'Only pre-2020': lambda w: w.start_time.year < 2020,
    'Only 2020-2024': lambda w: 2020 <= w.start_time.year <= 2024,
}

for name, filter_fn in exclusions.items():
    mask = np.array([filter_fn(w) for w in weekly_full.index])
    f_sub = f_full[mask]
    c_sub = c_full[mask]
    n_sub = len(f_sub)

    print(f"\n\n{'═' * 70}")
    print(f"  {name.upper()} ({n_sub} weeks)")
    print(f"{'═' * 70}")

    if n_sub < MAX_LAG + 5:
        print(f"  ⚠ Too few weeks ({n_sub}) — skipping")
        continue

    if f_sub.std() == 0 or c_sub.std() == 0:
        print(f"  ⚠ One series is constant — skipping")
        continue

    data_fc_sub = pd.DataFrame({'compliance': c_sub, 'friction': f_sub})
    data_cf_sub = pd.DataFrame({'friction': f_sub, 'compliance': c_sub})

    fc_sub = run_granger(data_fc_sub[['compliance', 'friction']], f'F→C {name}')
    cf_sub = run_granger(data_cf_sub[['friction', 'compliance']], f'C→F {name}')
    print_results(fc_sub, f'Friction → Compliance ({name})')
    print_results(cf_sub, f'Compliance → Friction ({name})')
    summarize(fc_sub, cf_sub, name)

# ── Also test on 30-row master excluding any Dec 2025 rows ──────────────
print(f"\n\n{'═' * 70}")
print(f"  ORIGINAL 30-ROW MASTER CSV")
print(f"{'═' * 70}")
print(f"  (Index-scored — Dec 2025 exclusion may not apply since rows are")
print(f"   week indices without explicit dates.  Reporting for completeness.)")

data_path = os.path.join(REPO_ROOT, 'Control_Proof',
                         'master_reflexive_correlation_data.csv')
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    friction = df['Epstein_Friction_Index'].values.astype(float)
    compliance = df['Institutional_Compliance_Index'].values.astype(float)
    n_orig = len(df)
    max_lag_orig = 4
    print(f"  Rows: {n_orig} (testing lags 1-{max_lag_orig})")

    data_orig_fc = pd.DataFrame({'compliance': compliance, 'friction': friction})
    data_orig_cf = pd.DataFrame({'friction': friction, 'compliance': compliance})

    fc_orig = run_granger(data_orig_fc[['compliance', 'friction']], 'F→C orig', max_lag_orig)
    cf_orig = run_granger(data_orig_cf[['friction', 'compliance']], 'C→F orig', max_lag_orig)
    print_results(fc_orig, 'Friction → Compliance (30-row)')
    print_results(cf_orig, 'Compliance → Friction (30-row)')
    summarize(fc_orig, cf_orig, '30-row master')
else:
    print(f"  ⚠ File not found: {data_path}")

# ── Comparison table ─────────────────────────────────────────────────────
print(f"\n\n{'═' * 70}")
print(f"  COMPARISON SUMMARY")
print(f"{'═' * 70}")
print(f"""
  This test checks whether the Granger causality direction is robust
  when December 2025 (the densest month) is removed.

  Key question: Does the directional finding change?
    - If YES: the direction is fragile and Dec 2025-dependent
    - If NO: the direction is a genuine feature of the broader timeline

  IMPORTANT: Granger causality assumes stationarity.  See Task 2
  (first-differenced series) for the stationarity-corrected version.
""")
print("=" * 70)
