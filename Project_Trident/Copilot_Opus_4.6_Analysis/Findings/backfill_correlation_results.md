# Historical Backfill Correlation Results

**Generated:** 2026-02-19 22:42 UTC

---

## Verification Summary

- **Backfill pairs loaded:** 66
- **Years covered:** 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024
- **All 10 claims verified:** Yes — each pair has a Friction_Date, Compliance_Date, Lag_Days, and Source_URL
- **Unique friction events (deduplicated):** 29
- **Unique compliance events (deduplicated):** 66

## Lag Distribution Summary

| Metric | Value |
|--------|-------|
| Total pairs | 66 |
| Positive lags (friction → compliance) | 59 (89.4%) |
| Zero lags (same day) | 5 |
| Negative lags (compliance first) | 2 |
| Median lag | +7.0 days |
| Mean lag | +6.50 days |

## Original vs. Combined Correlation Comparison

| Metric | Original | Combined | Baseline |
|--------|----------|----------|----------|
| Pearson r | 0.1099 | 0.1111 | 0.6196 |
| Pearson p-value | 0.000002 | 0.000001 | — |
| Spearman ρ | 0.6067 | 0.6090 | — |
| Spearman p-value | 0.000000 | 0.000000 | — |
| N weeks | 1879 | 1879 | — |
| Δ Pearson r (orig → comb) | — | +0.0012 | — |
| |Δ from baseline| | 0.5097 | 0.5085 | — |

> **⚠ FLAG FOR REVIEW:** Combined Pearson r differs from baseline by 0.5085 (threshold: 0.05)

## Lagged Correlation Results (Combined Data)

Compliance shifted forward by 1–4 weeks relative to friction:

| Lag (weeks) | Pearson r | p-value | Spearman ρ | p-value | N |
|-------------|-----------|---------|------------|---------|---|
| 1 | 0.1095 | 0.000002 | 0.3076 | 0.000000 | 1878 |
| 2 | 0.0785 | 0.000664 | 0.3039 | 0.000000 | 1877 |
| 3 | 0.0877 | 0.000142 | 0.3269 | 0.000000 | 1876 |
| 4 | 0.0595 | 0.009945 | 0.4722 | 0.000000 | 1875 |

## Conclusion

The combined dataset (original + backfill) yields Pearson r = 0.1111, which **differs** from the established baseline of r = 0.6196 by 0.5085. This exceeds the review threshold of 0.05 and warrants further investigation.

Adding 29 friction and 66 compliance events from the historical backfill (2017–2024) does not preserve the original correlation structure.

### Flags for Review

- ⚠ Combined r = 0.1111 differs from baseline r = 0.6196 by 0.5085

