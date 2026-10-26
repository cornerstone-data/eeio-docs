---
title: Cornerstone EEIO
site:
  hide_outline: true
---

The Cornerstone EEIO model is a multi-regional environmentally-extended input-output model. It links countries' economies through international trade and attaches greenhouse gas emissions to every sector. Cornerstone EEIO is the successor of the USEEIO and CEDA models; see [](intro/cornerstone-eeio-history.md).

Cornerstone EEIO 2026 was developed to produce cradle-to-gate emission factors for the goods and services that organizations commonly buy. These **emission factors are the primary data product** of the 2026 release: spend-based factors, in kg CO₂e per USD, for 405 sectors across 148 countries, 21 regional averages and one global average. They are most commonly used for Scope 3 measurements in corporate inventories and for academic and policy research.

The [2026-rc release](releases/rc.md) publishes the spend-based GHG emission factors. The full 2026-v1 release adds a 2017–2026 time series and will be accompanied by the model matrices, in a format still to be decided.

:::{card} Understand EEIO
:link: intro/what-is-eeio.md
New to EEIO? Start with a short, visual primer on how EEIO models work and where Cornerstone EEIO comes from.
:::

## Technical documentation

How the model is built, how the emission factors are calculated from it, and how both are checked.

::::{grid} 1 2 2 3
:class: track-technical

:::{card} The IO model
:link: io/index.md
How country tables are linked through trade into one global model.
:::

:::{card} The GHG extension
:link: ee/index.md
Where the emissions data come from and how they reach each sector.
:::

:::{card} Calculating the emission factors
:link: factors/calculation.md
From the model matrices to published factors, including price-year and purchaser-price adjustments.
:::

:::{card} Margin emission factors
:link: factors/margins.md
How the emission factors of trade and transport margins are prepared.
:::

:::{card} The code
:link: code/index.md
The pipelines that build the model and publish the emission factors.
:::

:::{card} How we validate
:link: validation/index.md
The checks behind each release.
:::

:::{card} How we benchmark
:link: benchmarking/index.md
How the results compare with independent evidence.
:::

:::{card} Look up a country
:link: reference/methods-by-country.md
The methods and data behind each country in the model.
:::

::::

## Releases

What each release contains and how it differs from USEEIO and CEDA.

::::{grid} 1 2 2 3
:class: track-releases

:::{card} 2026-rc release note
:link: releases/rc.md
The first release candidate, with the spend-based emission factors.
:::

::::

## User guide

How to get the emission factors and apply them to your own data.

::::{grid} 1 2 2 3
:class: track-user

:::{card} What's in a release
:link: factors/whats-in-a-release.md
The emission factor workbook, tab by tab.
:::

:::{card} Applying the factors
:link: factors/user-guidance.md
Choosing the sector, country, year, currency and price basis.
:::

:::{card} FAQs
:link: faq.md
Short answers to common questions.
:::

::::
