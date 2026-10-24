---
title: Frequently asked questions
---

:::{tip} Summary
Short answers to the questions we hear most about Cornerstone EEIO 2026. Each answer links to the page with the full explanation. Cornerstone EEIO is the successor of USEEIO and CEDA, so many answers compare it with those models.
:::

% Source notes for maintainers (not rendered).
% - Structure adapted from the CEDA 2025 FAQ (Watershed, updated 2025-11-11).
% - Lines marked TODO(confirm) hold claims that need sign-off before the final release.

## About Cornerstone EEIO 2026

:::{dropdown} What is Cornerstone EEIO 2026?
A multi-regional environmentally-extended input-output (EEIO) model that produces spend-based greenhouse gas emission factors, in kg CO₂e per USD, for 405 sectors across 148 countries, 21 regional averages and one global average. It combines USEEIO's detailed picture of the US economy with CEDA's global coverage and trade modeling. See [](releases/rc.md).
:::

:::{dropdown} What is the Cornerstone Sustainability Data Initiative, and how does it relate to USEEIO and CEDA?
Cornerstone launched in August 2025 to bring USEEIO and CEDA together into one open, comprehensive dataset of Scope 3 spend-based emission factors. Cornerstone EEIO 2026 is the first release of that combined model. It is the continuation of both USEEIO v1.4 and CEDA 2025. Learn more at [cornerstonedata.org](https://cornerstonedata.org/).
:::

:::{dropdown} What is changing compared with USEEIO and CEDA?
Three groups of changes:

1. **A more current US economy that accounts for imports.** US tables are rebuilt for every year from 2017 to 2024, manufacturing uses facility-reported emissions, and imports are modeled where they are made.
2. **Newer data for Europe, the UK and China, and better gap-filling for other countries.**
3. **A validation process that feeds back into the model.** Third-party benchmarks review the sectors behind about 50% of global emissions.

The full list is in the [](releases/change-log.md). Side-by-side summaries are in [](releases/summary-useeio.md) and [](releases/summary-ceda.md).
:::

:::{dropdown} Are the changes driven by methodology or by real-world change?
Both. Data updates reflect real-world change, such as new economic, trade and emissions data. Methodology changes reflect modeling improvements, such as modeling US imports by origin and the auto-balanced structural reflection (ABSR) method. Against CEDA 2025, data updates add about 5.8% to the global production-weighted factor and methodology changes remove about 27.5%. Against USEEIO v1.4 (US), data updates add 0.4% and methodology changes remove 1.2%.
:::

:::{dropdown} How much will my footprint change?
It depends on which sectors and countries your spend falls in.

- **Coming from CEDA 2025:** global production-weighted factors fall by 23.3%. In a sample of 400 corporate footprints, the median company sees a 14% decrease.
- **Coming from USEEIO v1.4:** US factors change by −0.8% overall. In the same sample, the median company sees a 1.3% decrease.

A small median can hide large moves in individual sectors, in both directions. See [](releases/summary-ceda.md) and [](releases/summary-useeio.md).
:::

:::{dropdown} The overall change is a decrease, so why are some of my factors increasing?
Several drivers push individual factors up:

- **US imports.** USEEIO treated the US as a closed economy. Cornerstone models each import in the country that made it. Many imports come from more emissions-intensive economies such as China and India, so US factors tend to rise by 10 to 30% on average. This is the main upward pressure for USEEIO users.
- **Facility-reported emissions.** For example, US cement now matches the totals reported by cement plants, which USEEIO undercounted by about 20%.
- **New country data.** For example, China's battery factor rises by about 30% as production shifted from lead-acid to lithium-ion.

Other factors fall. For example, European electricity factors fall in every EU country, driven by more renewables and higher energy prices.
:::

:::{dropdown} Are these changes expected?
Yes. They come from newer data and from better modeling, and each is documented in the [](releases/change-log.md). Where a gap against third-party benchmarks remains, it is documented as a known discrepancy (see [](benchmarking/index.md)).
:::

:::{dropdown} Why is it called a "release candidate"?
2026 is the first time CEDA and USEEIO are combined in one model, and the first time a time series is released. The two-phase release gives companies time to assess the impact on their most recent year of measurements while the time series is under development. The release candidate (2026-rc.1) is published on October 27, 2026. The final version (2026-v0.1), with the 2017–2026 time series, follows in early December 2026. See [](releases/rc.md).
:::

:::{dropdown} Will the 2024–2026 factors change between the release candidate and the final version?
We don't foresee significant changes, but some sector–country combinations could move because of improvements made while developing the time series. If you need numbers for reporting or rebaselining, wait for the final version.
:::

:::{dropdown} Why did the versioning change from numbers to years?
Each release is named after the year it is published, so Cornerstone EEIO 2026 is released in 2026 and the 2027 version in 2027. This replaces the different naming schemes used by USEEIO (v1.4) and CEDA (v4.1, then CEDA 2025).
:::

:::{dropdown} When is the next update?
Releases are published every October so companies can plan for them. The next, Cornerstone EEIO 2027, will be released in October 2027. Cornerstone EEIO 2026 will stay methodologically stable for at least five years, so you have a consistent basis to rebaseline and set targets.
:::

:::{dropdown} Is this just a price index adjustment of the previous numbers?
No. Each release incorporates the most recent economic, trade and emissions data for each country. Price indices are applied only to years after the base year, for which no reported data exists yet (for example 2025 and 2026 are adjusted from the 2024 base year).
:::

:::{dropdown} Did the sectors change?
Yes, slightly. Cornerstone EEIO uses 405 sectors, based on the BEA input-output commodity codes, versus 400 in CEDA. Following the model reconciliation, the waste sector is split into seven sectors and aluminum into primary and secondary. Home appliances are a single sector. A NAICS-to-Cornerstone mapping tab is included in the release, so you can map your existing categories. See the [](releases/change-log.md#change-log-model-reconciliation).
:::

:::{dropdown} Did the file format change?
The release is one Excel workbook with a cover, a data dictionary, a producer-price tab and a purchaser-price tab for each year, and five auxiliary tabs. See [](factors/whats-in-a-release.md). 
% TODO(confirm): whether the layout differs from the CEDA 2025 files customers know, and whether a CSV/long format is also published.
:::

## Which release to use

:::{dropdown} Which release should I use for my 2026 measurements?
Use the Cornerstone EEIO 2026 factors from the `2026PRO` or `2026PUR` tab. We recommend matching the release year to the year being measured. Until the final version is published in December, treat the factors as a release candidate.
:::

:::{dropdown} Can I use the release candidate for my 2024 and 2025 measurements?
Yes. It has factors for 2024, 2025 and 2026 dollars. The base year is 2024, so 2024 is the year most directly backed by data, and the 2025 and 2026 factors are adjusted from it with price indices. If your reporting is being finalized, consider waiting for the final version.
:::

:::{dropdown} Why can 2026 measurements use factors built on 2024 data?
The underlying sources are published with a lag. For example, national input-output tables and GHG inventories typically cover a year that is one to three years old. Every spend-based database inherits this lag, so it is standard to match the release to the year of measurement. Cornerstone builds 2025 and 2026 factors by adjusting the 2024 base year with price indices.
:::

:::{dropdown} My reporting year isn't the calendar year. Which factors should I use?
Use the factors for the calendar year in which most of your data falls. If your data is split equally, use the newer set. For example, for a fiscal year from April 1, 2025 to March 31, 2026, use the 2026 factors. Alternatively, apply the 2026 factors to data from January 1, 2026 and the previous year's factors before that.
:::

:::{dropdown} I'm in mid-2026 or later. Can I already measure 2027?
Use the 2026 factors for the portion of 2027 you've measured, and update when Cornerstone EEIO 2027 is published in October 2027. If you adjust the 2026 factors yourself, apply only a price index (for example a national price index) and don't edit the factors otherwise. Auditors generally accept this approach.
% TODO(confirm): confirm the guidance wording with the audit/assurance team.
:::

:::{dropdown} I'm measuring a past year (2017–2023). What should I use?
The final release, due in December 2026, will include a time series from 2017 to 2026. All years use the same methodology, and only the underlying country data changes, so each year captures decarbonization that happened that year (for example the US electricity grid). Until then, use the previous version you already use (CEDA 2025 or USEEIO v1.4).
:::

:::{dropdown} I was using CEDA or USEEIO. Do I need to rebaseline or restate previous years?
The time series is designed for exactly this. Because every year from 2017 to 2026 is built with one methodology, you can recalculate prior years on a consistent basis and compare them. Whether to restate is a decision under your own company's policy and your target framework. Rebaselining thresholds are usually based on significance, so talk to your verifier. See [](releases/summary-ceda.md) and [](releases/summary-useeio.md) for the expected change.
% TODO(confirm): wording about SBTi / GHG Protocol recalculation thresholds.
:::

:::{dropdown} Can I keep using CEDA 2025 or USEEIO for 2026?
We recommend using Cornerstone EEIO 2026 for 2026 measurements, since it supersedes both. If you have a reason to stay on a previous version, apply a price index to it, and be ready to explain the choice to your verifier.
% TODO(confirm): whether CEDA 2025 and USEEIO v1.4 stay available, and for how long.
:::

## Using the factors

:::{dropdown} Should I use `D` or `N`?
Use `N`, the total emission factor, for purchased goods and services. It includes the emissions of the sector itself and of its whole supply chain. `D` covers only what the sector emits directly. Using `D` leaves out the supply chain, and adding `D` to `N` double counts. The factor tabs in the release report the total (`Total GHGs`) and each gas. See [](reference/notation.md).
:::

:::{dropdown} How do I find the right sector for a purchase? What if it spans several sectors?
Match the purchase to the *good or service you bought*, not to the supplier's industry. Use the description in the **Sector Descriptions** tab (405 sectors), and the **NAICS to Cornerstone mapping** tab if your categories are NAICS-based. If a purchase spans several sectors, split the spend across them, or choose the one that best describes most of the spend. See [](factors/user-guidance.md).
:::

:::{dropdown} Do I need to add up factors across the supply chain (for example raw steel plus steel products)?
No. Factors already include all upstream emissions, so a manufactured good already includes the raw materials. For example, the factor for a steel product includes the iron and steel mill behind it. Choose the single factor closest to what you bought. This applies to every industry, including food, metals and plastics.
:::

:::{dropdown} How do I choose between producer and purchaser price?
The producer price is what the producer receives. The purchaser price adds trade and transport margins, and is what you pay for a ready-to-buy product. If you're unsure, use producer prices, which are more conservative. If you're confident your spend includes typical margins, for example buying off-the-shelf goods at retail, use purchaser prices. See [](factors/user-guidance.md).
% TODO(confirm): align with the User guidance page (the plan describes three columns).
:::

:::{dropdown} Where do the margins come from, and do they apply to every country?
Cornerstone converts producer-price factors to purchaser-price factors using US trade and transport margins for every country, since comparable margin data isn't available everywhere. Where a country's actual margins differ, its purchaser-price factors could be too high or too low. Producer-price factors aren't affected.
:::

:::{dropdown} What year and currency are the factors in?
Factors are in kg CO₂e per USD in current-year dollars, so a factor in the 2026 tab applies to spend in 2026 US dollars. To use spend in another currency, convert it to USD at the year-of-spend rate, using the **Exchange Rates** tab (local currency per USD for 221 countries and territories, from Open Exchange Rates), then apply the factor for that year. See [](factors/user-guidance.md).
:::

:::{dropdown} My spend is in a different year than the factor tabs. What should I do?
Prefer the tab for the year of your spend. If the release doesn't have your year, use a sector-specific price index to bring your spend to a year that does, rather than a general consumer price index. Cornerstone doesn't support alternative monetary adjustments beyond that, because they change the resulting factor significantly.
% TODO(confirm): which price index the 2025/2026 adjustment uses (BEA sector-level?), to state it here.
:::

:::{dropdown} Can I apply my own price index adjustments?
For years covered by the release, use the factors as published, because they are traceable and easy to audit. Only adjust beyond the published years, and keep the adjustment limited to a price index.
:::

:::{dropdown} How do I use the factors for goods bought from, or made in, another country?
Choose the country where the product was produced. If you don't know it, use this order, from most to least relevant:

1. Country of manufacture
2. Country of the supplier
3. Country of purchase
4. Country of your company's headquarters

If a country has no factors of its own, use its regional average. The **Locations** tab shows which of the 249 locations have their own country factors (148 do) and which region each belongs to.
:::

:::{dropdown} What if my supplier is in a country with no data?
Use the factor for the region it belongs to, or the global average if the region isn't clear. See the **Locations** tab and [](reference/methods-by-country.md).
:::

:::{dropdown} What do the Scope 3 categories cover?
The factors cover upstream emissions up to the point of purchase, so they apply to the upstream categories: purchased goods and services (1), capital goods (2), upstream transportation and distribution (4), waste generated in operations (5), business travel (6), and upstream leased assets (8), as well as the upstream part of category 3. They don't cover downstream emissions (categories 9–15).
% TODO(confirm): category 3 treatment, and whether to list 7 (employee commuting) as supported.
:::

:::{dropdown} Can I use the factors for purchased electricity (Scope 2)?
No. Use utility or grid emission factors with your own activity data (kWh) for Scope 2, and for any other category where you have activity data. Spend-based factors are for screening and for purchases where activity data isn't available.
:::

:::{dropdown} What aren't the factors designed for?
Cornerstone factors are sector averages per dollar. They are not suited to comparing two products or two suppliers in the same sector, to showing the effect of a supplier's own reduction efforts, or to categories the model doesn't cover (government services, taxes, fees and interest, used assets). When you have supplier-specific or activity data, use it in place of spend-based factors. Use spend-based factors for screening, hotspotting and categories where better data isn't available.
% TODO(confirm): link to intro/uses-and-limits.md once it is written and added to the nav in myst.yml.
:::

:::{dropdown} Are the factors suitable for GHG Protocol Scope 3 reporting and for target setting?
Cornerstone factors are designed for spend-based Scope 3 calculations under the GHG Protocol Corporate Value Chain (Scope 3) Standard. Guidance from the GHG Protocol and from target-setting bodies sets what data quality is expected, so check the current requirements for your framework.
% TODO(confirm): GHG Protocol third-party database listing and SBTi acceptance status for Cornerstone EEIO 2026 (CEDA was on the GHG Protocol's list).
:::

## Understanding the results

:::{dropdown} Why did a factor change between releases?
Look at three things in order: the data (new tables or emissions for that country), the methodology (for example US imports, ABSR, model reconciliation) and the price year (a different dollar year changes factors even with no real change). The [](releases/change-log.md) lists every change, and the release notes give examples.
:::

:::{dropdown} Why does the same sector have very different factors in different countries?
Three reasons: the emissions intensity of each country (for example its electricity grid), the economic structure of the sector in that country, and the trade structure, meaning where its inputs are imported from. Factors for a sector in countries with detailed data differ for real reasons, but see the next question for countries with less data.
:::

:::{dropdown} What does a country's tier mean for how much I can rely on its factors?
Countries are grouped in four tiers by the input-output data available for them. Tier 0 (US) has detailed annual tables, Tier 1 (China, Japan, South Korea, UK) uses detailed national tables, Tier 2 (60 countries) uses coarser multi-regional tables from FIGARO or ICIO, and Tier 3 (83 countries) has no usable table and uses a template built from other countries, scaled to the country's emissions per unit of GDP and its own electricity intensity. Factors for Tier 3 countries carry more uncertainty. See [](io/country-tiers.md) and [](reference/methods-by-country.md).
:::

:::{dropdown} How do the factors compare with USEEIO, CEDA, EXIOBASE or other datasets?
Differences come from the data vintage, the sector classification, the price basis and the treatment of trade. Compare on the same basis, meaning the same year, currency and price basis, before reading the gap. Cornerstone benchmarks against about 1,000 third-party sources for the sectors behind about 50% of global emissions, and documents the gaps that remain. See [](benchmarking/index.md).
:::

:::{dropdown} Are emissions counted where they occur, or by where the producer is based?
It depends on the source. National inventories (US, China) use the territorial basis: emissions within the country's borders. Air emissions accounts, FIGARO and ICIO use the residence basis: emissions by a country's resident businesses wherever they occur. The model uses each source as published. The two differ most for countries with large international transport fleets or many visitors. See [](ee/index.md).
:::

:::{dropdown} What's included in the factors?
- **Boundary:** cradle to gate, meaning all upstream emissions up to the point of purchase.
- **Gases:** all seven (CO₂, CH₄, N₂O, HFCs, PFCs, SF₆, NF₃), reported separately and as a total in CO₂e.
- **GWPs:** IPCC AR6 100-year values (CH₄ is 29.8 for fossil and 27.0 for non-fossil methane, and N₂O is 273). The **GWP** tab in the release lists them.
- **Land:** farming emissions are counted. Land use, land-use change and forestry (LULUCF) is not, including carbon removals.
- **Not counted:** household direct emissions (such as fuel burned at home), since they don't come from a producing sector.

% TODO(confirm): biogenic CO2 statement (CEDA excluded it), transport well-to-wheel treatment, and whether capital goods are treated as upstream purchases for every sector.
:::

:::{dropdown} Which GWP version is used?
IPCC AR6, 100-year time horizon. Sources that report in AR5 CO₂-equivalents are converted to AR6 gas by gas. Prior versions of USEEIO used earlier GWPs, so a share of the change versus those models comes from the GWP update. Cornerstone EEIO 2026 also fixes a double application of the AR5-to-AR6 conversion.
:::

:::{dropdown} Do the factors come with uncertainty ranges?
Not in this release. Spend-based factors are sector averages, so uncertainty is higher for individual products, and for Tier 3 countries. See the assumptions in [](io/index.md) and the validation results in [](benchmarking/index.md).
% TODO(confirm): whether uncertainty estimates are planned for the final version.
:::

:::{dropdown} Why did my factor for [sector] in [country] change by so much?
Large moves in a single sector are possible, and some are explained in the release notes (for example batteries in China, power in Germany, and light trucks in the US). If you can't explain a change with the [](releases/change-log.md), please report it. See "How do I report a possible error" below.
:::

## For verifiers and auditors

:::{dropdown} How do I trace a factor back to its data sources and methods?
Start with [](reference/methods-by-country.md), which lists the data and methods behind every country. The [IO model](io/index.md) and [GHG extension](ee/index.md) pages describe the method step by step, and the [](releases/change-log.md) lists what changed against USEEIO and CEDA. Methodology decisions are discussed openly on [GitHub](https://github.com/cornerstone-data/methods/discussions).
:::

:::{dropdown} How do I cite a specific release?
Cite the version, the release date and the Zenodo DOI, which are on the cover tab of the workbook. The release candidate (2026-rc.1) is archived at [doi.org/10.5281/zenodo.23396891](https://zenodo.org/doi/10.5281/zenodo.23396891). See [](releases/index.md).
% TODO(confirm): suggested citation text, and whether the final release gets a new DOI.
:::

:::{dropdown} How is the model validated and benchmarked?
Cornerstone reviews the sectors behind about 50% of global emissions against third-party benchmarks built from about 1,000 sources. Each review ends in a sharper benchmark, a model improvement or a documented known discrepancy. See [](benchmarking/index.md) and [](validation/index.md).
:::

:::{dropdown} Does the model follow the GHG Protocol boundary conditions?
Cornerstone EEIO follows a cradle-to-gate boundary and includes all seven Kyoto gases. Land use change isn't included, but farming emissions are.
% TODO(confirm): GHG Protocol minimum boundary statement and SBTi methodology questions (well-to-wheel, direct land-use change), as in the CEDA 2025 FAQ.
:::

:::{dropdown} Is the model open? Where are the code and data?
The emission factors are free to use. Documentation and the methodology discussions are public at [github.com/cornerstone-data](https://github.com/cornerstone-data).
% TODO(confirm): code repository availability and the license of the source data.
:::

:::{dropdown} Which published methodology supports relying on the factors?
The approach builds on the peer-reviewed hybrid-LCA and EEIO literature, including Suh et al. (2004) on system boundary selection with hybrid approaches and Suh (2005) on developing a sectoral environmental database for input-output analysis. See the references on each methodology page.
% TODO(confirm): add the final reference list (carry over from CEDA 2025 FAQ, plus the multi-regional and ABSR references).
:::

## Practical

:::{dropdown} Where do I download the factors?
On [Zenodo](https://zenodo.org/doi/10.5281/zenodo.23396891). Each release is a single Excel workbook. See [](factors/whats-in-a-release.md).
:::

:::{dropdown} What license are the factors under, and what attribution is required?
The factors are published by the Cornerstone Sustainability Data Initiative under a Creative Commons Attribution 4.0 International (CC BY 4.0) license. You can use and redistribute them, including commercially, as long as you give credit and indicate any changes.
:::

:::{dropdown} I'd like to explain the switch to Cornerstone in my report. What do you recommend?
State the source (Cornerstone EEIO 2026 and its DOI), the base year and dollar year, the reason you switched, and that the change in your emissions has two parts: real-world and data changes, and methodology changes. If you're coming from USEEIO, mention that imports are now modeled by country of origin, which tends to increase US factors. If you're coming from CEDA, mention the new China and Europe data. Quantify the effect if you can with the release's change summaries.
:::

:::{dropdown} Can I get help applying the changes to my footprint?
For more detail, or custom support on how the changes affect your footprint, you can sign up for a demo of the enterprise product [here](https://watershed.com/en-GB/solutions/ceda).
:::

:::{dropdown} How do I report a possible error or ask a question?
Open an issue on [GitHub](https://github.com/cornerstone-data/eeio-docs/issues). Please include the sector code, the country, the year and the tab (`PRO` or `PUR`), so we can reproduce it.
:::

+++

:::{div}
:class: page-status
Applies to: 2026-rc.1 · Last reviewed: 2026-rc.1
:::
