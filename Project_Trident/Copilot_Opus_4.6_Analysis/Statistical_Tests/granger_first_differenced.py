#!/usr/bin/env python3
"""
First-Differenced Granger Causality Test
Purpose: Address stationarity concerns by testing Granger causality on
         first-differenced series (Δfriction, Δcompliance) rather than levels.

Future Recommendation item:
    "Test with first-differenced series (Δfriction, Δcompliance) to address
     stationarity"

Granger causality assumes stationarity.  If the friction and compliance
series have trends or unit roots, the standard Granger test may produce
spurious results.  First-differencing (Δx_t = x_t - x_{t-1}) removes
trends and is the standard remedy.

This script:
  1. Tests both series for stationarity (ADF test)
  2. Runs Granger causality on LEVELS (baseline)
  3. Runs Granger causality on FIRST DIFFERENCES
  4. Compares results — if differencing changes the conclusion, the
     level-based result was unreliable.

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
from statsmodels.tsa.stattools import grangercausalitytests, adfuller

MAX_LAG = 8


def run_adf(series, name):
    """Run Augmented Dickey-Fuller test for stationarity."""
    result = adfuller(series, maxlag=MAX_LAG, autolag='AIC')
    stat, p, used_lag, nobs, crit, icbest = result
    stationary = p < 0.05
    tag = "✅ STATIONARY" if stationary else "⚠️ NON-STATIONARY"
    print(f"  {name}:")
    print(f"    ADF statistic: {stat:.4f}")
    print(f"    p-value: {p:.6f}")
    print(f"    Lags used: {used_lag}")
    print(f"    Result: {tag}")
    return stationary, p


def run_granger(data, max_lag=MAX_LAG):
    """Run Granger causality and return results list."""
    results = []
    try:
        gc = grangercausalitytests(data, maxlag=max_lag, verbose=False)
        for lag in range(1, max_lag + 1):
            f_stat = gc[lag][0]['ssr_ftest'][0]
            p_val = gc[lag][0]['ssr_ftest'][1]
            results.append({'lag': lag, 'f_stat': f_stat, 'p': p_val})
    except Exception as exc:
        print(f"  Error: {exc}")
    return results


def print_results(results, label):
    """Print a Granger results table."""
    print(f"\n  ── {label} ──")
    print(f"  {'Lag':>6} {'F-stat':>10} {'p-value':>10} {'Sig?':>8}")
    print(f"  {'─' * 36}")
    for r in results:
        sig = "✓" if r['p'] < 0.05 else "✗"
        print(f"  {r['lag']:>6} {r['f_stat']:>10.4f} {r['p']:>10.4f} {sig:>8}")
    sig_lags = [r for r in results if r['p'] < 0.05]
    if sig_lags:
        print(f"  → Significant at lags: {', '.join(str(r['lag']) for r in sig_lags)}")
    else:
        print(f"  → No significant lags")


# ── Load data ────────────────────────────────────────────────────────────
print("=" * 70)
print("FIRST-DIFFERENCED GRANGER CAUSALITY TEST")
print("=" * 70)
print("\nTests Granger causality on Δfriction and Δcompliance to address")
print("stationarity assumptions.")
print("Datasets: original pre-2026 via original_data_loader.py\n")

friction_events = load_friction_events()
compliance_events = load_compliance_events()
weekly = build_weekly_counts(friction_events, compliance_events)
f_series = weekly['friction'].values.astype(float)
c_series = weekly['compliance'].values.astype(float)
n = len(f_series)

# ── Step 1: Stationarity tests ──────────────────────────────────────────
print(f"\n{'═' * 70}")
print(f"  STEP 1: STATIONARITY TESTS (Augmented Dickey-Fuller)")
print(f"{'═' * 70}")
print(f"  Series length: {n} weeks\n")

print("  LEVELS (raw series):")
f_stat_levels, f_p_levels = run_adf(f_series, "Friction (levels)")
c_stat_levels, c_p_levels = run_adf(c_series, "Compliance (levels)")

# First differences
f_diff = np.diff(f_series)
c_diff = np.diff(c_series)

print(f"\n  FIRST DIFFERENCES (Δ series):")
f_stat_diff, f_p_diff = run_adf(f_diff, "ΔFriction")
c_stat_diff, c_p_diff = run_adf(c_diff, "ΔCompliance")

# ── Step 2: Granger on LEVELS (baseline) ────────────────────────────────
print(f"\n\n{'═' * 70}")
print(f"  STEP 2: GRANGER CAUSALITY ON LEVELS (baseline)")
print(f"{'═' * 70}")

data_fc = pd.DataFrame({'compliance': c_series, 'friction': f_series})
data_cf = pd.DataFrame({'friction': f_series, 'compliance': c_series})

fc_levels = run_granger(data_fc[['compliance', 'friction']])
cf_levels = run_granger(data_cf[['friction', 'compliance']])
print_results(fc_levels, 'Friction → Compliance (LEVELS)')
print_results(cf_levels, 'Compliance → Friction (LEVELS)')

# ── Step 3: Granger on FIRST DIFFERENCES ────────────────────────────────
print(f"\n\n{'═' * 70}")
print(f"  STEP 3: GRANGER CAUSALITY ON FIRST DIFFERENCES")
print(f"{'═' * 70}")

data_fc_diff = pd.DataFrame({'d_compliance': c_diff, 'd_friction': f_diff})
data_cf_diff = pd.DataFrame({'d_friction': f_diff, 'd_compliance': c_diff})

fc_diff = run_granger(data_fc_diff[['d_compliance', 'd_friction']])
cf_diff = run_granger(data_cf_diff[['d_friction', 'd_compliance']])
print_results(fc_diff, 'ΔFriction → ΔCompliance (FIRST DIFF)')
print_results(cf_diff, 'ΔCompliance → ΔFriction (FIRST DIFF)')

# ── Step 4: Also test the 30-row master ─────────────────────────────────
print(f"\n\n{'═' * 70}")
print(f"  STEP 4: 30-ROW MASTER CSV (Index Scores)")
print(f"{'═' * 70}")

data_path = os.path.join(REPO_ROOT, 'Control_Proof',
                         'master_reflexive_correlation_data.csv')
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    friction = df['Epstein_Friction_Index'].values.astype(float)
    compliance = df['Institutional_Compliance_Index'].values.astype(float)
    n_orig = len(df)
    max_lag_orig = 4

    print(f"  Rows: {n_orig}")

    # ADF on levels
    print(f"\n  LEVELS:")
    run_adf(friction, "Friction Index (levels)")
    run_adf(compliance, "Compliance Index (levels)")

    # ADF on diffs
    f_diff_orig = np.diff(friction)
    c_diff_orig = np.diff(compliance)
    print(f"\n  FIRST DIFFERENCES:")
    run_adf(f_diff_orig, "ΔFriction Index")
    run_adf(c_diff_orig, "ΔCompliance Index")

    # Granger on levels
    print(f"\n  Granger on LEVELS:")
    data_orig_fc = pd.DataFrame({'compliance': compliance, 'friction': friction})
    data_orig_cf = pd.DataFrame({'friction': friction, 'compliance': compliance})
    fc_orig_lev = run_granger(data_orig_fc[['compliance', 'friction']], max_lag_orig)
    cf_orig_lev = run_granger(data_orig_cf[['friction', 'compliance']], max_lag_orig)
    print_results(fc_orig_lev, 'Friction → Compliance (30-row LEVELS)')
    print_results(cf_orig_lev, 'Compliance → Friction (30-row LEVELS)')

    # Granger on first differences
    print(f"\n  Granger on FIRST DIFFERENCES:")
    max_lag_diff = 3  # fewer lags due to lost observation
    data_orig_fc_d = pd.DataFrame({'d_c': c_diff_orig, 'd_f': f_diff_orig})
    data_orig_cf_d = pd.DataFrame({'d_f': f_diff_orig, 'd_c': c_diff_orig})
    fc_orig_diff = run_granger(data_orig_fc_d[['d_c', 'd_f']], max_lag_diff)
    cf_orig_diff = run_granger(data_orig_cf_d[['d_f', 'd_c']], max_lag_diff)
    print_results(fc_orig_diff, 'ΔFriction → ΔCompliance (30-row DIFF)')
    print_results(cf_orig_diff, 'ΔCompliance → ΔFriction (30-row DIFF)')
else:
    print(f"  ⚠ File not found: {data_path}")

# ── Comparison ───────────────────────────────────────────────────────────
print(f"\n\n{'═' * 70}")
print(f"  COMPARISON: LEVELS vs FIRST DIFFERENCES")
print(f"{'═' * 70}")

fc_lev_sig = [r['lag'] for r in fc_levels if r['p'] < 0.05]
cf_lev_sig = [r['lag'] for r in cf_levels if r['p'] < 0.05]
fc_dif_sig = [r['lag'] for r in fc_diff if r['p'] < 0.05]
cf_dif_sig = [r['lag'] for r in cf_diff if r['p'] < 0.05]

print(f"\n  Event-count dataset ({n} weeks):")
print(f"  {'':30} {'LEVELS':>20} {'FIRST DIFF':>20}")
print(f"  {'─' * 70}")
print(f"  {'F→C significant lags':30} {str(fc_lev_sig):>20} {str(fc_dif_sig):>20}")
print(f"  {'C→F significant lags':30} {str(cf_lev_sig):>20} {str(cf_dif_sig):>20}")

if fc_dif_sig == fc_lev_sig and cf_dif_sig == cf_lev_sig:
    print(f"\n  ✅ CONSISTENT: First-differencing does NOT change the Granger result.")
    print(f"     The level-based finding is robust to stationarity correction.")
elif not fc_dif_sig and not cf_dif_sig:
    print(f"\n  ⚠️ CHANGES CONCLUSION: First-differencing DESTROYS all Granger causality.")
    print(f"     The level-based results were driven by trends, not genuine predictive")
    print(f"     relationships between friction and compliance changes.")
else:
    print(f"\n  ⚠️ PARTIALLY CHANGES: First-differencing alters the Granger pattern.")
    print(f"     Some relationships survive but the overall conclusion shifts.")

print(f"""
  WHAT THIS MEANS:
    - If levels and diffs agree: the Granger result is genuine
    - If diffs show nothing: the level-based Granger was an artifact of
      shared trends (both series rising or falling together over time)
    - First-differencing is the MORE RELIABLE test because it satisfies
      the stationarity assumption that Granger causality requires
""")
print("=" * 70)
