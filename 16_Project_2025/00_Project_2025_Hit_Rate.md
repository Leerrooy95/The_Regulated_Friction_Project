# Project 2025 → Repository Hit-Rate Analysis

**Purpose**: Cross-reference the 30 chapter directives of Project 2025's *Mandate for Leadership* against the event corpus already documented in `_AI_CONTEXT_INDEX/` and the wider repository, to see how much of what this repo tracks corroborates, executes, or extends specific Project 2025 chapter recommendations.

**Method**: Targeted keyword/entity searches across the full repository (department names, named authors, and each chapter's specific proposals — Schedule F, mifepristone, NOAA, CFPB, Ex-Im Bank, etc.), followed by close reads of the most relevant files (the `Administrative_State_Audit/` node timelines, `Node_Dossiers/tier2_purged_officials.md`, `09_CURRENT_THREADS.md`, `02_MEDIA_FIREWALL.md`, `04_CAPITAL_ARCHITECTURE.md`, `08_KEY_DATASETS.md`). Every row is anchored to a specific repo file; verification status follows this repository's own three-tier convention (✅ VERIFIED / ⚠️ PARTIALLY VERIFIED), plus a fourth category, **NO REPO MATCH**, added for this analysis to honestly record the absence of a hit — consistent with the repo's stated standard of documenting negative findings (see `CONTEXT_ROUTER.md`, "What NOT to Assume").

**Companion file**: `project_2025_mapping.csv` (Date, Chapter, Directive, Repo_Event, Verification_Status, Repo_Source_File — 47 rows).

**Important framing note**: This is *not* an independent audit of full Project 2025 implementation — that work already exists and is better resourced (Center for Progressive Reform/Governing for Impact's tracker reports 53% of the domestic agenda, 283/532 actions, initiated or completed as of the February 2026 update; project2025.observer reports ~48–50%; both are cited in the attached overview document). This analysis instead asks a narrower question: **of the events this specific OSINT repository happens to have already documented (friction-compliance timeline, administrative-state audit, purged-officials log, media/capital architecture), how many independently corroborate a named Project 2025 chapter directive?** The two figures measure different things and should not be conflated.

---

## Headline Numbers

| Metric | Count |
|---|---|
| Total Project 2025 chapters (Ch.1–30) | 30 |
| Chapters with at least one repo-documented event | 9 (Ch.1, 2, 3, 4, 5, 9, 17, 26, 28) |
| Chapters with **no** corresponding repo event found | 21 |
| Total mapped CSV rows | 47 |
| Rows marked ✅ VERIFIED | 21 |
| Rows marked ⚠️ PARTIALLY VERIFIED | 5 |
| Rows marked NO REPO MATCH | 21 |
| Repo-corpus hit rate (chapters with ≥1 real match) | **~27–30%** (8/30 if Ch.1 — which has no independent event of its own — is excluded as adjacent-only; 9/30 if included) |

The repo's own hit rate is lower than the independent trackers' ~48–53% because this repository was never built as a Project 2025 tracker — it was built around a different thesis (calendar-timed friction/compliance clustering, Gulf capital architecture, the Epstein leverage network, and the media firewall). Where its existing threads happen to overlap with Project 2025 chapters — chiefly the DOGE→OPM→DOJ "administrative state" consolidation loop, which a prior Copilot/Opus 4.6 analysis (`Project_Trident/Copilot_Opus_4.6_Analysis/Administrative_State_Audit/`) already mapped in detail — the correspondence is strong and well-sourced. Where the repo has no existing thread (Education, EPA, HHS abortion policy, HUD, Interior, Labor, Transportation, VA, Ex-Im Bank, the Federal Reserve, SBA, FEC, most of Ch.22's tax specifics), there is simply no data to report, and this analysis says so plainly rather than stretching a weak inference.

---

## Chapters With Repo-Documented Matches

| Chapter | Author | Match Strength | Summary |
|---|---|---|---|
| **Ch.3 — Central Personnel Agencies** (Schedule F) | Devine, Kirk, Dans | **Strongest** | Direct, granular, dated match. OPM's Schedule F guidance (Jan 20, 2025) → "Fork in the Road" (Jan 28) → probationary firings (Feb 14) → RIF guidance (Feb 26) → DOGE disbanded/absorbed into OPM (Nov 24, 2025) → Schedule Policy/Career final rule strips ~50,000 positions of MSPB protection (Feb 5, 2026). This is close to a 1:1 execution record of the chapter's core ask. |
| **Ch.17 — Department of Justice** | Gene Hamilton | **Strong** | Six dated events: Thursday Night Massacre (Feb 2025), White House bypassing DOJ to fire U.S. Attorneys, Bondi's Weaponization Working Group (Feb 5, 2025), 230+ DOJ lawyers fired/6,400+ departures, Ed Martin's removal (Jan/Feb 2026), and Bondi's own firing (Apr 2, 2026). Matches the chapter's "expand political appointees, align litigation with the president's agenda" directive closely. |
| **Ch.9 — USAID** | Max Primorac | **Strong** | USAID formally dissolved into the State Dept July 1, 2025; only 718 of ~10,500 positions survived (6.8%) — nearly a literal execution of "deradicalize/dismantle USAID." |
| **Ch.5 — Department of Homeland Security** | Ken Cuccinelli | **Moderate** | Noem fired Mar 5, 2026; DHS "shutdown" thread running Feb–June 2026; SAVE America Act centralizing state voter data into the DHS SAVE database. None of this confirms the chapter's specific "break DHS into a standalone border agency" recommendation — it documents DHS instability and data-authority expansion, which is adjacent but not identical. |
| **Ch.4 — Department of Defense** | Christopher Miller | **Moderate** | Hegseth's April 2, 2026 wartime purge of Gen. George, Gen. Hodne, and the Army's Chief of Chaplains matches the chapter's loyalty-over-seniority personnel theme; the chapter's specific DEI/transgender/COVID-discharge items have no independent repo event. |
| **Ch.28 — Federal Communications Commission** | Brendan Carr | **Moderate, with an irony flag** | Carr (the chapter's own author, now FCC Chair) fast-tracking the Paramount/WBD merger and the Oracle-led TikTok divestiture both touch the chapter's "rein in Big Tech" mandate, but the repo documents these as enabling large-scale *consolidation* into allied private hands (Ellison/Oracle/a16z/MGX) rather than the chapter's stated Section 230/antitrust rationale. Flagged as directionally related, not a clean match. |
| **Ch.2 — Executive Office of the President** | Russ Vought | **Moderate** | Vought's OMB role is explicitly tied by the repo to institutionalizing DOGE post-Musk, and he co-sponsors the Cabinet Bible Study — corroborated but sourced mainly through the repo's own dossier rather than independent citation within it. |
| **Ch.26 — Trade** | Navarro / Lassman | **Weak-Moderate** | SCOTUS struck down IEEPA tariffs (Feb 20, 2026); pivot to Section 122 (15% global surcharge, expiring Jul 24, 2026). Directionally consistent with Navarro's tariff approach but executed under different statutory authority than his proposed Reciprocal Trade Act. |
| **Ch.1 — White House Office** | Rick Dearborn | **Weak / adjacent only** | No independent event; only corroborated through the DOJ chain-of-command bypass logged under Ch.17. Listed for completeness, not counted as a strong hit. |

---

## Chapters With No Repo Match (21 of 30)

Ch.6 (State), Ch.7 (Intelligence Community), Ch.8 (Media Agencies/USAGM/CPB), Ch.10 (Agriculture), Ch.11 (Education), Ch.12 (Energy), Ch.13 (EPA), Ch.14 (HHS), Ch.15 (HUD), Ch.16 (Interior), Ch.18 (Labor), Ch.19 (Transportation), Ch.20 (Veterans Affairs), Ch.21 (Commerce/NOAA), Ch.22 (Treasury — the chapter's specific tax-bracket/IRS-DEI proposals; the repo's Treasury-adjacent stablecoin/CLARITY Act coverage is a different topic), Ch.23 (Export-Import Bank), Ch.24 (Federal Reserve), Ch.25 (SBA), Ch.27 (SEC/CFPB), Ch.29 (FEC), Ch.30 (FTC).

This is not evidence these directives went unimplemented — several (Department of Education restructuring, the EPA endangerment-finding rescission, Medicaid work requirements) are independently reported as enacted or in progress by mainstream outlets per the attached baseline documents. It only means **this specific repository's existing corpus does not currently document them**, most likely because the repo's collection focus (calendar-timed friction/compliance events, Gulf capital flows, the Epstein leverage network, and the DOGE/OPM/DOJ/FBI administrative-state loop) never had a reason to track, e.g., FERC rulemaking or VA disability-rating changes.

---

## Cross-Cutting Observations

1. **The strongest matches all cluster in one pre-existing repo thread.** Chapters 2, 3, 9, and 17 are all covered by the `Administrative_State_Audit/` analysis (a prior Copilot/Opus 4.6 deep-dive on the "DOGE → OPM → DOJ (+FBI)" consolidation loop, dated Feb 10, 2026). That analysis was not built with Project 2025 in mind, but it independently reconstructed almost exactly the mechanism Chapters 2–3 and 17 describe (Schedule F reclassification, OMB-driven bureaucratic alignment, DOJ as "the Shield"). This is the single highest-confidence overlap in the repository.

2. **Personnel-loyalty and purge patterns repeat across Ch.1, Ch.3, Ch.4, Ch.5, and Ch.17.** The `tier2_purged_officials.md` dossier's running log (Bongino, Noem, Bondi, Gen. George, Gen. Hodne, Maj. Gen. Green) is itself a cross-chapter signal: Project 2025's repeated instruction to replace career/independent leadership with loyalists shows up as a single recurring personnel-replacement pattern rather than 30 separate department-by-department stories.

3. **Ch.28 (FCC/Big Tech) is the one chapter where the repo shows outcome divergence from stated rationale.** Carr's chapter frames FCC action against Big Tech in free-speech/antitrust terms; the repo's Media Firewall and Ellison-node material instead documents Carr's FCC facilitating media-ownership *consolidation* (Paramount/WBD, TikTok into an Oracle-led consortium). Both are "FCC action shaping Big Tech," but the direction is closer to concentration than the chapter's stated deconcentration goal — worth flagging explicitly rather than counting as a clean hit.

4. **Absence is concentrated in domestic-agency substantive policy (not administrative-state mechanics).** Every chapter with no match (Agriculture, Education, Energy, EPA, HHS, HUD, Interior, Labor, Transportation, VA, Commerce/NOAA, Treasury tax specifics, Ex-Im, Fed, SBA, SEC/CFPB, FEC, FTC) is a substantive-policy chapter rather than a personnel/structural-power chapter. This is consistent with the repo's stated focus areas in `00_START_HERE.md` and `CONTEXT_ROUTER.md` — it was simply never built to track, e.g., NHTSA fuel-economy rulemaking.

---

## Suggested Next Steps (if you want to close some of these gaps)

- If you want independent-tracker-level coverage of the substantive-policy chapters (Education, EPA, HHS, etc.), the Center for Progressive Reform/Governing for Impact tracker and project2025.observer (both cited in the attached overview doc) are already doing that work at scale — worth linking rather than re-deriving inside this repo.
- If you want to extend *this* repo's own tracking, the highest-leverage additions (given what's already being tracked) would be: (a) a dedicated Department of Education node dossier, since Ch.11 is one of Project 2025's most consequential and most-reported chapters and currently has zero repo presence; (b) an EPA/endangerment-finding entry, since the repo's `07_METHODOLOGY.md`/`09_CURRENT_THREADS.md` framework would likely find a friction-compliance timing pattern there similar to the Schedule F case; and (c) closing the Ch.22 Treasury gap by distinguishing the chapter's tax-bracket proposal from the repo's existing (and unrelated) WLF/USD1 stablecoin coverage, so the two don't get conflated in future analysis.

---

*Analysis performed by cross-referencing the two attached Project 2025 baseline documents against the live `_AI_CONTEXT_INDEX/` and repository corpus as of the current session. All "VERIFIED" rows in `project_2025_mapping.csv` trace to a specific, already-sourced repo file; no new external web research was performed for this analysis — it is a corpus cross-reference, not a fresh investigation.*
