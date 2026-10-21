---
title: "GHG data by country tier"
---

:::{tip} Summary
The emissions data for each country follow its {term}`tier <Country tier>`: a detailed facility- and inventory-based model for the U.S., national sources for the four Tier 1 countries, the FIGARO or ICIO emissions data for Tier 2, and a scaled template for Tier 3. Within Tier 2, the detail available differs by source.
:::

:::{note} Draft
:class: dropdown
**Key visuals to add:** world map colored by GHG data source; timeline of emissions data years.
:::

## What each tier starts from

| {term}`Country tier` | Countries | Emissions source | Data year | Gas detail |
|---|---|---|---|---|
| Tier 0 | United States | National GHG inventory, placed on industries with facility, energy, and economic data | 2024 | All 7 gases |
| Tier 1 | China, Japan, South Korea, United Kingdom | National sources for each country | 2018–2023 | All 7 gases, with gaps filled for South Korea |
| Tier 2, FIGARO | 40 countries | FIGARO emissions data from Eurostat | 2023 | 6 gas groups |
| Tier 2, ICIO | 20 countries | OECD emissions data matched to the ICIO tables | 2020 | Total CO₂e only |
| Tier 3 | 83 countries | A template scaled to each country's fossil CO₂ per unit of GDP from {term}`EDGAR` | 2018 | CO₂, with other gases from U.S. ratios |
| Rest of world | | Pooled from four Tier 2 countries | 2020–2023 | As for those countries |

## Tier 0: The U.S. GHG model

The U.S. has the most detailed emissions data, and its model is built on all 405 common sectors.

**National totals.** The U.S. greenhouse gas inventory sets the national totals for 2024, by emitting activity and gas. These come from the University of Maryland's GHG inventory analysis, which follows the tables of EPA's *Inventory of U.S. Greenhouse Gas Emissions and Sinks*, with detail from EPA's inventory for 2023 where it is needed (for example, agricultural soils and fluorinated gases). The inventory is on a {term}`territorial basis <Territorial basis>`.

**Placing the totals on industries.** The inventory names an industry for some emissions and not others, so each emitting activity is placed on industries by one of these routes:

- **Directly.** Where the inventory names the industry, as for most process and fugitive emissions (petroleum and natural gas systems, cement, and other industrial processes), the emissions go to that industry.
- **Facility reports.** Most fuel burned at industrial plants is placed using what the plants themselves report: emissions reported to EPA's {term}`GHGRP`, and to the National Emissions Inventory, matched to one record per site. Power plants come from EPA's eGRID for 2024. For manufacturing natural gas, coal, and petroleum fuels, each industry's share comes from facility reports where they cover at least 80% of the industry's combustion, and from the Manufacturing Energy Consumption Survey (2022) where they don't.
- **Physical fuel use.** Fuel burned in vehicles and equipment is placed on the industries that use it, based on fuel volumes. Highway fuel is split by vehicle owner using Federal Highway Administration data for 2024, with federal fleets from GSA's Federal Fleet Report and private trucks by business type from the Census Bureau's Vehicle Inventory and Use Survey (2021). Industrial diesel is split across agriculture, construction, mining, and manufacturing from fuel sales and survey data.
- **Purchases.** The remaining emissions are allocated to the industries that buy the relevant fuel or product, in proportion to their purchases in the U.S. Use table.

**Households.** Emissions the inventory places in homes and personal vehicles go to households and are not in `B` (see [](index.md)).

## Tier 1: National sources

Each Tier 1 country's emissions come from its own national data.

| Country | Source | Data year | Sectors |
|---|---|---|---|
| China | Built from several sources (see below) | 2023 | 211, matching the IO table |
| Japan | Environmental data published with the Input-Output Tables for Japan | 2020 | Matching the IO table |
| South Korea | GHG data published with the Bank of Korea input-output tables | 2018 | Matching the IO table |
| United Kingdom | ONS atmospheric emissions accounts | 2023 | By industry |

China's data are on a territorial basis, and the UK's on a residence basis.

**China** has no published emissions table matching its IO table, so we build one:

- CO₂ from fossil fuels and cement sets the totals, from Our World in Data, and is placed on sectors by each sector's physical fuel use from China's national energy statistics.
- Power-sector CO₂ is set to match China's official 2023 grid emission factor.
- CH₄ and N₂O come from the Community Emissions Data System ({term}`CEDS`), and farm CH₄ and N₂O from China's first Biennial Transparency Report.
- Fluorinated gases come from China's first Biennial Transparency Report, brought forward to 2023 with {term}`EDGAR` trends.

Household fuel use is not separated in China's national totals, so its CO₂ is spread over the industries rather than left out.

**South Korea's** source covers six gases. The missing gas (NF₃) is estimated from the sector's CO₂ using the U.S. ratio.

Each country's emissions are then mapped to the common sectors with {term}`structural reflection <Structural reflection>`, the same as its IO table. Each national total is kept.

## Tier 2: FIGARO and ICIO emissions data

Tier 2 countries take their emissions from the same source as their IO table, so emissions and output line up sector by sector. The two sources differ a lot in detail.

|  | FIGARO | ICIO |
|---|---|---|
| Publisher | Eurostat | OECD |
| Version | 2026 | 2025 |
| Data year | 2023 | 2020 |
| Sectors | 64 industries (NACE Rev. 2) | 50 industries (ISIC Rev. 4) |
| Gases | CO₂, CH₄, N₂O, HFCs, PFCs, and SF₆ with NF₃ | Total CO₂e only |
| GWPs in source | AR5 | AR5 |
| Basis | Residence | Residence |

### FIGARO countries

FIGARO emissions come from two kinds of underlying data:

- **Air emissions accounts (30 countries).** The 27 EU member states report emissions by industry in their air emissions accounts. For Norway, Switzerland, and Türkiye, Eurostat fills in the industry split.
- **EDGAR estimates (10 countries).** For Argentina, Australia, Brazil, Canada, India, Indonesia, Mexico, Russia, Saudi Arabia, and South Africa, Eurostat estimates emissions by industry from {term}`EDGAR`. EDGAR groups some activities together, so we correct the split. Within mining, refining, and the power and gas utilities, CO₂, CH₄, and N₂O are re-split using {term}`CEDS` shares, holding the combined total fixed. Shares for steel, chemicals, and non-metallic minerals are also reset to CEDS, and process CO₂ is kept off trade and service industries.

For both groups, FIGARO's industries are first converted to products using FIGARO's supply table, to match the product-by-product IO table. The same broad sectors split in the IO table are split here too:

- Electricity, gas, and heat are separated using Eurostat energy balances and CEDS gas distribution methane.
- Agriculture is split into farm sectors using FAOSTAT CH₄ and N₂O and Eurostat agricultural accounts.
- Mining, non-metallic minerals, and basic metals are split as in the IO table.

The products are then mapped to the common sectors with {term}`ABSR`. The last gas group, SF₆ with NF₃, is split using the U.S. share of SF₆ in each sector.

### ICIO countries

The OECD data give one CO₂e total for each of the 50 industries, with no split by gas. Farming is split out first, using FAOSTAT CH₄ and N₂O, before the totals are mapped to the common sectors with ABSR. The split by gas comes entirely from the U.S. mix for each sector. Electricity is mapped as one sector, with no separate split for gas and heat.

## Tier 3: Template emissions

Tier 3 countries have no emissions data matched to an IO table. Their direct emission intensities start from the same template as their input recipe, a blend of Mexico (30%), Malaysia (30%), and Tunisia (40%). The template uses those countries' CO₂ emissions by industry for 2018, from the OECD's 2021 edition of CO₂ emissions embodied in international trade. Other gases are added using the U.S. ratio of total CO₂e to CO₂ in each sector.

Each country then adjusts the template two ways:

- **Overall level.** All intensities are scaled by the country's fossil CO₂ per unit of GDP relative to the template's. Fossil CO₂ is from EDGAR (version 6.0) for 2018, and GDP from the IMF World Economic Outlook (October 2021).
- **Electricity.** The electricity sector uses the country's own power-sector CO₂ from EDGAR for 2018, divided by the value of its electricity output: 2018 generation from the U.S. Energy Information Administration times an average electricity price from the World Bank.

## Rest of world

The rest-of-world region's direct emission intensities are the output-weighted average of four Tier 2 countries: Colombia and Chile (from ICIO) and Mexico and Türkiye (from FIGARO). See [](../io/index.md) for how the region is used.

(ghg-data-years)=
## Data years

Emissions data are published on different schedules, and the model uses the most recent for each country.

| Tier | Countries | Emissions data year |
|---|---|---|
| Tier 0 | United States | 2024 |
| Tier 1 | China, United Kingdom | 2023 |
| Tier 1 | Japan | 2020 |
| Tier 1 | South Korea | 2018 |
| Tier 2 | FIGARO countries | 2023 |
| Tier 2 | ICIO countries | 2020 |
| Tier 3 | 83 countries | 2018 |
| Rest of world | | 2020–2023, from its four countries |

Emissions stay at their data year. For the data year of each country's IO table, see [](../reference/methods-by-country.md).

:::{important} Key assumptions
:class: dropdown
**Data-year emissions describe current production**

- **Assumption:** Each country's emissions from its data year still describe 2024 production.
- **Why we make it:** Emissions data by sector, matched to each source's IO sectors, are published with a lag, in some cases of several years.
- **How it affects results:** Where emissions per unit of output have fallen since the data year, for example as electricity grids get cleaner, factors may be too high. The gap is largest for South Korea and Tier 3 countries (2018) and for Japan and ICIO countries (2020).

**ICIO countries take the U.S. gas mix**

- **Assumption:** For ICIO countries, the split of each sector's CO₂e total into gases follows the U.S. mix for that sector.
- **Why we make it:** The OECD data give only total CO₂e by industry.
- **How it affects results:** Total CO₂e for each sector is unchanged, but results by gas are less reliable. Where a country's methane or fluorinated-gas share differs from the U.S., for example in rice farming, gas-level results could be off.

**EDGAR-based FIGARO countries are re-split with CEDS**

- **Assumption:** For the 10 FIGARO countries whose emissions Eurostat estimates from EDGAR, CEDS gives a better split between mining, refining, and power and gas utilities.
- **Why we make it:** EDGAR merges some activities that CEDS keeps separate, such as public power plants and on-site generation, and refining and extraction.
- **How it affects results:** The split between these industries changes, but the country's total for the group is unchanged.

**Tier 3 countries share one template**

- **Assumption:** Tier 3 countries share one pattern of direct emission intensities. They differ only in their overall level, set by fossil CO₂ per unit of GDP, and in their electricity intensity.
- **Why we make it:** These countries have no emissions data by sector.
- **How it affects results:** Differences between Tier 3 countries in which sectors emit the most are not captured, and non-CO₂ gases are scaled with fossil CO₂. Factors for these countries carry more uncertainty than those for Tiers 0 to 2.
:::

:::{seealso} Checks we run
- Each country's total emissions are kept through splitting and allocation.
- **U.S. facility floor and ceiling.** After the U.S. emissions are allocated, every industry's emissions are held at or above what its own facilities report to the {term}`GHGRP`, and industries whose facilities cover nearly all their combustion are held at or below it. U.S. national totals for each activity and gas are unchanged.

See [Validation](#validation-hub).
:::

+++

:::{div}
:class: page-status
Applies to: RC · Last reviewed: RC
:::
