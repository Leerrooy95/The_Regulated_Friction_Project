# Dashboard Changelog — 2026-02-21

## Summary

Three HIGH priority additions implemented based on comprehensive dashboard audit.
All changes preserve existing functionality, disclaimer language, and color scheme.

---

## Task 0: Consolidate zyte-deploy Spider Files

**Result:** No action needed. All 6 target files (`doj_press_releases.py`,
`federal_register_eo.py`, `items.py`, `settings.py`, `pipelines.py`, `scrapy.cfg`)
were already identical between `zyte-deploy` and `main` branches following the
prior merge commit (`156c56f`). Imports verified successfully.

---

## Task 1: Add Prediction Tracker Tab

**Commit:** `a538421` — "Add Prediction Tracker tab with status badges"

**File changed:** `dashboard/app.py` (+90 lines)

**What was added:**
- New "Prediction Tracker" tab (6th tab, after Raw Data Explorer)
- 25 predictions sourced from README.md Testable Predictions table
- Summary metric cards: 11 Confirmed / 4 Failed / 10 Pending
- Prominent "Failed Predictions" section showing all 4 failed 13F predictions
- Filterable "All Predictions" table with status multiselect
- Rationale text emphasizing falsifiability and intellectual honesty
- Each prediction includes: Prediction, Timeframe, Status, Date Added

**Predictions by status:**
- 11 confirmed (event clustering, Tu BiShvat, Mandelson, BoP summit, annexation, etc.)
- 4 failed (PIF EA, Mubadala defense, Gulf SWF Oracle/defense, Gulf SWF Q4)
- 10 pending/tracking (DOGE instability, TikTok, Khanna, NTEU, Schedule P/C, etc.)

---

## Task 2: Add Key Statistics Table to Home Tab

**Commit:** `d397d2b` — "Add Key Statistics table to Home tab"

**File changed:** `dashboard/app.py` (+43 lines)

**What was added:**
- Collapsible `st.expander` titled "Key Findings (21 Verified)" on Home tab
- Positioned after the 4 metric cards, before Framework Overview
- 21-row table matching README.md Key Statistics exactly
- Conditional row styling: green tint for verified, red tint for failed
- Caption noting 20/21 verified and 1 entry documenting 3 failed predictions

**Key findings surfaced:**
- Core correlation, significance, ritual proximity, Project Trident
- Cross-validation chi-square, December 2025 cluster, event colocation
- January/February 2026 signal data, enforcement hollowing, Apollo pipeline
- 13F failures, Mubadala Bitcoin ETF, Board of Peace, historical backfill

---

## Task 3: Add Robustness Summary to Statistical Overview

**Commit:** `51ffe2a` — "Add Robustness Summary to Statistical Overview"

**File changed:** `dashboard/app.py` (+23 lines)

**What was added:**
- "Robustness Tests" subheader at top of Statistical Overview tab
- 6-row table showing test name, result, and pass/fail status
- Caption explaining the core correlation survives all adversarial tests
- Link to full scripts directory

**Tests displayed:**
| Test | Result | Status |
|------|--------|--------|
| Permutation (30-row, 1K shuffles) | r = 0.62, p < 0.001 | Pass |
| Permutation (multi-dataset, 10K shuffles) | rho = 0.61, p < 0.0001 | Pass |
| Granger causality (lag 1) | p = 0.0008 | Pass |
| Granger causality (lag 2) | p = 0.027 | Pass |
| Block bootstrap (autocorrelation-adjusted) | p = 0.008 | Pass |
| Dec 2025 exclusion | rho = 0.60, p < 0.0001 | Signal survives |

---

## Files Modified

| File | Lines Added | Lines Removed |
|------|-------------|---------------|
| `dashboard/app.py` | +156 | -1 |
| `dashboard/CHANGELOG_20260221.md` | (new) | — |

## Tab Structure (After Changes)

```
Home | Statistical Overview | Time Series & Scatter | Lag Distribution | Raw Data Explorer | Prediction Tracker
```

## No Breaking Changes

- All existing tabs, charts, controls, and data loading preserved
- Disclaimer language unchanged
- Color scheme unchanged (Red/Steel Blue/Teal/Navy)
- Reproducibility links preserved
- Sidebar controls unchanged
