---
title: "Calculating the emission factors"
---

:::{tip} Summary
The emission factors are the model's total emission factors (`N`): the CO₂e emitted across the whole supply chain per dollar of each commodity, by the country that produces it. This page follows the calculation from the matrices of [the IO model](../io/index.md) and [the GHG extension](../ee/index.md) to the published producer-price (PRO) and purchaser-price (PUR) factors for each year.
:::

:::{figure} ../figures/diagrams/ef-pipeline.svg
:label: fig-ef-pipeline
:alt: B and L feed step 1, total intensities M equals B times L. Step 2 weights by GWP, N equals C times M. Step 3 forms regional averages and fills gaps. Step 4 re-prices to each year, 2024, 2025 and 2026, giving the producer-price factors. Step 5 multiplies by phi, the producer share of the purchaser price, giving the purchaser-price factors. Notes say steps 1 to 3 are in 2024 U.S. dollars at producer price, step 4 uses U.S. price indexes, step 5 uses U.S. trade and transport margins, and margin emissions are published separately.
From the model matrices to the published factors. The base calculation is in 2024 dollars; each year's factors are re-priced from it. `φ` is the producer share of the purchaser price.
:::

## From the model to total emission factors

The IO model gives the total requirements `L`, the output needed from every sector in every country per dollar of final demand (see [](../io/index.md#total-requirements)). The GHG extension gives the direct emission intensities `B`, the kilograms of each gas a sector emits per dollar of its own output (see [](../ee/index.md)). The emission factors combine the two.

1. **Total intensities by gas.** `M = B × L` traces each sector's direct emissions through every round of suppliers. A column of `M` gives, for \$1 of one commodity from one country, the emissions of each gas anywhere in its supply chain.
2. **CO₂-equivalent.** The characterization factors `C` weight each gas by its 100-year GWP from the IPCC AR6, so `N = C × M` gives the total emission factors in kg CO₂e per dollar (see [](../ee/index.md#gases-and-global-warming-potentials)). The gas columns of the release are the rows of `M` in CO₂e, and Total GHGs is their sum.

For the 65 countries in Tiers 0 to 2 and the rest-of-world region, `L` is solved once for the whole multi-region table, so `M` follows supply chains across every border in the table. Each column of `N` is one commodity produced in one country, so a factor describes where a product is made, not where it is bought.

The factors are per dollar of commodity output at producer price, in 2024 U.S. dollars, the model's base year. They include every upstream supplier, but not the trade and transport services between the producer and the buyer, which are handled in [](#purchaser-price) and [](margins.md).

The direct emission factors `D = C × B`, which hold only what a sector emits itself, are part of the model but are not published as a separate table.

## Tier 3 countries

The 83 Tier 3 countries are not part of the multi-region table, so their factors are calculated one country at a time, from the template described in [](../io/country-tiers.md#tier-3-no-io-tables) and [](../ee/country-tiers.md#tier-3-template-emissions). Each country's domestic inputs carry its own direct emission intensities through its domestic total requirements, `(I − Adom)⁻¹`. Its imported inputs carry China's total emission factors from the multi-region table. The two parts are added to give the country's `M`.

## Regional and global averages

The release has a factor for each of 21 regions and one global average (`GLOB`). For each sector and each gas, a regional factor is the average of its member countries' factors, weighted by each country's output of that sector in 2024 dollars (`q`):

`N_region = Σ (N_country × q_country) ÷ Σ q_country`

Only countries in Tiers 0 to 2 have output data in the model, so Tier 3 countries are not included in the weighted average, even where they belong to the region. A region with no Tier 0 to 2 member uses the simple average of its members' factors instead. The global average is weighted the same way over every Tier 0 to 2 country. The rest-of-world region is used only inside the model and is not published.

## Filling missing country factors

A few country–sector combinations have a total factor of exactly zero, because the source tables have no output or no emissions for that sector in that country. A zero factor would understate emissions for anyone buying from that sector, so it is treated as missing: the country's factor is replaced by its region's factor, or by the global average where the regional factor is also zero. The replacement applies to every gas.

(reporting-years)=
## From the base year to each reporting year

Every source in the model is first brought to 2024 dollars: values are converted to U.S. dollars at the data year's exchange rate and re-priced to 2024 with a U.S. price index (see [](../io/country-tiers.md)). The model therefore produces 2024 factors, per 2024 dollar.

The factors for 2025 and 2026 are re-priced from the 2024 factors, sector by sector:

`N_t = N_2024 × PI(2024) ÷ PI(t)`

where `PI` is the sector's price index and `t` is the year. When a sector's prices rise, each dollar buys less of its output, so the factor per dollar falls. The emissions behind the factors are the same; only the dollar they are expressed in changes. Each year's factors are therefore in current dollars of that year.

The price index is the U.S. Bureau of Economic Analysis chain-type price index for gross output by industry (2017 = 100), mapped to the 405 sectors. The 2026 value is the average of the quarters published at the time of the release. Sectors without their own index keep a constant price. The same U.S. index is applied to every country, region and the global average.

(purchaser-price)=
## From producer to purchaser price

A purchaser pays more than the producer receives: wholesale, retail and transport businesses add their margins on the way to the buyer. Each dollar at purchaser price therefore contains less of the product itself. The purchaser-price factor converts the producer-price factor to this larger dollar:

`N_PUR = N_PRO × φ`, where `φ = 1 ÷ (1 + Σ A_margin)`

Here `A_margin` holds the margins paid on each commodity, in dollars of margin per dollar of the commodity at producer price, one row per margin sector, and `φ` is the producer share of the purchaser price.

- **Margins come from the U.S.** `A_margin` is built from U.S. margin data, on the industry-average margins paid by industries and business investment. The same `φ` is applied to every country, region and the global average (see the [key assumptions](../io/country-tiers.md#currency) for the IO tables).
- **Margins only.** The conversion covers trade and transport margins. Taxes and subsidies on products are not included.
- **Services and electricity have `φ = 1`.** They carry no trade margins, so their producer- and purchaser-price factors are the same.
- **Each year has its own `φ`.** The margin coefficients are re-priced to each year with the price indexes of the margin sector and of the commodity, so `φ` changes slightly from year to year.

The purchaser-price factor covers the emissions of making the product only. The emissions of the margin services themselves, such as running warehouses, stores and trucks, are not added to it; they are prepared as separate [margin emission factors](margins.md).

## Rounding

Published factors are rounded to three significant figures. Total GHGs is rounded from the unrounded total, so it may not equal the sum of the rounded gas values.

:::{important} Key assumptions
:class: dropdown
**2025 and 2026 factors reflect price changes only**

- **Assumption:** The supply chains and emission intensities of the 2024 model also describe 2025 and 2026. The factors for those years differ from 2024 only by the change in each sector's price.
- **Why we make it:** Input-output tables and emissions data for 2025 and 2026 are not yet available for any country.
- **How it affects results:** Real changes after 2024, such as a cleaner electricity grid or a shift in where inputs are bought, are not captured in the 2025 and 2026 factors.

**One U.S. price index for every country**

- **Assumption:** Each sector's U.S. price change applies to that sector in every country.
- **Why we make it:** Consistent sector-level price indexes in U.S. dollars are not available for every country and year.
- **How it affects results:** Where prices in a country moved differently from U.S. prices, or its exchange rate against the dollar changed, its factors for 2025 and 2026 could be too high or too low.

**U.S. margins and no product taxes in purchaser prices**

- **Assumption:** The U.S. share of trade and transport margins in each commodity's purchaser price applies in every country, and product taxes are left out of the conversion.
- **Why we make it:** Margin and tax data comparable to the U.S. tables are not available for every country.
- **How it affects results:** Where a country's margins or product taxes differ from the U.S., its purchaser-price factors could be too high or too low. Producer-price factors are not affected.

**Gross-output weights for regional averages**

- **Assumption:** A region's factor for a sector is the average of its member countries' factors weighted by their output of that sector, using only countries in Tiers 0 to 2.
- **Why we make it:** Output is the best available measure of how much of a sector's supply each country provides, and it is available only for countries with IO tables.
- **How it affects results:** The regional factor reflects the region's largest producers. Where a region's Tier 3 members produce differently from its Tier 0 to 2 members, their purchases are better represented by their own country factors.
:::

:::{seealso} Learn more
- Calculating total requirements and multipliers: the standard textbook on IO analysis [@millerInputoutputAnalysisFoundations2022]
- How BEA builds the U.S. IO accounts, including margins and price bases [@beaConceptsMethodsUS2009]
- How to choose between producer and purchaser price: [](user-guidance.md#choose-between-purchaser-and-producer-price)
- What each published table contains: [](whats-in-a-release.md)
:::

+++

:::{div}
:class: page-status
Applies to: 2026-rc.1 · Last reviewed: 2026-rc.1
:::
