---
title: Frequently asked questions
---

:::{tip} Summary
Short answers to the questions we hear most about Cornerstone EEIO and spend-based emission factors. Each answer links to the page with the full explanation. Cornerstone EEIO is the successor of USEEIO and CEDA, so many answers compare it with those models.
:::

## About Cornerstone EEIO

:::{dropdown} What is the Cornerstone Sustainability Data Initiative, and how does it relate to USEEIO and CEDA?
Cornerstone launched in August 2025 to bring USEEIO and CEDA together into one open, comprehensive dataset of Scope 3 spend-based emission factors. Cornerstone EEIO 2026 is the first release of that combined model, which builds on both USEEIO and CEDA. Today Cornerstone is the home of 3 additional datasets: eGRID, the GHG EF Hub and Orbae. Learn more at [cornerstonedata.org](https://cornerstonedata.org/), and see the [release candidate note](releases/rc.md) for what is in this release.
:::

:::{dropdown} What is changing compared with USEEIO and CEDA?
Three groups of changes:

1. **A more current US economy that accounts for imports.** US tables are rebuilt for every year from 2017 to 2024, manufacturing uses facility-reported emissions, and imports are modeled where they are made.
2. **Newer data for Europe, the UK and China, and better gap-filling for other countries.**
3. **A validation process that feeds back into the model.** Third-party benchmarks review the sectors behind about 50% of global emissions.

Examples with numbers are in [What changed](releases/rc.md#what-changed) in the release candidate note. The full list is in the [](releases/change-log.md). Side-by-side summaries are in [](releases/summary-useeio.md) and [](releases/summary-ceda.md).
:::

:::{dropdown} Are the changes driven by methodology or by real-world change?
Both. Data updates reflect real-world change, such as new economic, trade and emissions data. Methodology changes reflect modeling improvements, such as modeling US imports by origin and the auto-balanced structural reflection (ABSR) method. See the [](releases/change-log.md) and, for the size of each driver, [](releases/summary-ceda.md#what-drives-the-change-for-ceda-users) and [](releases/summary-useeio.md#what-drives-the-change-for-useeio-users).
:::

:::{dropdown} Why is it called a "release candidate"?
2026 is the first time CEDA and USEEIO are combined in one model, and the first time a time series of emission factors is released from either model. The two-phase release gives companies time to assess the impact on their most recent year of measurements while the time series is under development. The release candidate (2026-rc.1) is published on October 27, 2026. The full release (2026-v1), with the 2017–2026 time series and the model matrices, follows in early December 2026. See [](releases/rc.md).
:::

:::{dropdown} Will the 2024–2026 factors change between the release candidate and the final version?
We don't foresee significant changes, but some sector–country combinations could move because of improvements made while developing the time series. If you need numbers for reporting or rebaselining, wait for the final version. See [](releases/rc.md) for what to expect from the time series.
:::

:::{dropdown} When is the next update?
Releases are published every October so companies can plan for them. The next, Cornerstone EEIO 2027, will be released in October 2027.
:::

:::{dropdown} Did the sectors change?
Yes, slightly. Cornerstone EEIO uses 405 sectors, based on the BEA input-output commodity codes. When the USEEIO and CEDA teams reconciled their US models, they resolved the differences in sector definitions as follows.

**Changes compared to USEEIO**

- Electric utilities are aggregated into one sector (221100). USEEIO split them across three.
- Government and private transit are aggregated into one sector. USEEIO kept them separate.

**Changes compared to CEDA**

- Waste is split into seven sectors. CEDA had a single waste sector.
- Aluminum is split into primary and secondary sectors. CEDA merged them.
- Home appliances are one sector, as in the BEA tables. CEDA had four.

See the [model reconciliation](releases/change-log.md#change-log-model-reconciliation) section of the change log for all 18 differences.
:::

:::{dropdown} Did the file format change?
Yes. The new release is different from Open CEDA and from the USEEIO Supply Chain GHG Emission Factors v1.4. See [](factors/whats-in-a-release.md) for more details.
:::

## Moving from USEEIO or CEDA

:::{dropdown} How much will my footprint change?
It depends on which sectors and countries your spend falls in.

- **Coming from CEDA 2025:** global production-weighted factors fall by 23.3%. In a sample of 400 corporate footprints, the median company sees a 14% decrease.
- **Coming from the USEEIO Supply Chain GHG Emission Factors v1.4:** US factors change by −0.8% overall. In the same sample, the median company sees a 1.3% decrease.

A small median can hide large moves in individual sectors, in both directions. See [](releases/rc.md#how-do-the-emission-factors-change), [](releases/summary-ceda.md) and [](releases/summary-useeio.md).
:::

:::{dropdown} I was using CEDA or USEEIO. Do I need to rebaseline or restate previous years?
We do expect the majority of companies to be above the SBTi rebaselining threshold, but every company will have a different experience and ultimately whether to restate is a decision under your own company's policy and your target framework. This year, the release of the time series is designed for exactly this purpose. Because every year from 2017 to 2026 is built with one methodology, you can recalculate prior years on a consistent basis and compare them. See [](releases/rc.md) for what to expect from the time series, and [](releases/summary-ceda.md) and [](releases/summary-useeio.md) for how much your factors may move.
:::

:::{dropdown} Can I keep using CEDA 2025 or USEEIO for 2026?
We recommend using Cornerstone EEIO 2026 for 2026 measurements, since it supersedes both. If you have a reason to stay on a previous version, apply a price index to it, and explain the choice to your verifier. See [](releases/summary-ceda.md) and [](releases/summary-useeio.md) for what changed.
:::

:::{dropdown} I'd like to explain the switch to Cornerstone in my report. What do you recommend?
State the source (Cornerstone EEIO 2026) and the years you are applying the model to.

Suggested wording: "The changes this year are due to adopting Cornerstone EEIO 2026. The Cornerstone model combines CEDA's global coverage with USEEIO's detailed US data into a single model that supersedes them both. This model was adopted as an improvement in data quality, as it provides a more current picture of the global economy."

For numbers you can cite, see [What changed](releases/rc.md#what-changed) in the release candidate note, [](releases/summary-ceda.md) and [](releases/summary-useeio.md).
:::

## Using the factors

:::{dropdown} How do I choose between producer and purchaser price?
The producer price is what the producer receives. The purchaser price adds trade and transport margins, and is what you pay for a ready-to-buy product. If you're unsure, use producer prices, which are more conservative. If you're confident your spend includes typical margins, for example buying off-the-shelf goods at retail, use purchaser prices. See [](factors/user-guidance.md#choose-between-purchaser-and-producer-price).
:::

:::{dropdown} How do I use the factors for goods bought from, or made in, another country?
Choose the country where the product was produced. If you don't know it, use this order, from most to least relevant:

1. Country of manufacture
2. Country of the supplier
3. Country of purchase
4. Country of your company's headquarters

If a country has no factors of its own, use its regional average. The **Locations** tab shows which of the 249 locations have their own country factors (148 do) and which region each belongs to. See [](factors/user-guidance.md#step-2-choose-the-country).
:::

:::{dropdown} What if my supplier is in a country with no data?
Use the factor for the region it belongs to, or the global average if the region isn't clear. See the **Locations** tab, [](reference/methods-by-country.md) and [](factors/user-guidance.md#step-2-choose-the-country).
:::

:::{dropdown} What do the Scope 3 categories cover?
The factors cover upstream emissions up to the point of purchase, so they apply to the upstream categories: purchased goods and services (1), capital goods (2), upstream transportation and distribution (4), waste generated in operations (5), business travel (6), and upstream leased assets (8), as well as the upstream part of category 3. They don't cover downstream emissions (categories 9–15). See [](factors/user-guidance.md).
:::

:::{dropdown} Why does the same sector have very different factors in different countries?
Three reasons: the emissions intensity of each country (for example its electricity grid), the economic structure of the sector in that country, and the trade structure, meaning where its inputs are imported from. Factors for a sector in countries with detailed data differ for real reasons, but see the tier question below for countries with less data. For worked examples, see [](releases/rc.md#new-data-for-china) and [](releases/rc.md#new-data-for-europe).
:::

## Boundaries and reporting

:::{dropdown} Are the factors suitable for GHG Protocol Scope 3 reporting and for target setting?
Yes. Cornerstone factors are designed for spend-based Scope 3 calculations under the GHG Protocol Corporate Value Chain (Scope 3) Standard, and they follow its minimum boundary conditions: a cradle-to-gate boundary that covers all upstream emissions up to the point of purchase, all seven GHGs reported in CO₂e with IPCC AR6 100-year global warming potentials, and no downstream emissions. See [](factors/user-guidance.md) and [](ee/index.md).
:::

:::{dropdown} Does Cornerstone EEIO follow a cradle-to-gate boundary?
Yes. The factors cover all upstream emissions, from raw material extraction up to the point of purchase. Downstream use and end-of-life emissions are not included. See [](factors/user-guidance.md).
:::

:::{dropdown} Does Cornerstone EEIO account for direct land use change and land management emissions?
The factors do not account for direct land use change, but they do include land management emissions. Farming emissions are counted in the farm sectors, including methane from livestock and rice, N₂O from agricultural soils, and CO₂ from liming and urea. Land use, land-use change and forestry (LULUCF), including carbon removals, is not counted. See [](ee/index.md#what-is-and-isnt-counted).
:::

:::{dropdown} Does Cornerstone EEIO exclude any of the seven GHGs (CO₂, CH₄, N₂O, HFCs, PFCs, SF₆, NF₃)?
No. All seven GHGs are included. The release reports each gas separately, alongside the total, in kg CO₂e per USD. See [](ee/index.md#gases-and-global-warming-potentials) and [](factors/whats-in-a-release.md#producer-and-purchaser-price-tabs).
:::

:::{dropdown} Are biogenic emissions included in the factors?
No, biogenic emissions are not included.
:::

:::{dropdown} Which GWP version is used?
IPCC AR6, 100-year time horizon. Sources that report in AR5 CO₂-equivalents are converted to AR6 gas by gas. Prior versions of USEEIO used earlier GWPs, so a share of the change versus those models comes from the GWP update. Cornerstone EEIO 2026 also fixes a double application of the AR5-to-AR6 conversion. See [](ee/index.md#gases-and-global-warming-potentials), the GWP tab described in [](factors/whats-in-a-release.md#auxiliary-tabs) and the bug fixes in the [](releases/change-log.md).
:::

## Verification, licensing and support

:::{dropdown} How do I trace a factor back to its data sources and methods?
Start with [](reference/methods-by-country.md), which lists the data and methods behind every country. The [IO model](io/index.md) and [GHG extension](ee/index.md) pages describe the method step by step, and the [](releases/change-log.md) lists what changed against USEEIO and CEDA. Methodology decisions are discussed openly on [GitHub](https://github.com/cornerstone-data/methods/discussions). Benchmark results are in [](benchmarking/index.md).
:::

:::{dropdown} How do I cite a specific release?
Cite the version and the release date. For example the Cornerstone EEIO 2026-rc.1 released on October 27th, 2026. See [](factors/whats-in-a-release.md#cover) and [](releases/index.md).
:::

:::{dropdown} What license are the factors under, and what attribution is required?
The factors are published by the Cornerstone Sustainability Data Initiative under a Creative Commons Attribution 4.0 International (CC BY 4.0) license. You can use and redistribute them, including commercially, as long as you give credit and indicate any changes. Please attribute the factors to Cornerstone EEIO. See [](factors/whats-in-a-release.md#cover).
:::

:::{dropdown} What does a country's tier mean for how much I can rely on its factors?
Countries are grouped in four tiers by the input-output data available for them. Tier 0 (US) has detailed annual tables, Tier 1 (China, Japan, South Korea, UK) uses detailed national tables, Tier 2 (60 countries) uses coarser multi-regional tables from FIGARO or ICIO, and Tier 3 (83 countries) has no usable table and uses a proxy table built from other countries. Factors for Tier 3 countries carry more uncertainty. See [](io/country-tiers.md) for the IO data, [](ee/country-tiers.md) for the emissions data and [](reference/methods-by-country.md).
:::

:::{dropdown} Can I get help applying the changes to my footprint?
For more detail, or custom support on how the changes affect your footprint, you can sign up for a demo of the enterprise product [here](https://watershed.com/en-GB/solutions/ceda).
:::

:::{dropdown} How do I report a possible error or ask a question?
Open an issue on [GitHub](https://github.com/cornerstone-data/eeio-docs/issues). Please include the sector code, the country, the year and the tab (`PRO` or `PUR`), so we can reproduce it. For additional support, enquire about the enterprise product [here](https://watershed.com/en-GB/solutions/ceda).
:::

+++

:::{div}
:class: page-status
Applies to: 2026-rc.1 · Last reviewed: 2026-rc.1
:::
