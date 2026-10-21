---
title: "What's in a release"
---

:::{tip} Summary
The Cornerstone EEIO model is updated annually and versioned with the year of the release, so Cornerstone EEIO 2026 is released in 2026 and the 2027 version will be released in 2027. Every year, the releases will be publicly available in October. Each release publishes emission factors as a CSV file covering 405 sectors across 148 countries, 15 regions and one global average. To download the latest version, check out zenodo.
:::

## The release workbook

The release is one Excel workbook that contains: a cover, a data dictionary, a producer-price tab and a purchaser-price tab for each year the data is available for, and five auxiliary tabs.

### Cover

The first tab introduces the dataset and the release details:

- Description: cradle-to-gate greenhouse gas emission factors in kg CO₂e per USD, by good or service, location and year, in producer and purchaser price. Prices are in current-year dollars, so the dollar year matches the data year.
- Coverage: 148 countries and 21 regions, and 405 categories of goods and services (government services are not covered). The total and each gas (CO₂, CH₄, N₂O, HFCs, PFCs, NF₃, SF₆) are given in CO₂e, annually from 2018 to 2026.
- Publisher and license: Cornerstone Sustainability Data Initiative, under a Creative Commons Attribution 4.0 International license.

Below these details, the cover lists every other tab with a one-line description and points readers to the data dictionary and the model documentation.

### Producer and purchaser price tabs

There are two tabs for each year, with identical layouts: `{YEAR}PRO` for producer prices and `{YEAR}PUR` for purchaser prices. The producer price is the cost to the producer plus their profits and taxes paid. The purchaser price adds the value of sales and distribution. Read more about how to choose between purchaser and producer prices in [](prices-and-margins.md).

Each row is one sector in one location, and the columns are:

| Column | Meaning |
|---|---|
| Code | Good or service code, based on the BEA input-output commodity codes, which derive from NAICS. There are 405 categories. |
| Name | Name of the good or service. |
| Location | A UN three-letter country code, with additions for multi-country regions. |
| Total GHGs | Sum of all greenhouse gases, in kg CO₂e per USD. |
| CO2 | Carbon dioxide, in kg CO₂e per USD. |
| CH4 | Methane, in kg CO₂e per USD. |
| N2O | Nitrous oxide, in kg CO₂e per USD. |
| HFCs | Hydrofluorocarbons, in kg CO₂e per USD. |
| PFCs | Perfluorocarbons, in kg CO₂e per USD. |
| NF3 | Nitrogen trifluoride, in kg CO₂e per USD. |
| SF6 | Sulfur hexafluoride, in kg CO₂e per USD. |

Values are in current-year dollars: a factor in a 2024 tab applies to spend in 2024 dollars.

### Auxiliary tabs

The data dictionary and five other tabs support the data tabs. The data dictionary is the second tab in the workbook; the others follow the price tabs.

| Tab | What it contains |
|---|---|
| Data Dictionary | Definitions of each field in the data tabs. |
| Exchange rates | Local currency units per US dollar for 148 countries: country code and name, currency, unit, and one column per year from 2018 to 2026. Rates come from Open Exchange Rates (openexchangerates.org) and are Cornerstone's recommended rates for converting spend in local currency before applying the factors. |
| GWP | The 100-year global warming potentials from the IPCC AR6 that express each gas in CO₂e: CO₂ 1, CH₄ 27.9 (to confirm), N₂O 273, SF₆ 24,300 and NF₃ 17,400. HFCs and PFCs are already in CO₂e, so their factor is 1. |
| Cornerstone \<\> NAICS mapping | The correspondence between NAICS 2022 codes and Cornerstone codes: NAICS code and name, Cornerstone code and title, and a weight. When a NAICS industry is split across several Cornerstone codes, the weights show each share and add up to 1. |
| GoodsServices | The 405 sectors with their code, name and description. Cornerstone recommends using this description to map spend categories to emission factors. |
| Locations | Every location code and name used in the model: countries by their three-letter code, and regions. |

## Update cadence

The Cornerstone EEIO follows an annual update cycle. Every year we release a version named after the release year, so Cornerstone 2027 will be released in 2027. Releases are publicly available every October so companies can plan accordingly. Each release builds on one time series of emission factors: Cornerstone EEIO 2026 publishes the 2017 to 2026 series, and Cornerstone EEIO 2027 only adds the 2027 emission factors to it, so results stay continuous from one year to the next.

## Learn more

- **From the field:** *to be added*
- **Cornerstone papers:** *to be added*
- **Code:** *to be added*

+++

:::{div}
:class: page-status
Applies to: RC · Last reviewed: RC
:::
