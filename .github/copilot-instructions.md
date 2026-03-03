# Copilot Instructions — The Regulated Friction Project

## What This Repository Is

An OSINT research repository documenting statistically significant temporal correlations between "friction" events (scandals, document releases, media crises) and "compliance" events (policy shifts, financial moves, regulatory changes) from 2015–2026. The core finding is r = +0.6196 at a 7-day median lag (p = 0.0004). The project explicitly claims correlation, not causation.

## AI Context System

Before working on any research content, read `_AI_CONTEXT_INDEX/00_START_HERE.md` first, then use `_AI_CONTEXT_INDEX/CONTEXT_ROUTER.md` to find the right files for a given topic. The context index has 16 files covering theory, methodology, datasets, current threads, and a full repo audit.

## Architecture

### Dashboard (Streamlit)

The live dashboard at `regulatedfriction.streamlit.app` is a multi-tab Streamlit app:

- **`dashboard/app.py`** — Main entry point. Imports from the three modules below.
- **`dashboard/correlation_engine.py`** — Pure statistical computation (Pearson, Spearman, lag sweep, Fisher z, OLS regression). Zero Streamlit imports; testable independently.
- **`dashboard/data_loader.py`** — Data ingestion layer. Loads 4 sources with `@st.cache_data(ttl=3600)`. Paths auto-resolve relative to repo root.
- **`dashboard/constants.py`** — Colors, disclaimers, and framing text.
- **`dashboard/perplexity_verify.py`** — Signal verification via Perplexity API.

### Data Pipeline

1. **Scrapy spider** (`federal_register/`) runs daily on a DigitalOcean Droplet, scraping Federal Register EOs.
2. **GitHub Actions** (`daily_pipeline.yaml`) runs at 8:00 AM UTC: scrapes EOs, runs `daily_perplexity_update.py` (Perplexity sonar-pro), commits to `output/`.
3. **Sync workflow** (`sync_to_do_space.yml`) mirrors data to DigitalOcean Spaces after the daily pipeline succeeds.
4. **Dashboard** pulls from GitHub with 1-hour cache TTL.

### Intelligence Pipeline

`daily_perplexity_update.py` reads `intelligence_config.json` (tracked entities + active signals) and writes `output/daily_intelligence.json`. Requires `PERPLEXITY_API_KEY` env var.

### Correlation Reproduction

`Run_Correlations_Yourself/run_original_analysis.py` independently reproduces the core finding using only original datasets from `Control_Proof/` and `Project_Trident/`. It explicitly excludes `New_Data_2026/`.

## Build, Lint, and Test

### Validation (CI)

```bash
# Full validation (what CI runs on push to main):
python -m py_compile dashboard/app.py
python -m py_compile dashboard/data_loader.py
python -m py_compile dashboard/constants.py
python -m py_compile daily_perplexity_update.py
python dashboard/correlation_engine.py  # self-test when run directly
```

### Reproduce the core correlation

```bash
cd Run_Correlations_Yourself/
pip install -r requirements.txt  # pandas, numpy, scipy, statsmodels
python run_original_analysis.py
```

### Dashboard dependencies

```bash
pip install -r dashboard/requirements.txt  # streamlit, pandas, numpy, scipy, plotly, openai, requests
```

### Scrapy spider

```bash
pip install -r requirements.txt  # scrapy, shub, google-genai
scrapy crawl federal_register_eo -o output/latest_scrape.json
```

## Key Conventions

### Verification Levels

All claims use a three-tier system — respect these levels when adding or modifying content:

- ✅ **VERIFIED** — Multiple independent sources; reproducible
- ⚠️ **PARTIALLY VERIFIED** — Some evidence, gaps remain
- 🔍 **HYPOTHESIS** — Analytical interpretation from pattern observation

Sections marked `[Inference]` go beyond the data and must not be presented as established fact.

### Data Provenance

- `New_Data_2026/` CSVs are hand-scraped, not AI-generated (one exception: `oreateai.com` row was quarantined to `DATA_QUARANTINE.csv`).
- Any AI content mill sources must be moved to `DATA_QUARANTINE.csv`, never left in production CSVs.
- Retracted claims (Layers 2-3 from Grok-fabricated statistics) are in `Archive/Retracted_Three_Layer_References.md`. Do not re-introduce them.

### Node Dossiers

`_AI_CONTEXT_INDEX/Node_Dossiers/` contains entity profiles organized by tier (tier1 = primary nodes, tier2 = supporting entities, tier3 = system rules). See `NODE_INDEX.md` for the full roster.

### What NOT to Claim

- Do not assume central coordination — the pattern is described as emergent.
- Do not conflate correlation with causation.
- Do not assume failed predictions (Q4 2025 13F) succeeded — negative results are documented transparently.
- The "14-day lag" terminology is legacy (v10.2). The corrected measurement is 7-day median lag (v10.3). Use the latter.
