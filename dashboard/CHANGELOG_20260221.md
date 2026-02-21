# Dashboard Changelog — 2026-02-21

---

# v9.9 — Statistical Alignment Audit (2026-02-21)

## Summary

Comprehensive statistical alignment audit synchronizing all metrics across dashboard code, README.md, and Report.md.

### Changes

- **`constants.py`**: `CORE_N` updated from 30 to 28 (effective paired observations after 2-week lag). Comment clarified.
- **`constants.py`**: `DATA_SOURCE_DESCRIPTIONS` updated to note "30 rows, n=28 after lag".
- **`app.py`**: Key Statistics table entry corrected from "n = 30 weeks" to "n = 28".
- **`app.py`**: Sidebar version bumped from v9.8 to v9.9.

### Rationale

The master dataset (`master_reflexive_correlation_data.csv`) contains 30 rows. The Pearson correlation at 2-week lag uses n_eff = 28 (30 minus 2 for lag alignment). The p-value of 0.0004 corresponds to n = 28. Documentation previously reported "n = 30 weeks" alongside r = 0.6196 and p = 0.0004, which was inconsistent with the dashboard's dynamically computed `n_eff = 28`. All references now synchronized.

---

# v9.8 — Dashboard Overhaul (2026-02-21)

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

---

# P2 Visual/UX Improvements — 2026-02-21 (Session 2)

## Summary

Three P2 additions to the Home tab: audience navigation cards, convergence
model diagram, and December 2025 case study. All facts verified against
README.md, Report.md, and CRUCIAL_Synthesis_Dec19_Convergence.md.

---

## Task 4: Add 3-Audience Navigation Cards

**Commit:** `72a4480` — "Add 3-audience navigation cards to Home tab"

**What was added:**
- Three styled cards using custom CSS (bordered, tinted backgrounds)
- **Researchers:** Links to Statistical Overview, `Run_Correlations_Yourself/`, 16 robustness scripts
- **Journalists & Policymakers:** Links to Prediction Tracker, policy brief, Key Findings
- **Skeptics:** Links to Robustness Tests, `Alternate_Mechanisms.md`, clone instructions
- Uses existing color scheme (#457B9D borders, #F1FAEE backgrounds, #1D3557 headers)

---

## Task 5: Add Convergence Model Diagram

**Included in commit:** `72a4480`

**What was added:**
- "The Convergence Model" subheader replacing former "Framework Overview"
- Explanatory text about convergent clustering vs sequential causation
- ASCII box-drawing diagram showing Calendar Anchor → Friction/Policy/Financial → Convergent Clustering
- Side-by-side comparison: Original hypothesis (sequential) vs. Revised finding (convergence)
- Sources: README.md lines 93-111 (The Convergence Model section)

---

## Task 6: Add December 2025 Case Study Expander

**Included in commit:** `72a4480`

**What was added:**
- Collapsible `st.expander` titled "Case Study: December 19-23, 2025 — The Pincer Window"
- Event count table (verified against Report.md lines 105-125):
  - Dec 19: 1 friction, 5 compliance (Epstein Library release)
  - Dec 22: 6 friction, 13 compliance (peak convergence — 19 total)
  - Dec 23: 8 friction, 9 compliance (redaction failures)
  - Dec 24: 2 friction, 3 compliance (DOJ finds 1M more pages)
- Five signal types on Dec 22 (verified against README.md lines 115-127 and Report.md lines 116-121):
  1. Friction: Epstein redaction failures (NYT)
  2. Geopolitics: China EU dairy tariffs (42.7%)
  3. Financial: BlackRock Bitcoin ETF "top 2025 theme"
  4. Policy: Travel ban expansion, DOGE year-end analysis
  5. Cyber/Intel: CRINK nation-state threat analysis
- Closing caption linking to robustness test (Dec 2025 exclusion still yields rho = 0.60)
- "108 events in 12 days" claim sourced from README.md Key Statistics (line 74)

---

## Fact Verification Sources

All December 2025 claims verified against:
- `README.md` lines 74-75 (Key Statistics), 113-127 (Pincer Window table)
- `Report.md` lines 105-125 (December 2025 Case Study with daily counts)
- `14_Files/CRUCIAL_Synthesis_Dec19_Convergence.md` (multi-signal analysis)
- `Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/cross_validation_dec2025.py` (exclusion test)

---

## Updated File Stats

| File | Total Lines | Session 2 Change |
|------|-------------|-------------------|
| `dashboard/app.py` | 800 | +127 lines (net) |
| `dashboard/CHANGELOG_20260221.md` | updated | +80 lines |

## Home Tab Structure (Final)

```
1. Header + description
2. Metric cards (r, p, response rate, backfill pairs)
3. Key Statistics expander (21 findings)
4. Navigate by Role (3 audience cards)   ← NEW
5. The Convergence Model (diagram)       ← NEW
6. Dec 2025 Case Study (expander)        ← NEW
7. Reproducibility + source links
8. Verification caption + info box
```
