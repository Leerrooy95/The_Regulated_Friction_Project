# The Regulated Friction Project v10.8

A data-driven analysis of temporal correlations between friction events, policy shifts, and capital flows (2015–2026).

| | |
|---|---|
| **🔴 Live Dashboard** | **[regulatedfriction.me](https://regulatedfriction.me/)** — 8-tab intelligence dashboard with live pipeline data |
| **🤖 AI Assistant on Dashboard** | Gradient AI chatbot at [regulatedfriction.me](https://regulatedfriction.me/) with embedded `_AI_CONTEXT_INDEX` knowledge base |
| **⛪ Religion Connections Tracker** | [Religion Tracker](https://signalwebdevelopment.github.io/Religion_Tracker/) — automated live tracking of religious network connections |
| **💰 Crypto Conflict of Interest Tracker** | [Crypto COI Tracker](https://signalwebdevelopment.github.io/) — automated live tracking of crypto conflicts of interest |
| **OSINT ChatBot** | [BYOK ChatBot](https://personal-chatbot-qej0.onrender.com/login) — uses [_AI_CONTEXT_INDEX](https://github.com/Leerrooy95/The_Regulated_Friction_Project/tree/main/_AI_CONTEXT_INDEX) as reference ([source repo](https://github.com/Leerrooy95/OSINT_ChatBot)) |

| Quick Links | |
|---|---|
| **New here?** | [Glossary](14_Files/Glossary.md) |
| **AI Assistant?** | [_AI_CONTEXT_INDEX/00_START_HERE.md](_AI_CONTEXT_INDEX/00_START_HERE.md) |
| **In a rush?** | [Consolidation Pattern Significance](Project_Trident/Copilot_Opus_4.6_Analysis/Consolidation_Analysis/consolidation_pattern_significance.md) |
| **Run it yourself** | [Run_Correlations_Yourself/](Run_Correlations_Yourself/) |

---

## Core Finding

**Friction events predict compliance events with a 7-day median sequential lag.**

| Metric | Value |
|--------|-------|
| Correlation | r = +0.6196 |
| Significance | p = 0.0004 |
| Sample | n = 28 paired observations (30-week dataset) |

When high-visibility friction events spike (document releases, scandals, media cycles), institutional compliance events (policy shifts, financial moves, regulatory changes) follow within a 7-day median window (originally reported as ~14 days based on 2-week index binning; corrected in v10.3). This relationship has less than 0.05% probability of occurring by chance.

**What this does NOT claim:** Central coordination, conspiracy, or intentional orchestration. The pattern is emergent — multiple actors exploiting the same environmental signals (holidays, fiscal deadlines, media saturation) without requiring communication between them. Correlation ≠ causation. The claim is structural: the pattern exists and is statistically significant.

---

## Live Intelligence Pipeline

The [Live_Trackers](https://github.com/Leerrooy95/Live_Trackers) repository runs a 6-stage automated pipeline twice daily (08:00 & 20:00 UTC) via GitHub Actions, monitoring all active leverage nodes and producing real-time intelligence. Results are published to the public dashboard at **[regulatedfriction.me](https://regulatedfriction.me/)**.

| Stage | Tool | Output |
|-------|------|--------|
| 1. Node Tracker | Perplexity sonar-pro | `node_status.json` — live status of all leverage nodes |
| 2. Entity Extractor | Llama Scout 17B | `extracted_entities.json` — structured entities & relationships |
| 3. Convergence Detector | Local analysis | `convergence_report.json` — multi-node convergence windows |
| 4. Daily Intelligence | Perplexity sonar-pro | `daily_intelligence.json` — signal tracking & breaking news |
| 5. Fact Checker | Anthropic Claude | `fact_check.json` — claim verification & correction |
| 6. Rhetoric vs. Reality | Anthropic Claude | `rhetoric_reality.json` — three-column gap analysis with statute citations |

The dashboard at [regulatedfriction.me](https://regulatedfriction.me/) features 8 tabs: **Node Status**, **Intelligence**, **Convergence**, **Predictions**, **Entities**, **Charts**, **Rhetoric vs. Reality**, and **History** — with Chart.js visualizations (Thermostat Timeline, Dual-Track Stacked Area, Node Activation Heatmap) that accumulate data over time. A **Gradient AI chatbot** with the `_AI_CONTEXT_INDEX` knowledge base is available on the dashboard for interactive queries.

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
| **Core Correlation** | r = +0.6196 at 2-week index lag (p = 0.0004); actual median: 7 days | ✅ Verified |
| **Ritual Proximity** | 50.7% vs. 19.9% baseline (2.5x) | ✅ Verified |
| **Cross-validation** | χ² = 330.62 (p < 0.0001, 2,102 events) | ✅ Verified |
| **Historical Backfill** | 66 pairs across 2017-2024; Δr = +0.0012 (negligible impact) | ✅ Verified |
| **Q4 2025 13F Predictions** | 3 predictions tested | ❌ All 3 FAILED |
| **Board of Peace Summit** | ~50 countries, $7B pledged, $10B US | ✅ Confirmed |

→ **Full statistics**: [Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/](Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/)

**Note on failed predictions:** The Q4 2025 13F predictions (Gulf SWF positioning) failed. This is documented transparently — negative findings are data.

---

## AI Context Index

The `_AI_CONTEXT_INDEX/` directory provides structured context for AI assistants and researchers:

| File | Content |
|------|---------|
| `00_START_HERE.md` | Navigation guide, Dual-Track System, Cartel Statecraft Model |
| `01_CORE_THEORY.md` | Thermostat model, 7-day median lag (corrected from 14-day), convergence pattern, framework validation |
| `02_MEDIA_FIREWALL.md` | 1789 Capital, TCN, narrative infrastructure |
| `03_BOARD_OF_PEACE.md` | Private diplomacy, Kushner, Witkoff, capital pipeline |
| `04_CAPITAL_ARCHITECTURE.md` | Gulf SWF pipelines, DATA Act, AVAIO Arkansas |
| `05_CRINK_FRAMEWORK.md` | China-Russia-Iran-NK coordination patterns |
| `06_ATTENTION_ECONOMY.md` | Attention economy & quotas: cross-administration noise generator patterns |
| `07_METHODOLOGY.md` | Correlation methodology, verification standards |
| `08_KEY_DATASETS.md` | CSV schemas and data file reference |
| `09_CURRENT_THREADS.md` | Active leverage nodes (Maxwell, Iran, Gulf SWFs, Israel, Oracle, Arkansas, Religious Layer, April 2026 Window — 11 nodes) |
| `10_FRAMEWORK_VALIDATION.md` | High-profile statements validating framework |
| `11_LEVERAGE_THESIS.md` | Leverage thesis: Musk/Epstein origin, Iran extension, Anthropic standoff, capital architecture |

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
├── 15_The_Religious_Layer/       # Eschatological infrastructure, theological-policy pipeline
├── _AI_CONTEXT_INDEX/            # Structured context for AI assistants (12 files + Node Dossiers)
├── Project_Trident/              # Independent verification (Opus 4.6 — 16 statistical tests, 80+ docs)
├── Run_Correlations_Yourself/    # Reproducibility scripts
├── New_Data_2026/                # 2026 datasets
├── output/                       # Daily data synced from Live_Trackers pipeline
├── Archive/                      # Deprecated files (Streamlit dashboard, spider, old workflows)
└── .github/workflows/            # Single workflow: sync output from Live_Trackers
```

---

## The Media Firewall: Patriotic Capitalism Neutralization Layer

The Media Firewall thesis (see `12_The_Media_Firewall/`) documents how alternative media platforms funded by prime brokerage capital function as narrative infrastructure — directing populist energy toward high-valence cultural and foreign policy topics while maintaining structural silence on the financial architecture that capitalizes these ventures.

**The Neutralization Mechanism (2024–2026):**

Between 2024 and early 2026, a specific pattern of capital consolidation emerged within the alternative media venture capital space:

1. **Capital Acceleration:** A prime brokerage-backed venture fund grew from ~$200M to ~$2B AUM within approximately one year (2025), crossing the $1B institutional threshold. This growth coincided with the onboarding of senior political family members as partners and pre-inauguration alliance-building at private venues.

2. **Institutional Capture:** The fund's founder — a former Managing Director of Prime Brokerage at a major U.S. bank — was appointed to the Board of Directors of a federal housing agency (GSE), establishing a direct structural link between alternative media venture capital and government-sponsored enterprise governance.

3. **Media Firewall Expansion:** The same capital network funded a $10M round for a decentralized creator-economy platform and filed a $260M SPAC IPO, expanding the "parallel economy" thesis into public capital markets with high-profile political and media figures on the board.

4. **Defense Pivot:** The fund led a $60M Series C investment in a defense aerospace startup specializing in 3D-printed solid rocket propulsion, completing the capital circuit: prime brokerage → alternative media → federal housing governance → defense technology.

**Structural Implication:** The "patriotic capitalism" branding functions as a semiotic neutralization layer — wrapping the merger of prime brokerage capital with federal infrastructure in founding-era American symbolism, rendering it rhetorically immune to "foreign capture" or "institutional capture" framing. The fund simultaneously capitalizes the media platforms that remain silent on these very financial architectures.

→ **Full data**: [`12_The_Media_Firewall/Alternative_Capital_Expansion_24-26.csv`](12_The_Media_Firewall/Alternative_Capital_Expansion_24-26.csv)
→ **Node analysis**: [`12_The_Media_Firewall/Omeed_Malik_Forensic_Node_Analysis.md`](12_The_Media_Firewall/Omeed_Malik_Forensic_Node_Analysis.md)

---

## What's New (v10.8) — April 2026 Convergence Window Prediction — March 21, 2026

- **Pre-event prediction filed**: [April 2026 Convergence Window](10_Real-Time_Updates_and_Tasks/2026_March/April_2026_Convergence_Window.md) documents a predicted dual-track convergence (April 12–20) with explicit falsification criteria — filed *before* the window opens.
- **Track A (Accountability)**: AG Pam Bondi subpoenaed for April 14 deposition before House Oversight Committee on Epstein file handling and DOJ redactions (✅ [CNBC](https://www.cnbc.com/2026/03/17/epstein-pam-bondi-trump-doj-subpoena.html), [CBS News](https://www.cbsnews.com/news/epstein-files-pam-bondi-subpoena-house-oversight-committee/)).
- **Track B (Capital Architecture)**: CLARITY Act Senate legislative status now substantially verified — Senate Agriculture Committee advanced 12-11 party-line vote (January 29, 2026, ✅ [CNBC](https://www.cnbc.com/2026/01/29/senate-ag-committee-advances-crypto-bill-to-establish-cftc-regulatory-authority.html)); stablecoin yield "agreement in principle" reached by Senators Tillis (R-NC) + Alsobrooks (D-MD) + White House (March 20, 2026, ✅ [Politico](https://www.politico.com/live-updates/2026/03/20/congress/senators-strike-deal-with-white-house-to-resolve-bank-crypto-clash-00837464), [The Block](https://www.theblock.co/post/394554/lawmakers-breakthrough-agreement-in-principle-stablecoin-yield-sweeping-crypto-bill)); Senate Banking Committee markup targeted April 13–27 (⚠️ targeted). USD1/WLF/MGX capital architecture documented: ~$4.59B market cap, $2B MGX-Binance settlement in USD1, 135M WLFI airdrop active through April 17 (✅ verified via CoinGecko, CNBC, Binance).
- **Emoluments question**: Warren and Merkley raised constitutional concerns over MGX/USD1/WLF structure; no Congressional consent resolution or OLC opinion filed (✅ [Senate Banking Committee](https://www.banking.senate.gov/newsroom/minority/forwarding-merkley-warren-trump-linked-crypto-deal-is-a-staggering-conflict-of-interest)).
- **March 17–21 context events verified**: Ras Laffan LNG strike (✅), Brent crude ~$112/bbl (✅), Goldman unredacted Epstein document (✅), Bondi briefing walkout (✅), CBS News Radio closure (✅), Mullin DHS hearing (✅), Trump Pearl Harbor joke (✅), Tucker Carlson/Prof. Jiang interview (✅). Full verification: 18/20 claims verified.
- **Node 11 added** to [`09_CURRENT_THREADS.md`](_AI_CONTEXT_INDEX/09_CURRENT_THREADS.md): April 2026 Convergence Window with thermostat prediction and falsification criteria.

### Previous (v10.7) — Live Intelligence Pipeline & March 2026 Convergence — March 15, 2026

- **Live Trackers v2.1 pipeline fully operational**: 6-stage architecture (Perplexity → Llama Scout → Convergence Detection → Daily Intelligence → Anthropic Fact-Check → Rhetoric vs. Reality) running twice daily via GitHub Actions.
- **Public dashboard at [regulatedfriction.me](https://regulatedfriction.me/)**: 8 tabs with Chart.js visualizations (Thermostat Timeline, Dual-Track Stacked Area, Node Activation Heatmap) that accumulate data points over time.
- **Gradient AI chatbot deployed on dashboard**: Uses `_AI_CONTEXT_INDEX` knowledge base for interactive queries about live pipeline data and research context.
- **Rhetoric vs. Reality Stage 6**: Produces three-column gap analysis with statute citations (EO 14375, 22 U.S.C. § 288, 5 U.S.C. § 7511, War Powers Resolution) autonomously.
- **March 2026 analytical additions**: Board of Peace IOIA immunity bypass, Operation Epic Fury without AUMF, Schedule Policy Career reclassification (~50,000 positions), Indonesian ISF suspension.
- **Dashboard context injection**: Chatbot can answer questions about live dashboard data including node status, convergence events, and fact-check results.
- **Charts accumulate data over time**: Each pipeline run adds data points to the Thermostat Timeline, Dual-Track Stacked Area, and Node Activation Heatmap visualizations.

### Previous (v10.6) — Repository Cleanup & Pipeline Consolidation — March 12, 2026

- **Streamlit dashboard retired**: The Streamlit app (`regulatedfriction.streamlit.app`) has been replaced by the live static dashboard at [regulatedfriction.me](https://regulatedfriction.me/), which is driven by the unified [Live_Trackers](https://github.com/Leerrooy95/Live_Trackers) pipeline.
- **Repository simplified to research-only**: Deprecated files (Streamlit source, Federal Register Scrapy spider, old docs site, unused workflows) moved to `Archive/` — this repo now focuses exclusively on the research corpus and correlation data.
- **Single workflow**: Only `sync_from_live_trackers.yml` remains active, pulling the latest pipeline output (`node_status.json`, `daily_intelligence.json`, `convergence_report.json`, etc.) from Live_Trackers into `output/` daily at 10:00 UTC.

### Previous (v10.5) — Node Expansion, Verification & Pipeline Automation — March 9, 2026

- **Two new Active Leverage Nodes**: Node 8 ([Oracle Financial Stress / Stargate Contraction](_AI_CONTEXT_INDEX/09_CURRENT_THREADS.md)) and Node 9 ([Arkansas State-Level Preemption / Datacenter Capital Nexus](13_State_and_County_Analysis/)) added to `09_CURRENT_THREADS.md`.
- **Maxwell Node Dossier**: New Tier 1 dossier ([`tier1_maxwell_leverage.md`](_AI_CONTEXT_INDEX/Node_Dossiers/tier1_maxwell_leverage.md)) documenting clemency-for-testimony offer, VOCA funding mechanism, and administrative pincer — all verified with multiple sources.
- **FBI 302 release documented**: March 5–6 DOJ release of 16 additional Epstein pages, including three previously withheld FBI 302 interview summaries. Discrepancy discovered via Maxwell defense evidence index.
- **Epstein Class counter-frame**: New section in [`06_ATTENTION_ECONOMY.md`](_AI_CONTEXT_INDEX/06_ATTENTION_ECONOMY.md) documenting verified congressional counter-framing (Ossoff, Jeffries, Massie, MTG) and "Operation Epstein Fury" social media dynamics.
- **Arkansas forensic audit verified**: Independent verification ([24/28 ✅](Project_Trident/Copilot_Opus_4.6_Analysis/Arkansas_Law_Forensic_Audit_Verification.md)) of the Arkansas infrastructure and law forensic audits in [`13_State_and_County_Analysis/`](13_State_and_County_Analysis/).
- **Transparency**: New [`Unable_to_Verify_March_2026.md`](Project_Trident/Copilot_Opus_4.6_Analysis/Unable_to_Verify_March_2026.md) documenting items that could not be independently verified.
- **Automated intelligence pipeline**: Daily pipeline in [Live_Trackers](https://github.com/Leerrooy95/Live_Trackers) runs Perplexity node tracking, Llama Scout entity extraction, convergence detection, daily intelligence, and Anthropic fact-checking — outputs synced to `output/` in this repo.
- **Gradient AI agent**: DigitalOcean Gradient agent deployed as autonomous OSINT monitor using Claude Opus 4.6 for friction/compliance analysis.

### Previous (v10.4) — Prime Brokerage Capital & Alternative Media Integration — March 3, 2026

- **Patriotic Capitalism Neutralization Layer documented**: Structural mechanics of prime brokerage-backed venture capital using populist media funding to shield consolidation of government infrastructure and defense tech. See `12_The_Media_Firewall/`.
- **Alternative Capital Expansion dataset**: New CSV (`12_The_Media_Firewall/Alternative_Capital_Expansion_24-26.csv`) tracking 10 verified data points (Jan 2024 – March 2026).

### Previous (v10.3) — The High-Resolution Build — March 2, 2026

- **14-day lag corrected to 7-day median**: Actual median lag is **7 days** (mean: 6.5 days). The "14-day" figure was an artifact of 2-week index binning. See `04_Testing_and_Counters/ROBUSTNESS_AUDIT_v10.2.md`.
- **Robustness audit completed**: Permutation (10K shuffles, p = 0.0004), calendar-anchor clustering (71.2% shared anchors), temporal engine adaptation.
- **Source decontamination**: oreateai.com purged → `New_Data_2026/DATA_QUARANTINE.csv`. 2,121 URLs scanned; 2,110 clean.

### Previous (v10.1–v10.2) — February–March 1, 2026

- **Leverage Thesis documented** (`11_LEVERAGE_THESIS.md`), **Report.md rewritten for accessibility**, **live data pipeline active** (1006+ EOs), **Israel leverage node added** (completes four-node architecture).

---

## Independent Statistical Verification (Opus 4.6)

After the repository owner established the core correlations, **GitHub Copilot (Claude, Opus 4.6)** independently wrote and ran a suite of **16 statistical test scripts** to stress-test whether the findings hold up under rigorous scrutiny. Opus 4.6 did not build the datasets or run the original correlations — it received the data and results, then designed its own tests to challenge them.

**The core correlation (r = +0.6196, p = 0.0004) survived every robustness test applied:**

| Test | What It Checks | Result | Status |
|------|----------------|--------|--------|
| Permutation (10K shuffles) | Could the correlation be random noise? | p < 0.0001 | ✅ Pass |
| Granger causality (lag 1) | Does past friction *predict* future compliance? | p = 0.0008 | ✅ Pass |
| Block bootstrap (autocorr-adjusted) | Does temporal clustering inflate significance? | p = 0.008 | ✅ Pass |
| December 2025 exclusion | Is the pattern driven by one dense month? | ρ = 0.60 (holds) | ✅ Pass |
| Binary presence/absence | Does it depend on event magnitude? | r = 0.59 | ✅ Pass |
| Event-study framework | Do compliance events cluster after friction? | 20–42× above baseline | ✅ Pass |
| Partial correlation (political calendar) | Is Congress's schedule driving it? | < 1% explained | ✅ Pass |
| Historical backfill (2017–2024) | Does adding 66 historical pairs change it? | Δr = +0.0012 | ✅ Pass |
| Granger (first-differenced) | Does direction survive stationarity correction? | Consistent | ✅ Pass |
| Rolling window (13/26/52 wk) | Is it stable across time? | Multiple periods | ✅ Pass |
| Per-year normalization | Does 2025 concentration drive it? | ρ robust | ✅ Pass |

→ **Full test suite and results**: [Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/](Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/)
→ **Detailed findings**: [Project_Trident/Copilot_Opus_4.6_Analysis/Findings/](Project_Trident/Copilot_Opus_4.6_Analysis/Findings/)

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
| **Researchers** | [Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/](Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/) — 16 independent robustness tests by Opus 4.6 |
| **Journalists** | [14_Files/How_This_Happened-A_Policy_Brief.md](14_Files/How_This_Happened-A_Policy_Brief.md) |
| **Skeptics** | [Run_Correlations_Yourself/](Run_Correlations_Yourself/) — Fork and verify |
| **AI Assistants** | [_AI_CONTEXT_INDEX/00_START_HERE.md](_AI_CONTEXT_INDEX/00_START_HERE.md) |

---

## Methodology

1. **Multi-AI Verification**: Cross-checked using Claude, Grok, and Gemini
2. **Statistical Testing**: Pearson correlation, Mann-Whitney U, chi-square, Granger causality, permutation tests
3. **Independent Robustness Suite**: 16 statistical test scripts written by Opus 4.6 — permutation, autocorrelation-adjusted bootstrap, Granger causality, event-study, rolling-window, partial correlation, and more (see [`Statistical_Tests/`](Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/))
4. **Raw Event Counts**: Replaced subjective scoring with verifiable event counts
5. **Source Triangulation**: Government filings, financial data, news archives
6. **Explicit Limitations**: Documented in each module

→ **Full methodology**: [_AI_CONTEXT_INDEX/07_METHODOLOGY.md](_AI_CONTEXT_INDEX/07_METHODOLOGY.md)

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
| [Live_Trackers](https://github.com/Leerrooy95/Live_Trackers) | 6-stage automated intelligence pipeline (Perplexity → Llama Scout → Convergence → Intelligence → Fact-Check → Rhetoric vs. Reality) — powers the public dashboard at [regulatedfriction.me](https://regulatedfriction.me/) with 8 tabs, Chart.js visualizations, and Gradient AI chatbot |
| [Religion_Tracker](https://signalwebdevelopment.github.io/Religion_Tracker/) | Automated live tracking of religious network connections to policy infrastructure |
| [Crypto COI Tracker](https://signalwebdevelopment.github.io/) | Automated live tracking of cryptocurrency conflicts of interest |
| [OSINT_ChatBot](https://github.com/Leerrooy95/OSINT_ChatBot) | BYOK ChatBot using `_AI_CONTEXT_INDEX` as reference |
| [Project-Chrysanthemum_Japan-China-AI](https://github.com/Leerrooy95/Project-Chrysanthemum_Japan-China-AI) | Japan-China tech integration |
| [Sovereign-Capital-Audit](https://github.com/Leerrooy95/Sovereign-Capital-Audit) | Gulf SWF positioning |

> **Note:** The `output/` directory in this repository is synced daily from Live_Trackers via `sync_from_live_trackers.yml`, keeping local copies of pipeline outputs up to date.

> **Note:** DOGE_Global_Effects and BRICS-NDB-LocalCurrency-DiD were removed due to Grok-fabricated data. See [Archive/Retracted_Three_Layer_References.md](Archive/Retracted_Three_Layer_References.md).

---

## Contact

**GitHub**: [@Leerrooy95](https://github.com/Leerrooy95)

**Last updated**: March 21, 2026 (v10.8)

---

*The data is public. The code is public. The claims are reproducible and sourced.*
