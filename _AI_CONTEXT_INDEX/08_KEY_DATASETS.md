# Key Datasets: CSV Reference Guide

**Purpose**: Quick reference to all major data files in this repository, including schemas, row counts, and what each dataset is used for.

---

## Data Pipeline Architecture

### Live Data Sources
The Streamlit dashboard loads data from the following locations:
- `Control_Proof/master_reflexive_correlation_data.csv` - Core 30-week friction/compliance index
- `Run_Correlations_Yourself/historical_backfill_2017_2024.csv` - 66 historical event pairs
- `Run_Correlations_Yourself/negative_windows.csv` - 5 non-response windows
- `federal_register/Spider Output Files/items_federal_register_eo_1.json` - Live EO data from spider
- `output/*_extracted.json` - Latest LLM intelligence extractions (older in `output/archive/`)

### Data Update Flow
1. **DigitalOcean Droplet** runs Scrapy spiders daily (cron scheduled)
2. Spider saves JSON output to `federal_register/Spider Output Files/`
3. Push script commits and pushes data to GitHub
4. **Streamlit Community Cloud** pulls from GitHub and caches data (1-hour TTL)

### Cache Configuration
All data loaders use `@st.cache_data(ttl=3600)` (1-hour cache) to balance performance and freshness.

---

## Primary Analysis Datasets

### Epstein Files Timeline
| Field | Value |
|-------|-------|
| **Path** | `01_Levers_and_Frictions/Epstein_Files_timeline_updated.csv` |
| **Rows** | ~583 |
| **Columns** | `file`, `raw_date`, `date`, `doc_type`, `context` |
| **Date Range** | 1953-2025 |
| **Purpose** | Tracks Epstein-related document releases and media events |

### Master Timeline
| Field | Value |
|-------|-------|
| **Path** | `03_Master_Framework/MASTER_timeline_2015-2025_UPDATED.csv` |
| **Rows** | ~388 |
| **Columns** | `date`, `country`, `event_type`, `primary_entity`, `related_entities`, `description`, `financial_value`, `source`, `verification_status` |
| **Date Range** | 2012-2025 |
| **Purpose** | Core timeline of geopolitical, financial, and policy events |

### Thermostat Control Data
| Field | Value |
|-------|-------|
| **Path** | `05_Geopolitical_Vectors/thermostat_control_data.csv` |
| **Rows** | ~150 |
| **Columns** | `Theory_Label`, `Search_Query`, `Title`, `Link`, `Snippet`, `Source`, `Date` |
| **Date Range** | 2012-2025 |
| **Purpose** | Nation-state linkage data (Russia, Saudi, Gulf, China) |

### Coalition Narrative Map
| Field | Value |
|-------|-------|
| **Path** | `09_Silicon_Sovereignty/Coalition_Narrative_Map_2015-2025.csv` |
| **Rows** | ~456 |
| **Columns** | `Hash_ID`, `Phase`, `Vector_Focus`, `Search_Keyword`, `Media_Tier`, `Source_Domain`, `Published_Date`, `Title`, `Snippet`, `URL`, `Query_Used` |
| **Date Range** | 2015-2025 |
| **Purpose** | Media coverage patterns across phases |

---

## 2026 Data

### CRINK Intelligence Dataset
| Field | Value |
|-------|-------|
| **Path** | `New_Data_2026/CRINK_Intelligence_Dataset_Final_Verified.csv` |
| **Rows** | 34 |
| **Columns** | `date`, `event`, `category`, `snippet`, `source`, `link` |
| **Date Range** | January 2025 - January 2026 |
| **Purpose** | CRINK axis discourse tracking |
| **Categories** | Analysis (24), Military_Security (8), Cyber_Security (2) |

---

## Project Trident Data

### Final Dossier
| Field | Value |
|-------|-------|
| **Path** | `Project_Trident/project_trident_final_dossier.csv` |
| **Rows** | ~118 |
| **Columns** | `Date`, `Vector`, `Title`, `Snippet`, `Link`, `Source` |
| **Date Range** | Recent |
| **Purpose** | Compiled intelligence dossier |

### Temporal Correlations
| Field | Value |
|-------|-------|
| **Path** | `Project_Trident/temporal_correlations_analyzed.csv` |
| **Rows** | ~338 |
| **Columns** | `ritual_type`, `ritual_date`, `ritual_title`, `anchor_category`, `anchor_date`, `anchor_title`, `lag_days`, `correlation_strength` |
| **Date Range** | 2024-2025 |
| **Purpose** | Ritual-to-policy lag analysis (Project Trident) |

---

## Historical Backfill

### Historical Backfill (2017-2024)
| Field | Value |
|-------|-------|
| **Path** | `Run_Correlations_Yourself/historical_backfill_2017_2024.csv` |
| **Rows** | 66 |
| **Columns** | `Year`, `Friction_Event`, `Friction_Date`, `Compliance_Event`, `Compliance_Date`, `Lag_Days`, `Source_URL` |
| **Date Range** | 2017-2024 |
| **Purpose** | Historical friction→compliance pairs for extended analysis |

### Negative Windows
| Field | Value |
|-------|-------|
| **Path** | `Run_Correlations_Yourself/negative_windows.csv` |
| **Rows** | 5 |
| **Purpose** | Documented windows where pattern did NOT occur (falsification evidence) |

---

## Control Proof Data

### Correlation Results
| Field | Value |
|-------|-------|
| **Path** | `Control_Proof/correlation_results.txt` |
| **Type** | Text output |
| **Purpose** | Raw output from correlation analysis (r = 0.6196) |

### Master Reflexive Control
| Field | Value |
|-------|-------|
| **Path** | `Control_Proof/master_reflexive_correlation_data.csv` |
| **Rows** | 30 |
| **Purpose** | The 30-week hand-scored dataset producing r = 0.6196 |
| **Columns** | Weekly friction/compliance intensity indices (1-10 scale) |

---

## Additional 2026 Data Files

| File | Path | Rows | Purpose |
|------|------|------|---------|
| Additional Anchors | `New_Data_2026/Additional_Anchors_Jan2026_Final.csv` | ~50 | Policy, geopolitics, ritual events |
| Biopharma | `New_Data_2026/Biopharma.csv` | ~108 | FDA/DOGE conflict events |
| BlackRock Timeline | `New_Data_2026/BlackRock_Timeline_Full_Decade.csv` | ~674 | Crypto pivot, government ties |
| High Growth Companies | `New_Data_2026/High_Growth_Companies_2015_2026.csv` | ~1,049 | Biotech tracking (excluded from primary correlation) |
| Infrastructure Forensics | `New_Data_2026/Infrastructure_Forensics.csv` | ~107 | DOGE cuts, legislation |
| Timeline Update | `New_Data_2026/Timeline_Update_Jan2026_Corrected.csv` | ~99 | Dec 2025-Jan 2026 events |

---

## Data File Usage Guide

### For Reproducing r = 0.6196
```
Primary: Control_Proof/master_reflexive_correlation_data.csv
Script: Run_Correlations_Yourself/run_original_analysis.py
```

### For Project Trident Analysis
```
Primary: Project_Trident/temporal_correlations_analyzed.csv
Secondary: Project_Trident/project_trident_final_dossier.csv
```

### For 14-Day Periodicity Test
```
Files: 09_Silicon_Sovereignty/Coalition_Narrative_Map_2015-2025.csv
       + other Silicon Sovereignty CSVs
Result: χ² = 330.62
```

### For CRINK Analysis
```
Primary: New_Data_2026/CRINK_Intelligence_Dataset_Final_Verified.csv
Analysis: 05_Geopolitical_Vectors/CRINK_Analysis.md
```

### For Historical Backfill
```
Primary: Run_Correlations_Yourself/historical_backfill_2017_2024.csv
Finding: 66 pairs, median lag +7 days
```

---

## Dataset Summary Statistics

| Dataset | Records | Primary Use |
|---------|---------|-------------|
| MASTER_timeline | 388 | Core event timeline |
| Epstein_Files_timeline | 583 | Friction events |
| Coalition_Narrative_Map | 456 | Media patterns |
| temporal_correlations | 338 | Ritual-policy lags |
| CRINK_Intelligence | 34 | Adversary coordination |
| historical_backfill | 66 | Extended historical |
| **Total documented events** | **2,000+** | — |

---

## Data Quality Notes

### Verification Status
Most datasets include a `verification_status` field:
- `Verified` - Confirmed through multiple sources
- `Partial` - Some evidence, needs more
- `Unverified` - Single source only

### Known Issues
1. **Wrong_Correlations/**: Contains deprecated scripts that mixed datasets
2. **High_Growth_Companies**: Excluded from primary correlation (operational events)
3. **Date formats**: Some files use different date formats (YYYY-MM-DD vs MM-DD-YYYY)

---

## Key Sources

| Document | Location |
|----------|----------|
| Dataset Reference | `Project_Trident/DATASET_REFERENCE.md` |
| Transparency Note | `14_Files/TRANSPARENCY_NOTE_FOR_2026_ANALYSIS.md` |
| Glossary | `14_Files/Glossary.md` |

---

## Cross-References

- **For methodology**: `07_METHODOLOGY.md`
- **For core theory**: `01_CORE_THEORY.md`
- **For current analysis**: `09_CURRENT_THREADS.md`

---

## Pipeline Output Data

### Daily Intelligence
| Field | Value |
|-------|-------|
| **Path** | `output/daily_intelligence.json` |
| **Type** | JSON |
| **Source** | `daily_perplexity_update.py` (Perplexity sonar-pro) |
| **Purpose** | Daily intelligence summaries for tracked entities/signals |
| **Schema** | `signal_status`, `top_3_developments`, `new_alerts`, `summary` |

### LLM Extraction Outputs
| Field | Value |
|-------|-------|
| **Path** | `output/*_extracted.json` (latest), `output/archive/` (historical) |
| **Type** | JSON |
| **Source** | `test_api.py` (Llama-4-Scout) |
| **Purpose** | Clinical entity extraction from intelligence briefs |
| **Archives** | 13 historical runs (Feb 21-28, 2026) in `output/archive/` |

### Federal Register Data
| Field | Value |
|-------|-------|
| **Path** | `output/federal_register_data.json`, `output/latest_scrape.json` |
| **Type** | JSON |
| **Source** | `federal_register/spiders/` (Scrapy) |
| **Purpose** | Executive Order and DOJ press release tracking |

### Entity/Signal Configuration
| Field | Value |
|-------|-------|
| **Path** | `intelligence_config.json` |
| **Type** | JSON |
| **Categories** | sovereign_wealth, private_equity, government, geopolitical, tech_infrastructure, legal_regulatory |
| **Active Signals** | 5 (Iran-US military, Board of Peace, Epstein files, Russia-Ukraine, Gulf SWF capital) |

---

## Project Trident Aggregated Datasets

The `Project_Trident/Copilot_Opus_4.6_Analysis/Datasets/` directory contains 22 CSV files aggregated from across the repository for statistical testing. These are copies of primary datasets located in other directories. See `REPO_AUDIT_2026-03-01.md` for the full listing.

---

*This reference guide documents CSVs as of March 1, 2026.*
