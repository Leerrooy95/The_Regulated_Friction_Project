# Tier 3 Node Dossier: Geopolitical Thermostat Ruleset

**Node Type**: Geopolitical Thermostat (Ruleset)  
**Last Updated**: February 24, 2026  
**Trigger Conditions**: Any event timing analysis, calendar windows, convergence detection

---

## Purpose

This is the master logic file for timing analysis. It defines the 7-day median lag pattern (r = 0.6196 at 2-week index resolution), calendar anchor signals, and convergence detection rules documented in this repository. Load this dossier for any analysis involving event timing, calendar windows, or friction-compliance correlation.

---

## Core Rule: The 7-Day Median Lag

### The Statistical Finding

| Metric | Value | Verification |
|--------|-------|--------------|
| Correlation coefficient | r = +0.6196 | ✅ VERIFIED |
| Lag | 7 days median (mean 6.5); r = 0.6196 at 2-week index resolution | ✅ VERIFIED |
| Significance | p = 0.0004 | ✅ VERIFIED |
| Sample size | n = 28 paired observations (30-week dataset) | ✅ VERIFIED |
| Interpretation | Strong correlation | Standard statistical interpretation |

### What This Means

When analyzing a new event:

1. **If it's a friction event** (document release, scandal, media crisis): Look for compliance events (policy shifts, capital moves) in the **following 14-day window**
2. **If it's a compliance event** (policy shift, financial move): Look for friction events in the **preceding 14-day window**

### Lag Table

| Lag | Correlation | Interpretation |
|-----|-------------|----------------|
| 0 weeks (simultaneous) | r = -0.03 | No same-day relationship |
| **2 weeks (friction leads)** | **r = +0.6196** | **Strongest — friction predicts compliance** |
| 2 weeks (reverse) | r = -0.44 | Negative — compliance does NOT predict friction |

---

## Calendar Anchors

### Definition

**Calendar Anchor**: A predictable low-attention period that multiple actors may independently use as a timing signal. Events clustering on these dates may receive reduced scrutiny.

### Primary Calendar Anchors

| Anchor Type | Dates | Attention Level |
|-------------|-------|-----------------|
| **Winter Solstice Window** | Dec 19-23 | Very low (holiday travel, reduced staffing) |
| **Christmas-New Year** | Dec 24 - Jan 2 | Very low |
| **Summer Solstice Window** | Jun 19-23 | Moderate-low |
| **Major US Holidays** | July 4, Labor Day, Thanksgiving | Low |
| **Fiscal Deadlines** | End of quarters (Mar 31, Jun 30, Sep 30, Dec 31) | Variable (attention on specific topics) |
| **13F Filing Deadline** | 45 days after quarter end | Low (specialized audience) |

### December 2025 Case Study

The Dec 19-23, 2025 window demonstrated the convergence pattern:

| Date | Friction | Compliance | Key Events |
|------|----------|------------|------------|
| Dec 19 | 1 | 5 | Epstein Library release (DOJ) |
| Dec 22 | **6** | **13** | Peak convergence day |
| Dec 23 | **8** | **9** | Redaction failures exposed |

**Five signal types converged on Dec 22**:
1. Friction: Epstein redaction failures (NYT)
2. Geopolitics: China EU dairy tariffs (42.7%)
3. Financial: BlackRock Bitcoin ETF "top theme"
4. Policy: Travel ban expansion, DOGE analysis
5. Cyber/Intel: CRINK nation-state threat analysis

---

## Convergence Detection Rules

### Rule 1: Multiple Event Types

A convergence is detected when **3+ distinct event types** cluster within a **7-day window**:

| Event Type | Examples |
|------------|----------|
| Friction | Document releases, scandals, media crises |
| Policy | Executive orders, regulatory changes, enforcement actions |
| Financial | M&A announcements, 13F filings, credit facilities |
| Geopolitical | Diplomatic actions, military movements, treaty signings |
| Cyber/Intel | Breach disclosures, attribution announcements |

### Rule 2: Density Threshold

The dashboard uses **HIGH_DENSITY_THRESHOLD = 3** events per day to flag convergence windows.

### Rule 3: Calendar Anchor Proximity

Weight convergences higher if they fall within **±3 days** of a calendar anchor.

---

## Application Instructions

### Step 1: Classify the Event

| Category | Definition | Examples |
|----------|------------|----------|
| **Friction** | Attention-consuming; dominates media | File releases, scandals, celebrity drama |
| **Compliance** | Substantive institutional change | EOs, M&A, troop movements, policy shifts |
| **Calendar Anchor** | Predictable timing signal | Holidays, solstices, fiscal deadlines |

### Step 2: Identify the Window

```
Event Date: [DATE]
         │
    ─────┼─────
         │
  -14 days    +14 days
         │
   If FRICTION → Look FORWARD for compliance
   If COMPLIANCE → Look BACKWARD for friction
```

### Step 3: Check Calendar Proximity

Is the event within ±3 days of a calendar anchor?

| If YES | → Higher significance (expected low attention) |
| If NO | → Standard significance |

### Step 4: Count Convergence

How many event types cluster in the 7-day window?

| Count | Assessment |
|-------|------------|
| 1-2 | Normal activity |
| **3-4** | **Convergence detected** |
| **5+** | **High-density convergence** (flag for analysis) |

---

## Statistical Robustness

### Tests Passed

| Test | Result | Interpretation |
|------|--------|----------------|
| Permutation (1K shuffles) | r = 0.62, p < 0.001 | ✅ Not random |
| Block bootstrap (autocorrelation-adjusted) | p = 0.008 | ✅ Survives adjustment |
| December 2025 exclusion | ρ = 0.60, p < 0.0001 | ✅ Not dependent on single window |
| Granger causality (hand-scored) | F→C at lag 1, p = 0.0008 | ✅ Friction predicts compliance |
| Event colocation | 20-42x baseline | ✅ Strong clustering |
| Historical backfill (2017-2024) | 66 pairs, median lag +7 days | ✅ Pattern extends historically |

### Falsification Criteria

The framework would be falsified if:

1. r = 0.6196 cannot be reproduced
2. December 2025 clustering proves to be data artifact
3. Future friction-compliance windows show no pattern
4. Calendar anchors show random event distribution

---

## What This Ruleset Claims

1. ✅ **Pattern exists**: Friction and compliance cluster with statistical significance
2. ✅ **Calendar signals**: Low-attention windows attract multiple event types
3. ✅ **Emergent coordination**: Shared incentives can produce clustering without communication
4. ✅ **Structural, not causal**: The pattern exists regardless of intent

## What This Ruleset Does NOT Claim

1. ❌ Central coordination between actors
2. ❌ That friction *causes* compliance
3. ❌ Illegal activity
4. ❌ Individual intent

---

## Quick Reference Card

### For Any New Event

```
1. CLASSIFY: Friction or Compliance?
2. WINDOW: ±14 days from event
3. ANCHOR: Within ±3 days of holiday/solstice/deadline?
4. COUNT: How many event types in 7-day window?
5. ASSESS: 
   - 1-2 types = Normal
   - 3-4 types = Convergence
   - 5+ types = High-density (investigate)
```

### Key Numbers to Remember

| Metric | Value |
|--------|-------|
| Optimal lag | 7 days (median) |
| Correlation | r = 0.62 |
| Significance | p = 0.0004 |
| Convergence threshold | 3+ event types |
| High-density threshold | 3+ events/day |
| Historical median lag | +7 days |

---

## Cross-References

- **For methodology details**: `_AI_CONTEXT_INDEX/07_METHODOLOGY.md`
- **For core theory**: `_AI_CONTEXT_INDEX/01_CORE_THEORY.md`
- **For robustness tests**: `Project_Trident/Copilot_Opus_4.6_Analysis/Statistical_Tests/`
- **For datasets**: `Run_Correlations_Yourself/`

---

## When to Load This Dossier

**Always load for timing analysis.** Specifically when:
- Assessing whether an event falls within a significant window
- Analyzing convergence between multiple event types
- Checking calendar anchor proximity
- Applying the 7-day median lag framework

---

*This ruleset codifies the statistical findings documented in the repository. All metrics are reproducible via scripts in `Run_Correlations_Yourself/`.*
