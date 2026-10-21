---
title: "Change log vs. USEEIO"
---

:::{tip} Summary
Cornerstone EEIO 2026 is the continuation of the USEEIO Supply Chain GHG Emission Factors v1.4. For US factors, the net change is on median −1.0%, from 0.2474 to 0.2448 kg CO₂e per 2024 USD (production-weighted).

However, the net figure hides large changes that offset each other. Three changes drive about 95% of the impact: model reconciliation, nowcasting and facility-reported data, and the modeling of imports.
:::

## The changes at a glance

Emission factors are production-weighted totals for the United States, in kg CO₂e per 2024 USD.

| | Cornerstone 2026 vs. USEEIO v1.4 |
|---|---|
| Emission factor, before and after | 0.2474 to 0.2448 |
| **Net change** | **−1.0%** |
| Data updates | −4.2% |
| Methodology changes | +3.3% |
| Median change in a company's total footprint | −1.4% |
| Companies whose footprint moves by more than 20% | 6% |

*Company figures come from a sample of 400 corporate footprints that combine spend-based and activity data.*

:::{important} Your footprint may not follow the median
A company's change depends on which sectors and countries its spend falls in. A small median can hide large moves in individual sectors, in both directions.
:::

## What drives the change for USEEIO users

:::{figure} ../figures/diagrams/waterfall-vs-useeio.png
:label: waterfall-vs-useeio
:alt: Waterfall chart of the US emission factor from USEEIO v1.4 (0.2474) to Cornerstone 2026 (0.2448), by driver: model reconciliation, US data, nowcasting and facility data, trade impact, and benchmark-informed improvements.
:width: 100%

**Change in the US production-weighted emission factor from USEEIO v1.4 to Cornerstone 2026, by driver.** Percentages are changes relative to the USEEIO baseline. Increases are in coral and decreases in teal. The vertical axis starts at 0.22.
:::

### Model reconciliation

The USEEIO and CEDA teams reviewed 18 differences between the two models for the US. For each, they adopted one model's approach or proposed an improvement. Selected decisions:

| Topic | USEEIO | CEDA | Cornerstone |
|---|---|---|---|
| Waste | Split into 7 sectors | One sector | USEEIO: split into 7 |
| Aluminum | Primary and secondary separate | Merged | USEEIO: separate |
| Home appliances | One sector, as BEA | Four sectors | USEEIO: one sector |
| Accounting-only commodities | Kept in the tables | Removed, output recalculated | CEDA: remove |
| Electric utilities | 3 separate industries | One aggregated industry | CEDA: aggregate |
| Transit | Government and private separate | Aggregated | CEDA: aggregate |
| Households | Tracked as sector F01000 | Not always tracked | USEEIO: track F01000 |

Each decision is documented in the open discussion log (see Learn more).

### Nowcasting and facility-reported data

BEA publishes detailed (about 400-sector) US input-output tables only every 10 years, with a five-year lag. The latest is for 2017. Nowcasting rebuilds these tables for every year from 2017 to 2024, in BEA's own structure, using the same official statistics BEA uses.

Where most facilities in a sector report their emissions, those reports replace estimates based on fuel use data that is updated about every four years. The 2024 data includes 6,127 facility reports across 84 industries. More than 50% of the economic data behind the factors is now backed by reported annual data, beyond inflation adjustments.

### Trade impact: modeling imports

USEEIO treated the US as a closed economy: every product used in the US was assumed to be made in the US. Cornerstone uses trade data to model each import in the country that produced it. Many imports come from more emissions-intensive economies such as China and India, so US factors tend to rise by 10 to 30% on average. This is the main upward pressure and the main reason for the change for USEEIO users.

For example, about 40% of the US crude oil mix is imported. Emissions from that oil are allocated to the producing countries, and Canadian oil is up to twice as emissions-intensive as US oil.

**Case study: light trucks and utility vehicles.** The US factor rises by 24.1% (0.2925 to 0.3628 kg CO₂e per USD), mostly because of trade effects.

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

For the equivalent change log against CEDA, see [](changelog-ceda.md).

## Learn more

- **From the field:** *to be added*
- **Cornerstone papers:** *to be added*
- **Code:** [Methods discussion log](https://github.com/cornerstone-data/methods/discussions), the record of each model reconciliation decision.

+++

:::{div}
:class: page-status
Applies to: RC · Last reviewed: RC
:::
