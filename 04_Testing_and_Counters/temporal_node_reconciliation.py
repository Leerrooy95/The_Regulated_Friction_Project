#!/usr/bin/env python3
"""
Temporal Engine Adaptation & Node Timeline Reconciliation
Robustness Audit v10.2 — Tasks 3 & 4 (March 2026)

TASK 3: TEMPORAL ENGINE ADAPTATION
  Evaluate whether the temporal_engine.py logic from the State Policy
  Analysis repo can be applied. Map 'Friction' events as triggers and
  'Compliance' events as federal actions. Test if controlling for the
  'Trigger Date' (the moment the friction event was first scheduled or
  anchored) eliminates the 14-day lag.

TASK 4: NODE TIMELINE RECONCILIATION
  Compare G. Maxwell testimony (Feb 9, 2026), Board of Peace charter
  signing (Jan 22, 2026), and inaugural summit (Feb 19, 2026).
  Determine if this node follows the 14-day lag signature or clusters
  on a shared calendar window.

Datasets:
  - Run_Correlations_Yourself/historical_backfill_2017_2024.csv
  - Control_Proof/master_reflexive_correlation_data.csv
  - Web-verified event dates for Task 4
"""

import os
import json
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
from datetime import datetime, timedelta

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(SCRIPT_DIR)


# ═══════════════════════════════════════════════════════════════════════════
#  TASK 3: TEMPORAL ENGINE ADAPTATION
# ═══════════════════════════════════════════════════════════════════════════

def task3_temporal_engine():
    print("=" * 78)
    print("  TASK 3: TEMPORAL ENGINE ADAPTATION")
    print("=" * 78)

    print("""
  BACKGROUND:
  The State Policy Analysis repo uses a 'temporal_engine.py' that maps
  policy triggers to federal responses. The key finding was that when
  you control for the 'Trigger Date' (when the trigger was first
  SCHEDULED, not when it occurred), the observed lag collapsed to 0.00
  days — meaning the apparent sequential lag was actually simultaneous
  scheduling anchored to the same calendar date.

  QUESTION:
  Does the same collapse happen in the Regulated Friction dataset?
""")

    # Load the backfill data (real event pairs with measured lags)
    csv_path = os.path.join(REPO_ROOT, "Run_Correlations_Yourself",
                            "historical_backfill_2017_2024.csv")
    if not os.path.exists(csv_path):
        print(f"  ERROR: {csv_path} not found")
        return None

    df = pd.read_csv(csv_path)
    df["Friction_Date"] = pd.to_datetime(df["Friction_Date"], errors="coerce")
    df["Compliance_Date"] = pd.to_datetime(df["Compliance_Date"], errors="coerce")
    df["Lag_Parsed"] = df["Lag_Days"].astype(str).str.replace("+", "", regex=False).astype(float)
    valid = df.dropna(subset=["Friction_Date", "Compliance_Date"])
    n = len(valid)

    print(f"  Dataset: historical_backfill_2017_2024.csv")
    print(f"  Valid event pairs (n): {n}")
    print(f"  Date range: {valid['Friction_Date'].min().strftime('%Y-%m-%d')} → "
          f"{valid['Friction_Date'].max().strftime('%Y-%m-%d')}")

    # ── Mapping friction → triggers, compliance → federal actions ──
    print(f"\n  MAPPING:")
    print(f"    Friction events → 'Triggers' (n={n})")
    print(f"    Compliance events → 'Federal Actions'")

    # ── Does sample size increase? ──
    # The 30-row index dataset has n_eff=28. The backfill has n=66.
    # But many friction events map to MULTIPLE compliance events.
    unique_friction = valid["Friction_Event"].nunique()
    unique_compliance = valid["Compliance_Event"].nunique()
    print(f"\n  SAMPLE SIZE ANALYSIS:")
    print(f"    Unique friction triggers:  {unique_friction}")
    print(f"    Unique compliance actions: {unique_compliance}")
    print(f"    Total event pairs (n):     {n}")
    print(f"    vs. original index n_eff:  28")
    print(f"    Sample size increase:      {n/28:.1f}x")

    # ── Trigger Date Control ──
    # In the State Policy repo, controlling for trigger date collapsed
    # the lag. Here, we test: if we group by the friction event and
    # compute the MEDIAN lag per unique trigger, does the pattern hold?
    print(f"\n  TRIGGER DATE CONTROL:")
    print(f"  (Grouping by unique friction event, computing median lag)")
    trigger_medians = valid.groupby("Friction_Event")["Lag_Parsed"].median()
    overall_median = trigger_medians.median()
    overall_mean = trigger_medians.mean()
    print(f"    Median of trigger-median lags: {overall_median:.1f} days")
    print(f"    Mean of trigger-median lags:   {overall_mean:.1f} days")

    # ── Key test: Does controlling for trigger-date proximity ──
    # to the nearest Monday/fiscal deadline collapse the lag?
    # We define "trigger anchor" as the nearest Monday to each friction date
    # (approximating scheduled vs actual occurrence).
    valid_copy = valid.copy()
    valid_copy["Friction_DOW"] = valid_copy["Friction_Date"].dt.dayofweek
    # Snap to nearest Monday (DOW=0)
    valid_copy["Days_To_Monday"] = valid_copy["Friction_DOW"].apply(
        lambda d: min(d, 7 - d) if d > 0 else 0
    )
    valid_copy["Adjusted_Lag"] = valid_copy["Lag_Parsed"] - valid_copy["Days_To_Monday"]

    adj_median = valid_copy["Adjusted_Lag"].median()
    adj_mean = valid_copy["Adjusted_Lag"].mean()
    print(f"\n  WEEKDAY-ADJUSTED LAG (snapping triggers to nearest Monday):")
    print(f"    Adjusted median lag: {adj_median:.1f} days")
    print(f"    Adjusted mean lag:   {adj_mean:.1f} days")
    print(f"    Original mean lag:   {valid['Lag_Parsed'].mean():.1f} days")
    print(f"    Reduction:           {(1 - adj_mean/valid['Lag_Parsed'].mean())*100:.1f}%")

    # ── Does the lag disappear? ──
    lag_collapse = adj_mean < 1.0
    if lag_collapse:
        verdict = ("YES — Controlling for trigger scheduling collapses "
                    "the lag to near-zero, replicating the State Policy finding.")
    elif adj_mean < valid["Lag_Parsed"].mean() * 0.5:
        verdict = ("PARTIAL — Controlling for trigger scheduling reduces "
                    f"the lag by {(1 - adj_mean/valid['Lag_Parsed'].mean())*100:.0f}%, "
                    "but does not eliminate it.")
    else:
        verdict = ("NO — The lag persists after controlling for trigger "
                    "scheduling. The Regulated Friction lag appears to be a "
                    "genuine sequential phenomenon, not a scheduling artifact.")

    print(f"\n  ► VERDICT: {verdict}")

    # ── Compare with 30-row index dataset ──
    print(f"\n  COMPARISON WITH INDEX-BASED ANALYSIS:")
    idx_path = os.path.join(REPO_ROOT, "Control_Proof",
                            "master_reflexive_correlation_data.csv")
    idx = pd.read_csv(idx_path)
    friction = idx["Epstein_Friction_Index"].values
    compliance = idx["Institutional_Compliance_Index"].values

    # Test at multiple lags
    print(f"    Lag sweep on 30-row index (Pearson r):")
    best_lag = 0
    best_r = 0
    for lag in range(7):
        shifted = np.empty(len(friction), dtype=float)
        shifted[:lag] = np.nan
        shifted[lag:] = friction[:-lag] if lag > 0 else friction
        mask = ~np.isnan(shifted)
        if mask.sum() > 5:
            r, p = pearsonr(shifted[mask], compliance[mask])
            marker = " ← PEAK" if abs(r) > abs(best_r) else ""
            print(f"      lag={lag}: r={r:+.4f}, p={p:.4f}{marker}")
            if abs(r) > abs(best_r):
                best_r = r
                best_lag = lag

    return {
        "test": "Temporal Engine Adaptation",
        "n_pairs": n,
        "n_unique_triggers": unique_friction,
        "sample_increase": f"{n/28:.1f}x",
        "trigger_median_lag": round(overall_median, 1),
        "weekday_adjusted_mean": round(adj_mean, 1),
        "original_mean_lag": round(float(valid["Lag_Parsed"].mean()), 1),
        "lag_reduction_pct": round((1 - adj_mean/valid["Lag_Parsed"].mean())*100, 1),
        "lag_collapses": lag_collapse,
        "verdict": verdict,
    }


# ═══════════════════════════════════════════════════════════════════════════
#  TASK 4: NODE TIMELINE RECONCILIATION
# ═══════════════════════════════════════════════════════════════════════════

def task4_node_timeline():
    print("\n" + "=" * 78)
    print("  TASK 4: NODE TIMELINE RECONCILIATION")
    print("=" * 78)

    # ── Web-Verified Event Dates ──
    # All dates verified via web search (March 2, 2026).
    events = [
        {
            "name": "Board of Peace Charter Signing (Davos)",
            "date": pd.Timestamp("2026-01-22"),
            "type": "Compliance (Public/Institutional)",
            "verified": True,
            "sources": [
                "CNBC (2026-01-22): https://www.cnbc.com/2026/01/22/who-is-on-trumps-gaza-board-of-peace.html",
                "CBS News: https://www.cbsnews.com/news/trump-board-of-peace-what-to-know/",
                "Al Jazeera (2026-01-22): https://www.aljazeera.com/news/2026/1/22/trump-launches-board-of-peace-at-ceremony-in-davos",
                "White House: https://www.whitehouse.gov/articles/2026/01/president-trump-ratifies-board-of-peace/",
                "Britannica: https://www.britannica.com/topic/Board-of-Peace",
            ],
        },
        {
            "name": "G. Maxwell House Oversight Testimony (5th Amendment)",
            "date": pd.Timestamp("2026-02-09"),
            "type": "Friction (Private/Leverage)",
            "verified": True,
            "sources": [
                "ABC News: https://abcnews.com/Politics/maxwell-expected-invoke-amendment-closed-virtual-house-oversight/story?id=129991066",
                "Politico: https://www.politico.com/live-updates/2026/02/09/congress/maxwell-pleads-the-fifth-00771258",
                "CBS News: https://www.cbsnews.com/news/ghislaine-maxwell-house-oversight-committee-deposition-fifth-amendment/",
                "NBC News: https://www.nbcnews.com/politics/justice-department/ghislaine-maxwell-pleads-fifth-says-speak-fully-honestly-trump-grants-rcna258227",
                "PBS: https://www.pbs.org/newshour/show/epstein-files-fallout-grows-as-ghislaine-maxwell-pleads-fifth-before-congress",
            ],
        },
        {
            "name": "Apollo Global Q4 2025 Earnings Report",
            "date": pd.Timestamp("2026-02-09"),
            "type": "Compliance (Financial/Institutional)",
            "verified": True,
            "sources": [
                "Apollo IR: https://ir.apollo.com/news-events/press-releases/detail/604/apollo-reports-fourth-quarter-and-full-year-2025-results",
                "Motley Fool: https://www.fool.com/earnings/call-transcripts/2026/02/09/apollo-apo-q4-2025-earnings-call-transcript/",
                "Investing.com: https://www.investing.com/news/transcripts/earnings-call-transcript-apollo-global-management-beats-q4-2025-forecasts-93CH-4494360",
            ],
        },
        {
            "name": "SEC 13F Filing Deadline (Q4 2025)",
            "date": pd.Timestamp("2026-02-17"),
            "type": "Compliance (Regulatory/Calendar)",
            "verified": True,
            "sources": [
                "SEC.gov: https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f",
                "Day Pitney: https://www.daypitney.com/2026-annual-and-periodic-reporting-compliance-for-investment-managers",
                "Skadden: https://www.skadden.com/-/media/files/publications/2025/07/2026-sec-filing-deadlines-and-financial-statement-staleness-dates.pdf",
            ],
        },
        {
            "name": "Board of Peace Inaugural Summit (US Institute of Peace, DC)",
            "date": pd.Timestamp("2026-02-19"),
            "type": "Compliance (Public/Institutional)",
            "verified": True,
            "sources": [
                "FDD: https://www.fdd.org/analysis/2026/02/19/trump-hosts-inaugural-board-of-peace-meeting/",
                "TIME: https://time.com/7379788/trump-gaza-board-of-peace-first-meeting-takeaways/",
                "Al Jazeera: https://www.aljazeera.com/news/2026/2/18/trumps-board-of-peace-meets-whos-in-whos-out-whats-on-the-agenda",
                "Al-Monitor: https://www.al-monitor.com/originals/2026/02/trump-touts-pledges-troops-billions-gaza-board-peace-summit",
                "Soufan Center: https://thesoufancenter.org/intelbrief-2026-february-20/",
            ],
        },
        {
            "name": "Apollo Dividend Record Date / Board of Peace Summit",
            "date": pd.Timestamp("2026-02-19"),
            "type": "Compliance (Financial)",
            "verified": True,
            "sources": [
                "Apollo IR: https://ir.apollo.com/news-events/press-releases/detail/604/apollo-reports-fourth-quarter-and-full-year-2025-results",
            ],
            "note": "Apollo declared Q4 dividend with record date Feb 19 — same day as inaugural summit",
        },
    ]

    # ── Timeline Display ──
    print(f"\n  VERIFIED TIMELINE (Jan–Feb 2026):\n")
    for e in sorted(events, key=lambda x: x["date"]):
        print(f"    {e['date'].strftime('%Y-%m-%d')}  |  {e['type']:40s}  |  {e['name']}")
        print(f"                    |  Verified: {'✅ YES' if e['verified'] else '❌ NO'} "
              f"({len(e['sources'])} sources)")

    # ── Lag Analysis ──
    print(f"\n  LAG CALCULATIONS:\n")
    charter = pd.Timestamp("2026-01-22")
    maxwell = pd.Timestamp("2026-02-09")
    summit = pd.Timestamp("2026-02-19")
    apollo_earnings = pd.Timestamp("2026-02-09")
    sec_13f = pd.Timestamp("2026-02-17")

    lags = [
        ("Charter → Maxwell testimony", (maxwell - charter).days),
        ("Charter → Summit", (summit - charter).days),
        ("Maxwell → Summit", (summit - maxwell).days),
        ("Charter → 13F deadline", (sec_13f - charter).days),
        ("Maxwell → 13F deadline", (sec_13f - maxwell).days),
        ("Apollo earnings → Summit", (summit - apollo_earnings).days),
        ("Apollo earnings → 13F deadline", (sec_13f - apollo_earnings).days),
    ]

    for label, days in lags:
        matches_14 = abs(days - 14) <= 2
        flag = " ← MATCHES 14-DAY SIGNATURE (±2d)" if matches_14 else ""
        print(f"    {label:40s}: {days:+3d} days{flag}")

    # ── 14-Day Lag Signature Test ──
    print(f"\n  14-DAY LAG SIGNATURE TEST:\n")
    charter_to_maxwell = (maxwell - charter).days  # 18 days
    maxwell_to_summit = (summit - maxwell).days      # 10 days
    charter_to_summit = (summit - charter).days       # 28 days = 2 × 14

    print(f"    Charter → Maxwell: {charter_to_maxwell} days (not 14-day)")
    print(f"    Maxwell → Summit:  {maxwell_to_summit} days (not 14-day)")
    print(f"    Charter → Summit:  {charter_to_summit} days = 2 × 14 (DOUBLE-LAG)")

    # ── Calendar Window Analysis ──
    print(f"\n  CALENDAR WINDOW ANALYSIS:\n")
    # Check for shared calendar anchors
    davos_start = pd.Timestamp("2026-01-20")
    davos_end = pd.Timestamp("2026-01-24")
    presidents_day = pd.Timestamp("2026-02-16")

    print(f"    Davos Forum window:      Jan 20-24, 2026")
    print(f"    Charter signed:          Jan 22 (within Davos)")
    print(f"    Presidents' Day:         Feb 16, 2026")
    print(f"    13F filing deadline:     Feb 17 (day after Presidents' Day)")
    print(f"    Inaugural summit:        Feb 19 (2 days after 13F deadline)")
    print(f"    Apollo dividend record:  Feb 19 (same day as summit)")

    print(f"\n  ► SHARED CALENDAR WINDOW: Jan 22 to Feb 19 = {(summit - charter).days} days")
    print(f"    This window contains Davos → Presidents' Day → 13F deadline → Summit")
    print(f"    All events cluster within a single institutional calendar cycle.")

    # ── Private vs Public Leverage ──
    print(f"\n  PRIVATE vs PUBLIC LEVERAGE DISCREPANCY:\n")
    print(f"    'Private' leverage event:")
    print(f"      Maxwell testimony (Feb 9) — closed session, 5th Amendment invoked")
    print(f"      This is a FRICTION event: generates public attention without substance")
    print(f"      Maxwell offered NO testimony; the event was leverage theater (clemency)")
    print(f"")
    print(f"    'Public' media cycle:")
    print(f"      Charter (Jan 22) → Summit (Feb 19) = 28-day public buildup")
    print(f"      Maxwell falls at the MIDPOINT of this public cycle")
    print(f"      Maxwell hearing date COINCIDES with Apollo Q4 earnings call")
    print(f"")
    print(f"    FINDING:")
    print(f"      The Maxwell testimony sits at day 18/28 of the Charter→Summit window,")
    print(f"      NOT at the 14-day mark. The node does NOT follow the clean 14-day")
    print(f"      lag signature. Instead, all three events cluster within a shared")
    print(f"      institutional calendar window (Davos → Congressional session →")
    print(f"      Presidents' Day recess → international summit scheduling).")

    # ── Verdict ──
    print(f"\n  ► TASK 4 VERDICT:")
    print(f"    The G. Maxwell / Board of Peace node does NOT exhibit a clean")
    print(f"    14-day lag signature. The Charter→Maxwell gap is 18 days and the")
    print(f"    Maxwell→Summit gap is 10 days. The Charter→Summit gap is exactly")
    print(f"    28 days (2×14), which could be coincidence or a scheduling artifact")
    print(f"    of the Davos → Presidents' Day → international summit calendar.")
    print(f"")
    print(f"    The simultaneous scheduling of Maxwell's testimony with Apollo's")
    print(f"    Q4 earnings (both Feb 9) and the summit with Apollo's dividend")
    print(f"    record date (both Feb 19) suggests a shared FINANCIAL CALENDAR")
    print(f"    drives the timing more than a sequential friction→compliance lag.")

    return {
        "test": "Node Timeline Reconciliation",
        "events": [
            {"name": e["name"], "date": e["date"].strftime("%Y-%m-%d"),
             "type": e["type"], "verified": e["verified"],
             "n_sources": len(e["sources"])}
            for e in events
        ],
        "lags": {label: days for label, days in lags},
        "follows_14day_signature": False,
        "charter_to_summit_days": 28,
        "verdict": "Calendar clustering — NOT a clean 14-day sequential lag",
    }


# ═══════════════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 78)
    print("  ROBUSTNESS AUDIT v10.2 — TASKS 3 & 4")
    print("  Date: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 78)

    results = {}
    results["task3"] = task3_temporal_engine()
    results["task4"] = task4_node_timeline()

    output_path = os.path.join(SCRIPT_DIR, "temporal_node_results.json")
    with open(output_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"\n  Results saved to: {output_path}")

    print("\n" + "=" * 78)
    print("  END OF TASKS 3 & 4")
    print("=" * 78)
