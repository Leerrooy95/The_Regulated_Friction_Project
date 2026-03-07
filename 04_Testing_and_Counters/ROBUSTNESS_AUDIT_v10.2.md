# Robustness and Methodology Audit — Project v10.2

**Date:** March 2, 2026
**Scope:** Stress-test the primary findings of the Regulated Friction Project
**Standard:** Same adversarial rigor applied to the State Policy Analysis v1.4

---

## Executive Summary

This audit applied four independent stress tests to the Regulated Friction Project's core 14-day lag finding. The results are mixed and demand honest interpretation:

| Test | Result | Implication |
|------|--------|-------------|
| **Placebo (Permutation)** | r = 0.6196 survives 10,000 shuffles (p = 0.0004) | ✅ The correlation is **real**, not random noise |
| **Calendar-Anchor** | 71.2% of event pairs share the same calendar anchor | ⚠️ The lag is **partially explained** by calendar clustering |
| **Temporal Engine** | Weekday adjustment reduces lag by 28.2% but does NOT collapse it | ✅ The lag is a genuine sequential phenomenon, not a scheduling artifact |
| **Node Timeline** | Maxwell/Board of Peace does NOT follow the 14-day signature | ⚠️ Events cluster around a shared **financial calendar window** |

**Bottom line:** The friction→compliance correlation (r = 0.6196) is statistically genuine. However, the "14-day lag" label is misleading — the actual median lag in the backfill data is **7.0 days** (mean: 6.5 days). Calendar anchors explain *where* events cluster but not *why* they are sequenced. The lag is real, but it is closer to a **one-week institutional response** than the claimed two-week lag.

---

## Task 1: Placebo & Calendar-Anchor Test

### Part A: Placebo Test (Permutation Shuffle)

**Method:** Randomly shuffled the compliance indices 10,000 times and recomputed Pearson r at the 2-week lag. If the observed r = 0.6196 is a statistical artifact, random shuffles should produce equally strong correlations.

**Result:**
```
Observed r = 0.6196 at 2-week lag (parametric p = 0.0004)

Permuted distribution (n = 10,000, seed = 42):
  Mean  = -0.0006
  Std   = 0.1915
  95th percentile = 0.3195
  Max   = 0.6198

|permuted| ≥ |observed|: 3 / 10,000
Empirical p-value: 0.0004
```

**Verdict:** ✅ **SIGNIFICANT.** Only 3 of 10,000 random shuffles produced a correlation as strong as the observed r = 0.6196. The correlation is not a random artifact.

### Part B: Calendar-Anchor Test

**Method:** Using the 66-pair historical backfill dataset (2017–2024), computed each event's distance to its nearest calendar anchor (solstices, holidays, fiscal deadlines, 13F filings). Tested whether friction and compliance events share the same anchor.

**Result:**
```
Mean distance to nearest anchor:
  Friction events:   5.6 days
  Compliance events: 6.5 days

Events within 7 days of a calendar anchor:
  Friction:   81.8%
  Compliance: 65.2%

Friction & compliance share the SAME nearest anchor: 71.2%

Correlation between observed lag and anchor-distance difference:
  Pearson r = 0.1562 (p = 0.2105) — NOT significant
```

**Verdict:** ⚠️ **CALENDAR CLUSTERING DETECTED.** 71.2% of event pairs share the same nearest calendar anchor, meaning both the friction and compliance events in a pair are scheduled near the same holiday, fiscal deadline, or solstice. However, the lag *length* does not correlate with anchor proximity (r = 0.16, NS), meaning the calendar determines *when* events occur but not *how long* the gap between them lasts.

### ⚠️ Critical Data Concern: "14-Day Lag" Label

The backfill dataset reveals the actual lag distribution:

| Metric | Value |
|--------|-------|
| Mean observed lag | **6.5 days** |
| Median observed lag | **7.0 days** |
| Range | -3 to +15 days |

The "14-day lag" terminology comes from the 2-week shift applied to the 30-row index dataset (where each row represents one week). This 2-week shift maximizes the Pearson r. However, when actual calendar dates are used from the 66-pair backfill, the typical response time is **7 days**, not 14 days. The claim should be revised to "**approximately one-week institutional response lag**" or qualified as "**optimal at the 2-week index resolution**."

---

## Task 2: AI Noise & Source Provenance Audit

### Methodology

Audited all 7 CSV files in `New_Data_2026/` (2,121 total records) for:
1. AI-generated content in sources
2. Single-source reliance
3. Missing source URLs
4. February 2026 event verification

### Findings

| File | Records | Source Quality | Issues |
|------|---------|---------------|--------|
| **Additional_Anchors_Jan2026_Final.csv** | 52 | Mixed | 🚨 `oreateai.com/blog/` citation (row 11) — this is an AI content mill with Scam Detector score 45.3/100 and Trustpilot rating 1.8/5 |
| **Biopharma.csv** | 20 | ✅ Strong | All sources are Reuters, FDA.gov, Stat News, NYT |
| **BlackRock_Timeline_Full_Decade.csv** | 20+ | ✅ Strong | Institutional sources: OECD, WSJ, SEC, CSIS |
| **CRINK_Intelligence_Dataset_Final_Verified.csv** | 36 | ✅ Strong | 10/36 entries from CSIS (28%), remainder from Atlantic Council, Bush Center, CNN, NYT, JSTOR, RSIS — good diversity for a niche geopolitical topic |
| **High_Growth_Companies_2015_2026.csv** | 1,049 | ✅ Strong | Hand-scraped dataset with diverse primary sources (Nature, PubMed, ClinicalTrials.gov, Yahoo Finance, SEC, LinkedIn). 1 of 1,049 rows (0.1%) uses a Perplexity.ai link for Cellectis stock data — negligible |
| **Infrastructure_Forensics.csv** | 109 | ⚠️ Moderate | YouTube, Facebook used for specific news clips (Pope Francis death, DOGE announcement) — lower authority than direct sources but not AI-generated; 5 rows with missing date fields |
| **Timeline_Update_Jan2026_Corrected.csv** | 99 | ✅ Strong | NPR, AP, Reuters, NYT |

### 🚨 AI-Generated Noise Identified

1. **`oreateai.com/blog/`** (Additional_Anchors row 11): This is a confirmed AI content generation platform with:
   - Scam Detector score: 45.3/100 ([source](https://www.scam-detector.com/validator/oreateai-com-review/))
   - Trustpilot rating: 1.8/5 ([source](https://www.trustpilot.com/review/www.oreateai.com))
   - Hidden domain ownership
   - **Recommendation:** REMOVE this entry or replace with a primary source

2. **`Perplexity.ai`** (High_Growth_Companies row 503): A single Perplexity link out of 1,049 rows (0.1%) in a hand-scraped dataset. This is a negligible issue — the dataset overwhelmingly cites primary sources (Nature, PubMed, ClinicalTrials.gov, SEC filings, Yahoo Finance, LinkedIn).
   - **Recommendation:** Replace this single row's source with SEC EDGAR or Bloomberg link when convenient — not urgent

### February 2026 Compliance Event Verification

**Verified independently via financial filings and regulatory records:**

| Event | Date | Source Type | Independently Verified? |
|-------|------|------------|------------------------|
| Apollo Global Q4 2025 Earnings | Feb 9, 2026 | SEC filing / IR press release | ✅ Yes — [Apollo IR](https://ir.apollo.com/news-events/press-releases/detail/604/) |
| SEC 13F Filing Deadline (Q4 2025) | Feb 17, 2026 | SEC regulatory calendar | ✅ Yes — [SEC.gov FAQ](https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f) |
| Board of Peace Inaugural Summit | Feb 19, 2026 | Government / media | ✅ Yes — 5+ independent sources (TIME, Al Jazeera, FDD, PBS) |
| Palvella QTORIN™ Publication | Feb 2, 2026 | Scientific publication | ✅ Yes — [Manila Times / GlobeNewswire](https://www.manilatimes.net/2026/02/02/tmt-newswire/globenewswire/palvella-therapeutics-announces-scientific-publication/) |
| Abivax ECCO 2026 Presentation | Feb 21, 2026 | Medical conference | ✅ Yes — [TMCNet](https://www.tmcnet.com/usubmit/2026/02/21/10335950.htm) |

**Not independently verified (media flashbangs):**
- No February 2026 compliance events in `New_Data_2026/` CSVs rely solely on secondary media. The 2026 analysis primarily covers December 2025–January 2026 events.

---

## Task 3: Temporal Engine Adaptation

### Background

The State Policy Analysis repo's `temporal_engine.py` found that when you control for the *scheduled* trigger date (rather than the *observed* occurrence date), the apparent lag between triggers and federal responses collapsed to 0.00 days — meaning the correlation was driven by simultaneous scheduling, not sequential causation.

### Application to Regulated Friction

**Sample size increase:**
```
Original index dataset:   n_eff = 28 (weekly index scores)
Backfill event pairs:     n = 66 (2.4x increase)
Unique friction triggers: 29
Unique compliance actions: 65
```

**Trigger date control (grouping by unique friction event):**
```
Median of trigger-median lags: 6.0 days
Mean of trigger-median lags:   6.8 days
```

**Weekday adjustment (snapping triggers to nearest Monday):**
```
Original mean lag:    6.5 days
Adjusted mean lag:    4.7 days
Reduction:            28.2%
```

### Verdict

❌ **The lag does NOT collapse to zero.** Unlike the State Policy Analysis finding, controlling for trigger scheduling reduces the Regulated Friction lag by only 28.2% (from 6.5 to 4.7 days). The lag persists as a **genuine sequential phenomenon**. This is actually a *stronger* finding for the project — the friction→compliance sequence is not simply simultaneous scheduling.

**However**, the persistent lag is ~5–7 days, not 14 days. The "14-day" label derives from the 2-week index resolution, not from actual calendar-day measurements.

### Lag Sweep Confirmation

```
Lag sweep on 30-row index (Pearson r):
  lag=0: r = -0.0323 (p = 0.8653)
  lag=1: r = +0.5034 (p = 0.0054)
  lag=2: r = +0.6196 (p = 0.0004)  ← PEAK
  lag=3: r = +0.2849 (p = 0.1497)
  lag=4: r = -0.4069 (p = 0.0391)
  lag=5: r = -0.6064 (p = 0.0013)
  lag=6: r = -0.3363 (p = 0.1081)
```

The peak at lag=2 (weeks) is confirmed. The strong negative correlation at lag=5 is also notable — it suggests an oscillating "thermostat" pattern where friction leads compliance by ~2 weeks, then overcorrects at ~5 weeks.

---

## Task 4: Node Timeline Reconciliation

### Verified Timeline

All dates verified via multiple independent sources (March 2, 2026):

| Date | Event | Type | Sources |
|------|-------|------|---------|
| **2026-01-22** | Board of Peace Charter Signing (Davos) | Compliance (Public) | CNBC, CBS, Al Jazeera, White House, Britannica |
| **2026-02-09** | G. Maxwell House Oversight Testimony | Friction (Private) | ABC News, Politico, CBS, NBC, PBS |
| **2026-02-09** | Apollo Global Q4 2025 Earnings Report | Compliance (Financial) | Apollo IR, Motley Fool, Investing.com |
| **2026-02-17** | SEC 13F Filing Deadline (Q4 2025) | Compliance (Regulatory) | SEC.gov, Day Pitney, Skadden |
| **2026-02-19** | Board of Peace Inaugural Summit (DC) | Compliance (Public) | FDD, TIME, Al Jazeera, Al-Monitor, Soufan Center |
| **2026-02-19** | Apollo Q4 Dividend Record Date | Compliance (Financial) | Apollo IR |

### Lag Analysis

```
Charter → Maxwell testimony:  +18 days (NOT 14-day)
Charter → Summit:             +28 days (= 2 × 14, DOUBLE-LAG)
Maxwell → Summit:             +10 days (NOT 14-day)
Charter → 13F deadline:       +26 days
Maxwell → 13F deadline:        +8 days
Apollo earnings → Summit:     +10 days
```

### Finding: Calendar Window, Not Sequential Lag

The G. Maxwell / Board of Peace node does **NOT** exhibit a clean 14-day lag signature:

- **Charter → Maxwell = 18 days** (4 days longer than the claimed 14-day lag)
- **Maxwell → Summit = 10 days** (4 days shorter)
- **Charter → Summit = 28 days** (exactly 2 × 14, possibly coincidental)

Instead, all events cluster within a **shared institutional calendar window**:
1. **Jan 20–24:** Davos Forum → Charter signed Jan 22
2. **Feb 9:** Maxwell testimony ∧ Apollo Q4 earnings (same day)
3. **Feb 16–17:** Presidents' Day ∧ 13F filing deadline
4. **Feb 19:** Inaugural summit ∧ Apollo dividend record date

### Private vs Public Leverage Discrepancy

Maxwell's testimony (Feb 9) is a **friction event** — it generated maximum media attention but yielded zero substantive testimony (5th Amendment invoked 12+ times). The simultaneous scheduling with Apollo's Q4 earnings call suggests the date was chosen for **financial calendar compatibility**, not as a response to the Board of Peace charter.

The private leverage event (Maxwell) and the public compliance events (charter, summit) are **anchored to the same institutional calendar** (Davos → Congressional session → Presidents' Day recess → international summit), not linked by a sequential reaction mechanism.

---

## Data Concerns

The following concerns were identified during this audit:

### 🚨 Critical

1. **"14-Day Lag" Misnomer:** The backfill data shows a median lag of **7 days**, not 14. The "14-day" terminology comes from the 2-week index resolution. This should be corrected in `01_CORE_THEORY.md`, `intelligence_config.json`, and all public-facing claims. The actual finding is a **~7-day institutional response lag** that peaks at 2-week index resolution.

2. **AI-Generated Source (oreateai.com):** Entry in `Additional_Anchors_Jan2026_Final.csv` cites an AI content mill with trust score 45.3/100. This entry should be removed or re-sourced.

3. **Single Perplexity.ai Link (High_Growth_Companies row 503):** 1 of 1,049 rows (0.1%) in a hand-scraped dataset uses a Perplexity.ai link for Cellectis stock data. The dataset otherwise cites primary sources (Nature, PubMed, ClinicalTrials.gov, SEC filings). Low priority.

### ⚠️ Moderate

4. **CSIS Concentration in CRINK Dataset:** 10 of 36 entries (28%) from CSIS. While CSIS is a reputable think tank and CRINK is a niche topic with limited coverage, the remaining entries are well-diversified (Atlantic Council, Bush Center, CNN, NYT, JSTOR, RSIS).

5. **Social Media News Clips (Infrastructure_Forensics):** 11 of 109 rows cite YouTube or Facebook links. These are for specific news clips (Pope Francis death announcement, DOGE statements) rather than random social posts, but direct government or news outlet links would be more authoritative.

6. **Missing Date Fields:** 5 entries in `Infrastructure_Forensics.csv` have empty date fields, making them unusable for temporal analysis.

7. **Oscillating Pattern Not Documented:** The lag sweep shows strong negative correlation at lag=5 (r = -0.6064, p = 0.0013), suggesting a thermostat oscillation. This is as statistically significant as the positive lag=2 finding but is not discussed in the core theory documentation.

### ℹ️ Informational

8. **No February 2026 Events in New_Data_2026 CSVs:** Despite the directory name, the CSV files primarily cover events through January 2026. February 2026 compliance events exist in other files (09_CURRENT_THREADS.md, Report.md) but are not in the structured CSV data.

9. **Backfill Sample Size (n=66):** While 2.4x the original index sample, 66 pairs with 29 unique friction events is still a modest dataset for strong causal claims. The one-to-many mapping (single friction events spawning multiple compliance events) inflates the apparent sample size.

---

## Task 5: Weekday Frequency Distribution (Business Cycle Audit)

*Added in v10.3*

### Question

Is the 7-day median lag simply a "Friday News Dump → Friday Deal Close" artifact of the work week?

### Method

Computed weekday frequency distributions for all 66 friction and compliance events. Tested whether friction–compliance pairs share the same weekday at rates above chance (14.3% = 1/7).

### Results

**Friction Events (n=66):**
| Day | Count | % |
|-----|-------|---|
| Monday | 10 | 15.2% |
| Tuesday | 8 | 12.1% |
| **Wednesday** | **17** | **25.8%** |
| Thursday | 7 | 10.6% |
| **Friday** | **14** | **21.2%** |
| Saturday | 6 | 9.1% |
| Sunday | 4 | 6.1% |

**Compliance Events (n=66):**
| Day | Count | % |
|-----|-------|---|
| Monday | 14 | 21.2% |
| Tuesday | 14 | 21.2% |
| Wednesday | 12 | 18.2% |
| Thursday | 13 | 19.7% |
| Friday | 11 | 16.7% |
| Saturday | 0 | 0.0% |
| Sunday | 2 | 3.0% |

**Key Finding:** 30.3% of friction–compliance pairs share the same weekday (expected: 14.3%, ratio: 2.1×). Lags that are exact multiples of 7: 22.7% (expected: 14.3%).

**Chi-square uniformity test:**
- Friction weekday distribution: χ² = 13.55, p = 0.035 (non-uniform)
- Compliance weekday distribution: χ² = 22.03, p = 0.001 (strongly non-uniform — compliance avoids weekends)

### Verdict

⚠️ **PARTIAL WORK-WEEK ARTIFACT DETECTED.** The 7-day median lag is inflated by the business cycle: compliance events cluster on weekdays (97% Mon–Fri) while friction events cluster on Wednesday and Friday. However, the lag is not purely a weekday artifact — mean lag varies by friction weekday (Monday: 5.0d, Saturday: 9.3d), showing genuine variation beyond a fixed weekly cycle.

---

## Task 6: Financial Anchor Alignment (February 2026)

*Added in v10.3*

### Question

Do financial calendar anchors (earnings calls, SEC filing deadlines, dividend dates) provide a stronger explanatory cluster than the 7-day sequential lag?

### Method

Cross-referenced 11 February 2026 compliance events against verified financial anchors for Tier 1 entities:

| Anchor | Date | Source |
|--------|------|--------|
| BlackRock Q4 2025 Earnings | Jan 15, 2026 | [BlackRock IR](https://ir.blackrock.com/news-and-events/press-releases/press-releases-details/2025/BlackRock-to-Report-Fourth-Quarter-2025-Earnings-on-January-15th/) |
| Apollo Q4 2025 Earnings | Feb 9, 2026 | [Apollo IR](https://ir.apollo.com/news-events/press-releases/detail/604/) |
| SEC 13F Filing Deadline | Feb 17, 2026 | [SEC.gov](https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/) |
| Apollo Dividend Record Date | Feb 19, 2026 | [Apollo IR](https://ir.apollo.com/news-events/press-releases/detail/604/) |
| Oracle Q3 FY2026 Earnings | Mar 9, 2026 | [MarketBeat](https://www.marketbeat.com/earnings/reports/2026-3-9-oracle-co-stock/) |

### Results

| Metric | Value |
|--------|-------|
| Mean distance to nearest financial anchor | **1.7 days** |
| Median distance | **2.0 days** |
| Within 3 days of a financial anchor | **81.8%** |
| Within 7 days | **100%** |
| Exactly on a financial anchor date | **5 of 11 (45.5%)** |

**Comparison of clustering methods:**

| Method | Mean Distance to Nearest Anchor |
|--------|-------------------------------|
| **Financial anchors (Feb 2026)** | **1.7 days** |
| Sequential lag (backfill median) | 6.5 days |
| Calendar anchors (holidays/solstices) | 5.6–6.5 days |

Financial anchors provide **3.8× tighter clustering** than the sequential lag model.

### Key Simultaneous Events

- **Feb 9:** Apollo Q4 earnings = Maxwell testimony (same day)
- **Feb 17:** SEC 13F filing deadline
- **Feb 19:** Apollo dividend record date = Board of Peace inaugural summit (same day)

### Verdict

✅ **FINANCIAL ANCHORS ARE THE STRONGER EXPLANATORY VARIABLE** for the February 2026 compliance window. The events are better explained by the earnings/filing calendar of Tier 1 entities than by a sequential friction→compliance reaction. This does not invalidate the 7-day sequential lag for the historical backfill, but it suggests that during dense financial calendar periods, the "financial calendar hypothesis" may be primary.

---

## Reproducibility

All analyses in this audit are fully reproducible:

```bash
# Task 1: Placebo & Calendar-Anchor Test
python 04_Testing_and_Counters/placebo_calendar_anchor_test.py

# Tasks 3 & 4: Temporal Engine & Node Timeline
python 04_Testing_and_Counters/temporal_node_reconciliation.py
```

Machine-readable results are saved to:
- `04_Testing_and_Counters/placebo_calendar_results.json`
- `04_Testing_and_Counters/temporal_node_results.json`

---

## References

All web-verified sources used in this audit:

1. ABC News — Maxwell invokes 5th Amendment: https://abcnews.com/Politics/maxwell-expected-invoke-amendment-closed-virtual-house-oversight/story?id=129991066
2. Politico — Maxwell pleads the Fifth: https://www.politico.com/live-updates/2026/02/09/congress/maxwell-pleads-the-fifth-00771258
3. CBS News — Maxwell testimony: https://www.cbsnews.com/news/ghislaine-maxwell-house-oversight-committee-deposition-fifth-amendment/
4. NBC News — Maxwell 5th Amendment: https://www.nbcnews.com/politics/justice-department/ghislaine-maxwell-pleads-fifth-says-speak-fully-honestly-trump-grants-rcna258227
5. PBS — Epstein files fallout: https://www.pbs.org/newshour/show/epstein-files-fallout-grows-as-ghislaine-maxwell-pleads-fifth-before-congress
6. CNBC — Board of Peace members: https://www.cnbc.com/2026/01/22/who-is-on-trumps-gaza-board-of-peace.html
7. CBS News — Board of Peace: https://www.cbsnews.com/news/trump-board-of-peace-what-to-know/
8. Al Jazeera — Board of Peace Davos: https://www.aljazeera.com/news/2026/1/22/trump-launches-board-of-peace-at-ceremony-in-davos
9. White House — Board of Peace: https://www.whitehouse.gov/articles/2026/01/president-trump-ratifies-board-of-peace/
10. Britannica — Board of Peace: https://www.britannica.com/topic/Board-of-Peace
11. FDD — Inaugural summit: https://www.fdd.org/analysis/2026/02/19/trump-hosts-inaugural-board-of-peace-meeting/
12. TIME — Five takeaways: https://time.com/7379788/trump-gaza-board-of-peace-first-meeting-takeaways/
13. Al Jazeera — Summit agenda: https://www.aljazeera.com/news/2026/2/18/trumps-board-of-peace-meets-whos-in-whos-out-whats-on-the-agenda
14. Soufan Center — Board of Peace analysis: https://thesoufancenter.org/intelbrief-2026-february-20/
15. Apollo IR — Q4 2025 results: https://ir.apollo.com/news-events/press-releases/detail/604/apollo-reports-fourth-quarter-and-full-year-2025-results
16. SEC.gov — 13F FAQ: https://www.sec.gov/rules-regulations/staff-guidance/division-investment-management-frequently-asked-questions/frequently-asked-questions-about-form-13f
17. Scam Detector — oreateai.com review: https://www.scam-detector.com/validator/oreateai-com-review/
18. Trustpilot — oreateai.com: https://www.trustpilot.com/review/www.oreateai.com

---

## Cross-Reference: Opus 4.6 Independent Robustness Suite

In addition to the four stress tests in this audit, **GitHub Copilot (Claude, Opus 4.6)** independently wrote and ran **16 statistical test scripts** covering permutation testing, Granger causality (multiple variants), autocorrelation-adjusted bootstrap, event-study analysis, rolling-window correlation, partial correlation, historical backfill, and per-year normalization. The core correlation (r = +0.6196) survived every test.

→ **Full test suite and results**: `Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/README.md`
