# Heritage_2026_Successor_Documents

**Location:** `16_Project_2025/Heritage_2026_Successor_Documents/`
**Snapshot date:** 2026-10-01
**Subject:** Heritage Foundation Special Report No. 323, *Saving America by Saving the Family: A Foundation for the Next 250 Years* (Jan 8, 2026). Shorthand used in conversation: "Project 2026" (a media/critic nickname; Heritage says no such project exists and describes SR323 as the first in a series of special reports).

## What this folder is

A layout-first resource, built the same way as the Project 2025 work one level up: first lay out what the document asks for, then check each ask against the real world. SR323 is much smaller than the Mandate for Leadership, so the register is one file instead of a chapter-by-chapter synthesis.

## Files

| File | What it is |
|---|---|
| `SR323_Overview.md` | Synthesis of the report: thesis, structure, three federal mechanisms, cost framing, reading cautions (with text-line references) |
| `sr323_asks_register.csv` | 72 asks with actor, mechanism, dollar figure, trackability, and **status as of 2026-10-01** with evidence and source URL |
| `sr323_claims_register.csv` | 33 falsifiable claims (checkable stats, contested causal claims, one normative example) with how to test each. Not yet tested |
| `SR323_Baseline_Metrics.md` | "Before" numbers to lock in today so change can be measured later |
| `SR323_Internal_Inconsistencies.md` | 13 internal discrepancies in the report (7 verified against the text, 6 flagged) |

## Status vocabulary

Same as the Project 2025 mapping one level up, plus one added value:
- **VERIFIED** — the ask (or a substantially identical measure) is enacted/issued/implemented.
- **PARTIALLY VERIFIED** — part of it, or a narrower/different measure.
- **PENDING** *(new for this folder)* — formal movement but not enacted (bill passed one chamber, proposed rule, committee passage). Added because most SR323 asks are legislative proposals, and "blocked" would overstate what happened.
- **ATTEMPTED — BLOCKED/REVERSED**, **AFFIRMATIVELY CONTRADICTED**, **NO MATCH FOUND** — as before.

Column `Predates_SR323`: Y if the matching action occurred before Jan 8, 2026. A match that predates the report cannot be credited to it (the report often cites such actions as existing baseline). Matching is not causation: a match means "the world contains this measure," not "SR323 caused it."

## Headline tallies (as of 2026-10-01)

- 72 asks: 6 VERIFIED, 26 PARTIALLY VERIFIED, 5 PENDING, 1 AFFIRMATIVELY CONTRADICTED, 34 NO MATCH FOUND.
- Of the 6 VERIFIED, 3 predate the report (C07 green-subsidy repeal, E09 IVF actions, E11 religious-liberty bodies). The 3 after Jan 8, 2026: C08 (ROAD to Housing Act NEPA exclusions), E01 (state school phone bans, a state patchwork), E12 (EPA endangerment-finding repeal).
- The report's signature federal mechanisms (NEST, FAM credit, HCE credit) and the executive-order/OMB family-impact asks (A01–A06) each have **no match found**. The one new "NEST Act" in Congress (H.R. 7422) is an unrelated first-time-homebuyer account that shares the name.
- Of 54 federal-checkable asks: 25 no match, 19 partial, 5 pending, 5 verified.
- Where the report's own baseline moved: Trump Accounts ($1,000 newborn deposit) launched July 4, 2026 (B09), which the report treats as the platform for NEST.

## How to use it

- **Re-run:** each January and July. Update the `Status_2026-10-01` column name to the new date (or add a new column), keep the old one, and compare.
- **Event-dated tracking is thin right now** (14 rows have any action dated after Jan 8, 2026). The snapshot-date column and baseline metrics are the useful time anchors.
- **Claims register:** test CL01 (welfare marriage penalty) and CL02 (housing/affordability) first — the two examples that started this.

## Method and limits

- Asks extracted from the full text (all ~5,500 body lines read; endnotes not read). Four segments were extracted in parallel by research agents, and key figures were spot-checked against the source text by hand.
- Status research ran with web search; four of the highest-impact findings were re-checked against the cited pages (ROAD Act, Treasury proposed rule, KIDS Act, EPA repeal). The Trump Accounts launch rests on Treasury/news results that were not opened directly.
- NO MATCH FOUND rows rest on absence of evidence from general searches; congress.gov bill search was unavailable, so bill statuses come from secondary sources. The `Confidence` column says how solid each row is.
- Adjustments made to raw research ratings: E03, E04, D01, D04, B04 set to PENDING; C05 set to NO MATCH FOUND (Trump Accounts is a different vehicle from the proposed USAs).
- A few asks are implicit (B10, B11: a critique implies a fix) or retrospective (E09: the report endorses an action already taken); the `Ask` text says so.
- Not examined: endnotes, and the methods of cited studies.

## This is a snapshot, not a verdict

Unlike the Project 2025 folder one level up — which closed out after four correction rounds — most of this report's asks are still in motion (bills pending, rules proposed) rather than settled history. Treat the 2026-10-01 numbers as a dated snapshot to be re-run, not a final tally.
