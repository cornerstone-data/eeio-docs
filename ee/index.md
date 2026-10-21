---
title: "The GHG extension: overview"
---

:::{tip} Summary
The GHG extension attaches each sector's own greenhouse gas emissions to the IO model, as emissions of each gas per dollar of output (`B`). Every country follows the same steps, but the emissions data behind them, and how much detail they carry, depend on the country's tier.
:::

:::{note} Draft
:class: dropdown
**Key visual to add:** pipeline from source emissions → split and map to the common sectors → convert to AR6 → divide by output → `B`.
:::

## What the extension adds

The IO model traces the dollars that flow through supply chains. The GHG extension adds what each sector emits while making its output. For each country and sector it records:

- **Emissions** (`E`): kilograms of each gas emitted by the sector in a year.
- **Direct emission intensities** (`B`): those emissions divided by the sector's output (`q`), so kilograms of each gas per dollar of output.

`B` holds direct emissions only: what the sector emits from its own fuel use, processes, and other activities. Emissions from the sector's suppliers come in through the supply chain (`L`), not through `B`. For example, the emissions from generating electricity stay with the power sector, and other sectors' purchased electricity reaches them through `L`.

Characterization factors (`C`) then weight each gas by its global warming potential, which gives the direct emission factors `D = C × B` and the total emission factors `N = C × B × L` (see [](../reference/notation.md)).

## Gases and global warming potentials

`B` has a row for each of seven gases or gas groups: carbon dioxide (CO₂), methane (CH₄), nitrous oxide (N₂O), hydrofluorocarbons (HFCs), perfluorocarbons (PFCs), sulfur hexafluoride (SF₆), and nitrogen trifluoride (NF₃).

They are combined into CO₂-equivalent with 100-year {term}`GWPs <GWP>` from the IPCC's Sixth Assessment Report (AR6). Methane is valued two ways: fossil methane, from fuel production and use, at 29.8, and non-fossil methane, from farming and waste, at 27.0. Fossil methane is valued higher because, once it breaks down, it leaves CO₂ that was not already in the atmosphere.

Several sources report emissions as CO₂-equivalent using older GWPs from the Fifth Assessment Report (AR5). These are converted to AR6, gas by gas.

## What is and isn't counted

`B` covers emissions from producing goods and services. Some emissions in national inventories do not come from a producing sector, and they are left out:

- **Household direct emissions.** Fuel burned in homes and in personal vehicles is emitted by households, not by an industry, so it is not in `B`.
- **Land use, land-use change, and forestry (LULUCF).** Emissions and removals from land are not included.

## Accounting basis

Emissions data are compiled on one of two bases, and the model uses each source as published:

- **{term}`Territorial basis`:** emissions that occur within the country's borders. National GHG inventories use this basis, and so do the U.S. and China data.
- **{term}`Residence basis`:** emissions by the country's resident businesses, wherever they occur. Air emissions accounts use this basis, as do the {term}`FIGARO` and {term}`ICIO` emissions data. Emissions from a country's airlines and shipping companies abroad are counted for that country.

The residence basis matches how IO tables define a country's economy, so it suits an IO model. The two bases differ most for countries with large international transport fleets or many visitors. See [](country-tiers.md) for the basis of each source.

## From source emissions to `B`

Every country's emissions go through the same steps:

1. **Start from source emissions by source sector.** Each source reports emissions on its own sector list, which can be anything from hundreds of activities (the U.S. inventory) to 50 industries (ICIO).
2. **Split broad sectors where better data exist.** Some sources lump together sectors with very different emissions, such as electricity, gas, and heat, or all of farming. Where other data can separate them, the broad sector is split first, keeping its total.
3. **Spread onto the common sectors.** Each source sector's emissions are spread over the matching common sectors with {term}`ABSR`, weighted by U.S. emission intensities. The country's total for each source sector is kept.
4. **Fill in missing gas detail.** Where a source does not separate every gas, the missing split is taken from the U.S. mix for the same sector.
5. **Convert to AR6** where the source used other GWPs.
6. **Divide by output.** Emissions for each sector are divided by the same sector's output in the IO model, giving `B`.

The U.S. model is built directly on the 405 common sectors, so steps 3 and 4 do not apply. [](country-tiers.md) gives the sources and the variations for each tier.

## Data years

Emissions data are published on different schedules, and the model uses the most recent of each.

| Emissions data year | Countries |
|---|---|
| 2024 | United States |
| 2023 | China, United Kingdom, FIGARO countries (Tier 2) |
| 2020 | Japan, ICIO countries (Tier 2) |
| 2018 | South Korea |

Emissions stay at their data year. Output, the denominator of `B`, is re-priced to 2024 dollars, so each country's `B` is its data-year emissions per 2024 dollar.

:::{important} Key assumptions
:class: dropdown
**U.S. intensities shape detail within each source sector**

- **Assumption:** Within each source sector, a country's emissions are spread over the common sectors in proportion to U.S. emission intensities.
- **Why we make it:** Outside the U.S., emissions data come on far fewer sectors than the 405 common sectors, and the U.S. data are the most detailed available.
- **How it affects results:** Each country's total for each source sector is correct, but its split between detailed sectors follows the U.S. pattern. Where a country's mix of processes differs from the U.S. (for example, a different steelmaking route), detailed sectors within the same source sector could be too high or too low.

**Data-year emissions per 2024 dollar**

- **Assumption:** Each country's emissions from its data year still describe 2024 production.
- **Why we make it:** Emissions data for 2024 are not yet published for most countries.
- **How it affects results:** Where emissions per unit of output have fallen since the data year, for example as electricity grids get cleaner, factors may be too high. The gap is largest for South Korea (2018) and for Japan and ICIO countries (2020).

**Household emissions are excluded**

- **Assumption:** Direct emissions from homes and personal vehicles are not assigned to any sector.
- **Why we make it:** They are not emitted in producing goods or services, so they do not belong in emission factors for purchases.
- **How it affects results:** Totals in `B` are lower than national inventory totals. Emissions from fuel *production* for household use, such as refining, are still counted, in the producing sectors.

**Mixed accounting basis**

- **Assumption:** Each source is used on its published basis, territorial or residence.
- **Why we make it:** Converting between bases needs data on emissions by residents abroad and non-residents at home, which are not consistently available.
- **How it affects results:** Transport emissions in particular may be counted differently for territorial-basis countries (the U.S. and China) than for the others.
:::

:::{seealso} Checks we run
- Splitting and mapping keep each country's source totals, so its total emissions in the model match its source data.
- U.S. totals by gas match the national inventory.

See [Validation](#validation-hub).
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
