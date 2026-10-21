---
title: "Change log vs. CEDA"
---

:::{tip} Summary
Cornerstone EEIO 2026 replaces CEDA 2025. The global production-weighted emission factor falls by 24.1%, from 0.6957 to 0.5281 kg CO₂e per 2024 USD. Data updates raise factors (+6.3%) and methodology changes lower them by more (−28.6%). Four changes drive about 95% of the impact: benchmark-informed improvements, auto-balanced structural reflection (ABSR), new data for China, and new data for Europe.
:::

## The changes at a glance

Emission factors are global production-weighted totals, in kg CO₂e per 2024 USD.

| | Cornerstone 2026 vs. CEDA 2025 |
|---|---|
| Emission factor, before and after | 0.6957 to 0.5281 |
| **Net change** | **−24.1%** |
| Data updates | +6.3% |
| Methodology changes | −28.6% |
| Median change in a company's total footprint | −13.7% |
| Companies whose footprint moves by more than 20% | 24% |

*Company figures come from a sample of 400 corporate footprints that combine spend-based and activity data.*

:::{important} Your footprint may not follow the median
A company's change depends on which sectors and countries its spend falls in. A small median can hide large moves in individual sectors, in both directions.
:::

## What the science improvements mean in practice

1. **A more current picture of the US economy that accounts for imports.** US input-output tables are rebuilt for every year from 2017 to 2024, manufacturing uses facility-reported emissions, and imports are modeled where they are made.
2. **Newer data for Europe, the UK and China, and better gap-filling for the rest.** Europe moves from the OECD's ICIO tables to Eurostat's FIGARO (through 2023). China moves to the latest National Bureau of Statistics tables (through 2023), with more sectors. Countries without data are filled with the auto-balanced structural reflection method.
3. **A validation process that feeds back into the model.** Third-party benchmarks review the sectors behind about 50% of global emissions. Gaps are traced and fixed in the data or the method, not overridden in the output.

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

Cornerstone adopts FIGARO, Eurostat's official input-output and emissions dataset. FIGARO is more granular than the OECD dataset for Europe, is available through 2023, and is updated every year, matching Cornerstone's release cadence.

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

For the equivalent change log against USEEIO, see [](changelog-useeio.md).

## Learn more

- **From the field:** *to be added*
- **Cornerstone papers:** *to be added*
- **Code:** *to be added*

+++

:::{div}
:class: page-status
Applies to: RC · Last reviewed: RC
:::
