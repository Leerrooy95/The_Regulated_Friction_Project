# Node Dossier Index — Modular Context for Event Analysis

**Purpose**: This index enables AI assistants to selectively load relevant historical context when analyzing new friction or compliance events. Instead of reading one massive file, the AI should identify matching entities and pull only the specific dossiers needed for that analysis.

**Last Updated**: March 16, 2026 | **Parent**: `_AI_CONTEXT_INDEX/`

---

## How to Use This Index

When analyzing a new event:

1. **Identify entities** mentioned in the event (people, organizations, locations, funds)
2. **Match to dossiers** below using the "Trigger Entities" column
3. **Load only relevant files** for contextual analysis
4. **Apply the Tier 3 ruleset** to assess timing significance

**Example**: If analyzing a news item about "Kushner" and "Saudi Arabia," load:
- `tier1_kushner_historical.md` (background context)
- `tier2_affinity_qxo.md` (current capital exposure)
- `tier2_sovereign_wealth_movers.md` (PIF positioning)
- `tier3_thermostat_ruleset.md` (timing analysis rules)

---

## Tier Structure

| Tier | Name | Function | When to Load |
|------|------|----------|--------------|
| **Tier 1** | Historical Friction Nodes | Established precedent and background | When analyzing events involving named historical actors or locations |
| **Tier 2** | Active Capital Nodes | Current financial positioning (2025-2026) | When analyzing capital movements, deals, or entity positioning |
| **Tier 3** | Geopolitical Thermostat | Analysis ruleset | Always load for timing analysis |

---

## Tier 1: Historical Friction Nodes (The Precedent)

These dossiers document historical context that may become relevant when matching entities appear in new events. Load these for deep background.

| Dossier | File | Trigger Entities | Summary |
|---------|------|------------------|---------|
| **Zorro Ranch / Epstein Architecture** | `tier1_zorro_ranch_epstein.md` | Epstein, Zorro Ranch, San Rafael Ranch, New Mexico, Huffines, DOJ files, document releases | Documents the 1993 purchase, 2023 sale to Huffines family, renaming, and active Feb 2026 investigations. Provides context for ongoing file releases. |
| **Kushner Historical Node** | `tier1_kushner_historical.md` | Charles Kushner, Jared Kushner, pardon, Kushner Companies, 666 Fifth Avenue, France diplomatic crisis, ambassador summons, Jean-Noël Barrot | Documents the Kushner family's business history, Charles Kushner's 2005 conviction and 2020 pardon, the foundation of the family's real estate and political capital, and the 2025-2026 France diplomatic crisis (2 ignored summons, barred from ministerial access). |
| **Maxwell Leverage Node** | `tier1_maxwell_leverage.md` | Maxwell, Ghislaine, clemency, VOCA, trafficking funds, administrative pincer, survivor infrastructure, Epstein network, FPC Bryan, House Oversight | Documents Maxwell's Phase 0 infrastructure role (1991–2003), current leverage position (clemency negotiation, habeas petition, 5th Amendment invocation), and the Administrative Pincer mechanism (VOCA funding freeze in Epstein infrastructure states). |
| **Bin Sulayem / Epstein Connection** | `tier1_binsulayem_epstein.md` | bin Sulayem, DP World, Epstein, Great St. James, UAE | Documents 4,700+ mentions in Epstein files, Feb 2026 resignation, and network connections. |

---

## Tier 2: Active Capital Nodes (The Present)

These dossiers document current financial positioning that the dashboard tracks in real-time. Load these when analyzing capital movements.

| Dossier | File | Trigger Entities | Summary |
|---------|------|------------------|---------|
| **Affinity Partners & QXO** | `tier2_affinity_qxo.md` | Affinity Partners, Kushner, QXO, Apollo, Marc Rowan, Beacon Roofing, Phoenix Holdings | Documents Jared Kushner's $3B Apollo credit exposure, QXO as sole 13F holding, and the governance-financing pipeline through Board of Peace. |
| **Sovereign Wealth Movers** | `tier2_sovereign_wealth_movers.md` | PIF, Mubadala, Saudi Arabia, UAE, sovereign wealth fund, SWF, 13F, Bitcoin ETF, GlobalFoundries | Documents Q4 2025/Q1 2026 movements of Saudi PIF and Mubadala, including defense exits, Bitcoin accumulation, and gaming consolidation. |
| **Egypt-Gulf Integration** | `tier2_egypt_gulf_integration.md` | Egypt, Sisi, Ras El-Hekma, ADQ, Cairo, Suez | Documents Egypt's financial integration with Gulf SWFs as geographic bridge between Gulf capital and Mediterranean. |
| **UAE Coordination Node** | `tier2_uae_coordination_node.md` | UAE, Abu Dhabi, Russia-Ukraine talks, BRICS, mBridge, OPEC+, Kushner, Witkoff, Board of Peace | Documents UAE's function as multi-track coordination node: Russia-Ukraine negotiation venue + BRICS member + mBridge participant + OPEC+ coordination with Russia + US diplomatic operations via Kushner/Witkoff. |
| **Entity Leadership Profiles** | `tier2_entity_leadership_profiles.md` | SoftBank, Masayoshi Son, Vision Fund, Saudi PIF, Yasir Al-Rumayyan, Mubadala, Khaldoon Al Mubarak, MGX, Sheikh Tahnoon, 1789 Capital, Omeed Malik, Stargate | Verified leadership structure of entities in capital architecture: SoftBank Group, Saudi PIF, UAE Mubadala, UAE MGX, and 1789 Capital. Board interlocking, capital flow authority, and royal family governance. |
| **Religious Infrastructure** | `tier2_religious_infrastructure.md` | Paula White, Dan Patrick, Ralph Drollinger, Capitol Ministries, Doug Wilson, CREC, CUFI, John Hagee, Pete Hegseth (theological context), White House Faith Office, Religious Liberty Commission, Christian Zionism, eschatology, NAR, Carrie Prejean Boller, Candace Owens (enforcement boundary) | Documents the eschatological policy pipeline: four theological input channels (White House Faith Office, Capitol Ministries weekly Bible study, CREC/Pentagon worship, CUFI lobbying), Hegseth as convergence node, enforcement mechanism (Corporate → Government → Intelligence escalation), denominational fault line, and Vought personnel overlap. |
| **Purged Officials** | `tier2_purged_officials.md` | Bongino, Noem, Bondi, Randy George, David Hodne, William Green Jr., fired, removed, purged, second-term removals, acting AG, acting CSA, wartime firing | Running log of cabinet, military, and senior officials removed during Trump's second term. Documents friction-adjacency pattern, replacement logic (loyalty over seniority), and wartime precedents. Includes Bongino (Dec 2025), Noem (Mar 5), Bondi (Apr 2), and the three-general April 2 purge. |

---

## Tier 3: Geopolitical Thermostat (The Ruleset)

This is the master logic file. Load this for any timing analysis.

| Dossier | File | Trigger Conditions | Summary |
|---------|------|-------------------|---------|
| **Thermostat Ruleset** | `tier3_thermostat_ruleset.md` | Any event timing analysis, calendar windows, convergence detection | Defines the 7-day median lag pattern (r = 0.6196 at 2-week index resolution), calendar anchor signals, and convergence detection rules. Use this to assess whether an event falls within a statistically significant window. |

---

## Quick Reference: Entity → Dossier Mapping

| Entity | Load These Dossiers |
|--------|---------------------|
| Epstein / DOJ files | `tier1_zorro_ranch_epstein.md`, `tier1_binsulayem_epstein.md`, `tier1_maxwell_leverage.md`, `tier3_thermostat_ruleset.md` |
| Kushner (Jared) | `tier1_kushner_historical.md`, `tier2_affinity_qxo.md`, `tier3_thermostat_ruleset.md` |
| Kushner (Charles) | `tier1_kushner_historical.md` |
| France diplomatic crisis / ambassador summons | `tier1_kushner_historical.md` |
| Apollo / Marc Rowan | `tier2_affinity_qxo.md`, `tier3_thermostat_ruleset.md` |
| QXO / Beacon | `tier2_affinity_qxo.md`, `tier3_thermostat_ruleset.md` |
| Saudi PIF | `tier2_sovereign_wealth_movers.md`, `tier2_entity_leadership_profiles.md`, `tier3_thermostat_ruleset.md` |
| Mubadala / UAE | `tier2_sovereign_wealth_movers.md`, `tier2_entity_leadership_profiles.md`, `tier3_thermostat_ruleset.md` |
| New Mexico / Zorro Ranch | `tier1_zorro_ranch_epstein.md`, `tier1_maxwell_leverage.md` |
| Maxwell / Ghislaine / clemency | `tier1_maxwell_leverage.md`, `tier1_zorro_ranch_epstein.md`, `tier3_thermostat_ruleset.md` |
| VOCA / trafficking funds / survivor infrastructure | `tier1_maxwell_leverage.md` |
| Administrative pincer / impunity | `tier1_maxwell_leverage.md` |
| Board of Peace | `tier2_affinity_qxo.md`, `tier2_sovereign_wealth_movers.md`, `tier3_thermostat_ruleset.md` |
| Bin Sulayem / DP World | `tier1_binsulayem_epstein.md`, `tier3_thermostat_ruleset.md` |
| Great St. James Island | `tier1_binsulayem_epstein.md`, `tier1_zorro_ranch_epstein.md` |
| Egypt / Sisi / Ras El-Hekma | `tier2_egypt_gulf_integration.md`, `tier2_sovereign_wealth_movers.md`, `tier3_thermostat_ruleset.md` |
| UAE diplomatic venue / Abu Dhabi talks | `tier2_uae_coordination_node.md`, `tier2_sovereign_wealth_movers.md`, `tier3_thermostat_ruleset.md` |
| Russia-Ukraine negotiations | `tier2_uae_coordination_node.md`, `tier3_thermostat_ruleset.md` |
| BRICS / mBridge | `tier2_uae_coordination_node.md`, `tier2_sovereign_wealth_movers.md` |
| OPEC+ Russia coordination | `tier2_uae_coordination_node.md` |
| Iran cyber operations / Handala / Clalit | `sources/2026-02-28_Cyber_Kinetic_Timeline_Analysis.md`, `tier3_thermostat_ruleset.md` |
| Operation Robert / Trump emails hack | `sources/2026-02-28_Cyber_Kinetic_Timeline_Analysis.md` |
| Cyber-kinetic sequencing / timeline analysis | `sources/2026-02-28_Cyber_Kinetic_Timeline_Analysis.md`, `tier3_thermostat_ruleset.md` |
| Bennett phone hack / Operation Octopus | `sources/2026-02-28_Cyber_Kinetic_Timeline_Analysis.md` |
| Nahal Soreq / nuclear data breach | `sources/2026-02-28_Cyber_Kinetic_Timeline_Analysis.md` |
| SoftBank / Masayoshi Son / Vision Fund | `tier2_entity_leadership_profiles.md`, `tier2_sovereign_wealth_movers.md`, `tier3_thermostat_ruleset.md` |
| MGX / Sheikh Tahnoon | `tier2_entity_leadership_profiles.md`, `tier2_uae_coordination_node.md`, `tier3_thermostat_ruleset.md` |
| Stargate Project | `tier2_entity_leadership_profiles.md`, `tier2_uae_coordination_node.md` |
| Yasir Al-Rumayyan | `tier2_entity_leadership_profiles.md`, `tier2_sovereign_wealth_movers.md` |
| Khaldoon Al Mubarak | `tier2_entity_leadership_profiles.md`, `tier2_uae_coordination_node.md` |
| 1789 Capital / Omeed Malik | `tier2_entity_leadership_profiles.md`, `02_MEDIA_FIREWALL.md` |
| Paula White / White House Faith Office | `tier2_religious_infrastructure.md`, `09_CURRENT_THREADS.md` (Node 10) |
| Ralph Drollinger / Capitol Ministries | `tier2_religious_infrastructure.md` |
| Doug Wilson / CREC / Pilgrim Hill | `tier2_religious_infrastructure.md` |
| CUFI / John Hagee / Christian Zionism | `tier2_religious_infrastructure.md` |
| Dan Patrick / Religious Liberty Commission | `tier2_religious_infrastructure.md` |
| Pete Hegseth (theological context) | `tier2_religious_infrastructure.md`, `09_CURRENT_THREADS.md` (Node 10) |
| Carrie Prejean Boller / enforcement boundary | `tier2_religious_infrastructure.md` |
| Russell Vought (theological overlap) | `tier2_religious_infrastructure.md` |
| New Apostolic Reformation (NAR) | `tier2_religious_infrastructure.md` |
| Eschatological infrastructure / denominational fault line | `tier2_religious_infrastructure.md`, `15_The_Religious_Layer/The_Religious_Layer.md` |
| Purged officials / fired officials / second-term removals | `tier2_purged_officials.md` |
| Pam Bondi / acting AG Todd Blanche | `tier2_purged_officials.md`, `09_CURRENT_THREADS.md` (Node 5, March/April 2026 Events) |
| Gen. Randy George / Army CSA removed | `tier2_purged_officials.md`, `09_CURRENT_THREADS.md` (Node 2) |
| Gen. David Hodne / Maj. Gen. William Green Jr. | `tier2_purged_officials.md`, `09_CURRENT_THREADS.md` (Node 2) |
| Dan Bongino / FBI Deputy Director / Dec 17 resignation | `tier2_purged_officials.md`, `06_ATTENTION_ECONOMY.md` |
| Kristi Noem / DHS firing / Special Envoy | `tier2_purged_officials.md`, `09_CURRENT_THREADS.md` (DHS Shutdown section) |

---

## Integration with Main Context Index

This Node Dossier system is a **supplement** to the main `_AI_CONTEXT_INDEX/` files:

- For **methodology and statistics**: Continue using `07_METHODOLOGY.md`
- For **current research threads**: Continue using `09_CURRENT_THREADS.md`
- For **full capital architecture**: Continue using `04_CAPITAL_ARCHITECTURE.md`
- For **religious/eschatological infrastructure**: Use `tier2_religious_infrastructure.md` or `15_The_Religious_Layer/`
- For **historical friction context**: Use Node Dossiers

The Node Dossiers are designed for **targeted loading** when specific entities appear, rather than comprehensive background reading.

---

## Analytical Standards

All Node Dossiers follow these standards:

1. **Verification levels**: ✅ VERIFIED, ⚠️ PARTIALLY VERIFIED, 🔍 HYPOTHESIS
2. **Source citations**: All factual claims cite sources
3. **No conspiracy claims**: Pattern documentation, not coordination claims
4. **Structural interpretation**: The pattern exists; causation is not claimed
5. **Negative findings documented**: Failed predictions and absence of evidence are reported

---

*This modular architecture enables efficient context loading without reading the entire repository.*
