#!/usr/bin/env python3
"""
Partial Correlation Controlling for Political Activity Index
Purpose: Test whether the friction-compliance correlation survives after
         controlling for a "political activity" proxy based on the
         congressional session calendar.

Future Recommendation item:
    "Partial correlation controlling for a 'political activity' index
     (e.g., congressional session calendar)"

Rationale: Both friction and compliance events may cluster during periods
of high political activity (e.g., when Congress is in session, during
budget debates, confirmation hearings, etc.).  If a political activity
index explains most of the co-movement, the friction-compliance
correlation is confounded — it reflects shared timing with the political
calendar, not a direct friction→compliance mechanism.

Political Activity Index construction:
  - Congressional session weeks score higher than recess weeks
  - Typical annual pattern: Jan-Jul in session (with short recesses),
    Aug recess, Sep-Dec in session (with breaks)
  - Major recess periods: Presidents' Day (Feb), Easter (Mar/Apr),
    Memorial Day (May), July 4th, August recess, Columbus Day (Oct),
    Thanksgiving (Nov), Christmas/New Year (Dec-Jan)

Source: US Senate Dates of Sessions (senate.gov), Congress.gov calendars,
        Congressional Research Service reports on legislative calendars.

Datasets used: original pre-2026 datasets via original_data_loader.py
"""

import os
import warnings
import pandas as pd
import numpy as np
from scipy.stats import pearsonr, spearmanr

from original_data_loader import (
    load_friction_events, load_compliance_events, build_weekly_counts, REPO_ROOT
)

warnings.filterwarnings('ignore', category=FutureWarning)


def build_political_activity_index(weekly_index):
    """Build a political activity index based on congressional session calendar.

    Uses the well-documented annual congressional pattern:
      - Jan-Jul: In session (high activity), with 1-week recesses around
        Presidents' Day, Easter, Memorial Day
      - Aug: Recess (low activity)
      - Sep-mid Oct: In session (high activity)
      - Late Oct-early Nov: Recess around elections
      - Mid Nov-mid Dec: Lame duck / end-of-session (high activity)
      - Late Dec: Holiday recess (low activity)

    Scores range from 0 (recess) to 1 (peak session).
    """
    scores = []
    for period in weekly_index:
        ts = period.start_time
        month = ts.month
        day = ts.day
        week_of_year = ts.isocalendar()[1]

        # Base score by month (in-session months = 0.7-1.0, recess = 0.1-0.3)
        if month == 1:
            # New Congress convenes; State of the Union prep
            score = 0.8 if day > 7 else 0.5  # first week is organizing
        elif month == 2:
            # In session but Presidents' Day recess (mid-Feb)
            score = 0.5 if 14 <= day <= 21 else 0.8
        elif month == 3:
            # In session; possible Easter recess at end
            score = 0.8
        elif month == 4:
            # Easter/Passover recess (typically 2 weeks early-mid April)
            score = 0.4 if day <= 14 else 0.8
        elif month == 5:
            # In session; Memorial Day recess last week
            score = 0.5 if day >= 25 else 0.9
        elif month == 6:
            # Peak legislative session (appropriations, NDAA)
            score = 1.0
        elif month == 7:
            # In session early July; July 4 recess; back late July
            score = 0.3 if 1 <= day <= 7 else 0.8
        elif month == 8:
            # August recess — lowest activity
            score = 0.1
        elif month == 9:
            # Back in session after Labor Day
            score = 0.3 if day <= 7 else 0.9
        elif month == 10:
            # In session early; Columbus Day recess; election prep
            score = 0.7
        elif month == 11:
            # Election season; Thanksgiving recess; lame duck starts
            score = 0.4 if 20 <= day <= 30 else 0.6
        elif month == 12:
            # Lame duck session early Dec; holiday recess mid-late Dec
            score = 0.8 if day <= 15 else 0.2
        else:
            score = 0.5

        scores.append(score)

    return np.array(scores)


def partial_correlation(x, y, z):
    """Compute partial correlation between x and y, controlling for z.

    Uses the standard formula:
        r_xy.z = (r_xy - r_xz * r_yz) / sqrt((1 - r_xz²)(1 - r_yz²))
    """
    r_xy, _ = pearsonr(x, y)
    r_xz, _ = pearsonr(x, z)
    r_yz, _ = pearsonr(y, z)

    numerator = r_xy - r_xz * r_yz
    denominator = np.sqrt((1 - r_xz**2) * (1 - r_yz**2))

    if denominator == 0:
        return float('nan'), float('nan')

    r_partial = numerator / denominator

    # Approximate p-value using t-test
    n = len(x)
    df = n - 3  # 3 variables
    if df <= 0:
        return r_partial, float('nan')
    t_stat = r_partial * np.sqrt(df / (1 - r_partial**2))
    from scipy.stats import t as t_dist
    p_value = 2 * t_dist.sf(abs(t_stat), df)

    return r_partial, p_value


# ── Load data ────────────────────────────────────────────────────────────
print("=" * 70)
print("PARTIAL CORRELATION — CONTROLLING FOR POLITICAL ACTIVITY")
print("=" * 70)
print("\nTests whether friction-compliance correlation survives after")
print("controlling for the congressional session calendar.")
print("Datasets: original pre-2026 via original_data_loader.py\n")

friction_events = load_friction_events()
compliance_events = load_compliance_events()
weekly = build_weekly_counts(friction_events, compliance_events)
f_series = weekly['friction'].values.astype(float)
c_series = weekly['compliance'].values.astype(float)
n = len(f_series)

# Build political activity index
pol_index = build_political_activity_index(weekly.index)

# ── Correlations ─────────────────────────────────────────────────────────
print(f"\n{'═' * 70}")
print(f"  STEP 1: BIVARIATE CORRELATIONS")
print(f"{'═' * 70}")
print(f"  Weeks: {n}\n")

r_fc, p_fc = pearsonr(f_series, c_series)
rho_fc, p_rho_fc = spearmanr(f_series, c_series)
print(f"  Friction vs Compliance:")
print(f"    Pearson  r = {r_fc:.4f} (p = {p_fc:.6f})")
print(f"    Spearman ρ = {rho_fc:.4f} (p = {p_rho_fc:.6f})")

r_fp, p_fp = pearsonr(f_series, pol_index)
rho_fp, _ = spearmanr(f_series, pol_index)
print(f"\n  Friction vs Political Activity:")
print(f"    Pearson  r = {r_fp:.4f} (p = {p_fp:.6f})")
print(f"    Spearman ρ = {rho_fp:.4f}")

r_cp, p_cp = pearsonr(c_series, pol_index)
rho_cp, _ = spearmanr(c_series, pol_index)
print(f"\n  Compliance vs Political Activity:")
print(f"    Pearson  r = {r_cp:.4f} (p = {p_cp:.6f})")
print(f"    Spearman ρ = {rho_cp:.4f}")

# ── Partial correlation ──────────────────────────────────────────────────
print(f"\n\n{'═' * 70}")
print(f"  STEP 2: PARTIAL CORRELATION (controlling for political activity)")
print(f"{'═' * 70}")

r_partial, p_partial = partial_correlation(f_series, c_series, pol_index)
print(f"\n  Friction-Compliance | controlling for Political Activity:")
print(f"    Partial r = {r_partial:.4f} (p = {p_partial:.6f})")
print(f"    Raw r     = {r_fc:.4f}")
change = r_fc - r_partial
pct_change = (change / abs(r_fc)) * 100 if r_fc != 0 else 0
print(f"    Change: {change:+.4f} ({pct_change:+.1f}%)")

if abs(change) < 0.01:
    print(f"\n  ✅ Political activity explains ALMOST NONE of the correlation.")
    print(f"     The friction-compliance relationship is independent of the")
    print(f"     congressional calendar.")
elif abs(pct_change) < 20:
    print(f"\n  ✅ Political activity explains only a SMALL portion ({pct_change:.0f}%).")
    print(f"     Most of the friction-compliance correlation is independent of")
    print(f"     the congressional calendar.")
elif abs(pct_change) < 50:
    print(f"\n  ⚠️ Political activity explains a MODERATE portion ({pct_change:.0f}%).")
    print(f"     The congressional calendar is a confound but doesn't fully")
    print(f"     account for the friction-compliance relationship.")
else:
    print(f"\n  ⚠️ Political activity explains MOST ({pct_change:.0f}%) of the correlation.")
    print(f"     The friction-compliance co-movement may largely reflect shared")
    print(f"     timing with the political calendar rather than a direct mechanism.")

# ── Seasonal analysis ────────────────────────────────────────────────────
print(f"\n\n{'═' * 70}")
print(f"  STEP 3: SEASONAL BREAKDOWN")
print(f"{'═' * 70}")

week_starts = weekly.index.to_timestamp()
months = week_starts.month

print(f"\n  {'Month':>7} {'Friction':>10} {'Compliance':>12} {'Pol Index':>11} {'Both>0':>8}")
print(f"  {'─' * 48}")
for m in range(1, 13):
    mask = months == m
    if mask.sum() == 0:
        continue
    f_m = f_series[mask]
    c_m = c_series[mask]
    p_m = pol_index[mask]
    both_nonzero = ((f_m > 0) & (c_m > 0)).sum()
    month_name = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'][m]
    print(f"  {month_name:>7} {f_m.mean():>10.2f} {c_m.mean():>12.2f} "
          f"{p_m.mean():>11.2f} {both_nonzero:>8}")

# ── Subperiod analysis ───────────────────────────────────────────────────
print(f"\n\n{'═' * 70}")
print(f"  STEP 4: SESSION vs RECESS PERIODS")
print(f"{'═' * 70}")

in_session = pol_index >= 0.7
recess = pol_index <= 0.3

for label, mask in [('In session (activity ≥ 0.7)', in_session),
                     ('Recess (activity ≤ 0.3)', recess)]:
    f_sub = f_series[mask]
    c_sub = c_series[mask]
    n_sub = len(f_sub)
    if n_sub < 5 or f_sub.std() == 0 or c_sub.std() == 0:
        print(f"\n  {label}: {n_sub} weeks — insufficient variation")
        continue
    r_sub, p_sub = pearsonr(f_sub, c_sub)
    rho_sub, p_rho_sub = spearmanr(f_sub, c_sub)
    print(f"\n  {label}: {n_sub} weeks")
    print(f"    Pearson  r = {r_sub:.4f} (p = {p_sub:.6f})")
    print(f"    Spearman ρ = {rho_sub:.4f} (p = {p_rho_sub:.6f})")

# ── Also test the 30-row master ─────────────────────────────────────────
print(f"\n\n{'═' * 70}")
print(f"  STEP 5: 30-ROW MASTER CSV (for comparison)")
print(f"{'═' * 70}")

data_path = os.path.join(REPO_ROOT, 'Control_Proof',
                         'master_reflexive_correlation_data.csv')
if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    friction_hs = df['Epstein_Friction_Index'].values.astype(float)
    compliance_hs = df['Institutional_Compliance_Index'].values.astype(float)
    n_hs = len(df)

    # The 30-row dataset doesn't have explicit dates, so we can't directly
    # map it to the congressional calendar.  Instead, we use the week index
    # to create a synthetic political activity proxy.
    # Assumption: 30 weeks ≈ 7 months, likely covering a single congressional
    # session window.
    week_indices = df['Week_Index'].values
    # Simple oscillating proxy (session-recess-session pattern over 30 weeks)
    pol_proxy = 0.5 + 0.3 * np.sin(2 * np.pi * week_indices / 12)

    r_raw, p_raw = pearsonr(friction_hs, compliance_hs)
    r_part, p_part = partial_correlation(friction_hs, compliance_hs, pol_proxy)

    print(f"\n  30-row master (using synthetic political activity proxy):")
    print(f"    Raw Pearson  r = {r_raw:.4f} (p = {p_raw:.4f})")
    print(f"    Partial      r = {r_part:.4f} (p = {p_part:.4f})")
    print(f"    Change: {r_raw - r_part:+.4f}")
    print(f"\n    NOTE: The 30-row dataset has no date labels, so this uses")
    print(f"    a synthetic oscillating proxy — interpret with caution.")

# ── Bottom line ──────────────────────────────────────────────────────────
print(f"\n\n{'═' * 70}")
print(f"  BOTTOM LINE")
print(f"{'═' * 70}")
print(f"""
  The political activity index (based on the congressional session calendar)
  is tested as a confounding variable for the friction-compliance correlation.

  If political activity explains most of the correlation, then friction and
  compliance events are simply both more likely during busy political periods
  (Congress in session, budget debates, confirmation hearings) — and the
  correlation reflects shared timing rather than a direct mechanism.

  If the partial correlation remains strong after controlling for political
  activity, then friction and compliance co-move even within periods of
  similar political activity — supporting a direct mechanism.

  Sources for congressional calendar:
    - US Senate Dates of Sessions: senate.gov/legislative/DatesofSessionsofCongress.htm
    - Congress.gov Floor Calendars: congress.gov/calendars-and-schedules
    - CQ Roll Call Congressional Calendar (annual PDFs)
""")
print("=" * 70)
