---
title: "Cornerstone EEIO 2026 - RC"
---

## Release date: October 27th, 2026

:::{tip} Summary
The Cornerstone EEIO 2026 - RC (Release Candidate) is the first stage of a phased approach to releasing the Cornerstone EEIO 2026 model, the successor of USEEIO and CEDA. It is a global environmentally-extended input-output (EEIO) model that produces spend-based emission factors, in kg CO₂e per USD for 405 sectors across 148 countries, plus 15 regional averages and one global average. It uses 2024 as the base year and is available to use for 2024, 2025 and 2026 measurements.

This release candidate will be superseded in December by the release of the Cornerstone EEIO 2026 final version, which will include a time series from 2017 to 2026.

Download this release on Zenodo here.
:::

:::{note} Why have a Release Candidate?
:class: dropdown
2026 is an unprecedented year of development because it is the first time we are combining CEDA and USEEIO into one model and also the first time we are releasing a time series. The intention behind having a two phased approach to the release is to give companies additional time for impact assessments on their most recent year of measurements, while the developers finish the validation process for the time series. This enables companies to understand footprint changes before applying the time series.
:::

:::{note} Will there be any changes for years 2024 to 2026 once the time series is released?
:class: dropdown
We do not foresee significant changes, but some sector-country combinations could be impacted by improvements driven from the time series model development. Users should consider this version as a release candidate and wait for the final 2026 version of this model that will be released in early December for reporting and rebaselining purposes.
:::

:::{note} What to expect from the time series?
:class: dropdown
The time series (2017-2026) will use the same methodology for all years and only change the underlying data that represents each country’s economic structure and emissions data. For example, in the US each year of the dataset will use the US electricity grid emissivity for each year, capturing any decarbonization on this sector year over year.

This is the first time that either USEEIO or CEDA releases a time series built this way. In the past CEDA has released a time series built with inflation adjustments for years prior and after the base year. Moving forward the Cornerstone EEIO will only apply inflation adjustments to the years after the base year, for which there is no reported data (e.g. 2025 and 2026 are inflation adjusted from the 2024 base year).

To learn more about the methodology behind Cornerstone EEIO refer to [the IO model](../io/index.md) and [the GHG extension](../ee/index.md).
:::

## What changed

Cornerstone EEIO 2026 combines USEEIO’s detailed picture of the US economy with CEDA’s global coverage and trade modeling, representing a step change improvement to both models.

Three groups of improvements sit behind the changes.

1. **A more current picture of the US economy that accounts for imports**. US input-output tables are rebuilt for every year from 2017 to 2024, manufacturing uses facility-reported emissions, and imports are modeled where they are made.
2. **Newer data for Europe, the UK and China, and better gap-filling for the rest.** Europe moves from the OECD’s ICIO tables to Eurostat’s FIGARO (through 2023). China moves to the latest National Bureau of Statistics tables (through 2023), with more sectors. Countries without data are filled with the auto-balanced structural reflection method.
3. **A validation process that feeds back into the model.** Third-party benchmarks review the sectors behind about 50% of global emissions. Gaps are traced and fixed in the data or the method and documented when unresolved.

Together these make the 2017–2026 time series possible.

## Why do these improvements matter?

They translate real world changes to corporate footprints. Three examples show how:

### New data for China

Cornerstone adopts the most recent economic data released by the Chinese National Bureau of Statistics (2023 vs. 2020), which reflects methodology changes, changes in the economic structure, and sector-specific decarbonization.

For example, China’s battery factor rises by ~30% driven by a change in the composition of battery production in China. From 2020 to 2023, battery production more than tripled, but more importantly it shifted to require more Lithium-ion and less Lead-acid as inputs. This is because the majority of the market growth in batteries are in EVs and grid storage that require lithium-ion. Lithium-ion needs lithium chemicals and power-hungry cell factories, being more carbon intensive per dollar than lead-acid batteries, driving the emission factor up.

:::{figure} ../images/rc-china-battery.png
:label: rc-china-battery
:alt: Stacked bar chart of China battery production. In 2020, output was 382 GWh, mostly lead-acid. In 2023, output was 1,183 GWh, mostly lithium-ion.
:width: 65%

**China battery production, 2020 and 2023.** Output in GWh. The split by battery type is approximate. Sources: NBS input-output tables 2020 and 2023; MIIT; China lead-acid battery industry statistics.
:::

### New data for Europe

Cornerstone adopts the most recent release of FIGARO, Eurostat’s official input-output and emissions dataset. FIGARO is more granular than the OECD dataset for Europe, is available through 2023 vs. 2020, and is updated every year, matching Cornerstone’s release cadence.

This data update lowers European factors by about 4% in median. The most significant change is in electricity factors, which fall in every EU country. This change is driven by an increase in renewable energy and by an increase in energy prices due to the gas-supply shocks the Ukraine war has caused in Europe. For example, Germany’s power factor fell by 60%, as renewables grew from 35% to over 50% of generation and wholesale power prices more than doubled.

:::{figure} ../images/rc-germany-power.png
:label: rc-germany-power
:alt: Bar showing that about 25% of the fall in Germany's power emission factor comes from a cleaner grid and about 75% from higher prices.
:width: 100%

**Germany's power emission factor falls by 60%.** About 25% of the change comes from a cleaner grid, as renewables grew from 35% to over 50% of generation, and about 75% from higher prices, as wholesale power prices more than doubled, from about €44 to €95 per MWh. Sources: Ember, Öko-Institut, SMARD, Vattenfall.
:::

### Incorporation of imports in the US

USEEIO treated the US as a closed economy: every product used in the US was assumed to be made in the US. Cornerstone uses trade data to model each import in the country that produced it. Many imports come from more emissions-intensive economies such as China and India, so US factors tend to rise by 10 to 30% on average. This is the main upward pressure and the main reason for the change for USEEIO users. One example is light trucks and utility vehicles. The US factor rises by ~24.1%, mostly because the majority of the components of these vehicles are manufactured in South East Asia.

## How do the emission factors change?

The charts compare the new factors with each model they replace.

:::{figure} ../images/rc-factor-comparison.png
:label: rc-factor-comparison
:alt: Two waterfall charts. Against CEDA 2025, the factor goes from 0.6957 to 0.5281 (24.1% lower), with data updates adding 6.3% and methodology changes removing 28.6%. Against USEEIO v1.4 for the US, it goes from 0.2474 to 0.2448 (1.0% lower), with data updates removing 4.2% and methodology changes adding 3.3%.
:width: 100%

**Emission factors fall 24.1% against CEDA 2025 and 1.0% against USEEIO v1.4 (US).** Production-weighted totals in kg CO₂e per 2024 USD, split into data updates and methodology changes.
:::

:::{important} Your footprint may not follow the median
A company’s change depends on which sectors and countries its spend falls in. A small median can hide large moves in individual sectors, in both directions.
:::

For a more detailed change log against the USEEIO or CEDA, please refer to Change Log vs. USEEIO and Change Log vs. CEDA.

## Give feedback

[Open an issue on GitHub](https://github.com/cornerstone-data/eeio-docs/issues/new).

+++

:::{div}
:class: page-status
Applies to: RC · Last reviewed: RC
:::
