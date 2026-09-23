# Project 2025 Mapping — Research Progress Checkpoint

**Purpose of this file**: This is a resumability checkpoint, not a finished deliverable. If this work gets interrupted (session ends, usage limit, etc.), a fresh session should read this file first, then `project_2025_mapping.csv`, to see exactly what is done, what is in progress, and what is left — without redoing completed chapters or re-researching from scratch.

**How to resume**: Open `project_2025_mapping.csv`, find the chapters marked `PENDING` below, and continue the same methodology (see "Methodology" section) starting from the first `PENDING` chapter. Update this file's status table and the "Session Log" at the bottom after every batch of chapters completed, then commit + push both files together.

---

## Why this file exists (context for a resuming session)

The original `project_2025_mapping.csv` (v1) only checked Project 2025 chapter directives against events already documented inside this repository's own `_AI_CONTEXT_INDEX/` corpus. That produced a lot of honest "NO REPO MATCH" rows for chapters this repo was never built to track (Education, EPA, HHS, Energy, etc.).

The repo owner then ran independent web-research passes on three of those chapters (Ch.12 Energy, Ch.13 EPA, Ch.14 HHS) and found something the repo-only pass missed: **several Project 2025 directives were attempted, and then blocked, reversed, or left contested by courts/litigation** — not just "implemented" or "no match." That is a third outcome category the original methodology didn't have a slot for. This surfaced a new verification-status value:

- `ATTEMPTED — BLOCKED/REVERSED` — the administration took the action the chapter called for, and a court (or other check) blocked, vacated, enjoined, or reversed it, in whole or part, as of the source's research date.

This file tracks finishing that same web-research pass (methodology below) across the remaining chapters that still show `NO REPO MATCH` in the CSV, so the final CSV has three honest outcome buckets for every chapter: **executed**, **attempted-but-blocked**, or **no corresponding action found even after web research**.

---

## Methodology (apply identically to every remaining chapter)

For each chapter, using the chapter's directive text from `Project_2025_Mandate_for_Leadership_Chapter-by-Chapter_Policy.md` as the target:

1. Web-search for concrete actions taken by the named agency/official matching the directive, dated as precisely as possible.
2. **Explicitly search for the blindspot**: litigation, injunctions, vacaturs, congressional blocks, agency reversals, or walk-backs of any action found in step 1. An implemented policy that was later struck down is not the same as one that stuck — both need their own row.
3. Only include rows backed by identifiable, real sources (outlet name + approximate date). No fabricated citations.
4. Use verification statuses consistent with the existing convention:
   - `VERIFIED` — action confirmed by multiple/credible sources, not currently blocked
   - `ATTEMPTED — BLOCKED/REVERSED` — action taken, then blocked/vacated/enjoined/reversed (cite the court/mechanism)
   - `PARTIALLY VERIFIED` — action or pledge confirmed but outcome/completion is unresolved, forward-looking, or only partially executed
   - `NO REPO MATCH` → for chapters where even web research turns up nothing concrete, relabel as `NO MATCH FOUND (web-researched)` to distinguish "we checked the web and found nothing" from the original pass's "we only checked the repo."
5. Repo_Source_File column for new rows should read: `Ch.N — <Department> (<Author>) [web research — not repo corpus]`, matching the convention already used for Ch.12/13/14.
6. Append new rows to `project_2025_mapping.csv` (do not renumber/reorder existing rows — always append).
7. After finishing a chapter (or a batch), update the status table below and re-run the Python CSV validation (`csv.reader`, check column-count consistency) before committing.

---

## Chapter Status Tracker

| Chapter | Department | Status | Notes |
|---|---|---|---|
| Ch.1 | White House Office | DONE (v1, repo-only, adjacent) | Structural/loyalty chapter; unlikely to have a single discrete event even with web research — left as-is unless a resuming session finds something concrete |
| Ch.2 | Executive Office of the President (OMB) | DONE (v1, repo-only) | Vought/OMB — repo-sourced, adequate |
| Ch.3 | Central Personnel Agencies (Schedule F) | DONE (v1, repo-only) | Strongest match in the repo; no further work needed |
| Ch.4 | Department of Defense | DONE (v1, repo-only) | Hegseth purge covered; DEI/transgender/COVID-discharge sub-items still unmatched — low priority for a re-pass |
| Ch.5 | Department of Homeland Security | DONE (v1, repo-only) | Noem firing + SAVE Act covered |
| Ch.6 | Department of State | DONE (v2, web-researched) | Rubio reorg, ambassador purge, China visa crackdown; treaty-freeze sub-directive only partially matched |
| Ch.7 | Intelligence Community | DONE (v2, web-researched) | ODNI 2.0 downsizing, DEI-role firings upheld in court; EO 12333 revision — no match found |
| Ch.8 | Media Agencies (USAGM/CPB) | DONE (v2, web-researched) | Strong "blocked/reversed" case study: USAGM/VOA shutdown fought through multiple rounds of litigation, still unresolved as of Sep 2026; CPB defunding EO blocked by court on First Amendment grounds but the same goal achieved anyway via a separate congressional rescission (CPB has since shut down) — a distinct "blocked-then-achieved-via-alternate-route" pattern worth flagging in the Hit Rate doc |
| Ch.9 | USAID | DONE (v1, repo-only) | Strong match; no further work needed |
| Ch.10 | Department of Agriculture | DONE (v2, web-researched) | Climate-Smart Commodities canceled; SNAP work-req waiver terminations self-reversed amid litigation; GMO labeling — court forced expansion, opposite of repeal; sugar subsidies increased, opposite of elimination |
| Ch.11 | Department of Education | DONE (v2, web-researched) | High-value batch: ED RIF blocked by district court + 1st Circuit, then unblocked by SCOTUS emergency stay (legality still unresolved); student-loan-to-SBA transfer enjoined; PSLF restriction rule vacated by two district courts; Title I/IDEA block-grant proposals rejected by Congress; Title IX rewrite and school-choice tax credit both verified as implemented |
| Ch.12 | Department of Energy | DONE (v2, web-researched) | Includes a confirmed ATTEMPTED — BLOCKED/REVERSED row (DOE grant terminations ruled unconstitutional) |
| Ch.13 | Environmental Protection Agency | DONE (v2, web-researched) | Endangerment finding repeal executed but under active litigation (unresolved, not yet blocked) |
| Ch.14 | Health and Human Services | DONE (v2, web-researched) | Includes a confirmed ATTEMPTED — BLOCKED/REVERSED row (mifepristone access restriction stayed by SCOTUS) |
| Ch.15 | Housing and Urban Development | DONE (v2, web-researched) | AFFH rule ended (verified); disparate-impact and devolution proposals still in rulemaking/budget-request stage, not final |
| Ch.16 | Department of the Interior | DONE (v2, web-researched) | ANWR leasing reinstated (though zero bids so far) and 30x30 revoked verified; Bears Ears/Grand Staircase monument shrinkage and ESA rollback both facing pending litigation |
| Ch.17 | Department of Justice | DONE (v1, repo-only) | Strong match; no further work needed |
| Ch.18 | Department of Labor | DONE (v2, web-researched) | EO 14173 contractor-DEI rollback and EEOC religious-accommodation reorientation verified; comp-time/Sabbath-mandate legislation never enacted |
| Ch.19 | Department of Transportation | DONE (v2, web-researched) | California EV-waiver revocation via novel CRA use is in contested litigation; FAA privatization directive notably declined by DOT's own Secretary; Jones Act waived-then-narrowed |
| Ch.20 | Department of Veterans Affairs | DONE (v2, web-researched) | Notable self-halt case: VA's Feb 2026 disability-rating rule was suspended by the Secretary within two days after backlash, without being formally rescinded — a third outcome variant beyond "blocked" or "reversed" |
| Ch.21 | Department of Commerce (NOAA) | DONE (v2, web-researched) | Commerce Secretary Lutnick explicitly disavowed Project 2025's NOAA privatization plank at his confirmation hearing even as NOAA/NWS staff cuts proceeded; EDA proposed for elimination twice but Congress kept funding it |
| Ch.22 | Department of the Treasury | DONE (v2, web-researched) | Notable reversal: the enacted "One Big Beautiful Bill Act" kept the existing 7-bracket/21%-corporate-rate structure rather than adopting this chapter's specific two-rate (15%/30%)/18%-corporate proposal — a clear divergence, not just an absence of data. IRS funding rescission and DEI-office closure both verified |
| Ch.23 | Export-Import Bank | DONE (v2, web-researched) | Notable reversal: rather than moving toward abolition (de Rugy's view), the administration has actively expanded EXIM's usage as a China-competition tool (record $10B "Project Vault" loan) — the opposing author's (Hazelton's) "retain it" view is what materialized |
| Ch.24 | Federal Reserve | DONE (v2, web-researched) | High-value blocked/reversed case: Trump's attempted for-cause removal of Fed Governor Lisa Cook was blocked by the Supreme Court 5-4 (Trump v. Cook, Jun 29, 2026); separately, this chapter's own author (Paul Winfree) was hired as new Fed Chair Kevin Warsh's first policy adviser, even though Warsh has publicly distanced himself from the chapter's dual-mandate-elimination proposal |
| Ch.25 | Small Business Administration | DONE (v2, web-researched) | COVID-loan fraud crackdown strongly verified ($22B referred to Treasury); DEI-targeting policy shift verified; disaster-lending-to-private-insurance shift not found (current guidance runs opposite) |
| Ch.26 | Trade | DONE (v1, repo-only) | Section 122/IEEPA covered; could add a web-researched blocked/reversed angle later (low priority) |
| Ch.27 | SEC & CFPB | DONE (v2, web-researched) | Highest-value blocked/reversed case in this whole pass: CFPB shutdown attempt hit a preliminary injunction, a partial D.C. Circuit stay, reinstatement, then the injunction was vacated on appeal in Aug 2025 — then a *separate* Fed-funding-lapse maneuver by Vought was independently blocked by a district court in Dec 2025 (NTEU v. Vought). Agency is "largely inoperable" but not formally abolished; litigation still unresolved. Section 1071 repeal failed in Congress but was achieved administratively via a narrowing rule instead |
| Ch.28 | Federal Communications Commission | DONE (v1, repo-only) | Covered; could add a web-researched Section 230/TikTok-litigation angle later (low priority) |
| Ch.29 | Federal Election Commission | DONE (v2, web-researched) | FEC lost voting quorum entirely (May 2025), achieving the chapter's deregulatory goal by attrition rather than policy; Commissioner Weintraub's disputed removal remains legally unresolved |
| Ch.30 | Federal Trade Commission | DONE (v2, web-researched) | Mixed/contradictory record: FTC's Meta monopolization case was rejected by a federal judge (Nov 2025, on appeal) — a blocked/reversed outcome — while the chapter's "reduce antitrust enforcement generally" directive was NOT followed (Ferguson's FTC kept aggressive merger enforcement) |

**Remaining chapters pending as of this checkpoint: Ch.10, 11, 15, 16, 18, 19, 20, 21, 22, 23, 24, 25, 27, 29, 30 (15 chapters)** — Ch.6/7/8 completed in this pass (see Session Log).

---

## Session Log

- **Session 1** (mapping v1): Built initial repo-only CSV (47 rows), Hit Rate doc, PR #197 opened.
- **Session 2** (mapping v2): User identified the blocked/reversed blindspot and independently web-researched Ch.12, Ch.13, Ch.14 (added rows 49–63). Merged that expanded CSV into the repo copy, added this checkpoint file, and dispatched three parallel background research batches for the remaining PENDING chapters.
- **Session 2, Batch A landed**: Ch.6 (State), Ch.7 (Intelligence Community), Ch.8 (USAGM/CPB) researched and appended (18 new rows, CSV now 80 data rows). Notable finding: Ch.8's CPB defunding EO was blocked by a federal court on First Amendment grounds, but the administration achieved the same goal anyway via a separate $9B congressional rescissions package — CPB has since shut down operations. Batches B (7 domestic-agency chapters) and C (8 economic/regulatory chapters) still running in background as of this log entry.

