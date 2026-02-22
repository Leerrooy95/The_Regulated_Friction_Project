# Methodology: Correlation Verification and Standards

**Purpose**: Documents the statistical methodology, verification standards, and how to interpret the r-values and significance tests used throughout this repository.

---

## Key Claims

| Claim | Verification | Evidence Location |
|-------|--------------|-------------------|
| Primary correlation r = 0.6196 is reproducible | ✅ VERIFIED | `Run_Correlations_Yourself/run_original_analysis.py` |
| p-value = 0.0004 (n = 28) | ✅ VERIFIED | Same script |
| Multiple robustness tests pass | ✅ VERIFIED | `Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/` |
| Independent verification completed | ✅ VERIFIED | `14_Files/VERIFICATION_REPORT_Jan2026.md` |

---

## How to Reproduce the Analysis

### Quick Start
```bash
cd Run_Correlations_Yourself/
pip install -r requirements.txt
python run_original_analysis.py
```

### What the Script Produces

**Part 1**: r = 0.6196 (2-week lag, n = 28) - Primary correlation
**Part 2**: Mann-Whitney U p = 0.002 - Project Trident
**Part 3**: χ² = 330.62 (14-day periodicity) - Cross-validation

---

## Understanding the Statistics

### Pearson Correlation (r)

| r Value | Interpretation |
|---------|----------------|
| 0.0 | No relationship |
| ±0.1-0.3 | Weak |
| ±0.3-0.5 | Moderate |
| ±0.5-0.7 | **Strong** |
| ±0.7-1.0 | Very strong |

**Our finding (r = +0.6196)**: Strong positive correlation - when friction events spike, compliance events follow ~14 days later.

### p-value Interpretation

| p-value | Interpretation |
|---------|----------------|
| p > 0.05 | Not statistically significant |
| p < 0.05 | Statistically significant |
| p < 0.01 | Highly significant |
| p < 0.001 | **Extremely significant** |

**Our finding (p = 0.0004)**: Less than 0.05% probability this occurred by chance.

### Granger Causality

Tests whether one time series helps **predict** another.

| Lag | F-statistic | p-value | Significant? |
|-----|-------------|---------|--------------|
| 1 | 32.49 | < 0.0001 | YES |
| 2 | 14.74 | < 0.0001 | YES |
| 3 | 8.68 | < 0.0001 | YES |
| 4 | 6.43 | < 0.0001 | YES |

**Interpretation**: Friction events significantly **predict** compliance events at all lags tested.

---

## Robustness Tests

### Test Suite Location
`Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/`

### Available Scripts

| Script | Purpose |
|--------|---------|
| `permutation_test.py` | Shuffle-based significance |
| `autocorrelation_adjusted_test.py` | Block bootstrap |
| `normalized_correlation.py` | Per-year normalized correlation |
| `cross_validation_dec2025.py` | Dec 2025 exclusion test |
| `rolling_window_correlation.py` | Sliding-window analysis |
| `event_study_framework.py` | Compliance response analysis |
| `granger_causality_test.py` | Predictive direction test |

### Results Summary

| Test | Result | Verdict |
|------|--------|---------|
| Permutation (1K shuffles) | r = 0.62 significant (p < 0.001) | ✅ Pass |
| Autocorrelation adjustment | Pearson p = 0.008 (block-bootstrap), Spearman ρ = 0.61 | ✅ Both survive |
| Dec 2025 exclusion | Pearson r drops 6%, Spearman ρ = 0.60 | ✅ Signal survives |
| Normalized (binary) | r = 0.59 (p < 0.0001) | ✅ Presence/absence holds |
| Event-study | Friction dates attract 20–42x more compliance | ✅ Strong colocation |
| Granger (hand-scored) | F→C at lag 1 (p = 0.0008), lag 2 (p = 0.027) | ✅ Predictive |

---

## Dataset Scope and Classification

### Friction Events (attention-consuming)
- Epstein-related releases and coverage
- Political events and media reactions
- Crisis events
- DOGE/FDA conflict events

### Compliance Events (policy/financial positioning)
- Policy and geopolitics
- Government ties
- Strategic shifts
- Crypto pivots
- FDA/regulatory changes
- Financial performance indicators

### What's Excluded from Primary Correlation

**High_Growth_Companies_2015_2026.csv** (1,049 records) is excluded because:
- Contains operational events (clinical milestones, earnings)
- These follow medical/market schedules, not strategic calendar exploitation
- Including them dilutes r = 0.6685 to r = 0.5268

**Location**: `14_Files/TRANSPARENCY_NOTE_FOR_2026_ANALYSIS.md`

---

## Verification Levels

Throughout the repository, claims are marked:

| Mark | Meaning |
|------|---------|
| ✅ VERIFIED | Confirmed through multiple independent sources |
| ⚠️ PARTIALLY VERIFIED | Some evidence supports; needs more verification |
| 🔍 HYPOTHESIS | Proposed but not yet verified |
| ❌ FAILED | Prediction did not materialize |

---

## Scout Methodology

**Core Approach**: Observe and report patterns without claiming intent or coordination.

**What it does**:
- Documents patterns
- Notes correlations
- Flags timing
- Verifies through multiple sources

**What it doesn't do**:
- Claim conspiracy
- Assert intent
- Accuse individuals of coordination

---

## Multi-AI Verification

**Process**: Cross-checking findings across multiple AI systems (Claude, Grok, Gemini) to identify blind spots or biases.

**Why**: Different AI systems have different training data. Convergent findings are more robust.

---

## Source Triangulation

**Standard**: Major claims require verification from at least two independent sources.

**Source Types Used**:
| Type | Examples |
|------|----------|
| Government primary | DHS.gov, SEC filings, DOJ releases |
| Wire services | AP, AFP, Reuters |
| Major outlets | NPR, CNN, Bloomberg, WSJ |
| Investigative | ProPublica, Byline Times |
| International | France24, Al Jazeera |

---

## Known Limitations

1. **Event classification subjectivity**: What counts as "friction" vs "compliance" involves judgment
2. **Autocorrelation present**: High temporal clustering (r = 0.67 at lag 1 for friction)
3. **Outlier sensitivity**: December 2025 disproportionately influential
4. **Dataset mixing errors**: See `Run_Correlations_Yourself/Wrong_Correlations/` for archived mistakes

---

## Common Questions

### Why r = 0.6196 vs r = 0.6685?

| Correlation | Dataset | Scope |
|-------------|---------|-------|
| r = 0.6196 | 30-week hand-scored | Original pre-2026 data |
| r = 0.6685 | 1,027 strategic events | 2026 raw event counts |
| r = 0.5268 | 2,069 total events | Including operational events |

All three are valid for their scopes. The 0.6196 is the canonical reference.

### What about autocorrelation?

High autocorrelation (r = 0.67) means friction events cluster temporally. This is controlled for via block bootstrap (p = 0.008) and first-differenced Granger tests.

### What about December 2025?

Removing December 2025 drops Pearson r by 6% but Spearman ρ remains 0.60. The pattern survives exclusion.

---

## Key Sources

| Document | Location |
|----------|----------|
| Run Correlations README | `Run_Correlations_Yourself/README.md` |
| Original analysis script | `Run_Correlations_Yourself/run_original_analysis.py` |
| Verification Report | `14_Files/VERIFICATION_REPORT_Jan2026.md` |
| Transparency Note | `14_Files/TRANSPARENCY_NOTE_FOR_2026_ANALYSIS.md` |
| Glossary | `14_Files/Glossary.md` |

---

## Cross-References

- **For core theory**: `01_CORE_THEORY.md`
- **For datasets**: `08_KEY_DATASETS.md`
- **For statistical tests**: `Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/`

---

## Quick Facts

| Fact | Value |
|------|-------|
| Primary correlation | r = +0.6196 |
| Sample size | n = 28 (after lag) |
| Significance | p = 0.0004 |
| Granger F-statistic (lag 1) | 32.49 |
| December 2025 Z-score | 2.35 (top 1% of months) |

---

*This summary distills content from `Run_Correlations_Yourself/`, `14_Files/VERIFICATION_REPORT_Jan2026.md`, `14_Files/TRANSPARENCY_NOTE_FOR_2026_ANALYSIS.md`, and `14_Files/Glossary.md`.*
