---
title: "Summary of changes vs. CEDA"
---

:::{tip} Summary
Cornerstone EEIO 2026 is the continuation of CEDA 2025. For global factors, the net change is on median −23.3% in kg CO₂e per 2024 USD (production-weighted), driven by a combination of data and methodology changes.
:::

:::{figure} ../images/summary-vs-ceda.png
:label: summary-vs-ceda
:alt: Waterfall chart of the global emission factor. From CEDA 2025 at 0.6942, data updates add 5.8% and methodology changes remove 27.5%, ending at 0.5324 for Cornerstone 2026, 23.3% lower.
:width: 80%

**Cornerstone 2026 against CEDA 2025 (global).** Global production-weighted total emission factor, in kg CO₂e per 2024 USD, split into data updates and methodology changes.
:::

::::{important} Your footprint may not follow the median
:class: dropdown
A company's change depends on which sectors and countries its spend falls in. A small median can hide large moves in individual sectors, in both directions. From a sample of 400 corporate footprints, the median company will experience a decrease of 14%. Open this box to see the full range.

:::{figure} ../images/company-footprint-change-ceda.png
:label: company-footprint-change-ceda
:alt: Histogram of the change in the footprint of 400 companies against CEDA. Nearly all companies decrease, mostly between 0% and 40%, with a median of a 14% decrease. A few companies change by less than 1% or increase slightly.
:width: 90%

**Change in the footprint of 400 companies, Cornerstone 2026 against CEDA 2025.** Each bar groups companies by the percentage change in their total footprint. Bars outside the shaded ±20% band are in green. Bar heights are approximate.
:::
::::

## What drives the change for CEDA users

Four changes drive ~95% of the impact: China data, Europe and global data, ABSR and benchmark-informed improvements.

:::{figure} ../images/drivers-vs-ceda.png
:label: drivers-vs-ceda
:alt: Waterfall chart of the global emission factor from CEDA 2025 (0.6942) to Cornerstone 2026 (0.5324), by driver. China data adds 7.6%, Europe and other global data lower it by 1.8%, ABSR lowers it by 11.0% and benchmark-informed improvements lower it by 17.2%. Model reconciliation, US data, nowcasting, bug fixes and UK and global trade data are each within 0.7% of zero.
:width: 100%

**Change in the global production-weighted emission factor from CEDA 2025 to Cornerstone 2026, by driver.** Percentages are changes relative to the CEDA 2025 baseline. The vertical axis starts at 0.50.
:::

### New data for China

Cornerstone adopts the most recent economic data released by the Chinese National Bureau of Statistics (2023 vs. 2020), which reflects methodology changes, changes in the economic structure, and sector-specific decarbonization.

For example, China's battery factor rises by ~30% driven by a change in the composition of battery production in China. From 2020 to 2023, battery production more than tripled, but more importantly it shifted to require more lithium-ion and less lead-acid as inputs. This is because the majority of the market growth in batteries is in EVs and grid storage, which require lithium-ion. Lithium-ion needs lithium chemicals and power-hungry cell factories, being more carbon intensive per dollar than lead-acid batteries, driving the emission factor up.

:::{figure} ../images/rc-china-battery.png
:label: summary-china-battery
:alt: Stacked bar chart of China battery production. In 2020, output was 382 GWh, mostly lead-acid. In 2023, output was 1,183 GWh, mostly lithium-ion.
:width: 65%

**China battery production, 2020 and 2023.** Output in GWh. The split by battery type is approximate. Sources: NBS input-output tables 2020 and 2023; MIIT; China lead-acid battery industry statistics.
:::

### New data for Europe

Cornerstone adopts the most recent release of FIGARO, Eurostat's official input-output and emissions dataset. FIGARO is more granular than the OECD dataset for Europe, is available as a time series through 2023, and is updated every year, matching Cornerstone's release cadence.

This data update lowers European factors by about 4% in median. The most significant change is in electricity factors, which fall in every EU country. This change is driven by an increase in renewable energy and by an increase in energy prices due to the gas-supply shocks the Ukraine war has caused in Europe. For example, Germany's power factor fell by 60%, as renewables grew from 35% to over 50% of generation and wholesale power prices more than doubled.

### Auto-balanced structural reflection (ABSR)

Structural reflection is the method CEDA uses to give every country the same sectors. ABSR improves it. It achieves two goals that are hard to deliver together in a global model:

- All countries share the same 405 sectors, so emission factors compare like for like.
- Each economy balances production and consumption, in both money and emissions.

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

+++

:::{div}
:class: page-status
Applies to: RC · Last reviewed: RC
:::
