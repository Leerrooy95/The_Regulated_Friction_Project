# Node Dossier Index — Modular Context for Event Analysis

**Purpose**: This index enables AI assistants to selectively load relevant historical context when analyzing new friction or compliance events. Instead of reading one massive file, the AI should identify matching entities and pull only the specific dossiers needed for that analysis.

**Last Updated**: March 1, 2026 | **Parent**: `_AI_CONTEXT_INDEX/`

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
| Epstein / DOJ files | `tier1_zorro_ranch_epstein.md`, `tier1_binsulayem_epstein.md`, `tier3_thermostat_ruleset.md` |
| Kushner (Jared) | `tier1_kushner_historical.md`, `tier2_affinity_qxo.md`, `tier3_thermostat_ruleset.md` |
| Kushner (Charles) | `tier1_kushner_historical.md` |
| France diplomatic crisis / ambassador summons | `tier1_kushner_historical.md` |
| Apollo / Marc Rowan | `tier2_affinity_qxo.md`, `tier3_thermostat_ruleset.md` |
| QXO / Beacon | `tier2_affinity_qxo.md`, `tier3_thermostat_ruleset.md` |
| Saudi PIF | `tier2_sovereign_wealth_movers.md`, `tier2_entity_leadership_profiles.md`, `tier3_thermostat_ruleset.md` |
| Mubadala / UAE | `tier2_sovereign_wealth_movers.md`, `tier2_entity_leadership_profiles.md`, `tier3_thermostat_ruleset.md` |
| New Mexico / Zorro Ranch | `tier1_zorro_ranch_epstein.md` |
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

---

## Integration with Main Context Index

This Node Dossier system is a **supplement** to the main `_AI_CONTEXT_INDEX/` files:

- For **methodology and statistics**: Continue using `07_METHODOLOGY.md`
- For **current research threads**: Continue using `09_CURRENT_THREADS.md`
- For **full capital architecture**: Continue using `04_CAPITAL_ARCHITECTURE.md`
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
