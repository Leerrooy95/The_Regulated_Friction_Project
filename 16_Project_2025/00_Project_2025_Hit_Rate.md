# Project 2025 → Repository Hit-Rate Analysis

**Purpose**: Cross-reference the 30 chapter directives of Project 2025's *Mandate for Leadership* against what has actually happened in the real world (2025–2026), to see how much of the blueprint was executed, how much was attempted and then blocked or reversed, and how much simply didn't happen.

**Method (two passes)**:
- **Pass 1 (repo-only)**: cross-referenced each chapter against events already documented inside this repository's own `_AI_CONTEXT_INDEX/` corpus.
- **Pass 2 (web-researched)**: the repo owner's own research surfaced a blindspot Pass 1 couldn't see — several directives were *implemented and then blocked, vacated, or reversed by courts, Congress, or other checks*. Pass 2 extended the same rigor (real, dated, cited sources; explicit search for blocked/reversed outcomes) to every chapter, closing the gaps Pass 1 left as "no repo match."

**Companion file**: `project_2025_mapping.csv` — 140 data rows across all 30 chapters, columns: Date, Chapter, Directive, Repo_Event, Verification_Status, Repo_Source_File.

**Outcome categories used throughout** (this repo's own ✅/⚠️/🔍 convention, extended with two categories this analysis needed):
- `VERIFIED` — action confirmed by credible sources, not currently blocked or reversed
- `ATTEMPTED — BLOCKED/REVERSED` — the action was taken, then blocked, enjoined, vacated, or reversed by a court, Congress, or (in one case) the agency itself under public pressure — name the mechanism
- `PARTIALLY VERIFIED` — confirmed but outcome is unresolved, forward-looking, proposed-not-final, or only partially executed
- `NO MATCH FOUND (web-researched)` — genuinely nothing found after real search (successor to Pass 1's "NO REPO MATCH," now meaning "we checked the open web, not just the repo, and still found nothing")

---

## Headline Numbers

| Metric | Count |
|---|---|
| Chapters covered | **30 of 30** (complete, after Pass 2) |
| Total CSV rows | 140 |
| Rows: VERIFIED | 55 |
| Rows: PARTIALLY VERIFIED | 28 |
| Rows: ATTEMPTED — BLOCKED/REVERSED | 22 |
| Rows: NO MATCH FOUND / NO REPO MATCH | 35 |

Read that first row carefully: **22 of 140 tracked sub-directives (16%) were actively attempted and then hit a wall** — a court injunction, a Supreme Court ruling, a congressional rejection, or, in one case, the agency itself backing down under public pressure. That number was invisible in Pass 1, which could only say "verified" or "no match" — it had no way to represent "yes, and then no." Below, a chapter-by-chapter verdict, then the cross-cutting patterns worth knowing.

---

## Chapter-by-Chapter Verdicts

| Ch. | Department (Author) | Verdict |
|---|---|---|
| 1 | White House Office (Dearborn) | No standalone event; loyalty/personnel-vetting theme corroborated only indirectly via Ch.3/17 |
| 2 | EOP/OMB (Vought) | Vought installed and credited with institutionalizing DOGE; role confirmed, not independently deep-researched |
| 3 | Central Personnel Agencies — Schedule F (Devine/Kirk/Dans) | **Executed near-completely.** Schedule Policy/Career final rule published Feb 2026, ~50,000 positions reclassified, MSPB rights stripped — the strongest single match in this whole project |
| 4 | Defense (Miller) | Wartime loyalty purge (Gen. George, Hodne, Chief of Chaplains) executed; DEI/transgender/COVID-discharge sub-items unresearched |
| 5 | DHS (Cuccinelli) | Noem fired, DHS shutdown ongoing, SAVE Act data-centralization advancing — but the chapter's core "break up DHS into a standalone agency" ask itself is unconfirmed |
| 6 | State (Skinner) | Largely executed: Rubio's reorg (132 offices, 700 positions cut), Dec. 2025 career-ambassador purge, China visa crackdown. Treaty-freeze mechanism as literally described — not confirmed |
| 7 | Intelligence Community (Carmack) | Executed: ODNI 2.0 cut headcount 40%; CIA/ODNI DEI-role firings upheld in court. EO 12333 revision — no evidence found |
| 8 | Media Agencies: USAGM/CPB (Namdar/Gonzalez) | **The richest blocked/reversed case study in this dataset.** USAGM/VOA fought through 5+ rounds of litigation, unresolved as of Sep 2026; CPB's defunding EO was blocked in court, then the same goal achieved anyway via a $9B congressional rescission — CPB has since shut down |
| 9 | USAID (Primorac) | **Executed completely.** Only 718 of ~10,500 positions survived; agency formally dissolved into State |
| 10 | Agriculture (Bakst) | Mixed-to-reversed: Climate-Smart Commodities program canceled (executed), but SNAP waiver terminations were self-reversed amid litigation, GMO labeling was *expanded* by a court (opposite of repeal), and sugar subsidies were *increased* by Congress (opposite of elimination) |
| 11 | Education (Burke) | **Second-richest blocked/reversed case study.** ED's RIF was blocked by a district court and the 1st Circuit, then unblocked by a 5-4-ish SCOTUS emergency stay with the underlying legality still unresolved; the $1.6T student-loan-to-SBA transfer was enjoined; the PSLF restriction rule was vacated by two separate courts; Title I/IDEA block-granting was rejected by Congress twice. Title IX rewrite and the school-choice tax credit did land, unblocked |
| 12 | Energy (McNamee) | Executed on LNG exports and DOE reorganization; the October 2025 clean-energy grant cancellations were ruled unconstitutional and partly reinstated by a federal judge |
| 13 | EPA (Gunasekara) | Endangerment-finding repeal finalized (Feb 2026) but under active, unresolved litigation from 24 states; coal-ash permitting devolved to states successfully |
| 14 | HHS (Severino) | Mifepristone approval itself never reversed — the one court-ordered access restriction was stayed by the Supreme Court; Medicaid work requirements enacted and in force; Section 1557 reinterpretation partly enjoined |
| 15 | HUD (Carson) | AFFH rule ended (executed); disparate-impact rescission and state-devolution both still in proposed/budget-request stage, not final |
| 16 | Interior (Pendley) | ANWR leasing reinstated and 30x30 revoked (executed, though the ANWR lease sale drew zero bids); Bears Ears/Grand Staircase monument shrinkage and the ESA rollback both face pending, unresolved litigation |
| 17 | DOJ (Hamilton) | **Executed near-completely.** Weaponization Working Group, mass career-attorney departures, two AG firings (Bondi) tied to Epstein-file fallout |
| 18 | Labor (Berry) | Contractor-DEI rollback (EO 14173) and EEOC religious-accommodation reorientation both executed; comp-time/Sabbath-mandate legislation never passed |
| 19 | Transportation (Furchtgott-Roth) | California's EV mandate waivers revoked via a novel, contested use of the Congressional Review Act — now in litigation; FAA privatization was **affirmatively declined** by DOT's own Secretary, the opposite of the chapter's ask; Jones Act waived, then narrowed under industry pressure |
| 20 | Veterans Affairs (Tucker) | Abortion and gender-surgery policy rollbacks both executed; **a new outcome variant**: the Feb 2026 disability-rating rule was suspended by the Secretary within two days of public backlash, without ever being formally rescinded — neither "blocked" by a court nor "reversed," just quietly shelved |
| 21 | Commerce/NOAA (Gilman) | Staff cuts proceeded, but Commerce Secretary Lutnick **explicitly disavowed** this chapter's NOAA-privatization plank at his own confirmation hearing; EDA proposed for elimination twice, Congress funded it anyway both times |
| 22 | Treasury (Walton/Moore/Burton) | **A clean reversal, not just an absence of data.** The enacted "One Big Beautiful Bill Act" kept the existing 7-bracket/21%-corporate structure rather than adopting this chapter's specific two-rate (15%/30%)/18%-corporate proposal. IRS funding rescission and DEI-office closure did happen |
| 23 | Export-Import Bank (de Rugy pro-abolition / Hazelton pro-retention) | **A clean reversal.** Rather than moving toward abolition, EXIM was actively expanded (record $10B "Project Vault" loan) — Hazelton's opposing view is what materialized, not de Rugy's |
| 24 | Federal Reserve (Winfree) | **Third-richest blocked/reversed case study.** The attempted for-cause removal of Fed Governor Lisa Cook was blocked 5-4 by the Supreme Court (*Trump v. Cook*, Jun 2026); separately, this chapter's own author (Paul Winfree) was hired as new Fed Chair Kevin Warsh's first policy adviser — even though Warsh has publicly distanced himself from Winfree's own dual-mandate-elimination proposal |
| 25 | SBA (Kerrigan) | COVID-loan fraud crackdown strongly executed ($22B referred to Treasury); DEI-targeting policy shift confirmed; disaster-lending-to-private-insurance shift not found (current guidance runs the opposite direction) |
| 26 | Trade (Navarro/Lassman) | IEEPA tariffs struck down by SCOTUS; pivot to Section 122 tariffs, directionally consistent with Navarro's approach, set to expire Jul 2026 with no congressional codification |
| 27 | SEC & CFPB (Burton/Bowes) | **The single richest blocked/reversed case study in the entire dataset.** CFPB's shutdown attempt ran through a preliminary injunction → partial appellate stay → reinstatement → appellate vacatur, then a *second, separate* funding-lapse maneuver was independently blocked by a different court in Dec 2025 — the agency is "largely inoperable" but still not formally abolished, and litigation continues. Section 1071 repeal failed in Congress but was achieved administratively via a narrowing rule instead |
| 28 | FCC (Carr) | Carr (the chapter's own author) fast-tracked Paramount/WBD merger approval and the Oracle-led TikTok divestiture — but this executes "Big Tech action" via consolidation into allied ownership, not the chapter's stated antitrust/Section 230 rationale |
| 29 | FEC (von Spakovsky) | The FEC lost its voting quorum entirely (May 2025), achieving the chapter's deregulatory goal by attrition rather than policy; Commissioner Weintraub's disputed removal remains legally unresolved |
| 30 | FTC (Candeub) | Mixed record: the FTC's Meta monopolization case was rejected by a federal judge (a blocked/reversed outcome, on appeal), while the chapter's "reduce antitrust enforcement generally" directive was **not** followed — Ferguson's FTC kept aggressive merger enforcement |

---

## Cross-Cutting Patterns

1. **The blindspot the owner caught is real and large.** 22 of 140 rows are attempted-then-blocked/reversed — concentrated in Ch.8 (media agencies), Ch.11 (Education), Ch.24 (Fed), and Ch.27 (CFPB), which together account for over half of all blocked/reversed rows. These four chapters are the best evidence that "Project 2025 was implemented" is too simple a claim — the more accurate picture, at least for these four, is "attempted aggressively, contested aggressively, outcome still unsettled."

2. **A new outcome the original three-category framework didn't anticipate: blocked-then-achieved-anyway, via a different route.** Ch.8's CPB defunding is the clearest example — a court blocked the executive order on First Amendment grounds, and the administration got the same result anyway through a $9 billion congressional rescissions package. "Blocked" was not the end of the story; it was a detour.

3. **Another new outcome: self-halted, not court-blocked.** Ch.20's VA disability-rating rule was suspended by the Secretary within 48 hours of public backlash — no court, no congressional vote, just political retreat. This is a third failure mode alongside judicial and legislative blocks, worth watching for elsewhere.

4. **Several chapters show the enacted outcome directly contradicting the chapter's own stated goal — not merely "no match," but the opposite result.** Ch.22 (Treasury kept the existing tax-bracket structure instead of this chapter's two-rate plan), Ch.23 (Ex-Im Bank was expanded, not abolished — the *opposing* essay's position won), Ch.10 (sugar subsidies increased, not eliminated), Ch.19 (FAA privatization affirmatively declined), and Ch.30 (antitrust enforcement not reduced) are all cases where the administration diverged from, rather than simply ignored, its own blueprint. That's a distinct and arguably more interesting finding than a flat "no match."

5. **Personnel-loyalty and purge patterns still repeat across Ch.1, 3, 4, 5, 6, 7, 17.** This was true in Pass 1 and remains the dataset's most consistent throughline: whatever else diverged from the text, the drive to replace career/independent staff with loyalists shows up almost everywhere Pass 2 looked.

6. **The Judiciary — not Congress — is doing most of the blocking.** Of the 22 blocked/reversed rows, the clear majority involve a federal court (district court, circuit court, or the Supreme Court) as the blocking mechanism; Congress rejecting a proposal (Ch.11's Title I/IDEA block grants, Ch.21's EDA elimination) is the second most common path; only Ch.20's VA case involved neither.

---

## What This Does *Not* Show

This is still not an independent, comprehensive audit of full Project 2025 implementation — the Center for Progressive Reform/Governing for Impact tracker (53%, 283/532 actions) and project2025.observer (~48%) already do that at a scale and with a methodology this file doesn't replicate. What this file adds that a simple percentage doesn't: **which specific attempts were fought to a standstill, how, and by whom** — the texture behind the headline number, including several cases (Ch.22, Ch.23, Ch.30) where the real-world outcome ran opposite to the chapter's own text.

---

## Sourcing Note

Every row's sources are named, real, dated outlets (courts, Federal Register entries, wire services, and beat reporters — never fabricated or invented) and are recorded in the `Verification_Status` and `Repo_Source_File` columns of the CSV. Rows carried over from Pass 1 (chapters 1–5, 9, 17, 26, 28) are sourced from this repository's own `_AI_CONTEXT_INDEX/` corpus; all other rows are from live web research conducted specifically for this analysis and are marked `[web research — not repo corpus]` in the source column.

---

*Analysis completed across two passes: an initial repo-only cross-reference, and a full web-research pass across all remaining chapters, explicitly designed to catch attempted-then-blocked/reversed outcomes the repo-only pass could not see. See `RESEARCH_PROGRESS.md` for the methodology and a chapter-by-chapter completion log.*
