# Repository Audit — March 1, 2026

**Audit Date**: 2026-03-01  
**Auditor**: Automated AI audit  
**Repository Version**: v10.1 (per README.md)

---

## Purpose

Exhaustive inventory of every directory and file in The Regulated Friction Project, documenting contents, function, and cross-references.

---

## Root-Level Files

| File | Type | Content | Questions Answered |
|------|------|---------|-------------------|
| `README.md` | Markdown | Project overview, core finding (r=0.6196), statistics, repo structure map, methodology summary | What is this project? What's the evidence? |
| `Report.md` | Markdown | Detailed analysis of friction-compliance clustering, terminology, model mechanics, robustness tests, failed Q4 2025 13F predictions | How does the model work in depth? Where have predictions failed? |
| `QUICK_START.md` | Markdown | Data pipeline setup guide (DigitalOcean Droplet, GitHub push automation, Streamlit dashboard, caching fixes) | How do I deploy the automated pipeline? |
| `IMPLEMENTATION_SUMMARY.md` | Markdown | Technical record of pipeline fixes (cache TTL, cron automation, validation checklist) | What infrastructure issues were resolved? |
| `daily_perplexity_update.py` | Python | Standalone Perplexity (sonar-pro) intelligence pipeline; loads entities/signals from `intelligence_config.json`; outputs to `output/daily_intelligence.json` | How does the daily automated intelligence gathering work? |
| `test_api.py` | Python | Llama-4-Scout-17B clinical entity extraction pipeline; sends `intel.txt` to GitHub AI inference endpoint | How does the LLM entity extraction work? |
| `intelligence_config.json` | JSON | Tracked entities (6 categories: SWF, PE, government, geopolitical, tech, legal), 5 active signals, framework context | What entities and signals does the pipeline monitor? |
| `intel.txt` | Text | Mission brief / input text for `test_api.py` LLM extraction | What is the current intelligence focus? |
| `merge_spider_output.py` | Python | Merges Scrapy spider JSON output files | How are spider outputs consolidated? |
| `push_spider_data.sh` | Shell | Pushes scraped data to remote storage | How does scraped data reach the dashboard? |
| `requirements.txt` | Text | Python dependencies for root-level scripts | What packages does this project need? |
| `scrapy.cfg` | Config | Scrapy project configuration | How is the web scraping framework configured? |
| `scrapinghub.yml` | YAML | Scrapinghub/Zyte deployment configuration | How is the scraper deployed to cloud? |

---

## `.devcontainer/`

| File | Content |
|------|---------|
| `devcontainer.json` | VS Code dev container configuration for consistent development environment |

**Dependencies**: None  
**Questions answered**: How to set up a local dev environment?

---

## `.github/workflows/`

| File | Content |
|------|---------|
| `daily_pipeline.yaml` | GitHub Actions workflow running `daily_perplexity_update.py` on schedule |
| `sync_to_do_space.yml` | Syncs `_AI_CONTEXT_INDEX`, `output/`, `Run_Correlations_Yourself/`, `Control_Proof/`, `intelligence_config.json`, and key docs to DigitalOcean Space |
| `validate.yml` | Runs `py_compile` validation on dashboard and pipeline Python files |

**Dependencies**: `daily_perplexity_update.py`, `dashboard/`, `output/`  
**Questions answered**: How is CI/CD automated? What gets synced to production?

---

## `.vscode/`

| File | Content |
|------|---------|
| `settings.json` | VS Code workspace settings |

---

## `00_Quick_Breakdowns/`

| File | Type | Content |
|------|------|---------|
| `About_Me.md` | Markdown | Author biography (Austin Smith, 29, Arkansas, Army National Guard Cavalry Scout → security → research methodology). Explains "Numbers Station" concept and scout methodology origin. |
| `Copilot_Executive_Synthesis_Feb2026.md` | Markdown | AI-generated executive synthesis of repository findings as of February 2026 |

**Dependencies**: References `01_Levers_and_Frictions/`, `03_Master_Framework/`  
**Questions answered**: Who created this project and why? What is the scout methodology?

---

## `01_Levers_and_Frictions/`

| File | Type | Content |
|------|------|---------|
| `Epstein_Files_timeline.csv` | CSV | Temporal mapping of Epstein document releases (original) |
| `Epstein_Files_timeline_updated.csv` | CSV | Updated Epstein document release timeline |

**Dependencies**: Referenced by `03_Master_Framework/`, `Project_Trident/`  
**Questions answered**: When were Epstein documents released? What was the temporal pattern?

---

## `02_Anchors_and_Financials/`

| File | Type | Content |
|------|------|---------|
| `pep_banking_combined.csv` | CSV | Financial data on politically exposed persons and banking patterns |
| `pep_banking_sentiment.csv` | CSV | Sentiment analysis of financial narratives around PEPs |

**Dependencies**: Referenced by `03_Master_Framework/`, `_AI_CONTEXT_INDEX/04_CAPITAL_ARCHITECTURE.md`  
**Questions answered**: How do financial actors reposition during friction windows?

---

## `03_Master_Framework/`

| File | Type | Content |
|------|------|---------|
| `MASTER_reflexive_control_2015-2025.csv` | CSV | Reflexive control event mapping (2015-2025) |
| `MASTER_timeline_2015-2025_UPDATED.csv` | CSV | Updated master timeline of friction/compliance events |
| `updated_master_theory.csv` | CSV | Theory-linked event dataset |

**Dependencies**: Core dataset directory; referenced by nearly all analysis files  
**Questions answered**: What is the comprehensive timeline linking friction → compliance → capital flows?

---

## `04_Testing_and_Counters/`

| File | Type | Content |
|------|------|---------|
| `expanded_historical_backtest.csv` | CSV | Historical backtest of correlation (2017-2024) |
| `merged_backtest_counters.csv` | CSV | Counter-hypotheses and alternative explanations tested |

**Dependencies**: `Project_Trident/`, `Run_Correlations_Yourself/`  
**Questions answered**: Does the correlation survive robustness testing? What contradicts the finding?

---

## `05_Geopolitical_Vectors/`

| File | Type | Content |
|------|------|---------|
| `Board_of_Peace_Security_Architecture.md` | Markdown | Three-layer enforcement model: private contractors (UG Solutions), state proxies (Pakistan), cyber infrastructure (Palo Alto/CyberArk + G42 AI). ISF deployment under UN Resolution 2803. |
| `CRINK_Analysis.md` | Markdown | China-Russia-Iran-NK coordination discourse analysis. Sept 26, 2025 convergence. 34 records Jan 2025-Jan 2026. |
| `Global_Election_Analysis.md` | Markdown | Election timing correlations with friction windows globally |
| `Graham_Venezuela_Analysis.md` | Markdown | Sen. Graham's public statement timing aligned with Venezuela policy shifts |
| `Graham_Venezuela_Posts_Timeline.csv` | CSV | Timeline of Graham's Venezuela-related posts |
| `January_2026_Parallel_Operations_Timeline.md` | Markdown | Venezuela (high attention) vs. Yemen (low attention) simultaneous events; attention distribution mechanics |
| `Venezuela_Privatization_Amnesty_Stack_Feb2026.md` | Markdown | Multi-layered Venezuela reset: economic, political, legal, structural |
| `thermostat_control_data.csv` | CSV | Calendar anchor mapping against event clustering |

**Dependencies**: `_AI_CONTEXT_INDEX/03_BOARD_OF_PEACE.md`, `_AI_CONTEXT_INDEX/05_CRINK_FRAMEWORK.md`, `11_Protest_Dynamics_and_Funding/`  
**Questions answered**: What geopolitical events validate the pattern? How does the Board of Peace govern Gaza reconstruction? What is CRINK? How does Venezuela fit?

---

## `06_Visualizations/`

| File | Type | Content |
|------|------|---------|
| `1766389347560.jpg` | Image | Visual diagram (content requires image viewing) |

**Dependencies**: Various analysis directories  
**Questions answered**: Visual representation of framework elements

---

## `07_My_Previous_Epstein_Research/`

| File | Type | Content |
|------|------|---------|
| `Epstein OSINT — Ultimate Report.pdf` | PDF | Pre-framework Epstein investigation report |
| `Epstein_China_Breif.pdf` | PDF | China intelligence links to Epstein network |
| `Timeline.pdf` | PDF | Original Epstein event timeline |
| `Timeline_Updated.pdf` | PDF | Updated Epstein timeline |

**Dependencies**: `01_Levers_and_Frictions/`  
**Questions answered**: What was researched before the thermostat framework emerged? What are the Epstein-China connections?

---

## `08_How_It's_Possible/`

| File | Type | Content |
|------|------|---------|
| `08_How_Its_Possible.md` | Markdown | Mechanisms enabling the pattern: regulatory gaps, CFIUS exemptions, FARA non-compliance |
| `DOJ_Probe_Results.csv` | CSV | DOJ investigation outcomes dataset |
| `Phase_0_Maxwell_Pivot.csv` | CSV | Maxwell negotiation/leverage timeline |
| `pincer_data.csv` | CSV | Temporal pincer window data |

**Dependencies**: `Project_Trident/Capital_Flow_Opacity_Framework.md`, `14_Files/How_This_Happened-A_Policy_Brief.md`  
**Questions answered**: How can this pattern exist in a regulated system? What mechanisms enable it?

---

## `09_Silicon_Sovereignty/`

| File | Type | Content |
|------|------|---------|
| `SILICON_SOVEREIGNTY_REPORT.md` | Markdown | Core hypothesis: friction events deployed to anchor tech transfers. 4 validation tests passed. r=0.62 correlation in 2,105-event cross-dataset; χ²=330.62 (p<0.0001, 14-day periodicity). December 2025 "pincer" model. |
| `CRUCIAL-Cross_Verification_Check.md` | Markdown | Independent AI verification of Silicon Sovereignty claims |
| `Infrastructure_Consolidation_Pattern_Jan2026.md` | Markdown | Tech consolidation during friction windows (Jan 2026) |
| `Coalition_Narrative_Map_2015-2025.csv` | CSV | Media narrative patterns (456 records) |
| `REFINED_supercomputer_geopolitics (1).csv` | CSV | US-China exascale computing race chronology |
| `Regulatory_Map_Data_CLEANED.csv` | CSV | 76 regulatory/compliance events mapped to friction dates |
| `VOCA_funding_timeline_clean.csv` | CSV | Victim services funding cuts following friction events (667 records) |

**Dependencies**: `04_Testing_and_Counters/`, `_AI_CONTEXT_INDEX/04_CAPITAL_ARCHITECTURE.md`  
**Questions answered**: Is the 7-day median lag driven by compute/AI infrastructure moves? What is Silicon Sovereignty? Are there cover-and-liquidate sequences?

---

## `10_Real-Time_Updates_and_Tasks/`

| File | Type | Content |
|------|------|---------|
| `README.md` | Markdown | Directory overview and purpose |

### `10_Real-Time_Updates_and_Tasks/2026_January/`

| File | Type | Content |
|------|------|---------|
| `Daily Tasks January 18, 2026.md` | Markdown | Daily research log |
| `January 14, 2026.md` | Markdown | Daily research log |
| `January 17, 2027 Analysis.txt` | Text | Analysis notes (filename suggests 2027 but likely 2026 typo) |
| `January_22_2026.md` | Markdown | Daily research log |
| `Saudi Bitcoin Influence and Geopolitics.md` | Markdown | Saudi Bitcoin strategy analysis |

### `10_Real-Time_Updates_and_Tasks/2026_February/`

| File | Type | Content |
|------|------|---------|
| `February-05-2026.md` | Markdown | Daily research log |
| `February-26-2026.md` | Markdown | Daily research log |

### `10_Real-Time_Updates_and_Tasks/Tasks/`

| File | Type | Content |
|------|------|---------|
| `README.md` | Markdown | Task directory overview |
| `CRINK.md` | Markdown | CRINK tracking task |
| `Cuba.md` | Markdown | Cuba analysis task |
| `Elite_Watch.md` | Markdown | Elite entity monitoring task |
| `Epstein_Files_Theory.md` | Markdown | Epstein files analysis task |
| `Financial_Anchor.md` | Markdown | Financial anchor monitoring task |
| `Media_Cycle_Density.md` | Markdown | Media cycle density tracking task |
| `Netherlands.md` | Markdown | Netherlands analysis task |
| `Policies_Daily.md` | Markdown | Daily policy tracking task |
| `Protests_FaaS_Supply_Chain.md` | Markdown | Friction-as-a-Service supply chain task |
| `Saudi_Arabia.md` | Markdown | Saudi Arabia monitoring task |
| `Silence_Monitor.md` | Markdown | Media silence monitoring task |
| `Taiwan.md` | Markdown | Taiwan analysis task |
| `Ukraine.md` | Markdown | Ukraine analysis task |

**Dependencies**: `_AI_CONTEXT_INDEX/09_CURRENT_THREADS.md`  
**Questions answered**: What is being actively tracked? What are the current research priorities?

---

## `11_Protest_Dynamics_and_Funding/`

| File | Type | Content |
|------|------|---------|
| `README.md` | Markdown | FaaS (Friction-as-a-Service) framework: rent-a-crowd ($60-$200/day), mercenary canvassers, logistical dissent. 50.7% surge Dec 19 2025-Jan 15 2026. VOCA funding redirection. |
| `Protest_Funding_Audit.pdf` | PDF | Forensic audit of protest funding mechanisms |

**Dependencies**: `09_Silicon_Sovereignty/` (VOCA data), `_AI_CONTEXT_INDEX/09_CURRENT_THREADS.md`  
**Questions answered**: How are protests instrumentalized? Is there a supply chain for manufacturing friction? Why does VOCA funding get redirected?

---

## `12_The_Media_Firewall/`

| File | Type | Content |
|------|------|---------|
| `README.md` | Markdown | Heat Sink hypothesis: TCN, Daily Wire, PublicSq as "Media Firewall." Gulf SWF funding. Omeed Malik as structural nexus. Feb 27, 2026 boundary shift. |
| `1789_Symbolism_Analysis.md` | Markdown | Semiotic bridge: 1789 significance for US founding AND Saudi First State (1789 conquest). 1789 Capital FII appearance (Riyadh, Oct 2025). |
| `Omeed_Malik_Forensic_Node_Analysis.md` | Markdown | Malik's multi-platform control: Daily Caller, TCN, Substack. Prime Brokerage capital + populist narrative intersection. |
| `Super_Bowl_LX_Media_Firewall_Case_Study.md` | Markdown | Super Bowl LX messaging as Media Firewall case study |
| `Analyzing Geopolitical and Media Control.pdf` | PDF | Geopolitical media control analysis |

**Dependencies**: `_AI_CONTEXT_INDEX/02_MEDIA_FIREWALL.md`, `14_Files/Main_Characters.md`  
**Questions answered**: Who controls anti-establishment media? What are the structural conflicts of interest? How is narrative regulated?

---

## `13_State_and_County_Analysis/`

| File | Type | Content |
|------|------|---------|
| `arkansas_infrastructure_forensic_audit.md` | Markdown | Arkansas as legal infrastructure test case. Five elements: Act 373 (PSC override), Act 548 (data center tax incentives), PSC Docket 25-047-U (Jefferson Power Station), League of Women Voters v. Jester (ballot initiative firewall), AVAIO investor obscurity ($6B). |

**Dependencies**: `_AI_CONTEXT_INDEX/04_CAPITAL_ARCHITECTURE.md`, `Project_Trident/Copilot_Opus_4.6_Analysis/Arkansas_Federal_Energy_Bypass.md`  
**Questions answered**: How can infrastructure consolidation bypass democratic checks? What is the PSC's actual authority?

---

## `14_Files/`

| File | Type | Content |
|------|------|---------|
| `'Transparency'_Timeline.md` | Markdown | Document release timing (Epstein files, redaction failures) |
| `Alternate_Mechanisms.md` | Markdown | Alternative explanations tested and rejected |
| `CITATION.cff` | CFF | Machine-readable citation format |
| `CRUCIAL_Synthesis_Dec19_Convergence.md` | Markdown | December 19, 2025 convergence analysis (5 signal types) |
| `Case_Study_David_Barnes_Detention.md` | Markdown | Framework application to specific case |
| `China_State_Media_Null_and_Meanings.md` | Markdown | China's narrative role analysis |
| `Claude's_Analysis.md` | Markdown | Independent Claude AI verification |
| `FINANCIAL_RECEIPT_VERIFICATION.md` | Markdown | Financial flow audit documentation |
| `Glossary.md` | Markdown | 150+ term definitions (friction, compliance, calendar anchor, convergence, thermostat, etc.) |
| `How_This_Happened-A_Policy_Brief.md` | Markdown | Regulatory pathways: CFIUS §800.307, CHIPS Act gap, FARA non-compliance, Treasury OISP |
| `Implications.md` | Markdown | Policy implications if pattern is structural |
| `Main_Characters.md` | Markdown | Performative actors generating noise (Patel, Rubio, Hegseth, Noem) |
| `SOURCES.md` | Markdown | Master citation archive organized by category |
| `TRANSPARENCY_NOTE_FOR_2026_ANALYSIS.md` | Markdown | Transparency note for AI-assisted analysis |
| `Thermostat_Explained.md` | Markdown | Detailed thermostat metaphor explanation |
| `VERIFICATION_REPORT_Jan2026.md` | Markdown | January 2026 data validation report |
| `resistance_indicators.md` | Markdown | Indicators of institutional resistance to pattern |

**Dependencies**: Referenced by nearly all other directories  
**Questions answered**: Central documentation hub covering terminology, methodology, sources, policy implications, and verification.

---

## `Archive/`

| File | Type | Content |
|------|------|---------|
| `DROPLET_SETUP.md` | Markdown | DigitalOcean Droplet automation guide (crontab scheduling) |
| `Grok_Analysis.md` | Markdown | Grok-generated analysis of thermostat as coercive federalism (partially retracted due to fabrication) |
| `Repository_Synthesis.md` | Markdown | RETRACTED three-layer model; Layers 2-3 relied on Grok-fabricated statistics |
| `Retracted_Three_Layer_References.md` | Markdown | Transparency document identifying fabricated references |
| `crontab_template.txt` | Text | Crontab configuration template |

### `Archive/PIPELINE_RECOMMENDATIONS/`

| File | Type | Content |
|------|------|---------|
| `README.md` | Markdown | Pipeline recommendations overview |
| `01_SYNC_DEBUG_REPORT.md` | Markdown | Sync debugging report |
| `02_OPSEC_AUDIT.md` | Markdown | Operations security audit |
| `03_OPTIMIZATION_GUIDE.md` | Markdown | Pipeline optimization guide |

**Dependencies**: `Copilot_Opus_4.6_Analysis/Findings/AI_Fabrication_Case_Study.md`  
**Questions answered**: What infrastructure has been deprecated? What was retracted and why?

---

## `Control_Proof/`

| File | Type | Content |
|------|------|---------|
| `MASTER_reflexive_control_v2.csv` | CSV | Reflexive control dataset v2 |
| `correlation_results.txt` | Text | Core correlation output (r=0.6196, p=0.0004, n=28) |
| `master_reflexive_correlation_data.csv` | CSV | 30-row dataset with friction/compliance scoring |
| `reflexive_control_scraped_data.csv` | CSV | Scraped reflexive control data |
| `thermostat_control_data.csv` | CSV | Control dataset for robustness testing |

**Dependencies**: `Run_Correlations_Yourself/`, `Project_Trident/`  
**Questions answered**: What is the core statistical evidence? Can the correlation be independently verified?

---

## `New_Data_2026/`

| File | Type | Content |
|------|------|---------|
| `2026_Analysis.md` | Markdown | Revised thermostat model: simultaneous convergence (r=0.6685 at 0-lag). December 2025 pincer window. 5-signal convergence. |
| `Additional_Anchors_Jan2026_Final.csv` | CSV | 50 additional anchor events (Jan 2026) |
| `Biopharma.csv` | CSV | 108 biopharma events (FDA deregulation, DOGE cuts) |
| `BlackRock_Timeline_Full_Decade.csv` | CSV | 674 BlackRock events (2015-2025) |
| `CRINK_Intelligence_Dataset_Final_Verified.csv` | CSV | CRINK intelligence dataset (verified) |
| `High_Growth_Companies_2015_2026.csv` | CSV | 1,049 high-growth company records (excluded from primary correlation) |
| `Infrastructure_Forensics.csv` | CSV | 107 infrastructure forensic records |
| `Timeline_Update_Jan2026_Corrected (1).csv` | CSV | 99 corrected timeline events (Jan 2026) |

**Dependencies**: `Control_Proof/`, `Project_Trident/`  
**Questions answered**: How has the model evolved with 2026 data? What new datasets support or challenge the framework?

---

## `Project_Trident/`

| File | Type | Content |
|------|------|---------|
| `README.md` | Markdown | Project Trident overview |
| `Capital_Flow_Opacity_Framework.md` | Markdown | Three mechanisms: NULL field vulnerabilities, codified regulatory exemptions (CFIUS, CHIPS, FARA), administrative timing (7-day median lag) |
| `DATASET_REFERENCE.md` | Markdown | Dataset schemas for 5 core CSVs |
| `Ritual_Timing_Signal_Analysis.md` | Markdown | Ritual event proximity: 50.7% vs. 19.9% baseline (p=0.002 Mann-Whitney U) |
| `Verify_Trident_Analysis.py` | Python | Verification script for Trident analysis |
| `anchor_events_parsed.csv` | CSV | 70+ anchor events parsed |
| `project_trident_final_dossier.csv` | CSV | 118-record final dossier |
| `ritual_events_parsed.csv` | CSV | 51 ritual event signals |
| `temporal_correlations_analyzed.csv` | CSV | Temporal correlation analysis |

### `Project_Trident/Best_Data_For_Project_Trident/`

| File | Type | Content |
|------|------|---------|
| `Expanded_Policy_Anchors.csv` | CSV | Expanded policy anchor dataset |
| `Fund_Flow_Ritual_Coordination_2025.csv` | CSV | Fund flow and ritual event coordination data |
| `Holidays_2015_2025_Verified.csv` | CSV | Verified holiday calendar (2015-2025) |
| `Lag_Correlation_Analysis_Verified_Holidays.csv` | CSV | Lag correlation against verified holidays |
| `aid_timeline_clean.csv` | CSV | Clean aid event timeline |
| `policy_cleaned.csv` | CSV | Cleaned policy event dataset |
| `ritual_events_parsed.csv` | CSV | Ritual events (duplicate of parent) |
| `tech_filled_dates.csv` | CSV | Tech events with date filling |

### `Project_Trident/Claude_Code_Analysis/`

| File | Type | Content |
|------|------|---------|
| `README.md` | Markdown | Claude analysis directory overview |
| `13F_Analysis_Integration.md` | Markdown | 13F filing integration analysis |
| `Critical Model Analysis Framework.txt` | Text | Critical model analysis framework |
| `FaaS_Signal_Verification_Feb13.md` | Markdown | FaaS signal verification (Feb 13, 2026) |
| `Internal_Administrative_Friction_Verification.md` | Markdown | Internal admin friction verification |
| `LEAD_ANALYST_REVIEW.md` | Markdown | Lead analyst review document |
| `Phoenix_Settlement_Portfolio_and_New_Gaza.md` | Markdown | Phoenix Settlement Portfolio and New Gaza development analysis |
| `Pre_13F_Verification_Baseline.md` | Markdown | Q4 2025 13F prediction baseline |
| `Privatized_Integration_Networks_Q1_2026_Synthesis.md` | Markdown | Master synthesis: finance, governance, defense, territory, tech |

### `Project_Trident/Copilot_Opus_4.6_Analysis/`

| File | Type | Content |
|------|------|---------|
| `README.md` | Markdown | Copilot Opus analysis directory overview |
| `Arkansas_Federal_Energy_Bypass.md` | Markdown | DATA Act (S. 3585) CREU exemption from FERC/FPA/PURPA/PUHCA |
| `Enforcement_Hollowing_and_PineBridge_Analysis_Feb14_2026.md` | Markdown | 4 underreported agency actions, Schedule P/C, PineBridge Form D anomaly |
| `Evangelical_Network_Cross_Reference_Analysis.md` | Markdown | Evangelical networks across Russia/Gulf/Israel — parallel but separate |
| `February_2026_Consolidation_Timeline.md` | Markdown | Feb 2026 consolidation timeline |
| `February_2026_Supplementary_Addition.md` | Markdown | Supplementary analysis additions |
| `February_2026_System_Pattern_Analysis.md` | Markdown | System pattern analysis |
| `Final_Research_Sweep_Feb12.md` | Markdown | Research sweep completion (Feb 12) |
| `Forensic_Vetting_Board_of_Peace.md` | Markdown | Board of Peace forensic vetting |
| `Omeed_Malik_Forensic_Node_Analysis.md` | Markdown | Malik forensic analysis (duplicate location) |
| `TikTok_Algorithm_Anomaly_Investigation.md` | Markdown | TikTok algorithm anomaly investigation |
| `Total_Actor_and_Timeline_Synthesis.md` | Markdown | Repository-wide actor network (7 Tier 1, 6 Tier 2 entities), capital flow architecture, consolidated timeline |

### `Project_Trident/Copilot_Opus_4.6_Analysis/13F_Analysis/`

| File | Type | Content |
|------|------|---------|
| `13F_Holdings_Baseline_Q3_2025.csv` | CSV | Baseline 13F holdings (Q3 2025) |
| `13F_Holdings_Q4_2025.csv` | CSV | Q4 2025 13F holdings |
| `13F_Supplementary_Analysis_Feb14_2026.md` | Markdown | Supplementary 13F analysis |
| `13F_Verification_Report_Feb14_2026.md` | Markdown | 13F verification report |
| `Entity_13F_Cross_Reference.csv` | CSV | Entity cross-reference |
| `Q4_2025_Delta_Findings.md` | Markdown | Q4 2025 change findings |
| `Security_Level_Cross_Reference.csv` | CSV | Security-level cross-reference |

### `Project_Trident/Copilot_Opus_4.6_Analysis/Administrative_State_Audit/`

| File | Type | Content |
|------|------|---------|
| `DOGE_node_timeline.md` | Markdown | DOGE department operations timeline |
| `DOJ_node_timeline.md` | Markdown | DOJ department timeline |
| `FBI_node_timeline.md` | Markdown | FBI operations timeline |
| `OPM_node_timeline.md` | Markdown | OPM operations timeline |
| `repo_alignment.md` | Markdown | Alignment with repository framework |
| `verification_of_wiring_diagram.md` | Markdown | Wiring diagram verification |
| `wiring_diagram.md` | Markdown | Administrative state wiring diagram |

### `Project_Trident/Copilot_Opus_4.6_Analysis/Archive/`

| File | Type | Content |
|------|------|---------|
| `correlation_summary.md` | Markdown | Archived correlation summary |
| `feb11_system_pattern_working_draft.md` | Markdown | Working draft (Feb 11) |
| `granger_causality_results.md` | Markdown | Archived Granger causality results |
| `new_analysis_findings.md` | Markdown | Archived analysis findings |
| `scrutiny_report_feb8_2026.md` | Markdown | Scrutiny report (Feb 8) |

### `Project_Trident/Copilot_Opus_4.6_Analysis/Changelogs/`

| File | Type | Content |
|------|------|---------|
| `v9.2_Integration_Notes.md` | Markdown | v9.2 integration notes |
| `v9.3_Integration_Notes.md` | Markdown | v9.3 integration notes |
| `v9.4_Integration_Notes.md` | Markdown | v9.4 integration notes |
| `v11.0_Q4_2025_13F_Update.md` | Markdown | v11.0 Q4 2025 13F update |
| `v11.4_Total_Actor_Timeline_Synthesis.md` | Markdown | v11.4 actor timeline synthesis |

### `Project_Trident/Copilot_Opus_4.6_Analysis/Consolidation_Analysis/`

| File | Type | Content |
|------|------|---------|
| `consolidation_pattern_significance.md` | Markdown | Consolidation pattern significance analysis |

### `Project_Trident/Copilot_Opus_4.6_Analysis/Datasets/`

Contains 22 CSV files that are copies/aggregations of datasets from across the repo for use in statistical testing. Includes:
`Coalition_Narrative_Map_2015-2025.csv`, `Epstein_Files_timeline.csv`, `Expanded_Policy_Anchors.csv`, `Fund_Flow_Ritual_Coordination_2025.csv`, `Holidays_2015_2025_Verified.csv`, `Lag_Correlation_Analysis_Verified_Holidays.csv`, `MASTER_reflexive_control_v2.csv`, `MASTER_timeline_2015-2025_UPDATED.csv`, `REFINED_supercomputer_geopolitics (1).csv`, `Regulatory_Map_Data_CLEANED.csv`, `VOCA_funding_timeline_clean.csv`, `aid_timeline_clean.csv`, `anchor_events_parsed.csv`, `master_reflexive_correlation_data.csv`, `pep_banking_combined.csv`, `policy_cleaned.csv`, `project_trident_final_dossier.csv`, `reflexive_control_scraped_data.csv`, `ritual_events_parsed.csv`, `tech_filled_dates.csv`, `temporal_correlations_analyzed.csv`, `thermostat_control_data.csv`, `updated_master_theory.csv`

### `Project_Trident/Copilot_Opus_4.6_Analysis/Entity_Reports/`

| File | Type | Content |
|------|------|---------|
| `Palantir_Technologies_Deep_Dive.md` | Markdown | Palantir entity analysis |

### `Project_Trident/Copilot_Opus_4.6_Analysis/FaaS_Signal_Analysis/`

| File | Type | Content |
|------|------|---------|
| `feb9_2026_signal_verification.md` | Markdown | FaaS signal verification (Feb 9) |
| `january_2026_signal_analysis.md` | Markdown | January 2026 signal analysis |
| `recommendation_verification_feb9.md` | Markdown | Recommendation verification (Feb 9) |

### `Project_Trident/Copilot_Opus_4.6_Analysis/Findings/`

| File | Type | Content |
|------|------|---------|
| `AI_Fabrication_Case_Study.md` | Markdown | Grok fabrication audit; Layers 2-3 retracted |
| `backfill_correlation_results.md` | Markdown | Backfill correlation results |
| `backfill_guide.md` | Markdown | Backfill methodology guide |
| `dataset_provenance.md` | Markdown | Dataset provenance documentation |
| `first_differenced_granger.md` | Markdown | First-differenced Granger causality results |
| `flagged_references_feb10.md` | Markdown | Flagged references (Feb 10) |
| `granger_dec2025_robustness.md` | Markdown | Granger robustness excluding Dec 2025 |
| `granger_discrepancy_investigation.md` | Markdown | Granger discrepancy investigation |
| `historical_backfill.md` | Markdown | Historical backfill analysis |
| `partial_correlation_political_activity.md` | Markdown | Partial correlation with political activity |

### `Project_Trident/Copilot_Opus_4.6_Analysis/Influencer_Narrative_Timing/`

| File | Type | Content |
|------|------|---------|
| `media_firewall_narrative_timing_analysis.md` | Markdown | Media firewall narrative timing analysis |

### `Project_Trident/Copilot_Opus_4.6_Analysis/Narrative_Case_Studies/`

| File | Type | Content |
|------|------|---------|
| `Bondi_Hearing_Feb14_2026.md` | Markdown | AG Bondi hearing deflection pattern analysis |

### `Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/`

| File | Type | Content |
|------|------|---------|
| `.gitignore` | Config | Git ignore for test outputs |
| `autocorrelation_adjusted_test.py` | Python | Autocorrelation adjustment test |
| `backfill_analysis.py` | Python | Backfill analysis script |
| `backfill_lag_distribution.py` | Python | Backfill lag distribution analysis |
| `combined_dataset_correlation.py` | Python | Combined dataset correlation test |
| `cross_validation_dec2025.py` | Python | December 2025 cross-validation |
| `event_study_framework.py` | Python | Event-study analysis framework |
| `granger_causality_test.py` | Python | Granger causality test |
| `granger_discrepancy_investigation.py` | Python | Granger discrepancy investigation |
| `granger_exclude_dec2025.py` | Python | Granger test excluding Dec 2025 |
| `granger_first_differenced.py` | Python | First-differenced Granger test |
| `normalized_correlation.py` | Python | Normalized correlation analysis |
| `original_data_loader.py` | Python | Original data loading utility |
| `partial_correlation_political.py` | Python | Partial correlation with political activity |
| `permutation_test.py` | Python | Permutation test (1K shuffles) |
| `rolling_window_correlation.py` | Python | Rolling window correlation analysis |
| `year_distribution_audit.py` | Python | Year distribution audit |

### `Project_Trident/Copilot_Opus_4.6_Analysis/Verification_Reports/`

| File | Type | Content |
|------|------|---------|
| `prediction_tracker_feb9_2026.md` | Markdown | Prediction tracking (Feb 9) |

**Dependencies**: Extensive cross-references across entire repository  
**Questions answered**: What is the full analytical depth of the project? What statistical tests support the claims? What entities have been profiled? What predictions have been tracked?

---

## `Run_Correlations_Yourself/`

| File | Type | Content |
|------|------|---------|
| `README.md` | Markdown | Instructions for reproducing the three core correlations |
| `run_original_analysis.py` | Python | Reproduces three correlations: r=0.6196, Mann-Whitney U p=0.002, χ²=330.62 |
| `historical_backfill_2017_2024.csv` | CSV | Historical backfill dataset |
| `negative_windows.csv` | CSV | Windows where the pattern breaks (falsifiability) |
| `requirements.txt` | Text | Python dependencies for running verification |

### `Run_Correlations_Yourself/Wrong_Correlations/`

| File | Type | Content |
|------|------|---------|
| `README.md` | Markdown | Explanation of deprecated scripts |
| `DISCREPANCY_ANALYSIS.md` | Markdown | Discrepancy analysis between original and updated correlations |
| `independent_statistical_verification.py` | Python | Independent verification script |
| `original_correlation_test.py` | Python | Original correlation test |
| `reproduce_original_correlation.py` | Python | Original correlation reproduction |
| `reproduce_updated_correlation.py` | Python | Updated correlation reproduction |
| `run_original_analysis.py` | Python | Original analysis script (deprecated version) |

**Dependencies**: `Control_Proof/`, `Project_Trident/`  
**Questions answered**: Can I independently verify the core claims? What was wrong with previous correlation calculations?

---

## `dashboard/`

| File | Type | Content |
|------|------|---------|
| `app.py` | Python | 6-tab Streamlit dashboard: Home, Statistical Overview, Data Explorer, Prediction Tracker, Raw Data Explorer, Framework Explanation. Includes 🤖 Ask AI tab querying DO GenAI agent. |
| `constants.py` | Python | Core statistics constants (r=0.6196, n=28, p=0.0004, etc.) |
| `data_loader.py` | Python | Data loading utilities (loads from `output/`) |
| `correlation_engine.py` | Python | Correlation calculation engine |
| `perplexity_verify.py` | Python | Perplexity API verification utility |
| `requirements.txt` | Text | Dashboard Python dependencies |
| `CHANGELOG_20260221.md` | Markdown | v9.9 changelog (n corrected from 30 to 28, prediction tracker added) |

### `dashboard/.streamlit/`

| File | Type | Content |
|------|------|---------|
| `config.toml` | TOML | Streamlit theme/configuration |

**Dependencies**: `output/`, `intelligence_config.json`, `daily_perplexity_update.py`  
**Questions answered**: How are findings visualized? What does the live dashboard show?

---

## `docs/`

| File | Type | Content |
|------|------|---------|
| `index.html` | HTML | Static documentation landing page |
| `style.css` | CSS | Documentation styling |

### `docs/assets/`

| File | Type | Content |
|------|------|---------|
| `og-image.svg` | SVG | Open Graph social sharing image |

### `docs/validation/`

| File | Type | Content |
|------|------|---------|
| `VALIDATION_REPORT_2026-02-24.md` | Markdown | Validation report (Feb 24, 2026) |

**Dependencies**: Standalone  
**Questions answered**: What is the public-facing documentation?

---

## `federal_register/`

| File | Type | Content |
|------|------|---------|
| `__init__.py` | Python | Package init |
| `items.py` | Python | Scrapy item definitions |
| `middlewares.py` | Python | Scrapy middlewares |
| `pipelines.py` | Python | Scrapy data pipelines |
| `settings.py` | Python | Scrapy settings |

### `federal_register/spiders/`

| File | Type | Content |
|------|------|---------|
| `__init__.py` | Python | Spider package init |
| `federal_register_eo.py` | Python | Federal Register Executive Order spider |
| `doj_press_releases.py` | Python | DOJ press release spider |

### `federal_register/Spider Output Files/`

| File | Type | Content |
|------|------|---------|
| `README.md` | Markdown | Spider output directory overview |
| `items_federal_register_eo_1.json` | JSON | Scraped Federal Register EO data |

**Dependencies**: `scrapy.cfg`, `scrapinghub.yml`, `merge_spider_output.py`  
**Questions answered**: How is government data collected? What spiders exist?

---

## `output/`

| File | Type | Content |
|------|------|---------|
| `daily_intelligence.json` | JSON | Latest daily Perplexity intelligence output |
| `federal_register_data.json` | JSON | Aggregated Federal Register data |
| `latest_scrape.json` | JSON | Latest spider scrape output |
| `20260228_210448_extracted.json` | JSON | Latest LLM extraction (Feb 28) |
| `20260228_210448_raw.txt` | Text | Raw LLM output (Feb 28) |
| `20260228_210448_summary.txt` | Text | LLM summary (Feb 28) |

### `output/archive/`

Contains 13 sets of timestamped `_extracted.json`, `_raw.txt`, and `_summary.txt` files from Feb 21-28, 2026. These are historical LLM extraction outputs.

**Dependencies**: `daily_perplexity_update.py`, `test_api.py`, `dashboard/`  
**Questions answered**: What has the automated pipeline produced? What's the intelligence history?

---

## `_AI_CONTEXT_INDEX/`

| File | Type | Content |
|------|------|---------|
| `00_START_HERE.md` | Markdown | Navigation guide for AI models |
| `01_CORE_THEORY.md` | Markdown | Thermostat model, 7-day median lag, convergence pattern |
| `02_MEDIA_FIREWALL.md` | Markdown | 1789 Capital, TCN, narrative infrastructure |
| `03_BOARD_OF_PEACE.md` | Markdown | Private diplomacy, Kushner, Witkoff |
| `04_CAPITAL_ARCHITECTURE.md` | Markdown | Gulf SWF pipelines, Silicon Sovereignty |
| `05_CRINK_FRAMEWORK.md` | Markdown | China-Russia-Iran-NK coordination |
| `06_MAIN_CHARACTERS.md` | Markdown | Patel, Hegseth, Noem as noise generators |
| `07_METHODOLOGY.md` | Markdown | Correlation methodology, verification standards |
| `08_KEY_DATASETS.md` | Markdown | CSV schemas and data file reference |
| `09_CURRENT_THREADS.md` | Markdown | Active research questions (large file) |
| `10_FRAMEWORK_VALIDATION.md` | Markdown | High-profile statements validating framework |

### `_AI_CONTEXT_INDEX/Node_Dossiers/`

| File | Type | Content |
|------|------|---------|
| `NODE_INDEX.md` | Markdown | Modular entity loading index |
| `tier1_binsulayem_epstein.md` | Markdown | Bin Sulayem/DP World/Epstein connection |
| `tier1_kushner_historical.md` | Markdown | Kushner family business/political history |
| `tier1_zorro_ranch_epstein.md` | Markdown | Zorro Ranch / Epstein architecture |
| `tier2_affinity_qxo.md` | Markdown | Affinity Partners & QXO analysis |
| `tier2_egypt_gulf_integration.md` | Markdown | Egypt-Gulf financial integration |
| `tier2_sovereign_wealth_movers.md` | Markdown | PIF/Mubadala positioning |
| `tier2_uae_coordination_node.md` | Markdown | UAE multi-track coordination |
| `tier3_thermostat_ruleset.md` | Markdown | Master timing analysis ruleset |

### `_AI_CONTEXT_INDEX/sources/`

| File | Type | Content |
|------|------|---------|
| `2026-02-27_Carlson_Fitts_Control_Grid.md` | Markdown | Catherine Austin Fitts interview analysis |
| `2026-02-28_Arsenal_of_Freedom_Defense_Industrial_Convergence.md` | Markdown | Hegseth L3Harris visit / defense production |
| `2026-02-28_Cyber_Kinetic_Timeline_Analysis.md` | Markdown | Cyber-kinetic operation timeline |
| `2026-02-28_Iran_Strike_Target_Mapping.md` | Markdown | Iran strike target mapping against SWF infrastructure |

**Dependencies**: Self-referencing system; references all other directories  
**Questions answered**: How should an AI model understand this repository?

---

## File Count Summary

| Category | Count |
|----------|-------|
| Markdown files (.md) | ~120 |
| CSV data files (.csv) | ~50 |
| Python scripts (.py) | ~30 |
| PDF documents (.pdf) | 5 |
| JSON data files (.json) | ~20 |
| Configuration files | ~10 |
| Other (txt, sh, html, css, svg, jpg, cff, toml, yaml/yml) | ~15 |
| **Total files** | **~250** |

---

*Audit completed 2026-03-01. This document inventories every file and directory in the repository.*
