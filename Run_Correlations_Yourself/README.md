# Run Correlations Yourself

**Purpose:** Independent verification scripts for the reported correlations.

**Last Updated:** February 21, 2026

---

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Reproduce the three ORIGINAL correlations (pre-2026 datasets)
python run_original_analysis.py
```

---

## Scripts in This Folder

| Script | What It Reproduces | Datasets Used |
|--------|-------------------|---------------|
| `run_original_analysis.py` | Part 1: r = 0.6196 (2-week index lag, actual median: 7 days, n = 28)<br>Part 2: Mann-Whitney U p = 0.002<br>Part 3: χ² = 330.62 (7-day median periodicity) | Original pre-2026 CSVs from `Control_Proof/`, `Project_Trident/`, `09_Silicon_Sovereignty/` |

---

## Reported Correlations

| # | Correlation | Stat | Datasets | Script |
|---|-------------|------|----------|--------|
| 1 | Reflexive Control (2-week index lag; actual median: 7 days) | r = 0.6196 | 30-row master CSV | `run_original_analysis.py` Part 1 |
| 2 | Project Trident (ritual vs holiday proximity) | p = 0.002 | 533-row lag CSV | `run_original_analysis.py` Part 2 |
| 3 | Multi-Dataset Cross-Validation (7-day median periodicity) | χ² = 330.62 | 4 Silicon Sovereignty CSVs (2,102 records) | `run_original_analysis.py` Part 3 |

---

## Robustness Tests (Independent Opus 4.6 Analysis)

After the repository owner established the original correlations, **GitHub Copilot (Claude, Opus 4.6)** independently wrote a suite of 16 statistical test scripts to stress-test these findings. Opus 4.6 did not build the datasets or compute the original correlations — it received the data and designed its own tests to challenge them.

**The core correlation (r = +0.6196) survived every test.** Key results:

| Test | Result | Status |
|------|--------|--------|
| Permutation (10K shuffles) | p < 0.0001 | ✅ Pass |
| Granger causality (lag 1) | p = 0.0008 | ✅ Pass |
| Block bootstrap (autocorr-adjusted) | p = 0.008 | ✅ Pass |
| December 2025 exclusion | ρ = 0.60 | ✅ Pass |
| Binary presence/absence | r = 0.59 | ✅ Pass |
| Event-study framework | 20–42× above baseline | ✅ Pass |
| Partial correlation (political calendar) | < 1% explained | ✅ Pass |

For the full robustness test suite (16 scripts), see:

```bash
cd Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/
python permutation_test.py                   # Shuffle-based significance
python autocorrelation_adjusted_test.py      # Block bootstrap
python normalized_correlation.py             # Per-year normalized correlation
python cross_validation_dec2025.py           # Dec 2025 exclusion test
python rolling_window_correlation.py         # Sliding-window analysis
python event_study_framework.py              # Compliance response analysis
python granger_causality_test.py             # Predictive direction test
python partial_correlation_political.py      # Congressional calendar confound
```

→ **Full documentation**: [Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/README.md](../Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/README.md)

---

## Wrong_Correlations/ Subfolder

The `Wrong_Correlations/` subfolder contains archived scripts that are preserved for transparency:

- **`reproduce_updated_correlation.py`** — ⚠️ DEPRECATED. Previously produced r = 0.6685 using New_Data_2026 datasets. This correlation was produced in early January 2026 when the user accidentally mixed New_Data_2026 datasets into verification scripts. This was a user dataset-mixing error, not an AI computation error.
- **`reproduce_original_correlation.py`** and **`independent_statistical_verification.py`** — Had hardcoded paths to `/home/user/Epstein_Files_Uses_Theory/New_Data_2026/` instead of using relative paths to the correct original datasets.
- **`run_original_analysis.py`** — Archived copy (the corrected version is in the main folder).
- **`DISCREPANCY_ANALYSIS.md`** — Methodology comparison (still informative for understanding the r = 0.6685 → r = 0.6192 discrepancy).

---

*Last updated: February 21, 2026*
