#!/usr/bin/env python3
"""
Placebo & Calendar-Anchor Test — Robustness Audit v10.2 (March 2026)

TASK 1 from the Robustness and Methodology Audit.

Part A — PLACEBO TEST:
  Randomize the dates/ordering of compliance events 10,000 times and
  re-run Pearson r at the 2-week lag.  If the observed r = 0.6196 is
  genuinely sequential, it should beat >95% of the shuffled distribution.

Part B — CALENDAR-ANCHOR TEST:
  Align all friction and compliance events to the nearest 'Calendar
  Anchor' (solstices, major holidays, fiscal deadlines).  Compute the
  residual lag AFTER removing the anchor effect.  If the 14-day lag is
  a byproduct of simultaneous clustering around shared anchors, the
  residual correlation should collapse toward zero.

Part C — BACKFILL LAG ANALYSIS:
  Use the 66-pair historical_backfill_2017_2024.csv to test whether
  lag days correlate with proximity to calendar anchors.

Datasets used:
  - Control_Proof/master_reflexive_correlation_data.csv   (30-week index)
  - Run_Correlations_Yourself/historical_backfill_2017_2024.csv  (66 pairs)
"""

import os
import sys
import json
import numpy as np
import pandas as pd
from scipy.stats import pearsonr, spearmanr
from datetime import datetime, timedelta

SEED = 42
N_PERM = 10_000
rng = np.random.default_rng(SEED)

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)

# ── Calendar Anchors (from 01_CORE_THEORY.md and standard calendar) ──────
# These are the recurring dates the project identifies as "low-attention
# windows" or institutional scheduling anchors.
CALENDAR_ANCHORS = [
    # Solstices / Equinoxes
    ("Winter Solstice",  12, 21),
    ("Vernal Equinox",    3, 20),
    ("Summer Solstice",   6, 21),
    ("Autumnal Equinox",  9, 22),
    # Major US Holidays (fixed-date approximations)
    ("New Year's Day",    1,  1),
    ("MLK Day",           1, 20),
    ("Presidents' Day",   2, 17),
    ("Memorial Day",      5, 26),
    ("Independence Day",  7,  4),
    ("Labor Day",         9,  1),
    ("Veterans Day",     11, 11),
    ("Thanksgiving",     11, 27),
    ("Christmas",        12, 25),
    # Fiscal / Regulatory deadlines
    ("Q1 End / Tax Day",  4, 15),
    ("Q2 End",            6, 30),
    ("Q3 End",            9, 30),
    ("Q4 End / FY Close",12, 31),
    # 13F Filing deadlines (45 days after quarter end)
    ("13F Q1 Deadline",   5, 15),
    ("13F Q2 Deadline",   8, 14),
    ("13F Q3 Deadline",  11, 14),
    ("13F Q4 Deadline",   2, 14),
    # Religious / Cultural (mentioned in ritual analysis)
    ("Chanukah (approx)", 12, 18),
    ("Passover (approx)",  4, 15),
]


def nearest_anchor_distance(date_val):
    """Return the minimum absolute day distance from any calendar anchor."""
    if pd.isna(date_val):
        return np.nan
    year = date_val.year
    min_dist = 366
    for name, month, day in CALENDAR_ANCHORS:
        try:
            anchor = pd.Timestamp(year=year, month=month, day=day)
            dist = abs((date_val - anchor).days)
            # Also check previous/next year for cross-year anchors
            for dy in [-1, 0, 1]:
                try:
                    a = pd.Timestamp(year=year + dy, month=month, day=day)
                    d = abs((date_val - a).days)
                    if d < min_dist:
                        min_dist = d
                except ValueError:
                    pass
        except ValueError:
            pass
    return min_dist


def nearest_anchor_name(date_val):
    """Return the name of the nearest calendar anchor."""
    if pd.isna(date_val):
        return "N/A"
    year = date_val.year
    min_dist = 366
    best_name = "None"
    for name, month, day in CALENDAR_ANCHORS:
        for dy in [-1, 0, 1]:
            try:
                a = pd.Timestamp(year=year + dy, month=month, day=day)
                d = abs((date_val - a).days)
                if d < min_dist:
                    min_dist = d
                    best_name = name
            except ValueError:
                pass
    return best_name


# ═══════════════════════════════════════════════════════════════════════════
#  PART A — PLACEBO TEST (Permutation on 30-row index dataset)
# ═══════════════════════════════════════════════════════════════════════════

def part_a_placebo():
    print("=" * 78)
    print("  PART A: PLACEBO TEST — Permutation Shuffle (n=10,000)")
    print("=" * 78)

    csv_path = os.path.join(REPO_ROOT, "Control_Proof",
                            "master_reflexive_correlation_data.csv")
    if not os.path.exists(csv_path):
        print(f"ERROR: {csv_path} not found")
        return None

    df = pd.read_csv(csv_path)
    friction = df["Epstein_Friction_Index"].values
    compliance = df["Institutional_Compliance_Index"].values
    n = len(friction)
    print(f"\n  Dataset: master_reflexive_correlation_data.csv")
    print(f"  Rows: {n}  |  Permutations: {N_PERM:,}  |  Seed: {SEED}")

    # Observed 2-week lag correlation
    lag = 2
    shifted = np.empty(n, dtype=float)
    shifted[:lag] = np.nan
    shifted[lag:] = friction[:-lag]
    valid = ~np.isnan(shifted)
    r_obs, p_obs = pearsonr(shifted[valid], compliance[valid])
    print(f"\n  Observed 2-week lag r = {r_obs:.4f}  (parametric p = {p_obs:.4f})")

    # Permutation: shuffle compliance indices, recompute lagged r
    perm_r = np.empty(N_PERM)
    for i in range(N_PERM):
        shuffled_compliance = rng.permutation(compliance)
        perm_r[i] = np.corrcoef(shifted[valid], shuffled_compliance[valid])[0, 1]

    exceed = np.sum(np.abs(perm_r) >= np.abs(r_obs))
    p_empirical = (exceed + 1) / (N_PERM + 1)

    print(f"\n  Permuted distribution (compliance shuffled {N_PERM:,} times):")
    print(f"    Mean  = {np.mean(perm_r):.4f}")
    print(f"    Std   = {np.std(perm_r):.4f}")
    print(f"    5th   = {np.percentile(perm_r, 5):.4f}")
    print(f"    95th  = {np.percentile(perm_r, 95):.4f}")
    print(f"    Min   = {np.min(perm_r):.4f}")
    print(f"    Max   = {np.max(perm_r):.4f}")
    print(f"\n  |permuted| ≥ |observed|: {exceed} / {N_PERM}")
    print(f"  Empirical p-value: {p_empirical:.6f}")

    if p_empirical < 0.01:
        verdict = "SIGNIFICANT (p < 0.01): 14-day lag is NOT a random artifact."
    elif p_empirical < 0.05:
        verdict = "SIGNIFICANT (p < 0.05): 14-day lag unlikely random."
    else:
        verdict = "NOT SIGNIFICANT: 14-day lag could be random noise."

    print(f"\n  ► VERDICT: {verdict}")

    return {
        "test": "Placebo (Permutation)",
        "observed_r": round(r_obs, 4),
        "parametric_p": round(p_obs, 4),
        "empirical_p": round(p_empirical, 6),
        "n_permutations": N_PERM,
        "exceed_count": int(exceed),
        "perm_mean": round(float(np.mean(perm_r)), 4),
        "perm_std": round(float(np.std(perm_r)), 4),
        "verdict": verdict,
    }


# ═══════════════════════════════════════════════════════════════════════════
#  PART B — CALENDAR-ANCHOR TEST (using backfill event pairs)
# ═══════════════════════════════════════════════════════════════════════════

def part_b_calendar_anchor():
    print("\n" + "=" * 78)
    print("  PART B: CALENDAR-ANCHOR TEST — Do Events Cluster on Anchors?")
    print("=" * 78)

    csv_path = os.path.join(REPO_ROOT, "Run_Correlations_Yourself",
                            "historical_backfill_2017_2024.csv")
    if not os.path.exists(csv_path):
        print(f"ERROR: {csv_path} not found")
        return None

    df = pd.read_csv(csv_path)
    df["Friction_Date"] = pd.to_datetime(df["Friction_Date"], errors="coerce")
    df["Compliance_Date"] = pd.to_datetime(df["Compliance_Date"], errors="coerce")

    # Parse Lag_Days (strip '+' prefix)
    df["Lag_Parsed"] = df["Lag_Days"].astype(str).str.replace("+", "", regex=False).astype(float)

    valid = df.dropna(subset=["Friction_Date", "Compliance_Date"])
    n = len(valid)
    print(f"\n  Dataset: historical_backfill_2017_2024.csv")
    print(f"  Valid event pairs: {n}")

    # Compute anchor distances for friction and compliance dates
    valid = valid.copy()
    valid["Friction_Anchor_Dist"] = valid["Friction_Date"].apply(nearest_anchor_distance)
    valid["Compliance_Anchor_Dist"] = valid["Compliance_Date"].apply(nearest_anchor_distance)
    valid["Friction_Nearest"] = valid["Friction_Date"].apply(nearest_anchor_name)
    valid["Compliance_Nearest"] = valid["Compliance_Date"].apply(nearest_anchor_name)

    # ── Analysis 1: How close are events to anchors? ──
    f_mean_dist = valid["Friction_Anchor_Dist"].mean()
    c_mean_dist = valid["Compliance_Anchor_Dist"].mean()
    print(f"\n  Mean distance to nearest anchor:")
    print(f"    Friction events:   {f_mean_dist:.1f} days")
    print(f"    Compliance events: {c_mean_dist:.1f} days")

    # What % fall within 7 days of an anchor?
    f_near = (valid["Friction_Anchor_Dist"] <= 7).mean() * 100
    c_near = (valid["Compliance_Anchor_Dist"] <= 7).mean() * 100
    print(f"\n  Events within 7 days of a calendar anchor:")
    print(f"    Friction:   {f_near:.1f}%")
    print(f"    Compliance: {c_near:.1f}%")

    # ── Analysis 2: Do friction & compliance share the same anchor? ──
    same_anchor = (valid["Friction_Nearest"] == valid["Compliance_Nearest"]).mean() * 100
    print(f"\n  Friction & compliance share the SAME nearest anchor: {same_anchor:.1f}%")

    # ── Analysis 3: After controlling for anchor proximity, does lag persist? ──
    # If both events cluster on the same anchor, the "lag" is just the
    # difference in their distances from that anchor. We test whether the
    # observed lag distribution differs from what anchor clustering alone
    # would predict.
    lags = valid["Lag_Parsed"].values
    anchor_diffs = (valid["Compliance_Anchor_Dist"] - valid["Friction_Anchor_Dist"]).values

    if len(lags) > 5:
        r_lag_anchor, p_lag_anchor = pearsonr(lags, anchor_diffs)
        print(f"\n  Correlation between observed lag and anchor-distance difference:")
        print(f"    Pearson r = {r_lag_anchor:.4f}, p = {p_lag_anchor:.4f}")
    else:
        r_lag_anchor, p_lag_anchor = np.nan, np.nan

    # ── Analysis 4: Residual lag after removing anchor effect ──
    # Regress lag on anchor_diffs, check if residual lag is still ~14 days
    if len(lags) > 5 and not np.isnan(r_lag_anchor):
        slope, intercept = np.polyfit(anchor_diffs, lags, 1)
        predicted = slope * anchor_diffs + intercept
        residuals = lags - predicted
        mean_residual = np.mean(residuals)
        median_lag = np.median(lags)
        print(f"\n  Lag distribution:")
        print(f"    Mean observed lag:  {np.mean(lags):.1f} days")
        print(f"    Median observed lag: {median_lag:.1f} days")
        print(f"    Mean residual lag (after anchor adjustment): {mean_residual:.1f} days")
        print(f"    Median residual lag: {np.median(residuals):.1f} days")

    # ── Analysis 5: Calendar-shuffled placebo ──
    # Snap each event to its nearest anchor, then compute the shuffled lag
    print(f"\n  Calendar-Shuffled Test:")
    print(f"  (Snap all events to their nearest anchor date, recompute lags)")
    anchor_lags = (valid["Compliance_Anchor_Dist"] - valid["Friction_Anchor_Dist"]).values
    mean_anchor_lag = np.mean(np.abs(anchor_lags))
    mean_real_lag = np.mean(np.abs(lags))
    print(f"    Mean |anchor-based lag|: {mean_anchor_lag:.1f} days")
    print(f"    Mean |observed lag|:     {mean_real_lag:.1f} days")
    print(f"    Ratio (observed/anchor): {mean_real_lag/mean_anchor_lag:.2f}x" if mean_anchor_lag > 0 else "    Ratio: N/A")

    # ── Verdict ──
    print(f"\n  ► INTERPRETATION:")
    if same_anchor > 70:
        print(f"    ⚠ {same_anchor:.0f}% of event pairs share the same calendar anchor.")
        print(f"    The 14-day lag may be partially explained by calendar clustering.")
        cal_verdict = "CALENDAR CLUSTERING DETECTED"
    elif same_anchor > 40:
        print(f"    ⚠ {same_anchor:.0f}% of pairs share an anchor — moderate clustering.")
        print(f"    The 14-day lag is a MIX of sequential reaction and calendar effect.")
        cal_verdict = "MIXED — PARTIAL CALENDAR EFFECT"
    else:
        print(f"    ✅ Only {same_anchor:.0f}% share an anchor — calendar clustering is weak.")
        print(f"    The 14-day lag appears to be a genuine sequential pattern.")
        cal_verdict = "SEQUENTIAL PATTERN SUPPORTED"

    if not np.isnan(r_lag_anchor) and abs(r_lag_anchor) > 0.3:
        print(f"    ⚠ Anchor distances correlate with lag (r={r_lag_anchor:.2f}),")
        print(f"    suggesting calendar timing influences the lag length.")
    else:
        print(f"    ✅ Anchor distances do NOT correlate with lag (r={r_lag_anchor:.2f}),")
        print(f"    suggesting the lag is independent of calendar scheduling.")

    return {
        "test": "Calendar-Anchor",
        "n_pairs": n,
        "mean_friction_anchor_dist": round(f_mean_dist, 1),
        "mean_compliance_anchor_dist": round(c_mean_dist, 1),
        "pct_friction_within_7d": round(f_near, 1),
        "pct_compliance_within_7d": round(c_near, 1),
        "pct_same_anchor": round(same_anchor, 1),
        "lag_anchor_correlation": round(float(r_lag_anchor), 4) if not np.isnan(r_lag_anchor) else None,
        "lag_anchor_p": round(float(p_lag_anchor), 4) if not np.isnan(p_lag_anchor) else None,
        "mean_observed_lag": round(float(np.mean(lags)), 1),
        "median_observed_lag": round(float(np.median(lags)), 1),
        "verdict": cal_verdict,
    }


# ═══════════════════════════════════════════════════════════════════════════
#  PART C — BACKFILL LAG vs ANCHOR PROXIMITY (Detailed Breakdown)
# ═══════════════════════════════════════════════════════════════════════════

def part_c_lag_breakdown():
    print("\n" + "=" * 78)
    print("  PART C: LAG DISTRIBUTION vs CALENDAR ANCHOR PROXIMITY")
    print("=" * 78)

    csv_path = os.path.join(REPO_ROOT, "Run_Correlations_Yourself",
                            "historical_backfill_2017_2024.csv")
    if not os.path.exists(csv_path):
        print(f"ERROR: {csv_path} not found")
        return None

    df = pd.read_csv(csv_path)
    df["Friction_Date"] = pd.to_datetime(df["Friction_Date"], errors="coerce")
    df["Compliance_Date"] = pd.to_datetime(df["Compliance_Date"], errors="coerce")
    df["Lag_Parsed"] = df["Lag_Days"].astype(str).str.replace("+", "", regex=False).astype(float)
    df["Friction_Anchor_Dist"] = df["Friction_Date"].apply(nearest_anchor_distance)
    df["Compliance_Anchor_Dist"] = df["Compliance_Date"].apply(nearest_anchor_distance)
    df["Friction_Nearest"] = df["Friction_Date"].apply(nearest_anchor_name)

    valid = df.dropna(subset=["Friction_Date", "Compliance_Date"])

    # Group by triggering event and show anchor proximity
    print(f"\n  Top friction events and their anchor proximity:\n")
    for event in valid["Friction_Event"].unique()[:10]:
        subset = valid[valid["Friction_Event"] == event]
        f_date = subset["Friction_Date"].iloc[0]
        nearest = nearest_anchor_name(f_date)
        dist = nearest_anchor_distance(f_date)
        lags = subset["Lag_Parsed"].values
        print(f"    {event[:60]:60s}")
        print(f"      Date: {f_date.strftime('%Y-%m-%d')} | Nearest: {nearest} ({dist:.0f}d) | "
              f"Lags: {', '.join(f'+{x:.0f}' for x in lags)}")

    # Lag statistics by anchor proximity bucket
    print(f"\n  Lag statistics by friction-event anchor proximity:")
    valid_copy = valid.copy()
    valid_copy["Proximity_Bucket"] = pd.cut(
        valid_copy["Friction_Anchor_Dist"],
        bins=[0, 3, 7, 14, 30, 366],
        labels=["0-3d", "4-7d", "8-14d", "15-30d", "30+d"]
    )
    for bucket, group in valid_copy.groupby("Proximity_Bucket", observed=True):
        if len(group) > 0:
            lags = group["Lag_Parsed"]
            print(f"    {bucket:6s}: n={len(group):2d}, mean lag={lags.mean():+5.1f}d, "
                  f"median={lags.median():+5.1f}d")

    return {"test": "Lag Breakdown", "status": "complete"}


# ═══════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 78)
    print("  ROBUSTNESS AUDIT v10.2 — TASK 1: PLACEBO & CALENDAR-ANCHOR TEST")
    print("  Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 78)

    results = {}
    results["placebo"] = part_a_placebo()
    results["calendar_anchor"] = part_b_calendar_anchor()
    results["lag_breakdown"] = part_c_lag_breakdown()

    # Write machine-readable results
    output_path = os.path.join(SCRIPT_DIR, "placebo_calendar_results.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n  Results saved to: {output_path}")

    # ── Final Summary ──
    print("\n" + "=" * 78)
    print("  FINAL SUMMARY — TASK 1")
    print("=" * 78)

    if results["placebo"]:
        p = results["placebo"]
        print(f"\n  PLACEBO TEST:")
        print(f"    Observed r = {p['observed_r']} at 2-week lag")
        print(f"    Empirical p = {p['empirical_p']} ({N_PERM:,} permutations)")
        print(f"    → {p['verdict']}")

    if results["calendar_anchor"]:
        c = results["calendar_anchor"]
        print(f"\n  CALENDAR-ANCHOR TEST:")
        print(f"    {c['pct_same_anchor']}% of event pairs share the same anchor")
        print(f"    Lag-anchor correlation: r = {c['lag_anchor_correlation']}")
        print(f"    Mean observed lag: {c['mean_observed_lag']} days")
        print(f"    → {c['verdict']}")

    print("\n" + "=" * 78)
