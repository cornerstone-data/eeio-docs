---
title: "Country tiers"
---

:::{tip} In one sentence
Countries are grouped into tiers by the IO data available for them, from the detailed U.S. tables (Tier 0) to templates for countries with no usable published table (Tier 3).
:::

## What each tier starts from

The model covers 148 countries plus a rest-of-world region. A country's tier sets which table it starts from, how much sector detail that table has, and how it is valued.

| {term}`Country tier` | Countries | Starting tables |
|---|---|---|
| Tier 0 | United States | Cornerstone's nowcast {term}`Make and Use tables <Make/Use framework>` for 2024, after {term}`redefinitions <Redefinitions>`, following BEA's 2017 detailed schema |
| Tier 1 | China, Japan, South Korea, United Kingdom | IO tables published by each country's statistical agency |
| Tier 2 | 60 countries | The country's table from {term}`FIGARO` (40 countries) or the {term}`OECD ICIO` (20 countries) |
| Tier 3 | 83 countries | No usable table: a template built from other countries' tables |

## Tier 0: United States

The U.S. starts from Cornerstone's nowcast Make and Use tables for 2024. The Bureau of Economic Analysis (BEA) publishes detailed tables only every five years, and the latest are for 2017. Our nowcast tables estimate the economy for 2024 in the same form: Make and Use tables after redefinitions, following BEA's official 2017 detailed schema. The Make table shows which commodities each industry produces. The Use table shows which commodities each industry and each final user buys. Both are in millions of dollars.

**Why after redefinitions?** Many establishments make secondary products. A hotel runs a restaurant, for example, or a manufacturer does its own repair work. Redefinitions move these secondary products, and the inputs used to make them, to the industry where they are the primary product. Each industry's input recipe then describes the product it is named for more closely, which makes for cleaner emission factors.

The U.S. tables have 405 sectors. The U.S. tables matter beyond the U.S.: their detailed structure sets the model's common sector list, and it is used to split other countries' coarser sectors (see {term}`ABSR`).

## Tier 1: national tables

Four countries have detailed national IO tables that we use directly.

| Country | Source table | Data year | Sectors | Imports | Units |
|---|---|---|---|---|---|
| China | National Bureau of Statistics national IO table | 2023 | 211 | Not separated in the source; split using China's domestic and import shares from the OECD ICIO (2021 edition, 2018 data) | 10,000 yuan |
| Japan | Input-Output Tables for Japan | 2020 | 390 | Separate domestic and import tables | Million yen |
| South Korea | Bank of Korea input-output tables, detailed | 2018 | 381 | Separate domestic and import tables | Million won |
| United Kingdom | ONS Input-Output Analytical Tables, product by product | 2023 | 104 | Separate imports use table | £ million |

All four are symmetric IO tables, with the same sectors on rows and columns. Each one is prepared the same way:

1. **Map to the common sectors.** A correspondence links each national sector to one or more of the 405 common sectors. Where one national sector covers several common sectors, it is split using the U.S. structure as weights ({term}`structural reflection <Structural reflection>`).
2. **Split domestic and imported inputs** using the country's own domestic and import shares.
3. **Convert to 2024 U.S. dollars.** Values are converted at the data year's average exchange rate, then brought to 2024 prices with a U.S. price index.
4. **Keep the country's total output.** Total output by sector is anchored to the source table's gross output.

## Tier 2: FIGARO and OECD ICIO

Most of the remaining large economies come from one of two multi-regional databases. Both are already harmonized across countries, but they are much coarser than the U.S. tables. Where a country is in both, we use FIGARO.

|  | FIGARO | OECD ICIO |
|---|---|---|
| Countries in the model | 40 | 20 |
| Edition | 2026 | 2025 |
| Data year | 2023 | 2020 |
| Table type | Symmetric IO table, product by product | Symmetric IO table, industry by industry |
| Sectors | 64 products (CPA 2.1) | 50 industries (ISIC Rev. 4) |
| Units | € million, current prices | US\$ million, current prices |

**FIGARO countries:** the 27 EU member states, plus Argentina, Australia, Brazil, Canada, India, Indonesia, Mexico, Norway, Russia, Saudi Arabia, South Africa, Switzerland, and Türkiye.

**OECD ICIO countries:** Cambodia, Chile, Colombia, Costa Rica, Hong Kong, Iceland, Israel, Kazakhstan, Laos, Malaysia, Morocco, Myanmar, New Zealand, Peru, the Philippines, Singapore, Taiwan, Thailand, Tunisia, and Viet Nam.

Both databases are inter-country tables, so each country's own block of the table gives its domestic inputs, and the blocks for all other countries give its imports.

Before mapping, five of FIGARO's broad sectors are split into finer ones while keeping their totals: electricity, gas, and heat; water, sewerage, and waste; basic metals (steel, other ferrous, non-ferrous); non-metallic minerals (cement, other); mining (five sectors); and agriculture (11 farm sectors). The tables are then mapped to the common sectors with {term}`ABSR`, and converted to 2024 U.S. dollars the same way as Tier 1.

## Tier 3: template countries

The 83 countries that are in neither Tier 1 nor Tier 2 have no usable published table. They are not part of the multi-region table; their factors are calculated one country at a time.

- **Input recipe.** All 83 share one template recipe, a weighted blend of three Tier 2 economies: Mexico (30%), Malaysia (30%), and Tunisia (40%).
- **Imports.** Each country's own import share splits the template into domestic and imported inputs, with the same share for every sector. The supply chains behind those imports are approximated with China's.
- **Emissions.** Direct emission intensities are scaled to the country's own emissions per unit of GDP, and electricity uses the country's own emission intensity.

This template is separate from the rest-of-world region in the multi-region table, which is built from different countries (see [](index.md)).

## Currency

All tables are converted to 2024 U.S. dollars. Sector lists are reconciled in the later steps: mapping to the common sector list, linking with trade data, and balancing.

:::{note} Draft: to confirm
:class: dropdown
- U.S.: link to the nowcast method (how the 2024 tables are estimated) and how imported and domestic inputs are separated to give `Adom` and `Aimp`.
- Tier numbering: these docs call the U.S. Tier 0 and the other four national-table countries Tier 1; the model's configuration groups all five as Tier 1. Pick one convention.
- Valuation: tables differ in price basis (supply rows at basic prices; use rows at purchaser prices; industry output at basic or producer prices). The model assumes these differences do not affect `A`. Document this on the prices and margins page rather than per table here.
- Purchaser-price factors use U.S. margin ratios for all countries; document on the prices and margins page.
- Year mismatch: emissions are not adjusted to 2024, so direct intensities pair data-year emissions (e.g., Korea 2018, OECD ICIO 2020) with 2024 dollars.
- Tier 3: confirm the template weights and how imported supply chains are approximated before publishing.
- Decision for the team, Tier 3 vs. rest of world: imports from Tier 3 countries get the rest-of-world proxy (Colombia, Mexico, Türkiye, Chile), while those countries' own factors use the Tier 3 template (Mexico, Malaysia, Tunisia) with country-specific emission intensities. Either give the rest-of-world region intensities based on the Tier 3 countries, or keep the proxy as documented in the IO overview's assumptions.
:::

:::{note} Draft placeholder
:class: dropdown
Plan §3.2.5 · target: **RC (Oct 27)**


**Planned content**

- What each tier uses and why; link to Methods by country for any single country
- How tier affects detail and confidence

**Key visuals**

- 🖼 World map colored by tier
- 🖼 Share of global output and emissions by tier
:::

:::{important} Key assumptions
:class: dropdown
**Tier 3 countries share one recipe**

- **Assumption:** Tier 3 countries share one template input recipe. Each country differs only in its overall import share, applied equally to every sector, and in its direct emission intensities, which are scaled to the country's emissions per unit of GDP, with its own electricity intensity. Their imported supply chains are approximated with China's.
- **Why we make it:** These countries have no usable published IO table.
- **How it affects results:** Differences in industry structure between Tier 3 countries are not captured, and imports from countries other than China are given China's supply chains. Factors for these countries carry more uncertainty than those for Tiers 0 to 2.
- **Alternatives or sensitivity tested:** *To be written.*
:::

:::{seealso} Checks we run
*The validation behind this part of the model. See [Validation](#validation-hub).*
:::

## Learn more

- **From the field:** *to be added*
- **Cornerstone papers:** *to be added*
- **Code:** *to be added*

+++

:::{div}
:class: page-status
Applies to: RC · Last reviewed: RC
:::
