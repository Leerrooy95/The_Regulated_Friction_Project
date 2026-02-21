"""
Historical Friction-Compliance Explorer — Track A MVP Dashboard
Main Streamlit entry point.
"""

import numpy as np
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
from plotly.subplots import make_subplots

from constants import (
    COLOR_COMPLIANCE,
    COLOR_FRICTION,
    COLOR_LAG_HIGHLIGHT,
    COLOR_NEGATIVE_WINDOW,
    COLOR_NEUTRAL,
    COLOR_PREDICTION_BAND,
    COLOR_VARIANCE,
    DISCLAIMER,
    NEGATIVE_WINDOW_CONTEXT,
    NEGATIVE_WINDOW_FRAMING,
)
from correlation_engine import (
    compute_lag_bins,
    compute_lag_stats,
    compute_lag_sweep,
    compute_lagged_correlation,
    compute_regression,
    compute_spearman,
    compute_year_breakdown,
    fisher_ci,
)
from data_loader import load_backfill, load_core_dataset, load_eo_spider, load_negative_windows

# ── Page config ──────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Historical Friction-Compliance Explorer",
    page_icon="\U0001f4ca",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Load data ────────────────────────────────────────────────────────────
core_df = load_core_dataset()
backfill_df = load_backfill()
negative_df = load_negative_windows()
eo_df = load_eo_spider()

if core_df is None:
    st.stop()

# ── Sidebar ──────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("Friction-Compliance Explorer")
    st.caption("Track A | Correlation Model")
    st.divider()

    selected_lag = st.slider("Lag (weeks)", min_value=0, max_value=6, value=2)
    show_negatives = st.checkbox("Show negative windows", value=True)
    show_ci = st.checkbox("Show 95% confidence interval", value=True)

    st.divider()
    st.markdown("**Data Sources**")
    st.markdown("- `master_reflexive_correlation_data.csv` (30 obs)")
    st.markdown("- `historical_backfill_2017_2024.csv` (66 pairs)")
    st.markdown("- `negative_windows.csv` (5 windows)")
    st.markdown("- Federal Register EO spider (JSON)")
    st.divider()
    st.caption(DISCLAIMER)

# ── Compute statistics ───────────────────────────────────────────────────
friction = core_df["Epstein_Friction_Index"]
compliance = core_df["Institutional_Compliance_Index"]

r, p, n_eff = compute_lagged_correlation(friction, compliance, lag=selected_lag)
rho, p_spearman = compute_spearman(friction, compliance, lag=selected_lag)
r0, p0, _ = compute_lagged_correlation(friction, compliance, lag=0)
ci_low, ci_high = fisher_ci(r, n_eff)
lag_sweep = compute_lag_sweep(friction, compliance)
reg = compute_regression(friction, compliance, lag=selected_lag)

backfill_stats = None
if backfill_df is not None:
    backfill_stats = compute_lag_stats(backfill_df["lag_parsed"])

# ── Tabs ─────────────────────────────────────────────────────────────────
tab_home, tab_overview, tab_timeseries, tab_backfill, tab_data, tab_predictions = st.tabs([
    "Home",
    "Statistical Overview",
    "Time Series & Scatter",
    "Lag Distribution (Backfill)",
    "Raw Data Explorer",
    "Prediction Tracker",
])

# =====================================================================
# TAB 0: HOME
# =====================================================================
with tab_home:
    st.header("The Regulated Friction Project")
    st.markdown(
        "A data-driven analysis of temporal correlations between friction events, "
        "policy shifts, and capital flows (2015\u20132026)."
    )

    st.divider()

    # Metric cards
    h1, h2, h3, h4 = st.columns(4, gap="small")
    h1.metric("Pearson r", "0.6196", help="2-week lag, core 30-week dataset")
    h2.metric("p-value", "0.0004", help="Two-tailed significance")
    h3.metric("Response rate", "93%",
              help="% of friction events with compliance response within lag window")
    h4.metric("Backfill pairs", "66", help="2017\u20132024")

    st.caption(
        "When high-visibility friction events spike, institutional compliance events "
        "follow ~14 days later. This relationship has less than 0.05% probability of "
        "occurring by chance."
    )

    st.divider()

    # Key Statistics table (sourced from README.md Key Statistics)
    with st.expander("**Key Findings (21 Verified)**", expanded=False):
        key_stats_data = [
            {"Finding": "Friction \u2192 Compliance correlation", "Value": "r = +0.6196 (2-week lag)", "Status": "\u2705 Verified"},
            {"Finding": "Statistical significance", "Value": "p = 0.0004, n = 30 weeks", "Status": "\u2705 Verified"},
            {"Finding": "Ritual \u2192 Policy proximity", "Value": "50.7% vs. 19.9% baseline (2.5x)", "Status": "\u2705 Verified"},
            {"Finding": "Project Trident significance", "Value": "p = 0.002 (Mann-Whitney U)", "Status": "\u2705 Verified"},
            {"Finding": "Cross-validation (14-day periodicity)", "Value": "\u03c7\u00b2 = 330.62 (p < 0.0001, 2,102 events)", "Status": "\u2705 Verified"},
            {"Finding": "December 2025 cluster", "Value": "108 events in 12-day window", "Status": "\u2705 Verified"},
            {"Finding": "Dec 22 signal types", "Value": "5 (Friction, Geopolitics, Financial, Policy, Cyber)", "Status": "\u2705 Verified"},
            {"Finding": "Event colocation", "Value": "Friction dates attract 20\u201342x more compliance than random", "Status": "\u2705 Verified"},
            {"Finding": "January 2026 signal peaks", "Value": "3 peaks (Jan 3\u20139, Jan 20\u201322, Jan 27\u201331), 1 trough", "Status": "\u2705 Verified"},
            {"Finding": "January 2026 event density", "Value": "34 events: 12 friction, 19 compliance, 3 anchors", "Status": "\u2705 Verified"},
            {"Finding": "Feb 1\u201319 compliance window", "Value": "9 compliance events to 6 friction events in 19 days", "Status": "\u2705 Verified"},
            {"Finding": "13F visibility gap", "Value": "Architecture below 13F threshold \u2014 private deals, non-US, LP interests", "Status": "\u2705 Verified"},
            {"Finding": "Apollo credit pipeline", "Value": "$938B AUM, $305B originated 2025; $3B QXO + $3.5B xAI + $29B Meta", "Status": "\u2705 Verified"},
            {"Finding": "Enforcement hollowing (Prong 3)", "Value": "SEC 15%+, CFTC 21.5% cut, CFPB alerts killed, 50K positions", "Status": "\u2705 Verified"},
            {"Finding": "Feb 11 single-day compliance density", "Value": "7 compliance events (5 EOs + USDA + QXO) \u2014 highest in 2026", "Status": "\u2705 Verified"},
            {"Finding": "Bondi hearing \u00b17 day window", "Value": "17 compliance events vs ~3\u20134 baseline (+467%)", "Status": "\u2705 Verified"},
            {"Finding": "Q4 2025 13F: 3 predictions tested", "Value": "EA stable, Mubadala reversed, no Gulf SWF entries", "Status": "\u274c All 3 FAILED"},
            {"Finding": "Mubadala Bitcoin ETF expansion", "Value": "IBIT +46% (8.7M\u219212.7M shares); Abu Dhabi ~$1.04B", "Status": "\u2705 Verified"},
            {"Finding": "Board of Peace inaugural summit", "Value": "~50 countries, $7B pledged, $10B US, 10% of $70B need", "Status": "\u2705 Verified"},
            {"Finding": "Historical backfill (2017\u20132024)", "Value": "66 pairs, median +7d, 5 neg. windows, 10/10 claims verified", "Status": "\u2705 Verified"},
            {"Finding": "Backfill correlation impact", "Value": "\u0394r = +0.0012, \u0394\u03c1 = +0.0023 \u2014 baseline unaffected", "Status": "\u2705 Verified"},
        ]

        key_stats_df = pd.DataFrame(key_stats_data)

        def _style_key_stats(row):
            if "\u274c" in row["Status"]:
                return ["background-color: rgba(230, 57, 70, 0.15)"] * len(row)
            return ["background-color: rgba(42, 157, 143, 0.10)"] * len(row)

        styled = key_stats_df.style.apply(_style_key_stats, axis=1)
        st.dataframe(styled, use_container_width=True, hide_index=True)

        st.caption(
            "20 of 21 findings verified. 1 entry documents 3 failed 13F predictions "
            "(displayed in red). Source: README.md Key Statistics table."
        )

    st.divider()

    # Framework overview
    st.subheader("Framework Overview")

    st.markdown(
        "This dashboard tracks the **friction-compliance correlation**: when "
        "high-visibility events cluster, institutional compliance events follow at a "
        "statistically significant 2-week lag. **Core finding:** r\u2009=\u20090.6196, "
        "p\u2009=\u20090.0004 (30 weeks). **Historical validation:** 66 pairs across "
        "2017\u20132024, median lag +7 days. **Negative windows:** 5 confirmed. "
        "For the broader framework (regulatory exemptions, technical opacity), see the "
        "full repository."
    )

    st.divider()

    st.markdown(
        "**Reproducibility:** All findings are reproducible. Run the scripts "
        "in `Run_Correlations_Yourself/`."
    )
    st.markdown(
        "**Source:** [github.com/Leerrooy95/The_Regulated_Friction_Project]"
        "(https://github.com/Leerrooy95/The_Regulated_Friction_Project)"
    )

    st.caption(
        "Statistical findings have been independently verified by a separate "
        "AI agent (Copilot Opus 4.6) using adversarial methodology checks."
    )

    st.info("Navigate to the **Statistical Overview** tab to explore the correlation data.")

# =====================================================================
# TAB 1: STATISTICAL OVERVIEW
# =====================================================================
with tab_overview:
    st.header("Statistical Overview")

    # Metric row 1
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Pearson r (lag)", f"{r:.4f}", help=f"{selected_lag}-week lag, core dataset")
    c2.metric("p-value", f"{p:.4f}", help="Two-tailed significance")
    c3.metric("Observations", str(n_eff), help="Effective n after lag adjustment")
    if backfill_stats:
        c4.metric("Backfill pairs", str(backfill_stats["n"]), help="2017-2024")
        c5.metric("Median lag", f"+{backfill_stats['median']:.0f} days", help="Backfill median")
    else:
        c4.metric("Backfill pairs", "N/A")
        c5.metric("Median lag", "N/A")

    # Metric row 2
    c1, c2, c3 = st.columns(3)
    total_events = (backfill_stats["n"] if backfill_stats else 0) + (len(negative_df) if negative_df is not None else 0)
    response_rate = backfill_stats["n"] / total_events * 100 if total_events > 0 else 0
    c1.metric("Response rate", f"{response_rate:.0f}%",
              help=f"{backfill_stats['n'] if backfill_stats else 0} of {total_events} friction events")
    c2.metric("Non-response events",
              f"{len(negative_df) if negative_df is not None else 0} / {total_events}",
              help="Within expected variance")
    c3.metric("95% CI for r", f"[{ci_low:.2f}, {ci_high:.2f}]",
              help="Fisher z-transform confidence interval")

    st.divider()

    # Lag sweep chart
    st.subheader("Correlation by Lag (0-6 weeks)")
    lag_vals = sorted(lag_sweep.keys())
    r_vals = [lag_sweep[l][0] for l in lag_vals]
    colors = [COLOR_LAG_HIGHLIGHT if l == selected_lag else COLOR_NEUTRAL for l in lag_vals]

    fig_sweep = go.Figure(go.Bar(
        x=[f"Lag {l}" for l in lag_vals],
        y=r_vals,
        marker_color=colors,
        text=[f"{rv:.3f}" for rv in r_vals],
        textposition="outside",
    ))
    fig_sweep.update_layout(
        yaxis_title="Pearson r",
        height=300,
        margin=dict(t=20, b=40),
        yaxis=dict(range=[-0.8, 0.8]),
    )
    st.plotly_chart(fig_sweep, width='stretch')

    st.caption(
        f"0-lag Pearson: r = {r0:.4f} | "
        f"{selected_lag}-lag Spearman: \u03c1 = {rho:.4f}"
    )

    st.divider()

    # Negative windows framing
    if show_negatives and negative_df is not None:
        st.subheader("Negative Windows: Statistical Context")
        st.info(NEGATIVE_WINDOW_FRAMING)

        # Expandable formal test
        with st.expander("Formal statistical test: Is the 7% non-response rate unusual?"):
            st.markdown(
                "**Binomial test**:\n"
                f"- Observed: {len(negative_df)} non-responses in {total_events} trials "
                f"({len(negative_df) / total_events * 100:.1f}%)\n"
                "- H\u2080: true non-response rate = 0.20 (generous null)\n"
                "- Result: p = 0.006 (reject H\u2080 \u2014 the non-response rate is "
                "significantly *lower* than 20%)\n\n"
                "**Interpretation**: The 93% response rate is statistically significantly "
                "high. The 5 non-response events are *fewer* than would be expected under "
                "most reasonable models of random institutional behavior."
            )

        # Negative windows table with context
        display_df = negative_df.copy()
        display_df["Context"] = display_df["Friction_Event"].map(NEGATIVE_WINDOW_CONTEXT)
        st.dataframe(
            display_df[["Year", "Friction_Event", "Friction_Date", "Notes", "Context"]],
            width='stretch',
            hide_index=True,
        )

        st.caption(
            "Non-response classification reflects absence of EOs only. Broader "
            "compliance metrics for these windows are documented in negative_windows.csv."
        )


# =====================================================================
# TAB 2: TIME SERIES & SCATTER
# =====================================================================
with tab_timeseries:
    st.header("Time Series & Scatter Analysis")

    # Dual-axis time series
    st.subheader("Friction & Compliance Indices (30-Week Core Dataset)")

    fig_ts = make_subplots(specs=[[{"secondary_y": True}]])

    fig_ts.add_trace(
        go.Scatter(
            x=core_df["Week_Index"],
            y=core_df["Epstein_Friction_Index"],
            name="Friction Index",
            line=dict(color=COLOR_FRICTION, width=2),
            mode="lines+markers",
            marker=dict(size=5),
        ),
        secondary_y=False,
    )

    fig_ts.add_trace(
        go.Scatter(
            x=core_df["Week_Index"],
            y=core_df["Institutional_Compliance_Index"],
            name=f"Compliance Index",
            line=dict(color=COLOR_COMPLIANCE, width=2),
            mode="lines+markers",
            marker=dict(size=5),
        ),
        secondary_y=True,
    )

    fig_ts.update_xaxes(title_text="Week Index")
    fig_ts.update_yaxes(title_text="Friction Index (1-10)", secondary_y=False,
                        color=COLOR_FRICTION)
    fig_ts.update_yaxes(title_text="Compliance Index (1-10)", secondary_y=True,
                        color=COLOR_COMPLIANCE)
    fig_ts.update_layout(height=400, margin=dict(t=20, b=40),
                         legend=dict(orientation="h", yanchor="bottom", y=1.02))

    st.plotly_chart(fig_ts, width='stretch')
    st.caption(
        f"Visual inspection: friction peaks tend to precede compliance peaks "
        f"by approximately {selected_lag} week(s)."
    )

    st.divider()

    # Scatter + regression
    st.subheader(f"Scatter: Friction (lag {selected_lag}) vs. Compliance")

    fig_scatter = go.Figure()

    # Prediction band
    if show_ci:
        fig_scatter.add_trace(go.Scatter(
            x=np.concatenate([reg["x_line"], reg["x_line"][::-1]]),
            y=np.concatenate([reg["y_upper"], reg["y_lower"][::-1]]),
            fill="toself",
            fillcolor=COLOR_PREDICTION_BAND,
            line=dict(color="rgba(0,0,0,0)"),
            name="\u00b12 SD prediction band",
            showlegend=True,
        ))

    # Data points
    fig_scatter.add_trace(go.Scatter(
        x=reg["x"],
        y=reg["y"],
        mode="markers",
        marker=dict(size=10, color=COLOR_COMPLIANCE, opacity=0.7),
        name="Observations",
    ))

    # Regression line
    fig_scatter.add_trace(go.Scatter(
        x=reg["x_line"],
        y=reg["y_line"],
        mode="lines",
        line=dict(color=COLOR_FRICTION, width=2, dash="dash"),
        name=f"r = {r:.4f}, p = {p:.4f}",
    ))

    fig_scatter.update_layout(
        xaxis_title=f"Friction Index (lagged {selected_lag} weeks)",
        yaxis_title="Compliance Index",
        height=450,
        margin=dict(t=20, b=40),
    )
    st.plotly_chart(fig_scatter, width='stretch')

    col_left, col_right = st.columns(2)
    col_left.markdown(
        f"**Regression**: Compliance = {reg['slope']:.3f} \u00d7 Friction + {reg['intercept']:.3f}"
    )
    col_right.markdown(
        f"**r\u00b2 = {r**2:.4f}** \u2014 {r**2 * 100:.1f}% of compliance variance "
        f"explained by friction"
    )


# =====================================================================
# TAB 3: LAG DISTRIBUTION (BACKFILL)
# =====================================================================
with tab_backfill:
    st.header("Lag Distribution: Historical Backfill (2017\u20132024)")

    if backfill_df is None:
        st.warning("Backfill dataset not available.")
    else:
        lags = backfill_df["lag_parsed"].dropna()

        # Histogram
        fig_hist = go.Figure()
        fig_hist.add_trace(go.Histogram(
            x=lags,
            nbinsx=20,
            marker_color=COLOR_NEUTRAL,
            name="Lag Distribution",
        ))
        fig_hist.add_vline(x=lags.median(), line_dash="dash", line_color=COLOR_FRICTION,
                           annotation_text=f"Median: +{lags.median():.0f}d")
        fig_hist.add_vline(x=0, line_dash="solid", line_color="black",
                           annotation_text="Simultaneous")
        fig_hist.update_layout(
            xaxis_title="Lag (days)",
            yaxis_title="Count",
            height=350,
            margin=dict(t=20, b=40),
        )
        st.plotly_chart(fig_hist, width='stretch')

        # Bin table and year breakdown side by side
        col_bins, col_years = st.columns(2)

        with col_bins:
            st.subheader("Lag Bins")
            bin_data = compute_lag_bins(backfill_df["lag_parsed"])
            st.dataframe(pd.DataFrame(bin_data), hide_index=True, width='stretch')

        with col_years:
            st.subheader("Year Breakdown")
            year_df = compute_year_breakdown(backfill_df)
            st.dataframe(year_df, hide_index=True, width='stretch')

        st.divider()

        # Backfill timeline with negative windows
        st.subheader("Backfill Timeline")

        fig_timeline = go.Figure()

        # Positive events
        fig_timeline.add_trace(go.Scatter(
            x=backfill_df["Friction_Date"],
            y=backfill_df["lag_parsed"],
            mode="markers",
            marker=dict(size=8, color=COLOR_NEUTRAL),
            name="Friction\u2192Compliance Pair",
            text=backfill_df["Friction_Event"],
            hovertemplate="<b>%{text}</b><br>Lag: %{y} days<extra></extra>",
        ))

        # Variance band
        median_lag = float(lags.median())
        std_lag = float(lags.std())
        fig_timeline.add_hline(y=median_lag, line_dash="dot", line_color=COLOR_VARIANCE,
                               annotation_text=f"Median: +{median_lag:.0f}d")
        fig_timeline.add_hrect(
            y0=median_lag - std_lag, y1=median_lag + std_lag,
            fillcolor="rgba(233, 196, 106, 0.15)", line_width=0,
            annotation_text="\u00b11 SD",
        )

        # Negative windows as gray vertical bands
        if show_negatives and negative_df is not None:
            for _, row in negative_df.iterrows():
                fig_timeline.add_vrect(
                    x0=row["Friction_Date"], x1=row["Window_End"],
                    fillcolor=COLOR_NEGATIVE_WINDOW,
                    line_width=0,
                    annotation_text=str(row["Friction_Event"])[:30] + "...",
                    annotation_position="top left",
                    annotation_font_size=9,
                )

        fig_timeline.update_layout(
            xaxis_title="Friction Event Date",
            yaxis_title="Response Lag (days)",
            height=450,
            margin=dict(t=20, b=40),
        )
        st.plotly_chart(fig_timeline, width='stretch')

        if show_negatives:
            st.caption(
                "Gray bands = negative windows (friction events with no compliance "
                "response found in the 14-day Federal Register search window). "
                "These represent 7% of all examined events \u2014 expected statistical variance."
            )


# =====================================================================
# TAB 4: RAW DATA EXPLORER
# =====================================================================
with tab_data:
    st.header("Raw Data Explorer")

    data_choice = st.radio(
        "Select dataset:",
        ["Core 30-Week Data", "Historical Backfill (66 pairs)",
         "Negative Windows (5)", "Federal Register EOs (Spider)"],
        horizontal=True,
    )

    if data_choice == "Core 30-Week Data":
        st.dataframe(core_df, width='stretch', hide_index=True)
        st.download_button(
            "Download CSV", core_df.to_csv(index=False),
            "core_30_week_data.csv", "text/csv",
        )

    elif data_choice == "Historical Backfill (66 pairs)":
        if backfill_df is not None:
            years = st.multiselect(
                "Filter by year",
                sorted(backfill_df["Year"].unique()),
                default=sorted(backfill_df["Year"].unique()),
            )
            filtered = backfill_df[backfill_df["Year"].isin(years)]
            st.dataframe(
                filtered[["Year", "Friction_Event", "Friction_Date",
                           "Compliance_Event", "Compliance_Date", "Lag_Days"]],
                width='stretch', hide_index=True,
            )
            st.download_button(
                "Download CSV", filtered.to_csv(index=False),
                "historical_backfill_filtered.csv", "text/csv",
            )
        else:
            st.warning("Backfill dataset not available.")

    elif data_choice == "Negative Windows (5)":
        if negative_df is not None:
            st.dataframe(negative_df, width='stretch', hide_index=True)
            st.caption("5 of 71 events (7%) = expected variance for r = 0.62 model")
            st.download_button(
                "Download CSV", negative_df.to_csv(index=False),
                "negative_windows.csv", "text/csv",
            )
        else:
            st.warning("Negative windows dataset not available.")

    elif data_choice == "Federal Register EOs (Spider)":
        if eo_df is not None:
            st.dataframe(eo_df, width='stretch', hide_index=True)
            st.caption(f"Total EOs in spider dataset: {len(eo_df)}")
            st.download_button(
                "Download CSV", eo_df.to_csv(index=False),
                "federal_register_eos.csv", "text/csv",
            )
        else:
            st.warning("EO spider dataset not available.")

# =====================================================================
# TAB 5: PREDICTION TRACKER
# =====================================================================
with tab_predictions:
    st.header("Prediction Tracker")

    st.markdown(
        "Falsifiable predictions are the test of any model. This tracker shows all "
        "predictions made by this project, including failures. Three Q4 2025 13F "
        "predictions failed \u2014 this is recorded as data, not hidden."
    )

    st.divider()

    # ── Prediction data (sourced from README.md Testable Predictions table) ──
    predictions_data = [
        {"Prediction": "Event clustering at next file deadline", "Timeframe": "Ongoing", "Status": "\u2705 Confirmed", "Date Added": "Pre-v9.0"},
        {"Prediction": "Tu BiShvat policy action", "Timeframe": "Feb 1\u20132, 2026", "Status": "\u2705 Confirmed", "Date Added": "Pre-v9.0"},
        {"Prediction": "UK Mandelson disclosure", "Timeframe": "Feb\u2013Mar 2026", "Status": "\u2705 Confirmed", "Date Added": "Pre-v9.0"},
        {"Prediction": "Board of Peace first summit", "Timeframe": "Feb 19, 2026", "Status": "\u2705 Confirmed", "Date Added": "Pre-v9.0"},
        {"Prediction": 'Board of Peace = "Board of Profits"', "Timeframe": "Feb 2026", "Status": "\u2705 Confirmed", "Date Added": "v9.4"},
        {"Prediction": "West Bank annexation acceleration", "Timeframe": "Feb 2026", "Status": "\u2705 Confirmed", "Date Added": "v9.4"},
        {"Prediction": "Al-Tanf withdrawal / Iran concession", "Timeframe": "Feb 11, 2026", "Status": "\u2705 Confirmed", "Date Added": "v9.4"},
        {"Prediction": "Feb 1\u201319 compliance window density", "Timeframe": "Feb 2026", "Status": "\u2705 Confirmed", "Date Added": "v9.4"},
        {"Prediction": "Indonesia ISF troop deployment", "Timeframe": "2026", "Status": "\u2705 Confirmed", "Date Added": "v9.4"},
        {"Prediction": "ISF under BoP (not UN) command", "Timeframe": "Feb 2026", "Status": "\u2705 Confirmed", "Date Added": "v9.4"},
        {"Prediction": "1789 Capital \u2192 Anduril \u2192 WDS 2026 link", "Timeframe": "Feb 2026", "Status": "\u2705 Confirmed", "Date Added": "v9.4"},
        {"Prediction": "Q4 2025 13F: PIF EA position change", "Timeframe": "Feb 17+, 2026", "Status": "\u274c Failed", "Date Added": "v9.0"},
        {"Prediction": "Q4 2025 13F: Mubadala defense expansion", "Timeframe": "Feb 17+, 2026", "Status": "\u274c Failed", "Date Added": "v9.0"},
        {"Prediction": "Q4 2025 13F: New Gulf SWF Oracle/defense entries", "Timeframe": "Feb 17+, 2026", "Status": "\u274c Failed", "Date Added": "v9.0"},
        {"Prediction": "Gulf SWF Q4 positioning revealed", "Timeframe": "Feb 14, 2026", "Status": "\u274c Failed", "Date Added": "Pre-v9.0"},
        {"Prediction": "DOGE-predicted instability", "Timeframe": "Q1 2026", "Status": "\u23f3 Tracking", "Date Added": "Pre-v9.0"},
        {"Prediction": "California TikTok investigation findings", "Timeframe": "Q1 2026", "Status": "\u23f3 Pending", "Date Added": "Pre-v9.0"},
        {"Prediction": "Khanna investigation findings", "Timeframe": "Mar 2026", "Status": "\u23f3 Pending", "Date Added": "Pre-v9.0"},
        {"Prediction": "Arkansas PSC order text release", "Timeframe": "Q1 2026", "Status": "\u23f3 Pending", "Date Added": "v9.4"},
        {"Prediction": "QXO further acquisitions", "Timeframe": "2026", "Status": "\u23f3 Tracking", "Date Added": "v9.2"},
        {"Prediction": "EO 14375 legal challenge (IOIA authorization)", "Timeframe": "2026", "Status": "\u23f3 Pending", "Date Added": "v9.2"},
        {"Prediction": "NTEU court-ordered position list disclosure", "Timeframe": "Feb 27, 2026", "Status": "\u23f3 Pending", "Date Added": "v9.7"},
        {"Prediction": "Schedule Policy/Career implementation", "Timeframe": "Mar 9, 2026", "Status": "\u23f3 Pending", "Date Added": "v9.7"},
        {"Prediction": "Feb 11 compliance density repeat at next major hearing", "Timeframe": "Ongoing", "Status": "\u23f3 Pending", "Date Added": "v9.2"},
        {"Prediction": "Khanna investigation document deadline", "Timeframe": "Mar 1, 2026", "Status": "\u23f3 Pending", "Date Added": "v9.7"},
    ]

    pred_df = pd.DataFrame(predictions_data)

    # ── Summary counters ──
    n_confirmed = pred_df["Status"].str.contains("\u2705").sum()
    n_failed = pred_df["Status"].str.contains("\u274c").sum()
    n_pending = len(pred_df) - n_confirmed - n_failed

    m1, m2, m3 = st.columns(3)
    m1.metric("Confirmed", f"{n_confirmed} \u2705")
    m2.metric("Failed", f"{n_failed} \u274c")
    m3.metric("Pending / Tracking", f"{n_pending} \u23f3")

    st.divider()

    # ── Failed predictions (prominent display) ──
    st.subheader("Failed Predictions")
    st.caption(
        "These predictions were publicly made and publicly failed. "
        "The 13F visibility gap is now a documented finding: the architecture "
        "operates below 13F disclosure thresholds via private deals, non-US "
        "securities, and LP interests."
    )
    failed_df = pred_df[pred_df["Status"].str.contains("\u274c")].reset_index(drop=True)
    st.dataframe(failed_df, use_container_width=True, hide_index=True)

    st.divider()

    # ── Full prediction table with filter ──
    st.subheader("All Predictions")

    status_filter = st.multiselect(
        "Filter by status",
        ["\u2705 Confirmed", "\u274c Failed", "\u23f3 Pending", "\u23f3 Tracking"],
        default=["\u2705 Confirmed", "\u274c Failed", "\u23f3 Pending", "\u23f3 Tracking"],
    )

    filtered_pred = pred_df[pred_df["Status"].isin(status_filter)]
    st.dataframe(filtered_pred, use_container_width=True, hide_index=True)

    st.caption(
        f"Total: {len(pred_df)} predictions | "
        f"{n_confirmed} confirmed, {n_failed} failed, {n_pending} pending/tracking"
    )


# ── Footer ───────────────────────────────────────────────────────────────
st.divider()
st.caption(DISCLAIMER)
