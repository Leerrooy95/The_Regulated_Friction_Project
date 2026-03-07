# Methodology: Correlation Verification and Standards

**Purpose**: Documents the statistical methodology, verification standards, and how to interpret the r-values and significance tests used throughout this repository.

---

## v10.3 Precision Upgrade: From "14-Day Lag" to "7-Day Median Lag"

> **This is not a methodology change — it is a precision upgrade.**
>
> The underlying correlation (r = 0.6196, p = 0.0004) and all robustness tests are unchanged. What changed is the descriptive label applied to the lag:
>
> | Version | Resolution | Lag Label | Basis |
> |---------|-----------|-----------|-------|
> | **v10.2 Legacy** | 2-week index bins (n=30 rows, n=28 after lag) | "14-day lag" | Peak Pearson r at lag=2 bins |
> | **v10.3 High-Resolution** | Calendar-day backfill (n=66 pairs, 2017–2024) | "7-day median lag" | Actual measured median = 7 days (mean = 6.5) |
>
> The "14-day" figure was an artifact of the 2-week binning resolution used in the original 30-row index dataset. When the same events are measured at calendar-day resolution using the 66-pair historical backfill, the actual median response time is 7 days.
>
> **Evidence**: `04_Testing_and_Counters/ROBUSTNESS_AUDIT_v10.2.md`, `04_Testing_and_Counters/placebo_calendar_results.json`

---

## Key Claims

| Claim | Verification | Evidence Location |
|-------|--------------|-------------------|
| Primary correlation r = 0.6196 is reproducible | ✅ VERIFIED | `Run_Correlations_Yourself/run_original_analysis.py` |
| p-value = 0.0004 (n = 28) | ✅ VERIFIED | Same script |
| Multiple robustness tests pass (16 scripts) | ✅ VERIFIED | `Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/` |
| Independent verification by Opus 4.6 completed | ✅ VERIFIED | `Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/README.md` |

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

**Our finding (r = +0.6196)**: Strong positive correlation - when friction events spike, compliance events follow ~7 days later (median; measured at 2-week index resolution).

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

### Independent Verification by Opus 4.6

After the repository owner established the original correlations, **GitHub Copilot (Claude, Opus 4.6)** independently wrote and ran a suite of **16 statistical test scripts** to stress-test the findings. Opus 4.6 did not build the datasets or compute the original correlations — it received the data and designed its own tests to challenge them.

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
| Permutation (10K shuffles) | p < 0.0001 — observed r beat 10,000 random shuffles | ✅ Pass |
| Autocorrelation adjustment | Pearson p = 0.008 (block-bootstrap), Spearman ρ = 0.61 | ✅ Both survive |
| Dec 2025 exclusion | Pearson r drops 6%, Spearman ρ = 0.60 | ✅ Signal survives |
| Normalized (binary) | r = 0.59 (p < 0.0001) | ✅ Presence/absence holds |
| Event-study | Friction dates attract 20–42x more compliance | ✅ Strong colocation |
| Granger (hand-scored) | F→C at lag 1 (p = 0.0008), lag 2 (p = 0.027) | ✅ Predictive |
| Partial correlation (political calendar) | < 1% of correlation explained by congressional session | ✅ Not a confound |
| Granger (first-differenced) | Direction consistent after stationarity correction | ✅ Robust |
| Rolling window (13/26/52 wk) | Correlation present across multiple time periods | ✅ Not driven by one cluster |
| Historical backfill (66 pairs) | Δr = +0.0012 | ✅ Negligible impact |

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

## Lag=5 Negative Oscillation (r = −0.6064)

### Finding

The lag sweep reveals a strong **negative** correlation at lag=5 weeks:

```
Lag sweep on 30-row index (Pearson r):
  lag=0: r = −0.0323 (p = 0.8653)    — No simultaneous relationship
  lag=1: r = +0.5034 (p = 0.0054)    — Strong positive (emerging)
  lag=2: r = +0.6196 (p = 0.0004)    — PEAK positive ← Canonical finding
  lag=3: r = +0.2849 (p = 0.1497)    — Declining
  lag=4: r = −0.4069 (p = 0.0391)    — Reversal begins
  lag=5: r = −0.6064 (p = 0.0013)    — STRONG NEGATIVE ← Documented here
  lag=6: r = −0.3363 (p = 0.1081)    — Declining
```

### Theoretical Explanation: The Thermostat Cooling Cycle

The negative correlation at lag=5 is consistent with a **thermostat oscillation** — a self-regulating feedback loop in the friction→compliance system:

1. **Lag 0–2 (Heating phase):** A friction event creates an attention window. Compliance actors use this window to execute institutional changes. Friction and compliance move together (positive r).

2. **Lag 2 (Peak):** Maximum correlation. The compliance response is at its strongest. This is the 7-day median response window measured at index resolution.

3. **Lag 3–4 (Saturation):** The attention window closes. Media moves on. The friction "fuel" is exhausted. The correlation drops toward zero and begins inverting.

4. **Lag 5 (Cooling phase):** The system **overcorrects**. After a major compliance push (policy changes, financial moves), there is a period of institutional quiescence. Simultaneously, the absence of friction coverage may trigger a new friction event to maintain attention management. The result: high friction co-occurs with low compliance (and vice versa), producing a strong negative r.

5. **Lag 6+ (Reset):** The oscillation dampens and the system resets for the next cycle.

### Significance

- r = −0.6064 at lag=5 is **as statistically significant** as the primary finding (p = 0.0013 vs p = 0.0004)
- This suggests the friction→compliance system is **not one-directional** but oscillatory
- The full cycle is approximately **10 weeks** (peak-to-trough: lag 2 to lag 5 = 3 index bins)
- This oscillation is consistent with the "thermostat" metaphor: the system self-regulates to prevent either sustained attention or sustained compliance activity

### Implication

The "14-day lag" (now corrected to 7-day median) is only half the story. The full pattern is a **~10-week oscillation** where:
- Weeks 0–2: Friction → Compliance (positive coupling)
- Weeks 3–4: Transition/decorrelation
- Weeks 5–6: Friction → Anti-Compliance (negative coupling, "cooling off")

**Evidence**: `Run_Correlations_Yourself/run_original_analysis.py` (lag sweep), `04_Testing_and_Counters/ROBUSTNESS_AUDIT_v10.2.md`

---

## Business Cycle Artifact Check (v10.3)

### Finding

The weekday frequency analysis on the 66-pair backfill dataset reveals:

| Metric | Value | Expected by Chance |
|--------|-------|--------------------|
| Friction & compliance share SAME weekday | **30.3%** | 14.3% (1/7) |
| Lags that are exact multiples of 7 | **22.7%** | 14.3% |
| Friction events on Wednesday/Friday | **47.0%** | 28.6% |
| Compliance events on weekdays (Mon–Fri) | **97.0%** | 71.4% |

### Interpretation

The 7-day median lag is **partially** a business-cycle artifact. Events cluster on weekdays (compliance events almost never occur on weekends), and 30.3% of friction–compliance pairs share the same weekday (2.1x the expected rate). This "same-weekday" effect inflates the apparent 7-day signal.

However, the weekday effect does **not fully explain** the lag:
- Mean lag varies by friction weekday (Monday: 5.0d, Saturday: 9.3d), showing the lag is not a fixed weekday-to-weekday jump
- The chi-square test rejects uniform weekday distribution for both friction (p = 0.035) and compliance (p = 0.001), confirming systematic weekday clustering

### Verdict

The 7-day median lag is a **composite** of:
1. A genuine sequential friction→compliance response (~5–7 days)
2. A business-cycle anchoring effect (events snap to workdays)
3. Calendar-anchor clustering (71.2% of pairs share the same calendar anchor)

**Evidence**: `04_Testing_and_Counters/ROBUSTNESS_AUDIT_v10.2.md`

---

## Financial Anchor Alignment (v10.3)

### Finding (February 2026 Case Study)

Cross-referencing 11 February 2026 compliance events against Tier 1 entity financial anchors (BlackRock Q4 earnings, Apollo Q4 earnings, SEC 13F deadline, Apollo dividend record date):

| Metric | Value |
|--------|-------|
| Mean distance to nearest financial anchor | **1.7 days** |
| Median distance to nearest financial anchor | **2.0 days** |
| Events within 3 days of a financial anchor | **81.8%** |
| Events within 7 days of a financial anchor | **100%** |
| Events exactly on a financial anchor date | **5 of 11 (45.5%)** |

### Comparison

| Clustering Method | Mean Distance |
|-------------------|---------------|
| Financial anchors (Feb 2026) | **1.7 days** |
| 7-day sequential lag (backfill) | 6.5 days |
| Calendar anchors (holidays/solstices) | 5.6–6.5 days |

**Financial anchors provide 3.8x tighter clustering** than the sequential lag model. The February 2026 compliance window is better explained by the earnings/filing calendar of Tier 1 entities than by sequential friction→compliance reaction.

### Key Overlaps

- **Feb 9**: Apollo Q4 earnings = Maxwell testimony (same day)
- **Feb 17**: SEC 13F filing deadline
- **Feb 19**: Apollo dividend record date = Board of Peace inaugural summit (same day)

### Implication

For periods with dense financial anchors (earnings season, filing deadlines), the "financial calendar" is a stronger explanatory variable than the friction→compliance sequential lag. The 7-day median lag may represent the typical spacing between financial calendar events during earnings season, not a sequential reaction time.

**Evidence**: `04_Testing_and_Counters/temporal_node_reconciliation.py`, SEC EDGAR, Apollo IR

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

---

## Additional Methodology Resources

| Resource | Location | Content |
|----------|----------|---------|
| Scout methodology origin | `00_Quick_Breakdowns/About_Me.md` | Author's Army Cavalry Scout background → "Numbers Station" observational concept |
| 16 statistical test scripts | `Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/` | Permutation, autocorrelation, Granger, rolling window, event-study, partial correlation, and more |
| Dataset provenance | `Project_Trident/Copilot_Opus_4.6_Analysis/Findings/dataset_provenance.md` | Data origin documentation |
| AI fabrication case study | `Project_Trident/Copilot_Opus_4.6_Analysis/Findings/AI_Fabrication_Case_Study.md` | How Grok-fabricated data was identified and retracted (Layers 2-3) |
| Wrong correlations archive | `Run_Correlations_Yourself/Wrong_Correlations/` | Deprecated scripts that mixed datasets — preserved for transparency |
| Independent verification | `09_Silicon_Sovereignty/CRUCIAL-Cross_Verification_Check.md` | Cross-AI verification of Silicon Sovereignty claims |
| Validation report (Feb 24) | `docs/validation/VALIDATION_REPORT_2026-02-24.md` | External validation report |

*Updated March 2, 2026 (v10.3).*
