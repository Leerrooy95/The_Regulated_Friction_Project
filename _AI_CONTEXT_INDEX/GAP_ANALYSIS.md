# Gap Analysis — _AI_CONTEXT_INDEX vs. Repository Reality

**Date**: 2026-03-01  
**Method**: Compared exhaustive repo audit against all files in `_AI_CONTEXT_INDEX/`

---

## 1. Undocumented Files and Folders

The following exist in the repository but are **not referenced** anywhere in the current `_AI_CONTEXT_INDEX/`:

### Entire Directories Missing from Index

| Directory | Contents | Why It Matters |
|-----------|----------|----------------|
| `00_Quick_Breakdowns/` | `About_Me.md` (author bio, scout methodology origin), `Copilot_Executive_Synthesis_Feb2026.md` | Author context and methodology origin are undocumented in the index |
| `08_How_It's_Possible/` | `08_How_Its_Possible.md`, `DOJ_Probe_Results.csv`, `Phase_0_Maxwell_Pivot.csv`, `pincer_data.csv` | Mechanism explanation and Maxwell leverage data not indexed |
| `11_Protest_Dynamics_and_Funding/` | FaaS framework, protest funding audit PDF | Friction-as-a-Service supply chain completely absent from index |
| `13_State_and_County_Analysis/` | Arkansas forensic audit (Act 373, Act 548, AVAIO, PSC override) | Only briefly mentioned in `04_CAPITAL_ARCHITECTURE.md`; no dedicated index coverage |
| `Archive/` | Retracted three-layer model, Grok fabrication history, pipeline recommendations, droplet setup | Retraction history and infrastructure archaeology not indexed |
| `docs/` | Static HTML docs, validation report (Feb 24, 2026) | Public-facing documentation not indexed |
| `federal_register/` | Scrapy spiders (EO tracker, DOJ press releases), spider output | Data collection infrastructure not indexed |
| `dashboard/` | Streamlit app, correlation engine, data loader, changelog | Live dashboard application not indexed |
| `.github/workflows/` | CI/CD pipelines (daily_pipeline, sync, validate) | Automation infrastructure not indexed |

### Specific Files Missing from Index

| File | Location | Why It Matters |
|------|----------|----------------|
| `QUICK_START.md` | Root | Pipeline deployment guide not referenced |
| `IMPLEMENTATION_SUMMARY.md` | Root | Infrastructure fix documentation not referenced |
| `intelligence_config.json` | Root | Entity/signal configuration not documented in index |
| `daily_perplexity_update.py` | Root | Daily intelligence pipeline not documented in index |
| `test_api.py` | Root | LLM extraction pipeline not documented in index |
| `merge_spider_output.py` | Root | Spider data merging not documented |
| `Copilot_Executive_Synthesis_Feb2026.md` | `00_Quick_Breakdowns/` | Executive synthesis not indexed |
| `Protest_Funding_Audit.pdf` | `11_Protest_Dynamics_and_Funding/` | Forensic audit PDF not indexed |
| `Super_Bowl_LX_Media_Firewall_Case_Study.md` | `12_The_Media_Firewall/` | Case study not indexed |
| `1789_Symbolism_Analysis.md` | `12_The_Media_Firewall/` | Semiotic bridge analysis not indexed |
| `arkansas_infrastructure_forensic_audit.md` | `13_State_and_County_Analysis/` | State-level infrastructure analysis not indexed |
| `TRANSPARENCY_NOTE_FOR_2026_ANALYSIS.md` | `14_Files/` | AI transparency note not indexed |
| `resistance_indicators.md` | `14_Files/` | Resistance indicator analysis not indexed |
| `CITATION.cff` | `14_Files/` | Citation format file not indexed |
| `Arkansas_Federal_Energy_Bypass.md` | `Project_Trident/Copilot_Opus_4.6_Analysis/` | DATA Act federal bypass not indexed |
| `TikTok_Algorithm_Anomaly_Investigation.md` | `Project_Trident/Copilot_Opus_4.6_Analysis/` | TikTok anomaly not indexed |
| `AI_Fabrication_Case_Study.md` | `Project_Trident/.../Findings/` | Grok fabrication case study not indexed |
| `VALIDATION_REPORT_2026-02-24.md` | `docs/validation/` | Latest validation report not indexed |

### Project_Trident Subdirectories Largely Unindexed

The `_AI_CONTEXT_INDEX` mentions `Project_Trident/` in passing but does not document:
- `Claude_Code_Analysis/` (9 files including Privatized Integration Networks synthesis)
- `Copilot_Opus_4.6_Analysis/Administrative_State_Audit/` (7 files: DOGE, DOJ, FBI, OPM timelines)
- `Copilot_Opus_4.6_Analysis/Evangelical_Network_Cross_Reference_Analysis.md`
- `Copilot_Opus_4.6_Analysis/FaaS_Signal_Analysis/` (3 files)
- `Copilot_Opus_4.6_Analysis/Findings/` (10 files including provenance, discrepancy investigations)
- `Copilot_Opus_4.6_Analysis/Influencer_Narrative_Timing/` (1 file)
- `Copilot_Opus_4.6_Analysis/Narrative_Case_Studies/` (2 files: Bondi hearing analysis, Attention Economy cross-administration analysis)
- `Copilot_Opus_4.6_Analysis/Verification_Reports/` (1 file)
- `Copilot_Opus_4.6_Analysis/Consolidation_Analysis/` (1 file)
- `Copilot_Opus_4.6_Analysis/Entity_Reports/Palantir_Technologies_Deep_Dive.md`
- 16 Python statistical test scripts in `Statistical_Tests/`
- 5 changelog files in `Changelogs/`

---

## 2. Outdated References

| Index File | Reference | Issue |
|------------|-----------|-------|
| `00_START_HERE.md` | Node Dossiers table lists only 5 dossiers | Now 8 dossiers exist (missing: `tier1_binsulayem_epstein.md`, `tier2_egypt_gulf_integration.md`, `tier2_uae_coordination_node.md`) |
| `00_START_HERE.md` | "Repository Version: v10.1" | May need update if version has incremented |
| `06_ATTENTION_ECONOMY.md` | References "Kash Patel" and "Dan Bongino" | Bongino resigned Dec 17, 2025; Noem fired March 5, 2026; Mullin nominated. Renamed from `06_MAIN_CHARACTERS.md` and reframed as Attention Economy & Quotas. |
| `08_KEY_DATASETS.md` | Lists dataset locations | Does not include `New_Data_2026/Biopharma.csv`, `BlackRock_Timeline_Full_Decade.csv`, `Infrastructure_Forensics.csv`, or `output/` pipeline data |
| `08_KEY_DATASETS.md` | References dashboard data pipeline | Dashboard now has 6+ tabs, Ask AI feature, correlation engine — none documented |
| `10_FRAMEWORK_VALIDATION.md` | Last validation entry: Feb 21, 2026 (Sanders) | Feb 27-28, 2026 events (Arsenal of Freedom, Iran strikes) provide significant new validation/test data — not documented |

---

## 3. Missing Cross-References

| File A | File B | Missing Link |
|--------|--------|--------------|
| `11_Protest_Dynamics_and_Funding/README.md` (FaaS framework) | `09_Silicon_Sovereignty/VOCA_funding_timeline_clean.csv` | FaaS defunding mechanism references VOCA data but index doesn't connect them |
| `13_State_and_County_Analysis/arkansas_infrastructure_forensic_audit.md` | `Project_Trident/Copilot_Opus_4.6_Analysis/Arkansas_Federal_Energy_Bypass.md` | State-level and federal-level Arkansas bypass analyses not linked |
| `12_The_Media_Firewall/1789_Symbolism_Analysis.md` | `_AI_CONTEXT_INDEX/02_MEDIA_FIREWALL.md` | Semiotic bridge analysis exists but index doesn't reference it |
| `Project_Trident/Claude_Code_Analysis/Privatized_Integration_Networks_Q1_2026_Synthesis.md` | `_AI_CONTEXT_INDEX/03_BOARD_OF_PEACE.md` | Master synthesis covers Board of Peace but index doesn't link to it |
| `Archive/Retracted_Three_Layer_References.md` | `Project_Trident/Copilot_Opus_4.6_Analysis/Findings/AI_Fabrication_Case_Study.md` | Retraction history split across two files; neither referenced in index |
| `10_Real-Time_Updates_and_Tasks/Tasks/` (14 task files) | `_AI_CONTEXT_INDEX/09_CURRENT_THREADS.md` | Task templates not linked from current threads index |
| `sources/2026-02-28_Iran_Strike_Target_Mapping.md` | `_AI_CONTEXT_INDEX/04_CAPITAL_ARCHITECTURE.md` | Iran strikes directly impact documented SWF infrastructure; capital architecture index doesn't reference strike mapping |
| `sources/2026-02-28_Arsenal_of_Freedom_Defense_Industrial_Convergence.md` | `13_State_and_County_Analysis/arkansas_infrastructure_forensic_audit.md` | Defense industrial convergence in same Arkansas geography — not linked |
| `dashboard/app.py` (Prediction Tracker tab) | `Project_Trident/Copilot_Opus_4.6_Analysis/Verification_Reports/prediction_tracker_feb9_2026.md` | Dashboard prediction tracker and written prediction report not linked |
| `New_Data_2026/2026_Analysis.md` (0-lag convergence revision) | `_AI_CONTEXT_INDEX/01_CORE_THEORY.md` | Core theory mentions convergence but doesn't fully integrate the 0-lag finding |
| `14_Files/How_This_Happened-A_Policy_Brief.md` | `Project_Trident/Capital_Flow_Opacity_Framework.md` | Both document regulatory bypass mechanisms; not cross-linked in index |
| `docs/validation/VALIDATION_REPORT_2026-02-24.md` | `_AI_CONTEXT_INDEX/10_FRAMEWORK_VALIDATION.md` | External validation report not linked from framework validation index |
| `05_Geopolitical_Vectors/Venezuela_Privatization_Amnesty_Stack_Feb2026.md` | `_AI_CONTEXT_INDEX/09_CURRENT_THREADS.md` | Venezuela analysis exists but not referenced in current threads |
| `00_Quick_Breakdowns/About_Me.md` | `_AI_CONTEXT_INDEX/07_METHODOLOGY.md` | Scout methodology origin story not linked from methodology index |

---

## 4. Orphaned Content

| File | Location | Issue |
|------|----------|-------|
| `10_Real-Time_Updates_and_Tasks/2026_January/January 17, 2027 Analysis.txt` | Daily logs | Filename says "2027" — likely a typo for 2026. Content disconnected from any thread. |
| `Project_Trident/Copilot_Opus_4.6_Analysis/Omeed_Malik_Forensic_Node_Analysis.md` | Project_Trident | Duplicate of `12_The_Media_Firewall/Omeed_Malik_Forensic_Node_Analysis.md`. One copy is orphaned. |
| `Project_Trident/Copilot_Opus_4.6_Analysis/Archive/` (5 files) | Archive subdirectory | Working drafts and superseded analysis; no clear link to current versions |
| `06_Visualizations/1766389347560.jpg` | Visualizations | Single image file with no metadata, caption, or context document |
| `Analyzing Geopolitical and Media Control.pdf` | `12_The_Media_Firewall/` | PDF with no accompanying analysis or summary document |
| `Protest_Funding_Audit.pdf` | `11_Protest_Dynamics_and_Funding/` | PDF with no accompanying text summary |
| `Run_Correlations_Yourself/Wrong_Correlations/` (6 files) | Deprecated scripts | Deprecated but preserved; README explains but not linked from main verification path |
| `intel.txt` | Root | Input file for `test_api.py`; no documentation of its purpose or update cadence |
| `output/archive/` (39 files) | Historical outputs | Historical pipeline outputs; no index or analysis of trends across outputs |

---

## 5. Coverage Assessment

**Estimated index coverage of actual repository content**: ~35-40%

| Domain | Index Coverage | Gap Severity |
|--------|---------------|--------------|
| Core theory & statistics | ~90% | Low — well documented |
| Media firewall | ~75% | Medium — missing 1789 symbolism analysis, Super Bowl case study |
| Board of Peace | ~80% | Medium — missing Claude Code synthesis link |
| Capital architecture | ~70% | Medium — missing Arkansas state analysis, Iran strike impact |
| CRINK framework | ~85% | Low — mostly complete |
| Methodology | ~70% | Medium — missing scout methodology origin, statistical test scripts |
| Datasets | ~60% | High — many 2026 datasets and pipeline outputs not catalogued |
| Current threads | ~65% | Medium — missing task templates, Venezuela analysis |
| Infrastructure/Pipeline | ~10% | High — dashboard, spiders, CI/CD, daily pipeline nearly undocumented |
| Node Dossiers | ~65% | Medium — index missing 3 of 8 dossiers in listing |
| Project_Trident depth | ~25% | High — 80+ files, most not referenced in index |
| Retraction/fabrication history | ~5% | High — critical transparency info not in index |
| FaaS/Protest dynamics | ~0% | Critical — entirely absent from index |
| State-level analysis | ~10% | High — Arkansas audit not indexed |

---

## 6. Structural Issues

1. **No retraction/fabrication notice in index**: The repository transparently documents Grok fabrication and Layer 2-3 retraction in `Archive/` and `Findings/`, but the `_AI_CONTEXT_INDEX` makes no mention. An AI model reading only the index would not know about retracted claims.

2. **Pipeline infrastructure invisible**: The repository has a functioning automated intelligence pipeline (`daily_perplexity_update.py` → `output/daily_intelligence.json` → `dashboard/app.py`) that is completely invisible in the index.

3. **Duplicate content not flagged**: `Omeed_Malik_Forensic_Node_Analysis.md` exists in both `12_The_Media_Firewall/` and `Project_Trident/Copilot_Opus_4.6_Analysis/`. Several datasets exist in multiple locations (`Project_Trident/Copilot_Opus_4.6_Analysis/Datasets/` duplicates files from other directories).

4. **Source analysis directory underutilized**: `_AI_CONTEXT_INDEX/sources/` has only 4 files (all Feb 27-28, 2026). Earlier source analyses from Jan-Feb 2026 are scattered in `10_Real-Time_Updates_and_Tasks/` and not catalogued.

---

*Gap analysis completed 2026-03-01.*

---

## Changes Since March 1, 2026

**Last reviewed**: March 16, 2026

The following files have been added or significantly changed since the original gap analysis:

### New Files Added

| File | Location | Content | Gap Impact |
|------|----------|---------|------------|
| `06_ATTENTION_ECONOMY.md` | `_AI_CONTEXT_INDEX/` | Renamed from `06_MAIN_CHARACTERS.md`; rewritten as Attention Economy & Quotas framework with cross-administration comparison | **Closes gap**: Section 2 outdated reference about `06_MAIN_CHARACTERS.md` now resolved |
| `11_LEVERAGE_THESIS.md` | `_AI_CONTEXT_INDEX/` | New file formalizing the leverage mechanism: Musk/Epstein/Netanyahu origin case, Iran extension, Anthropic counter-example, capital architecture | **New content**: Not previously missing (didn't exist), but adds significant theoretical depth |
| `Statistical_Tests/README.md` | `Project_Trident/Copilot_Opus_4.6_Analysis/` | Documents 16-script robustness test suite (permutation, Granger, bootstrap, etc.) | **Partially closes gap**: Section 1 noted statistical test scripts unindexed; now have README documentation |
| `Unable_to_Verify_March_2026.md` | `Project_Trident/Copilot_Opus_4.6_Analysis/` | Tracks 9 items unable to verify as of March 6, 2026 (Schedule P/C, Section 122, BoP, Maxwell, etc.) | **New content**: Transparency mechanism for verification gaps |
| `Attention_Economy_and_Quotas_Cross_Administration_Analysis.md` | `Project_Trident/.../Narrative_Case_Studies/` | Cross-administration noise generator analysis (NCS-2026-002) | **Partially closes gap**: Section 1 noted Narrative_Case_Studies unindexed |
| `speaker-conversation-2026-03-06-22-58-42.md` | `Project_Trident/The_Speaker/March_2026/` | Gap analysis and prioritization of 14 update areas | **New content**: Speaker conversation exports |
| `speaker-conversation-2026-03-07-01-14-18.md` | `Project_Trident/The_Speaker/March_2026/` | 5 research gap findings (Mojtaba succession, Venezuela, Section 122, Mullin, OpenAI Pentagon) | **New content**: Speaker conversation exports |
| `sync_ai_context.yml` | `.github/workflows/` | New workflow for syncing AI context index | **Partially closes gap**: Section 1 noted `.github/workflows/` unindexed |
| `tier1_maxwell_leverage.md` | `_AI_CONTEXT_INDEX/Node_Dossiers/` | New Tier 1 dossier documenting Maxwell's Phase 0 infrastructure (1991–2003), current leverage position (clemency negotiation, habeas petition, 5th Amendment invocation at FPC Bryan), and the Administrative Pincer mechanism (VOCA funding freeze in Epstein infrastructure states NM/NV/NY). Integrates data from `08_How_It's_Possible/` directory files. | **Partially closes gap**: Section 1 noted `08_How_It's_Possible/` not indexed; now indexed via dossier cross-references and CONTEXT_ROUTER entries |
| `Arkansas_Law_Forensic_Audit_Verification.md` | `Project_Trident/Copilot_Opus_4.6_Analysis/` | Independent verification of 28 claims from `13_State_and_County_Analysis/Arkansas_Law_Forensic_Audit.md`. 20/28 ✅ VERIFIED, 8/28 ⚠️ PARTIALLY VERIFIED, 0 contradicted. | **Partially closes gap**: Section 1 noted `13_State_and_County_Analysis/` unindexed; now verified and integrated via Node 9 in `09_CURRENT_THREADS.md` |
| `tier2_religious_infrastructure.md` | `_AI_CONTEXT_INDEX/Node_Dossiers/` | New Tier 2 dossier documenting eschatological policy pipeline: Paula White (access controller), Capitol Ministries (curriculum), CREC/Doug Wilson (Pentagon denominational pipeline), CUFI/John Hagee (mass political base), Hegseth (convergence node), Dan Patrick / Religious Liberty Commission (enforcement), and the denominational fault line (Christian Zionism vs. Catholic/Replacement Theology). | **New content**: `15_The_Religious_Layer/` directory now fully indexed via Node 10 in `09_CURRENT_THREADS.md`, `tier2_religious_infrastructure.md` dossier, CONTEXT_ROUTER entries, and `00_START_HERE.md` references |

### Significant Changes to Existing Files

| File | Changes | Gap Impact |
|------|---------|------------|
| `09_CURRENT_THREADS.md` | Major March addenda: Iran war Day 7, Khamenei death, Strait of Hormuz, DHS Noem firing, Anthropic designation, Clinton depositions, TikTok lawsuit, Venezuela normalization, Speaker analysis findings, **Node 8: Oracle Financial Stress** (March 7). **March 8: Node 1 (Maxwell) upgraded with verified facility, clemency status, habeas petition, immunity rejection, cross-reference to new dossier. Node 9: Arkansas State-Level Preemption / Datacenter Capital Nexus — 11 verified data points covering Dec 2025 *Good Day Farm* ruling, $17B+ datacenter investment, Hugh McDonald conflict of interest, initiative restrictions, WV preemption template.** **March 16: Node 10: Religious Layer / Eschatological Infrastructure — theological-policy pipeline (Paula White, Capitol Ministries, CREC/Wilson, CUFI/Hagee), Hegseth convergence node, enforcement mechanism (Corporate → Government → Intelligence), denominational fault line, Vought personnel overlap.** | **Partially closes gap**: Section 2 noted current threads was out of date; Section 1 noted `13_State_and_County_Analysis/` unindexed |
| `10_FRAMEWORK_VALIDATION.md` | Added Sections 6 (Defense convergence), 7 (War widening), **8 (Oracle-Stargate contraction)** (March 7) | **Closes gap**: Section 2 noted validation entries stopped at Feb 21 |
| `04_CAPITAL_ARCHITECTURE.md` | Added Feb 28 kinetic impact, March 1-6 energy crisis, **March 7: Oracle Financial Stress, Stargate contraction, Energy crisis capital breaker** | **Partially closes gap**: Section 2 noted Iran strike impact not documented |
| `02_MEDIA_FIREWALL.md` | **Added March 7: Ellison Dual Exposure (Oracle × WBD)** — links capital architecture to media firewall through single individual | **New cross-reference**: Creates previously unmapped connection between `04_CAPITAL_ARCHITECTURE.md` and `02_MEDIA_FIREWALL.md` |
| `CONTEXT_ROUTER.md` | Updated March 6-7: Added routing for Iran war, DHS/Noem, Anthropic, Epstein DOJ, energy crisis, unable-to-verify file. **Updated March 8: Added routing for Maxwell leverage node (clemency, VOCA, administrative pincer, institutional plumbing); `08_How_It's_Possible/` directory now routed. Added routing for Arkansas law / state preemption / datacenter capital nexus (Node 9) and state-level democratic preemption / initiative restrictions.** | **Partially closes gap**: Router now covers more topics |
| `00_START_HERE.md` | Updated to v10.4; renamed `06_ATTENTION_ECONOMY.md` in table | **Partially closes gap**: Version updated |
| `NODE_INDEX.md` | **Updated March 8: Added `tier1_maxwell_leverage.md` to Tier 1 table; added entity mappings for Maxwell/Ghislaine/clemency, VOCA/trafficking funds, and administrative pincer** | **Partially closes gap**: Section 5 noted Node Dossiers coverage at ~65% |

### Gaps Partially or Fully Closed Since March 1

| Original Gap | Status | How Addressed |
|--------------|--------|---------------|
| `10_FRAMEWORK_VALIDATION.md` stopped at Feb 21 (Section 2) | ✅ **CLOSED** | Sections 6, 7, 8 added covering Feb 27 through March 7 |
| `06_MAIN_CHARACTERS.md` outdated (Section 2) | ✅ **CLOSED** | Renamed to `06_ATTENTION_ECONOMY.md` with full rewrite |
| Iran strikes not in capital architecture (Section 3) | ✅ **CLOSED** | Feb 28 and March 1-6 updates added to `04_CAPITAL_ARCHITECTURE.md` |
| Statistical test scripts unindexed (Section 1) | ⚠️ **PARTIALLY CLOSED** | README.md created; individual scripts still not catalogued |
| `.github/workflows/` not indexed (Section 1) | ⚠️ **PARTIALLY CLOSED** | `sync_ai_context.yml` added; referenced in `00_START_HERE.md` pipeline table |
| `08_How_It's_Possible/` not indexed (Section 1) | ⚠️ **PARTIALLY CLOSED** | `tier1_maxwell_leverage.md` integrates data from all 4 files in directory; CONTEXT_ROUTER entries added for Maxwell/VOCA/administrative pincer/institutional plumbing routing to directory files |
| Node Dossiers listing missing Maxwell (Section 5) | ✅ **CLOSED** | `tier1_maxwell_leverage.md` created; NODE_INDEX.md updated with entity mappings |
| Venezuela not referenced in current threads (Section 3) | ⚠️ **PARTIALLY CLOSED** | Venezuela normalization added to `09_CURRENT_THREADS.md` March updates |
| `00_START_HERE.md` version outdated (Section 2) | ✅ **CLOSED** | Updated to v10.4 |
| Capital architecture ↔ Media firewall not linked (new) | ✅ **CLOSED** | Ellison Dual Exposure section creates cross-reference |
| `13_State_and_County_Analysis/` unindexed (Section 1) | ⚠️ **PARTIALLY CLOSED** | Arkansas Law Forensic Audit verified (20/28 claims); integrated as Node 9 in `09_CURRENT_THREADS.md`; CONTEXT_ROUTER entries added; verification report created in Project_Trident |

### Gaps Still Open

The following gaps from the original March 1 analysis remain unaddressed:

| Gap | Severity | Section |
|-----|----------|---------|
| `00_Quick_Breakdowns/` not indexed | Medium | Section 1 |
| `11_Protest_Dynamics_and_Funding/` absent from index | Critical | Section 1 |
| `Archive/` retraction history not in index | High | Section 1 |
| `docs/` not indexed | Low | Section 1 |
| `federal_register/` not indexed | Medium | Section 1 |
| Dashboard application not indexed in detail | High | Section 1 |
| Pipeline infrastructure invisible | High | Section 6 |
| FaaS/Protest dynamics still absent from index | Critical | Section 5 |
| `08_KEY_DATASETS.md` missing 2026 datasets | High | Section 2 |
| Node Dossiers listing still missing 3 dossiers in `00_START_HERE.md` | Medium | Section 2 |
| Project_Trident depth coverage still ~30% | High | Section 5 |
| Orphaned content not cleaned up | Medium | Section 4 |
| Duplicate content (Omeed Malik) not resolved | Low | Section 6 |

### Updated Coverage Assessment

**Estimated index coverage**: ~45-50% (up from ~35-40% on March 1)

| Domain | March 1 Coverage | March 7 Coverage | Change |
|--------|-----------------|-------------------|--------|
| Core theory & statistics | ~90% | ~95% | ⬆ Leverage thesis + statistical test README |
| Media firewall | ~75% | ~85% | ⬆ Ellison dual exposure + source files indexed |
| Board of Peace | ~80% | ~80% | — No change |
| Capital architecture | ~70% | ~90% | ⬆ Major March updates (Oracle, energy crisis, Iran) |
| CRINK framework | ~85% | ~85% | — No change |
| Methodology | ~70% | ~75% | ⬆ Statistical test README |
| Datasets | ~60% | ~60% | — No change |
| Current threads | ~65% | ~90% | ⬆ Major March updates (9 nodes, March events, Arkansas verification) |
| Infrastructure/Pipeline | ~10% | ~15% | ⬆ sync_ai_context.yml added |
| Node Dossiers | ~65% | ~75% | ⬆ Maxwell dossier created; NODE_INDEX updated |
| Project_Trident depth | ~25% | ~30% | ⬆ Statistical tests, Unable to Verify, Narrative Case Studies |
| Framework validation | ~60% | ~95% | ⬆ Sections 6, 7, 8 added |
| Retraction/fabrication | ~5% | ~5% | — No change |
| FaaS/Protest dynamics | ~0% | ~0% | — No change (CRITICAL) |
| State-level analysis | ~10% | ~40% | ⬆ Arkansas Law Forensic Audit verified + Node 9 + CONTEXT_ROUTER routing |
| **Leverage thesis** | N/A | ~90% | 🆕 New file fully integrated |
| **Attention Economy** | ~50% | ~90% | ⬆ Renamed/rewritten + NCS routing |

---

*Gap analysis updated 2026-03-08. Previous update: 2026-03-07. Original analysis: 2026-03-01.*
