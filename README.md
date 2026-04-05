# The Regulated Friction Project v12.0

A data-driven analysis of temporal correlations between friction events, policy shifts, and capital flows (2015–2026).

| | |
|---|---|
| **🔴 Live Dashboard** | **[regulatedfriction.me](https://regulatedfriction.me/)** — 8-tab intelligence dashboard with live pipeline data |
| **🤖 AI Assistant on Dashboard** | Gradient AI chatbot at [regulatedfriction.me](https://regulatedfriction.me/) with embedded `_AI_CONTEXT_INDEX` knowledge base |
| **🏛️ Arkansas Trackers** | [Arkansas Tracker](https://leerrooy95.github.io/Arkansas_Tracker/) · [Arkansas Dashboard](https://ark.regulatedfriction.me/) — live tracking of Arkansas energy policy, regulatory decisions, and rhetoric vs. reality gap analysis (PSC dockets, Act 373, Entergy rate actions, ballot initiative restrictions) |
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
| `02_MEDIA_FIREWALL.md` | 1789 Capital, TCN (historical — bought out June 2025), narrative infrastructure |
| `03_BOARD_OF_PEACE.md` | Private diplomacy, Kushner, Witkoff, capital pipeline |
| `04_CAPITAL_ARCHITECTURE.md` | Gulf SWF pipelines, DATA Act, AVAIO Arkansas |
| `05_CRINK_FRAMEWORK.md` | China-Russia-Iran-NK coordination patterns |
| `06_ATTENTION_ECONOMY.md` | Attention economy & quotas: cross-administration noise generator patterns |
| `07_METHODOLOGY.md` | Correlation methodology, verification standards |
| `08_KEY_DATASETS.md` | CSV schemas and data file reference |
| `09_CURRENT_THREADS.md` | Active leverage nodes (Maxwell, Iran, Gulf SWFs, Israel, Oracle, Arkansas, Religious Layer, April 2026 Window, Zorro Ranch, Planet Labs Imagery Blackout — 15 nodes; Mueller death / lost testimony; Cuba crisis escalation) |
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

## What's New (v12.0) — Planet Labs Blackout, Verification Upgrades, Anthropic Contrast — April 5, 2026

Integrates the Planet Labs satellite imagery blackout (April 5, 2026) and three verification upgrades, all web-verified.

- **Planet Labs imagery blackout (April 5)**: Planet Labs (NYSE: PL) announced an indefinite blackout of all satellite imagery over Iran and Middle East conflict zones at US government request. All new and archived imagery since March 9 withheld; shift from 14-day delay to "managed distribution." Other US satellite firms (Vantor/Maxar, BlackSky) imposing similar restrictions. OSINT analysts, journalists, and human rights investigators lose independent ground-truth verification — the same imagery ecosystem that verified the Minab school strike (Node 14). PL stock surged +17% on compliance. Added as Node 15 in `09_CURRENT_THREADS.md`.
- **Anthropic contrast documented**: Anthropic refused Pentagon demands → lost contract → "supply chain risk" → Claude hit #1 App Store → Judge Lin ruled ban "Orwellian." Planet Labs complied → stock surged → no legal challenge → transparency severed. Two opposite responses to government pressure; both commercially rewarded by different audiences (consumers vs. defense investors). Demonstrates thermostat dynamics: resistance generates consumer friction (beneficial to resisting entity), compliance generates information suppression (beneficial to requesting authority).
- **Three verification upgrades**:
  - **Barak–Epstein Russia/Israel back channel** → ⚠️ to ✅ VERIFIED: 7+ independent outlets now confirm (Al Jazeera, Middle East Monitor, Drop Site News, Democracy Now, News.az, TJV News, Factually.co). Barak-Lavrov SPIEF meetings confirmed; Putin direct meeting NOT confirmed.
  - **SpaceX IPO** → ⚠️ to ✅ VERIFIED: Confidential SEC filing **April 1, 2026** confirmed (CNBC, Forbes, Teslarati). June–July 2026 Nasdaq listing; $1.5–1.75T valuation; $50B–$80B capital raise; Goldman Sachs, Morgan Stanley, JPMorgan lead underwriters.
  - **Epstein sought Putin meeting via Barak** → ⚠️ to ✅ VERIFIED (seeking confirmed; meeting NOT confirmed): DOJ files contain 5,553 Russia mentions, 1,005 Putin mentions; Kremlin denied meeting; multiple outlets confirm the seeking (Times of Israel, Straits Times, France24, Moscow Times, Meduza).
- **Files updated**: [`09_CURRENT_THREADS.md`](_AI_CONTEXT_INDEX/09_CURRENT_THREADS.md), [`11_LEVERAGE_THESIS.md`](_AI_CONTEXT_INDEX/11_LEVERAGE_THESIS.md), [`CONTEXT_ROUTER.md`](_AI_CONTEXT_INDEX/CONTEXT_ROUTER.md), [`00_START_HERE.md`](_AI_CONTEXT_INDEX/00_START_HERE.md), [`README.md`](README.md), [`Report.md`](Report.md).

### Previous (v11.9) — Ballroom Bypass, Bondi Firing, Military Purge, 25th Amendment Calls — April 3, 2026

Integrates four streams of April 1–3, 2026 developments, all web-verified before committing.

- **Ballroom bypass executed (April 2)**: NCPC voted 8-1 to approve the White House ballroom project the day after Judge Leon's injunction. NCPC Chair Will Scharf (White House Staff Secretary, Trump appointee) explicitly stated the court order "does not impact our action here today." Security/bunker construction continued. Public Citizen filed a statutory challenge alleging Scharf, Levenbach, and Blair lack the "city or regional planning" experience federal law requires. Updated in `09_CURRENT_THREADS.md` (March/April 2026 Events table) and `10_FRAMEWORK_VALIDATION.md` (Section 11 — bypass executed notation, Framework Alignment table, Framework Significance expanded).
- **Pam Bondi fired (April 2)**: Trump fired AG Bondi amid bipartisan criticism of Epstein file handling. Todd Blanche (Trump's former personal defense attorney, current Deputy AG) named acting AG. Congress confirmed the April 14 House Oversight deposition subpoena remains legally valid. Added to `09_CURRENT_THREADS.md` events table and `tier2_purged_officials.md`.
- **Military leadership purge mid-conflict (April 2)**: Hegseth fired Army Chief of Staff Gen. Randy George effective immediately — no modern precedent for senior command removal during active combat operations. Also removed: Gen. David Hodne (Army Transformation and Training Command) and Maj. Gen. William Green Jr. (Chief of Army Chaplain Corps — first chaplain chief firing in US history). Gen. Christopher LaNeve named acting CSA. Added to Node 2 (Iran war) in `09_CURRENT_THREADS.md` and `tier2_purged_officials.md`.
- **25th Amendment calls + approval ratings (April 3)**: Ty Cobb (Trump WH special counsel 2017–2018) called Trump "clearly insane" and demanded 25th Amendment invocation on Jim Acosta Show — notable as conservative former administration insider. UMass/YouGov poll: 33% approval (second-term low, down from 44% April 2025); Economist/YouGov: 35%. Added as April 3 entries in `09_CURRENT_THREADS.md` events table.
- **New dossier**: `_AI_CONTEXT_INDEX/Node_Dossiers/tier2_purged_officials.md` — running log of second-term removals with friction-adjacency pattern notes. Seeded: Bongino (Dec 17), Noem (Mar 5), Bondi (Apr 2), George/Hodne/Green (Apr 2).
- **Files updated**: [`09_CURRENT_THREADS.md`](_AI_CONTEXT_INDEX/09_CURRENT_THREADS.md), [`10_FRAMEWORK_VALIDATION.md`](_AI_CONTEXT_INDEX/10_FRAMEWORK_VALIDATION.md), [`CONTEXT_ROUTER.md`](_AI_CONTEXT_INDEX/CONTEXT_ROUTER.md), [`Node_Dossiers/NODE_INDEX.md`](_AI_CONTEXT_INDEX/Node_Dossiers/NODE_INDEX.md), [`Node_Dossiers/tier2_purged_officials.md`](_AI_CONTEXT_INDEX/Node_Dossiers/tier2_purged_officials.md) (new), [`README.md`](README.md).

### Previous (v11.7–v11.8) — Tucker Buyout, TPUSA Integration — April 2–3, 2026

- **Tucker Carlson/1789 Capital buyout** (v11.7): Carlson and Patel bought out all 1789 Capital investors (June 2025), making TCN independent. Post-buyout, Carlson broke with Trump over Iran policy — behavior consistent with Media Firewall thesis. All repository references updated.
- **TPUSA post-assassination merger** (v11.8): Kirk assassination → ADL neutralization → institutional consolidation (Erika Kirk CEO/Medal of Freedom/Air Force Academy Board). Equal Access Act legal architecture documented.

### Previous (v11.5–v11.6) — Four-Thread Integration, CRINK Update — April 1, 2026

- **Anthropic v. DoD PI granted** (Mar 26): Judge Lin called Pentagon ban "Orwellian" / "First Amendment retaliation." D.C. Circuit FASCSA case still pending.
- **White House ballroom PI granted** (Mar 31): Judge Leon — "steward, not the owner." DOJ appealed; NCPC bypass followed April 2.
- **April convergence window upgraded to quadruple-track**: Track A (Bondi deposition Apr 14), Track B (CLARITY Act Apr 13–27), Track C (FISA/SAVE Act Apr 20), Track D (Treasury waiver Apr 11).
- **BofA $72.5M Epstein settlement** (Mar 27, ✅); **Comer "botched" admission** (Mar 30, ✅).
- **CRINK late-March**: Kolodkin oil delivery to Cuba (Mar 30), China rice shipments, NK 10-missile salvo (Mar 14), Iran ceasefire restart, CRINK rift analysis — all web-verified.
- **Epstein 302 cross-reference**: Withheld FBI 302 summaries released Mar 5–6 track with Trump's "innocent people" / Greene's "my friends will get hurt" statements. [Inference] label applied.

### Previous (v11.1–v11.4) — Major Node Additions — March 22, 2026

- **Node 14** (AI Kill Chain): Anthropic ban → Maven targeting → Minab school strike (175 killed). Coercion template documented. 51/53 claims verified.
- **Node 13** (Musk/SpaceX-xAI): $1.25T merger, Tesla decline, Grok CSAM lawsuit, X Money, DOGE failure. 46/51 claims verified.
- **Node 11 Track C**: SAVE America Act / FISA Section 702 coupling. 29/30 claims verified.
- **Pre-September 2025 timeline**: Musk–Administration falling out (DOGE → Big Beautiful Bill → Epstein weaponization → reconciliation → files released).

### Previous (v10.8–v11.0) — Cuba Crisis, Zorro Ranch, Mueller Death — March 21, 2026

- **Node 12** (Zorro Ranch): NM investigation, truth commission, AG Torrez, ranch search, Kahn/Indyke depositions.
- **Cuba crisis**: Morón protests, grid collapse, embassy diesel refused, Anatoly Kolodkin tanker, Skipper/CRINK nexus.
- **Mueller death** (Mar 21): Permanently lost Epstein testimony. Trump: "He can no longer hurt innocent people!" Greene arc and Thiel "Epstein-adjacent" deployment documented.
- **April 2026 convergence window** (Node 11): Pre-event prediction filed with falsification criteria.

### Previous (v10.1–v10.7) — Pipeline, Verification, Infrastructure — February–March 15, 2026

- Live Trackers v2.1 pipeline (6-stage, 8-tab dashboard at [regulatedfriction.me](https://regulatedfriction.me/)).
- Nodes 8–9 added (Oracle Financial Stress, Arkansas State-Level Preemption).
- Leverage Thesis (`11_LEVERAGE_THESIS.md`), Report.md rewritten, 7-day median lag corrected, robustness audit, source decontamination.

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

1. Why did the same capital entity (1789 Capital) fund both the Media Firewall (TCN, PublicSq) and enforcement layer (Anduril) pitched to Saudi defense — and why did Tucker Carlson begin openly criticizing the administration only after buying out 1789 Capital's stake in June 2025?

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
| [Arkansas_Tracker](https://leerrooy95.github.io/Arkansas_Tracker/) | Live tracking of Arkansas energy policy, regulatory decisions, and rhetoric vs. reality gap analysis (PSC dockets, Act 373, Entergy rate actions, ballot initiative restrictions) |
| [Crypto COI Tracker](https://signalwebdevelopment.github.io/) | Automated live tracking of cryptocurrency conflicts of interest |
| [OSINT_ChatBot](https://github.com/Leerrooy95/OSINT_ChatBot) | BYOK ChatBot using `_AI_CONTEXT_INDEX` as reference |
| [Project-Chrysanthemum_Japan-China-AI](https://github.com/Leerrooy95/Project-Chrysanthemum_Japan-China-AI) | Japan-China tech integration |
| [Sovereign-Capital-Audit](https://github.com/Leerrooy95/Sovereign-Capital-Audit) | Gulf SWF positioning |

> **Note:** The `output/` directory in this repository is synced daily from Live_Trackers via `sync_from_live_trackers.yml`, keeping local copies of pipeline outputs up to date.

> **Note:** DOGE_Global_Effects and BRICS-NDB-LocalCurrency-DiD were removed due to Grok-fabricated data. See [Archive/Retracted_Three_Layer_References.md](Archive/Retracted_Three_Layer_References.md).

---

## Contact

**GitHub**: [@Leerrooy95](https://github.com/Leerrooy95)

**Last updated**: April 5, 2026 (v12.0)

---

*The data is public. The code is public. The claims are reproducible and sourced.*
