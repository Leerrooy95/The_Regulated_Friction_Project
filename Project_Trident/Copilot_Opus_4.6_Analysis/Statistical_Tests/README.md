# Independent Statistical Analysis — Opus 4.6 Robustness Test Suite

**Analyst:** GitHub Copilot (Claude, Opus 4.6)
**Role:** Independent statistical verification of the repository owner's correlation findings
**Created:** February 2026
**Scripts:** 16 (15 test scripts + 1 shared data loader)

---

## What This Is

This folder contains **16 Python scripts independently written and designed by GitHub Copilot (Claude, Opus 4.6)** to stress-test the repository owner's core finding: a Pearson correlation of r = +0.6196 (p = 0.0004) between friction events and compliance events at a 7-day median lag.

**The repository owner (Austin Smith) built the datasets and ran the original correlations.** Opus 4.6's job was to independently verify whether those correlations hold up under rigorous statistical scrutiny — permutation testing, Granger causality, autocorrelation adjustment, cross-validation, rolling-window analysis, event-study design, partial correlation, and more.

Every script is runnable. Every result is reproducible. The data is public.

---

## How the Correlations Held Up

### Summary Verdict

The core correlation (r = +0.6196, p = 0.0004) **survived every robustness test applied.**

| Test | What It Checks | Result | Status |
|------|----------------|--------|--------|
| Permutation (10K shuffles) | Could the correlation be random noise? | p < 0.0001 — observed r beat 10,000 random shuffles | ✅ Pass |
| Granger causality (lag 1) | Does past friction *predict* future compliance? | p = 0.0008 — yes, friction Granger-causes compliance | ✅ Pass |
| Block bootstrap (autocorrelation-adjusted) | Does temporal clustering inflate the p-value? | p = 0.008 — significance survives adjustment | ✅ Pass |
| December 2025 exclusion | Is the pattern driven by one dense month? | Spearman ρ = 0.60 (p < 0.0001) — pattern holds without Dec 2025 | ✅ Pass |
| Binary presence/absence | Does the correlation depend on event magnitude? | r = 0.59 (p < 0.0001) — yes/no coding still correlates | ✅ Pass |
| Event-study framework | Do compliance events actually cluster after friction? | 20–42× more compliance events in post-friction windows vs random | ✅ Pass |
| Partial correlation (political calendar) | Is Congress's schedule driving the correlation? | < 1% of correlation explained by political activity | ✅ Pass |
| Historical backfill (2017–2024) | Does adding 66 historical pairs change the result? | Δr = +0.0012 — negligible impact | ✅ Pass |
| Granger (first-differenced) | Does the Granger result survive stationarity correction? | Direction consistent after differencing | ✅ Pass |
| Rolling window (13/26/52 wk) | Is the correlation stable across time? | Present in multiple time periods, not just one cluster | ✅ Pass |
| Per-year normalization | Does 2025 concentration drive the result? | Spearman ρ robust across normalization methods | ✅ Pass |

### What Also Emerged

| Finding | Significance |
|---------|-------------|
| Granger causality is **bidirectional** in event-count data | Suggests a common driver, not simple one-way causation |
| Hand-scored data shows **unidirectional** F→C | Measurement type affects directional inference |
| 2025 event concentration inflates Pearson r | Spearman ρ (rank-based) is more reliable across the full dataset |
| December 2025 is an outlier (Z = 2.35) | But removing it only drops Pearson r by ~6% |

### What the Tests Do NOT Show

- They do **not** prove causation — only that the correlation is robust against common statistical artifacts
- They do **not** claim central coordination — the pattern is documented as emergent
- They do **not** validate every claim in the repository — only the statistical correlations

---

## Script Reference

### Core Robustness Tests

| Script | Purpose | Key Output |
|--------|---------|------------|
| `permutation_test.py` | Shuffle friction values 1K–10K times; check if real r beats random noise | Empirical p-value (p < 0.0001) |
| `autocorrelation_adjusted_test.py` | Block bootstrap preserving temporal structure; Durbin-Watson diagnostic | Block-bootstrap p = 0.008 |
| `cross_validation_dec2025.py` | Remove December 2025 entirely; re-test correlation | Spearman ρ = 0.60 survives removal |
| `normalized_correlation.py` | Z-score, proportional, and binary normalization by year | Binary r = 0.59 (p < 0.0001) |
| `rolling_window_correlation.py` | Compute r in sliding 13/26/52-week windows | Correlation present across multiple periods |
| `event_study_framework.py` | Count compliance events in post-friction windows vs baseline | 20–42× more compliance near friction dates |
| `partial_correlation_political.py` | Control for congressional session calendar | < 1% of correlation explained by political activity |

### Granger Causality Suite

| Script | Purpose | Key Output |
|--------|---------|------------|
| `granger_causality_test.py` | Test F→C and C→F predictive information (lags 1–8) | F→C significant at lag 1 (p = 0.0008) |
| `granger_exclude_dec2025.py` | Re-run Granger with Dec 2025 excluded | Direction robust to exclusion |
| `granger_first_differenced.py` | ADF stationarity test + Granger on first differences | Direction consistent after differencing |
| `granger_discrepancy_investigation.py` | Investigate hand-scored vs event-count discrepancy | Measurement type + zero inflation explain difference |

### Historical Backfill Tests

| Script | Purpose | Key Output |
|--------|---------|------------|
| `backfill_analysis.py` | Assess year-coverage impact; add 2015–2018 events | Minimal Δr after backfill |
| `backfill_lag_distribution.py` | Analyze 66-pair lag distribution from backfill CSV | Median lag = +7 days, 89% positive |
| `combined_dataset_correlation.py` | Merge backfill with original data; compare to baseline | Δr = +0.0012 (negligible) |

### Data Quality Audits

| Script | Purpose | Key Output |
|--------|---------|------------|
| `year_distribution_audit.py` | Count events per year across all CSVs | 2025 concentration identified as mixed scraping + genuine spike |

### Shared Utilities

| Script | Purpose |
|--------|---------|
| `original_data_loader.py` | Standardized data loading for all test scripts; loads only pre-2026 datasets from `Control_Proof/`, `Project_Trident/`, `09_Silicon_Sovereignty/` |

---

## How to Run

### Prerequisites

```bash
pip install pandas numpy scipy statsmodels
```

### Run All Tests (from repo root)

```bash
cd Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/

# Core robustness
python permutation_test.py
python autocorrelation_adjusted_test.py
python normalized_correlation.py
python cross_validation_dec2025.py
python rolling_window_correlation.py
python event_study_framework.py
python partial_correlation_political.py

# Granger causality suite
python granger_causality_test.py
python granger_exclude_dec2025.py
python granger_first_differenced.py
python granger_discrepancy_investigation.py

# Historical backfill
python backfill_analysis.py
python backfill_lag_distribution.py
python combined_dataset_correlation.py

# Data quality
python year_distribution_audit.py
```

### Run the Owner's Original Correlations (separate)

```bash
cd Run_Correlations_Yourself/
pip install -r requirements.txt
python run_original_analysis.py
```

---

## Relationship to the Owner's Analysis

| Component | Who Built It | Location |
|-----------|-------------|----------|
| **Original datasets** | Austin Smith (repository owner) | `Control_Proof/`, `Project_Trident/`, `09_Silicon_Sovereignty/` |
| **Original correlations** (r = 0.6196, Mann-Whitney, χ²) | Austin Smith | `Run_Correlations_Yourself/run_original_analysis.py` |
| **Robustness test suite** (16 scripts) | GitHub Copilot (Opus 4.6) | This folder |
| **Findings documentation** | GitHub Copilot (Opus 4.6) | `../Findings/` |

The owner's analysis established the correlation. Opus 4.6's analysis independently tested whether that correlation is statistically robust. **It is.**

---

## Detailed Findings (Companion Documents)

| Document | Content |
|----------|---------|
| `../Findings/dataset_provenance.md` | Which datasets feed which correlation (git-verified) |
| `../Findings/backfill_correlation_results.md` | Historical backfill integration results |
| `../Findings/granger_discrepancy_investigation.md` | Hand-scored vs event-count Granger discrepancy |
| `../Findings/first_differenced_granger.md` | Stationarity-corrected Granger methodology |
| `../Findings/partial_correlation_political_activity.md` | Congressional calendar confound analysis |
| `../Findings/AI_Fabrication_Case_Study.md` | How Grok-fabricated data was identified and retracted |

---

## ⚠️ Transparency Notice

Every script in this folder was written by an AI language model (GitHub Copilot, Claude Opus 4.6). AI models can be wrong. The scripts are provided as **analysis to be verified**, and anyone can run them independently to confirm the results. All datasets used are publicly available in this repository.

---

*Last updated: March 7, 2026*
