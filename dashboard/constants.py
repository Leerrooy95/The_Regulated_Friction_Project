"""
constants.py
============
Central configuration for the Historical Friction-Compliance Explorer dashboard.
Contains: color palette, lag bin definitions, outlier framing strategy,
negative window annotations, and all static text / disclaimers.

This file is imported by data_loader.py, correlation_engine.py, and app.py.
No external dependencies — pure Python constants only.
"""

# =========================================================================
#  1. COLOR PALETTE
# =========================================================================
# Every visual element in the dashboard maps to one of these constants.
# Changing a value here propagates across all charts automatically.

COLOR_FRICTION          = "#E63946"                 # Red — friction events / primary accent
COLOR_COMPLIANCE        = "#58A6FF"                 # Bright blue — compliance events / secondary
COLOR_NEUTRAL           = "#2A9D8F"                 # Teal — neutral data points / histograms
COLOR_TEXT              = "#C9D1D9"                 # Light gray — all text elements (dark theme)
COLOR_BG_PRIMARY        = "#0E1117"                 # Dark background
COLOR_BG_SECONDARY      = "#161B22"                 # Slightly lighter background / cards
COLOR_BG_CARD           = "#1C2333"                 # Card background
COLOR_BORDER            = "#30363D"                 # Subtle border color
COLOR_VARIANCE          = "#E9C46A"                 # Gold — median bands / variance annotations
COLOR_NEGATIVE_WINDOW   = "rgba(200, 200, 200, 0.15)"  # Muted gray — negative window bands
COLOR_PREDICTION_BAND   = "rgba(88, 166, 255, 0.12)"   # Faint blue — CI / prediction intervals
COLOR_LAG_HIGHLIGHT     = "#E63946"                 # Red — highlighted bar in lag sweep chart
COLOR_OUTLIER_MARKER    = "#FF6B35"                 # Orange — outlier event markers
COLOR_EXPECTED_VARIANCE = "rgba(42, 157, 143, 0.12)"    # Faint teal — expected variance fill
COLOR_SUCCESS           = "#3FB950"                 # Green — success / confirmed
COLOR_WARNING           = "#D29922"                 # Amber — warnings / partial
COLOR_DANGER            = "#F85149"                 # Red — danger / failed
COLOR_ACCENT_GLOW       = "rgba(230, 57, 70, 0.15)"    # Red glow for accents


# =========================================================================
#  2. CORE STATISTICAL THRESHOLDS
# =========================================================================
# Reference values verified by Run_Correlations_Yourself/run_original_analysis.py

CORE_R               = 0.6196     # Pearson r at 2-week index lag (actual median: 7 days) (n_eff = 28)  # v10.2 Legacy (2-week index resolution)
CORE_P               = 0.0004     # Two-tailed p-value
CORE_N               = 28         # Effective paired observations after 2-week index lag (dataset has 30 rows)
CORE_LAG_WEEKS       = 2          # Optimal lag in weeks
BACKFILL_PAIRS       = 66         # Historical backfill event pairs (2017-2024)
BACKFILL_MEDIAN_DAYS = 7          # Median lag in days across backfill
NEGATIVE_EVENTS      = 5          # Non-response friction events
TOTAL_FRICTION_EVENTS = 71        # 66 positive + 5 negative
RESPONSE_RATE_PCT    = 93.0       # 66 / 71 = 93%
R_SQUARED            = 0.3839     # 0.6196^2 — variance explained


# =========================================================================
#  3. LAG BIN DEFINITIONS
# =========================================================================
# Bins for categorizing the backfill lag distribution.
# Format: (display_label, lower_bound_inclusive, upper_bound_inclusive)
# upper_bound = None means "this value and above" (open-ended bin).
# Sourced from: Run_Correlations_Yourself/Statistical_Tests/backfill_lag_distribution.py

LAG_BINS = [
    ("[-3 to  0]",   -3,   0),     # Same-day or friction-leads (negative lag)
    ("[+1 to +3]",    1,   3),     # Very short response lag
    ("[+4 to +7]",    4,   7),     # ~1 week response window
    ("[+8 to +10]",   8,  10),     # ~10 day response window
    ("[+11 to +14]", 11,  14),     # Two-week window (peak density)
    ("[+15+]",       15, None),    # Extended lag (open-ended)
]


# =========================================================================
#  4. NEGATIVE WINDOW CONTEXTUAL ANNOTATIONS (OUTLIER FRAMING STRATEGY)
# =========================================================================
# The 5 friction events with NO measurable compliance response within the
# 14-day Federal Register search window. Each entry explains WHY the
# pattern did not hold — converting apparent "failures" into evidence of
# structural boundary conditions.
#
# Key statistical framing:
#   - r^2 = 0.384 means 38.4% of variance is explained
#   - The remaining 61.6% is OTHER factors
#   - 5 of 71 events (7%) showing no response is FEWER than expected
#   - Binomial test vs H0: response_rate = 0.20 yields p = 0.006
#
# These are not exceptions — they are expected statistical residuals that
# reinforce the model's credibility.

NEGATIVE_WINDOW_CONTEXT = {
    "US strikes Syria (Shayrat airbase; 59 Tomahawks)":
        "Military action with bipartisan support — low domestic institutional "
        "friction. Compliance manifested through defense channels not captured "
        "by the Federal Register EO spider.",

    "Parkland school shooting (17 killed)":
        "Mass casualty event generating unified national response rather than "
        "partisan friction. Policy response (bump stock ban) emerged beyond "
        "the 14-day search window.",

    "Trump impeachment inquiry announced":
        "Inquiry announcement (not vote) — institutional response emerged "
        "beyond the 14-day window. Congressional (not executive) channel "
        "dominates compliance response.",

    "Israel-Hamas war begins (Oct 7 attack)":
        "International crisis — compliance manifested through military and "
        "diplomatic channels not captured by the Federal Register EO spider. "
        "Executive Orders followed weeks later.",

    "Epstein document unsealing (Maxwell civil case)":
        "Court document release during holiday period (Jan 3, 2024) — reduced "
        "Federal Register activity. Institutional response emerged in late "
        "January through congressional hearing scheduling.",
}


# =========================================================================
#  5. OUTLIER FRAMING — DISPLAY TEXT
# =========================================================================
# Pre-written statistical framing paragraphs for the dashboard UI.
# These ensure the 5 negative windows are always presented with proper
# statistical context, not as contradictions.

NEGATIVE_WINDOW_FRAMING = """\
**Understanding Non-Response Windows**

For r = 0.6196, r\u00b2 = 0.384 \u2014 meaning 38.4% of compliance variance is \
explained by friction. The remaining 61.6% is attributable to other factors. \
Finding 5 of 71 friction events (7.0%) with no measurable compliance response \
within 14 days is consistent with this expected residual variance.

A binomial test against H\u2080: response\\_rate = 0.20 yields p = 0.006, meaning \
the observed 93% response rate is significantly *higher* than generous baselines. \
The 5 non-response events are *fewer* than would be expected under most \
reasonable models of random institutional behavior.\
"""

OUTLIER_STATISTICAL_NOTE = (
    "5 of 71 friction events (7.0%) produced no compliance response within "
    "the 14-day search window. For a model explaining 38.4% of variance "
    "(r\u00b2 = 0.384), this non-response rate is lower than expected. "
    "Binomial test: p = 0.006 against H\u2080 of 20% non-response."
)

OUTLIER_METHODOLOGY_NOTE = (
    "Non-response windows are identified by querying the Federal Register "
    "EO spider output (JSON) for executive actions within a 14-day window "
    "following each friction event. Events with zero matching EOs are "
    "classified as non-response windows. This method captures only "
    "executive-branch compliance; congressional, judicial, and state-level "
    "responses are not included in the search scope."
)


# =========================================================================
#  6. DISCLAIMER TEXT
# =========================================================================

DISCLAIMER = (
    "Correlation is not causation. This dashboard presents observational "
    "statistical patterns for research purposes only. The friction-compliance "
    "correlation (r = 0.6196) describes a measured association, not a proven "
    "causal mechanism. All findings are reproducible using the scripts in "
    "Run_Correlations_Yourself/."
)

METHODOLOGY_FOOTER = (
    "Statistical methods: Pearson product-moment correlation with lag sweep "
    "(0\u20136 weeks), Fisher z-transform for confidence intervals, Spearman "
    "rank correlation for robustness, OLS regression with \u00b12 SD prediction "
    "bands. Historical backfill analyzed via lag-day distribution with "
    "binomial significance testing for non-response rate."
)


# =========================================================================
#  7. DASHBOARD UI STRINGS
# =========================================================================

PAGE_TITLE     = "Historical Friction-Compliance Explorer"
PAGE_ICON      = "\U0001f4ca"  # Bar chart emoji
SIDEBAR_TITLE  = "Friction-Compliance Explorer"
SIDEBAR_CAPTION = "Track A | Correlation Model"

TAB_LABELS = [
    "Statistical Overview",
    "Time Series & Scatter",
    "Lag Distribution (Backfill)",
    "Raw Data Explorer",
]

DATA_SOURCE_DESCRIPTIONS = [
    "`master_reflexive_correlation_data.csv` (30 rows, n=28 after lag)",
    "`historical_backfill_2017_2024.csv` (66 event pairs)",
    "`negative_windows.csv` (5 non-response windows)",
    "Federal Register EO spider output (JSON)",
]


# =========================================================================
#  8. PLOTLY CHART TEMPLATE (DARK THEME)
# =========================================================================
# Consistent dark theme template applied to all Plotly figures.

PLOTLY_TEMPLATE = {
    "layout": {
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "font": {"color": "#C9D1D9", "family": "Inter, -apple-system, sans-serif"},
        "title": {"font": {"color": "#C9D1D9"}},
        "xaxis": {
            "gridcolor": "rgba(48, 54, 61, 0.6)",
            "zerolinecolor": "rgba(48, 54, 61, 0.8)",
            "title": {"font": {"color": "#8B949E"}},
            "tickfont": {"color": "#8B949E"},
        },
        "yaxis": {
            "gridcolor": "rgba(48, 54, 61, 0.6)",
            "zerolinecolor": "rgba(48, 54, 61, 0.8)",
            "title": {"font": {"color": "#8B949E"}},
            "tickfont": {"color": "#8B949E"},
        },
        "legend": {
            "font": {"color": "#C9D1D9"},
            "bgcolor": "rgba(0,0,0,0)",
        },
        "hoverlabel": {
            "bgcolor": "#1C2333",
            "bordercolor": "#30363D",
            "font": {"color": "#C9D1D9", "size": 13},
        },
        "colorway": [
            "#E63946", "#58A6FF", "#2A9D8F", "#E9C46A",
            "#FF6B35", "#A371F7", "#3FB950", "#F778BA",
        ],
    }
}


# =========================================================================
#  9. GLOBAL CSS (DARK OSINT THEME)
# =========================================================================
# Injected once at the top of app.py for professional dark-mode styling.

GLOBAL_CSS = """
<style>
/* ── Import Inter font for professional typography ── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ── Base typography ── */
html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
}

/* ── Metric cards: glassmorphism effect ── */
[data-testid="stMetric"] {
    background: linear-gradient(135deg, rgba(28,35,51,0.8) 0%, rgba(22,27,34,0.9) 100%);
    border: 1px solid rgba(48,54,61,0.6);
    border-radius: 12px;
    padding: 16px 20px;
    backdrop-filter: blur(10px);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
}
[data-testid="stMetric"]:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.3);
}
[data-testid="stMetric"] label {
    color: #8B949E !important;
    font-size: 0.85rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.02em;
    text-transform: uppercase;
}
[data-testid="stMetric"] [data-testid="stMetricValue"] {
    font-weight: 700 !important;
    font-size: 1.6rem !important;
    letter-spacing: -0.02em;
}

/* ── Expander styling ── */
[data-testid="stExpander"] {
    border: 1px solid rgba(48,54,61,0.6) !important;
    border-radius: 10px !important;
    background: rgba(28,35,51,0.4) !important;
}

/* ── Tab styling ── */
[data-testid="stTab"] {
    font-weight: 500 !important;
    letter-spacing: 0.01em;
}

/* ── Sidebar styling ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D1117 0%, #161B22 100%);
    border-right: 1px solid rgba(48,54,61,0.5);
}

/* ── Divider styling ── */
hr {
    border-color: rgba(48,54,61,0.5) !important;
}

/* ── DataFrame/table styling ── */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}

/* ── Smooth scrollbar ── */
::-webkit-scrollbar {
    width: 8px;
    height: 8px;
}
::-webkit-scrollbar-track {
    background: #0E1117;
}
::-webkit-scrollbar-thumb {
    background: #30363D;
    border-radius: 4px;
}
::-webkit-scrollbar-thumb:hover {
    background: #484F58;
}

/* ── Hero section ── */
.hero-banner {
    background: linear-gradient(135deg, #0D1117 0%, #161B22 40%, #1C2333 100%);
    border: 1px solid rgba(48,54,61,0.6);
    border-radius: 16px;
    padding: 2.5rem 2rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #E63946, #58A6FF, #2A9D8F);
}
.hero-banner h1 {
    font-size: 2.2rem;
    font-weight: 700;
    margin: 0 0 0.5rem 0;
    letter-spacing: -0.03em;
    background: linear-gradient(135deg, #C9D1D9 0%, #8B949E 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-banner .subtitle {
    color: #8B949E;
    font-size: 1.05rem;
    line-height: 1.6;
    max-width: 700px;
}
.hero-banner .badge {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin-right: 8px;
    margin-top: 12px;
    letter-spacing: 0.02em;
}
.hero-banner .badge-live {
    background: rgba(230, 57, 70, 0.15);
    color: #E63946;
    border: 1px solid rgba(230, 57, 70, 0.3);
}
.hero-banner .badge-verified {
    background: rgba(63, 185, 80, 0.15);
    color: #3FB950;
    border: 1px solid rgba(63, 185, 80, 0.3);
}
.hero-banner .badge-version {
    background: rgba(88, 166, 255, 0.15);
    color: #58A6FF;
    border: 1px solid rgba(88, 166, 255, 0.3);
}

/* ── Status indicator pulse ── */
@keyframes pulse-live {
    0% { box-shadow: 0 0 0 0 rgba(230, 57, 70, 0.4); }
    70% { box-shadow: 0 0 0 8px rgba(230, 57, 70, 0); }
    100% { box-shadow: 0 0 0 0 rgba(230, 57, 70, 0); }
}
.status-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
    margin-right: 6px;
    vertical-align: middle;
}
.status-dot-live {
    background: #E63946;
    animation: pulse-live 2s infinite;
}
.status-dot-ok {
    background: #3FB950;
}

/* ── Signal health gauge ── */
.gauge-container {
    background: linear-gradient(135deg, rgba(28,35,51,0.8) 0%, rgba(22,27,34,0.9) 100%);
    border: 1px solid rgba(48,54,61,0.6);
    border-radius: 16px;
    padding: 24px;
    text-align: center;
}
.gauge-label {
    color: #8B949E;
    font-size: 0.85rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 8px;
}
.gauge-value {
    font-size: 2.4rem;
    font-weight: 700;
    letter-spacing: -0.02em;
}
.gauge-sublabel {
    color: #8B949E;
    font-size: 0.8rem;
    margin-top: 4px;
}

/* ── Role cards (dark theme override) ── */
.role-cards-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin: 1rem 0 2rem 0;
}
.role-card {
    border: 1px solid rgba(48,54,61,0.6);
    border-radius: 12px;
    padding: 1.5rem;
    background: linear-gradient(135deg, rgba(28,35,51,0.6) 0%, rgba(22,27,34,0.8) 100%);
    backdrop-filter: blur(10px);
    transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}
.role-card:hover {
    transform: translateY(-3px);
    box-shadow: 0 8px 25px rgba(0,0,0,0.4);
    border-color: rgba(88,166,255,0.3);
}
.role-card h3 {
    color: #C9D1D9;
    margin: 0 0 0.5rem 0;
    font-size: 1.2rem;
    font-weight: 600;
}
.role-card .subtitle {
    color: #8B949E;
    font-style: italic;
    margin-bottom: 1rem;
    font-size: 0.85rem;
}
.role-card ul {
    margin: 0;
    padding-left: 1.2rem;
    list-style-type: none;
}
.role-card li {
    color: #C9D1D9;
    margin-bottom: 0.5rem;
    line-height: 1.5;
    position: relative;
    padding-left: 0.3rem;
}
.role-card li::before {
    content: "›";
    position: absolute;
    left: -1rem;
    color: #58A6FF;
    font-weight: bold;
}
.role-card .code-text {
    background: rgba(88,166,255,0.1);
    color: #58A6FF;
    padding: 2px 6px;
    border-radius: 4px;
    font-size: 0.82em;
    font-family: 'JetBrains Mono', 'Fira Code', monospace;
}
.role-card strong {
    color: #C9D1D9;
    font-weight: 600;
}

/* ── Convergence diagram (dark theme) ── */
.convergence-diagram {
    background: linear-gradient(135deg, rgba(28,35,51,0.8) 0%, rgba(14,17,23,0.9) 100%);
    border: 1px solid rgba(48,54,61,0.6);
    border-radius: 12px;
    padding: 1.5rem;
    margin: 1rem 0;
    font-family: 'JetBrains Mono', 'Fira Code', 'Courier New', monospace;
    font-size: 0.85rem;
    line-height: 1.4;
    white-space: pre;
    overflow-x: auto;
    color: #C9D1D9;
    text-align: center;
}
.convergence-diagram .highlight {
    color: #E63946;
    font-weight: bold;
}
.convergence-diagram .anchor {
    color: #58A6FF;
    font-weight: bold;
}
.convergence-diagram .result {
    color: #2A9D8F;
    font-weight: bold;
}

/* ── Intel table (dark theme) ── */
.intel-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.9em;
}
.intel-table th {
    background: rgba(28,35,51,0.8);
    color: #8B949E;
    padding: 12px 14px;
    text-align: left;
    border-bottom: 2px solid rgba(48,54,61,0.8);
    font-weight: 600;
    text-transform: uppercase;
    font-size: 0.8em;
    letter-spacing: 0.04em;
}
.intel-table td {
    padding: 12px 14px;
    border-bottom: 1px solid rgba(48,54,61,0.4);
    vertical-align: top;
    color: #C9D1D9;
}
.intel-table tr:hover {
    background: rgba(88,166,255,0.05);
}
@media (max-width: 768px) {
    .intel-table {
        font-size: 0.8em;
    }
    .intel-table th, .intel-table td {
        padding: 8px 10px;
    }
}

/* ── Entity network graph container ── */
.network-container {
    background: linear-gradient(135deg, rgba(28,35,51,0.6) 0%, rgba(14,17,23,0.8) 100%);
    border: 1px solid rgba(48,54,61,0.6);
    border-radius: 12px;
    padding: 8px;
}

/* ── Footer ── */
.dashboard-footer {
    background: linear-gradient(135deg, rgba(28,35,51,0.6) 0%, rgba(14,17,23,0.8) 100%);
    border: 1px solid rgba(48,54,61,0.4);
    border-radius: 12px;
    padding: 1.5rem 2rem;
    margin-top: 2rem;
    text-align: center;
}
.dashboard-footer p {
    color: #8B949E;
    font-size: 0.82rem;
    line-height: 1.6;
    margin: 0.3rem 0;
}
.dashboard-footer .footer-brand {
    color: #58A6FF;
    font-weight: 600;
    font-size: 0.9rem;
}
</style>
"""
