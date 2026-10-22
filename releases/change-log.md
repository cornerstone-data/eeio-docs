---
title: "Change log"
---

:::{tip} Summary
This table summarizes all the data and methodology changes behind Cornerstone EEIO 2026, compared to both USEEIO v1.4 and CEDA 2025.
:::

| Type of change | Category | What changed? |
|---|---|---|
| Data update | US data | Updated the U.S. GHG emissions data (totals and by sector) released by the **University of Maryland Greenhouse Gas Inventory and Analysis (UMD GHGIA)** [(link)](https://ghgi.cgs.umd.edu/data.html) from **2023 to 2024**. |
| Data update | UK data | Updated the UK IO tables released by the **U.K. Office for National Statistics** [(link)](https://www.ons.gov.uk/economy/nationalaccounts/supplyandusetables/datasets/ukinputoutputanalyticaltablesdetailed) from **2022 to 2023**, incorporating the most recent benchmark IO tables. Updated the U.K. GHG emissions data released by the **U.K. Office for National Statistics** [(link)](https://www.ons.gov.uk/economy/environmentalaccounts/datasets/ukenvironmentalaccountsatmosphericemissionsgreenhousegasemissionsbyeconomicsectorandgasunitedkingdom) from **2022 to 2023**, incorporating the most recent benchmark IO tables. |
| Data update | China data | Updated the China IO tables released by the **National Bureau of Statistics of China (NBS)** [(link)](https://www.stats.gov.cn/sj/ndsj/2025/html/sm03.htm) from **2020 to 2023**, incorporating the most recent benchmark IO tables. Updated the China GHG emissions data released by **Our World in Data (OWID)** [(link)](https://github.com/owid/co2-data), **Community Emissions Data System (CEDS)** [(link)](https://zenodo.org/records/10904361), and **Emissions Database for Global Atmospheric Research (EDGAR)** [(link)](https://edgar.jrc.ec.europa.eu/dataset_ghg80) from **2020 to 2023**, incorporating the most recent benchmark IO tables. |
| Data update | Europe & other global data | Updated the tier 2 country IO tables using Eurostat's Full International and Global Accounts for Research in Input-Output Analysis (FIGARO) [(link)](https://ec.europa.eu/eurostat/en/web/esa-supply-use-input-tables/database) for **2023** data where available and otherwise to **2020 OECD IO tables** [(link)](https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html). Updated the tier 2 country emissions data using **FIGARO's 2023 data** [(link)](https://ec.europa.eu/eurostat/en/web/esa-supply-use-input-tables/database) where available and otherwise to **2020 OECD IO tables** [(link)](https://www.oecd.org/en/data/datasets/inter-country-input-output-tables.html). |
| Data update | Global trade data | Updated global trade data released by the **United Nations Comtrade (BACI)** [(link)](https://www.cepii.fr/DATA_DOWNLOAD/baci/doc/baci_webpage.html) from **2023 to 2024**. Global trade data is supplemented with **FIGARO trade data** [(link)](https://ec.europa.eu/eurostat/en/web/esa-supply-use-input-tables/database) to fill gaps in BACI data. |
| Methodology improvements | Model reconciliation | USEEIO and CEDA teams reviewed 18 differences between the models for the US and either adopted one of the model's approaches or proposed an improvement. The differences can be categorized into 3 types: sectors schema, treatment of economic data and GHG attribution. For details on the differences, see the [model reconciliation section](#change-log-model-reconciliation) below. |
| Methodology improvements | Auto-balancing structural reflection (ABSR) | Improved disaggregation of non-US economic data into detailed sectors using a new block scaling method. |
| Methodology improvements | US nowcasting and facility reported data | Estimated detailed 2024 US IO tables from primary sources from 2017 to 2024, replicating the tables produced by the BEA. Used facility reported data to allocate emissions of manufacturing sectors, instead of survey data. |
| Methodology improvements | Bug fixes | Corrected errors in HS mapping. Corrected double application of AR5 to AR6 conversion. Corrected loading of the UK IO table. |
| Methodology improvements | Benchmark informed improvements | Leveraged third-party benchmark data created with ~1,000 data sources to review key sectors that drive ~50% of global emissions, producing one of three outcomes: benchmark improvements, model improvements or documentation of known discrepancies. More on why we benchmark in [](../benchmarking/index.md). |

(change-log-model-reconciliation)=
## Model reconciliation

The USEEIO and the US portion of CEDA had 18 methodological differences. Cornerstone EEIO adopted either one of the approaches for each difference or improved the approach. For more details on each topic, see our open discussions on [GitHub](https://github.com/cornerstone-data/methods/discussions).

### Sectors schema

| Item | USEEIO | CEDA | Cornerstone |
|---|---|---|---|
| **Waste sector** ([#8](https://github.com/cornerstone-data/methods/discussions/8)) | Split into 7 sectors | Single sector | **USEEIO: split into 7** |
| **Aluminum** ([#9](https://github.com/cornerstone-data/methods/discussions/9)) | Primary and secondary separate | Merged | **USEEIO: separate** |
| **Home appliances** ([#24](https://github.com/cornerstone-data/methods/discussions/24)) | One sector, as BEA | Four sectors | **USEEIO: one sector** |
| **Accounting-only commodities** ([#1](https://github.com/cornerstone-data/methods/discussions/1)) | Kept in tables (inferred) | Removed, output recalculated | **CEDA: remove** |

### Economic data

| Item | USEEIO | CEDA | Cornerstone |
|---|---|---|---|
| **Redefinitions** ([#3](https://github.com/cornerstone-data/methods/discussions/3)) | Before | After | **CEDA: after** |
| **Electric utilities** ([#7](https://github.com/cornerstone-data/methods/discussions/7)) | 3 separate industries | One aggregated industry | **CEDA: aggregate** |
| **Transit** ([#44](https://github.com/cornerstone-data/methods/discussions/44)) | Government and private separate | Aggregated | **CEDA: aggregate** |
| **B matrix steps** ([#16](https://github.com/cornerstone-data/methods/discussions/16)) | Adjust price, divide, convert | Divide, convert, adjust price | **USEEIO** |
| **Scrap** ([#5](https://github.com/cornerstone-data/methods/discussions/5)) | Adjusted out in v1, kept in v2 | Adjusted out of Make table | **Adjust scrap out** |

### GHG attribution

| Item | USEEIO | CEDA | Cornerstone |
|---|---|---|---|
| **Electricity across sectors** ([#33](https://github.com/cornerstone-data/methods/discussions/33)) | Split across 3 electric sectors | All in one sector (221100) | **CEDA: no split** |
| **Core GHG schema** ([#47](https://github.com/cornerstone-data/methods/discussions/47)) | NAICS codes, mapped to BEA later | BEA sectors directly | **Hybrid: NAICS plus BEA** |
| **Mobile Combustion Emissions** ([#39](https://github.com/cornerstone-data/methods/discussions/39)) | GHGI Table 3-13 by vehicle type | Two-layer fuel allocation, wide government spread | **Hybrid: Updated approach** |
| **Households** ([#41](https://github.com/cornerstone-data/methods/discussions/41)) | Tracked as sector F01000 | Not always tracked | **USEEIO: track F01000** |
| **Use table for attribution** ([#45](https://github.com/cornerstone-data/methods/discussions/45)) | Supply-Use, before redefinitions | Make/Use, after redefinitions | **CEDA: after redefinitions** |

For the summaries of these changes, see [](summary-useeio.md) and [](summary-ceda.md).

+++

:::{div}
:class: page-status
Applies to: RC · Last reviewed: RC
:::
