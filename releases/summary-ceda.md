---
title: "Summary of changes vs. CEDA"
---

:::{tip} Summary
Cornerstone EEIO 2026 replaces CEDA 2025. The global production-weighted emission factor falls by 24.1%, from 0.6957 to 0.5281 kg CO₂e per 2024 USD. Data updates raise factors (+6.3%) and methodology changes lower them by more (−28.6%). Four changes drive about 95% of the impact: benchmark-informed improvements, auto-balanced structural reflection (ABSR), new data for China, and new data for Europe.
:::

:::{figure} ../images/summary-vs-ceda.png
:label: summary-vs-ceda
:alt: Waterfall chart of the global emission factor. From CEDA 2025 at 0.6957, data updates add 6.3% and methodology changes remove 28.6%, ending at 0.5281 for Cornerstone 2026, 24.1% lower.
:width: 80%

**Cornerstone 2026 against CEDA 2025 (global).** Global production-weighted total emission factor, in kg CO₂e per 2024 USD, split into data updates and methodology changes.
:::

:::{important} Your footprint may not follow the median
A company's change depends on which sectors and countries its spend falls in. A small median can hide large moves in individual sectors, in both directions. From a sample of 400 corporate footprints, the median company will experience a decrease of 13.7%, and 24% of companies will see their footprint move by more than 20%.
:::

## What drives the change for CEDA users

:::{figure} ../figures/diagrams/waterfall-vs-ceda.png
:label: waterfall-vs-ceda
:alt: Waterfall chart of the global emission factor from CEDA 2025 (0.6957) to Cornerstone 2026 (0.5281), by driver. The largest are benchmark-informed improvements (−19.0%), ABSR (−10.7%) and China data (+7.8%).
:width: 100%

**Change in the global production-weighted emission factor from CEDA 2025 to Cornerstone 2026, by driver.** Percentages are changes relative to the CEDA 2025 baseline. Increases are in coral and decreases in teal. The vertical axis starts at 0.50.
:::

The smaller changes are model reconciliation (about 0%), US data (+0.1%), nowcasting and facility-reported data (−0.7%), bug fixes (−0.4%), and UK and global trade data (about 0%).

### Benchmark-informed improvements

This is the largest driver. See the benchmarking section below.

### Auto-balanced structural reflection (ABSR)

Structural reflection is the method CEDA uses to give every country the same sectors. ABSR improves it. It achieves two goals that are hard to deliver together in a global model:

- All countries share the same 405 sectors, so emission factors compare like for like.
- Each economy balances production and consumption, in both money and emissions.

### New data for China

China's National Bureau of Statistics released benchmark input-output tables for 2023. The last update was for 2020. The new tables come from China's 5th National Economic Census and have more detail: 211 sectors instead of 153.

This raises China's emission factors by about 10% at the median. It reflects methodology changes, changes in the economic structure, and sector-specific decarbonization. For example, China's battery factor rises by about 30%. Battery production grew from 382 GWh in 2020 to 1,183 GWh in 2023, and lithium-ion batteries, which are about twice as carbon-intensive per dollar as lead-acid, took a larger share.

### New data for Europe

Cornerstone adopts FIGARO, Eurostat's official input-output and emissions dataset. FIGARO is more granular than the OECD dataset for Europe, is available as a time series through 2023, and is updated every year, matching Cornerstone's release cadence.

This lowers European factors by about 4% at the median. Electricity factors fall in every EU country. For example, Germany's power factor falls by 60%, as renewables grew from 35% to over 50% of generation. The Netherlands' falls by 77%, after a coal ban and a gas-heavy grid.

## Third-party benchmarking

Cornerstone uses benchmark data built from about 1,000 sources to review the key sectors that drive about 50% of global emissions. Each review ends in one of three outcomes:

- **Sharper benchmark.** Scope and price assumptions are aligned, so the external reference is directly comparable to the model.
- **Model improvement.** The gap is traced to a data source or an allocation method, and fixed with more data or a corrected implementation.
- **Known discrepancy.** The difference is documented, because of a limitation in how the model is built or a gap in the data.

About 70% of country-sector pairs with a verified benchmark are within 25% of it. 21% are 25–50% apart and 10% are 50% or more apart.

| Outcome | Example | Gap before and after |
|---|---|---|
| Sharper benchmark | US electricity: the benchmark covered only private utilities, while the model also includes state and local utilities. Aligning scope gives a benchmark of 2.37 against the model's 2.44 kg CO₂e per USD. | 15% to 3% |
| Model improvement | Brazil dairy: the model was allocating methane from beef to dairy for lack of country-specific data. Brazil's national accounts of emissions and output fixed it. | 51% to 5% |
| Known discrepancy | US oil and gas: the benchmark roughly doubles methane using aerial and satellite measurements. The model uses the EPA inventory, as for every other sector. Resolving this needs more research. | 22% (stays) |

For the full list of data and methodology changes, see the [](change-log.md). For the equivalent summary against USEEIO, see [](summary-useeio.md).

## Learn more

- **From the field:** *to be added*
- **Cornerstone papers:** *to be added*
- **Code:** *to be added*

+++

:::{div}
:class: page-status
Applies to: RC · Last reviewed: RC
:::
