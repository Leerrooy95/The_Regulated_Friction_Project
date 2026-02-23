# The Regulated Friction Project v10.0

A data-driven analysis of temporal correlations between friction events, policy shifts, and capital flows (2015-2026).

**Live Dashboard**: [regulatedfriction.streamlit.app](https://regulatedfriction.streamlit.app)

| Quick Links | |
|-------------|---|
| **New here?** | [Glossary](14_Files/Glossary.md) |
| **AI Assistant?** | [_AI_CONTEXT_INDEX/00_START_HERE.md](_AI_CONTEXT_INDEX/00_START_HERE.md) |
| **In a rush?** | [Consolidation Pattern Significance](Project_Trident/Copilot_Opus_4.6_Analysis/Consolidation_Analysis/consolidation_pattern_significance.md) |
| **Run it yourself** | [Run_Correlations_Yourself/](Run_Correlations_Yourself/) |

---

## Core Finding

**Friction events predict compliance events at a 2-week lag.**

| Metric | Value |
|--------|-------|
| Correlation | r = +0.6196 |
| Significance | p = 0.0004 |
| Sample | n = 28 paired observations (30-week dataset) |

When high-visibility friction events spike (document releases, scandals, media cycles), institutional compliance events (policy shifts, financial moves, regulatory changes) follow ~14 days later. This relationship has less than 0.05% probability of occurring by chance.

**What this does NOT claim:** Central coordination, conspiracy, or intentional orchestration. The pattern is emergent — multiple actors exploiting the same environmental signals (holidays, fiscal deadlines, media saturation) without requiring communication between them. Correlation ≠ causation. The claim is structural: the pattern exists and is statistically significant.

---

## Understanding the Statistics

| r Value | Interpretation |
|---------|----------------|
| 0.0 | No relationship |
| ±0.3-0.5 | Moderate |
| **±0.5-0.7** | **Strong** ← Our finding |
| ±0.7-1.0 | Very strong |

The correlation is reproducible — run the scripts in `Run_Correlations_Yourself/` yourself.

---

## Key Statistics (Summary)

| Category | Finding | Status |
|----------|---------|--------|
| **Core Correlation** | r = +0.6196 at 2-week lag (p = 0.0004) | ✅ Verified |
| **Ritual Proximity** | 50.7% vs. 19.9% baseline (2.5x) | ✅ Verified |
| **Cross-validation** | χ² = 330.62 (p < 0.0001, 2,102 events) | ✅ Verified |
| **Historical Backfill** | 66 pairs across 2017-2024; Δr = +0.0012 (negligible impact) | ✅ Verified |
| **Q4 2025 13F Predictions** | 3 predictions tested | ❌ All 3 FAILED |
| **Board of Peace Summit** | ~50 countries, $7B pledged, $10B US | ✅ Confirmed |

→ **Full statistics table**: [14_Files/Key_Statistics.md](14_Files/Key_Statistics.md)

**Note on failed predictions:** The Q4 2025 13F predictions (Gulf SWF positioning) failed. This is documented transparently — negative findings are data.

---

## AI Context Index

The `_AI_CONTEXT_INDEX/` directory provides structured context for AI assistants and researchers:

| File | Content |
|------|---------|
| `00_START_HERE.md` | Navigation guide, Dual-Track System, Cartel Statecraft Model |
| `01_CORE_THEORY.md` | Thermostat model, 14-day lag, convergence pattern, framework validation |
| `02_MEDIA_FIREWALL.md` | 1789 Capital, TCN, narrative infrastructure |
| `03_BOARD_OF_PEACE.md` | Private diplomacy, Kushner, Witkoff, capital pipeline |
| `04_CAPITAL_ARCHITECTURE.md` | Gulf SWF pipelines, DATA Act, AVAIO Arkansas |
| `05_CRINK_FRAMEWORK.md` | China-Russia-Iran-NK coordination patterns |
| `06_MAIN_CHARACTERS.md` | Performative actors as noise generators |
| `07_METHODOLOGY.md` | Correlation methodology, verification standards |
| `08_KEY_DATASETS.md` | CSV schemas and data file reference |
| `09_CURRENT_THREADS.md` | Active leverage nodes (Maxwell, Iran, Gulf SWFs, Israel) |
| `10_FRAMEWORK_VALIDATION.md` | High-profile statements validating framework |

---

## Repository Structure

```
The_Regulated_Friction_Project/
├── 00_Quick_Breakdowns/          # Executive summaries
├── 01_Levers_and_Frictions/      # Control mechanisms, Epstein timeline
├── 02_Anchors_and_Financials/    # Financial anchor analysis
├── 03_Master_Framework/          # Core theory (2015-2025)
├── 04_Testing_and_Counters/      # Backtesting, counter-hypotheses
├── 05_Geopolitical_Vectors/      # Global election analysis, Venezuela
├── 06_Visualizations/            # Charts, diagrams
├── 07_My_Previous_Epstein_Research/  # Prior investigations (PDFs)
├── 08_How_It's_Possible/         # Methodological deep dives
├── 09_Silicon_Sovereignty/       # Tech geopolitics, VOCA funding
├── 10_Real-Time_Updates_and_Tasks/   # Daily logs (Jan-Feb 2026)
├── 11_Protest_Dynamics_and_Funding/  # Protest funding audits
├── 12_The_Media_Firewall/        # Media control, 1789 Capital analysis
├── 13_State_and_County_Analysis/ # Arkansas infrastructure audit
├── 14_Files/                     # Glossary, sources, main characters
├── _AI_CONTEXT_INDEX/            # Structured context for AI assistants
├── Project_Trident/              # Independent verification (Opus 4.6)
├── Run_Correlations_Yourself/    # Reproducibility scripts
├── New_Data_2026/                # 2026 datasets
├── federal_register/             # Scrapy spiders (automated scraping)
└── dashboard/                    # Streamlit dashboard source
```

---

## What's New (v10.0) — February 2026

- **Total Actor and Timeline Synthesis**: Repository-wide audit of 7 Tier 1 entities across Tech/AI, Diplomacy, Defense, Finance, Media domains
- **Statistical alignment audit**: n-count synchronized to n = 28 effective; verified r = 0.6196 against master dataset
- **Israel leverage node added**: Completes four-node architecture (Maxwell, Iran, Gulf SWFs, Israel) in `09_CURRENT_THREADS.md`
- **Dual-Track System documentation**: Track A (Information Leverage) + Track B (Capital Leverage) framework in context index
- **Framework validation statements**: Obama, Massie, Sanders quotes added to `01_CORE_THEORY.md`
- **Historical backfill complete**: 66 friction→compliance pairs (2017-2024) with negligible correlation impact

→ **Full changelog**: [CHANGELOG.md](CHANGELOG.md)

---

## Robustness Tests

The core correlation survives multiple validation methods:

| Test | Result |
|------|--------|
| Permutation (10K shuffles) | p < 0.0001 |
| Granger causality (lag 1) | p = 0.0008 |
| Block bootstrap (autocorrelation-adjusted) | p = 0.008 |
| December 2025 exclusion | ρ = 0.60 (pattern holds) |
| Binary presence/absence | r = 0.59 |

→ **Full robustness analysis**: [Project_Trident/Copilot_Opus_4.6_Analysis/](Project_Trident/Copilot_Opus_4.6_Analysis/)

---

## Key Questions

These questions arise from documented patterns and verified data:

1. Why does the same capital entity (1789 Capital) fund both the Media Firewall (TCN, PublicSq) and enforcement layer (Anduril) pitched to Saudi defense?

2. Why does Resolution 2803 place the ISF under Board of Peace command rather than UN peacekeeping — with the Chairman given personal appointment authority?

3. Why does the Board of Peace function as a corporate investment vehicle (verified PIF → Affinity → Phoenix → settlements → Gaza pipeline) while presenting as a diplomatic body?

4. Why does the most strategically significant financial architecture operate entirely below the SEC 13F visibility threshold?

5. Why was the Schedule Policy/Career rule published despite 94% public comment opposition — during the Epstein files media cycle?

6. Why did PIF concentrate from 57 US equity positions to just 6 in a single quarter — and where did the exited capital go?

→ **Full question list**: [Report.md](Report.md#key-questions)

---

## For Different Audiences

| Audience | Start Here |
|----------|------------|
| **Researchers** | [Project_Trident/](Project_Trident/) — Independent verification, robustness tests |
| **Journalists** | [14_Files/How_This_Happened-A_Policy_Brief.md](14_Files/How_This_Happened-A_Policy_Brief.md) |
| **Skeptics** | [Run_Correlations_Yourself/](Run_Correlations_Yourself/) — Fork and verify |
| **AI Assistants** | [_AI_CONTEXT_INDEX/00_START_HERE.md](_AI_CONTEXT_INDEX/00_START_HERE.md) |

---

## Methodology

1. **Multi-AI Verification**: Cross-checked using Claude, Grok, and Gemini
2. **Statistical Testing**: Pearson correlation, Mann-Whitney U, chi-square, Granger causality, permutation tests
3. **Raw Event Counts**: Replaced subjective scoring with verifiable event counts
4. **Source Triangulation**: Government filings, financial data, news archives
5. **Explicit Limitations**: Documented in each module

→ **Full methodology**: [14_Files/METHODOLOGY.md](14_Files/METHODOLOGY.md)

---

## Limitations & Disclaimer

This repository documents **correlations, not causation**. All findings derive from publicly available data using standard statistical methods.

**The author makes no claims about:**
- Intent or coordination between actors
- Individual motivations or culpability
- Whether patterns are deliberate or emergent

**The claim is structural:** Statistically significant clustering patterns exist and are reproducible.

---

## Connected Repositories

| Repository | Focus |
|------------|-------|
| [Project-Chrysanthemum_Japan-China-AI](https://github.com/Leerrooy95/Project-Chrysanthemum_Japan-China-AI) | Japan-China tech integration |
| [Sovereign-Capital-Audit](https://github.com/Leerrooy95/Sovereign-Capital-Audit) | Gulf SWF positioning |

> **Note:** DOGE_Global_Effects and BRICS-NDB-LocalCurrency-DiD were removed due to Grok-fabricated data. See [Archive/Retracted_Three_Layer_References.md](Archive/Retracted_Three_Layer_References.md).

---

## Contact

**GitHub**: [@Leerrooy95](https://github.com/Leerrooy95)

**Last updated**: February 23, 2026 (v10.0)

---

*The data is public. The code is public. The claims are reproducible and sourced.*
