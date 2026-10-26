---
title: "The code behind Cornerstone EEIO"
---

:::{tip} Summary
Cornerstone EEIO is built by two code pipelines. The open-source `bedrock` pipeline builds the U.S. part of the model. The `ceda` pipeline, currently closed-source, builds the rest of the global multi-regional model and calculates and publishes the emission factors.
:::

| Model component | Built by |
|---|---|
| U.S. Make and Use tables, direct requirements (`Adom`, `Aimp`), output and final demand | `bedrock` |
| U.S. GHG extension (`B`) | `bedrock` |
| U.S. trade and transport margins (`A_margin`) and price indexes | `bedrock` |
| IO tables and emissions for all other countries (Tiers 1 to 3) | `ceda` |
| Trade linking, balancing and the multi-regional total requirements (`L`) | `ceda` |
| Emission factors (`M`, `N`), regional averages, price-year and purchaser-price adjustments, margin emission factors | `ceda` |
| Published release files | `ceda` |

## `bedrock`: the U.S. model

[`bedrock`](https://github.com/cornerstone-data/bedrock) is an open-source pipeline that builds the U.S. components of the model. It brings together the U.S. methods of USEEIO and CEDA. It produces the Cornerstone nowcast Make and Use tables for 2017 to 2024 on BEA's 2017 detailed schema, along with the U.S. direct requirements, GHG extension, margins and price indexes listed above. Every methodology choice is set in a configuration file, so the effect of each choice can be tested on its own, and the results of each release are pinned so they can be reproduced exactly. The code is publicly available on GitHub under the Cornerstone Data Pipeline Attribution License, which requires attribution when it is used.

## `ceda`: the global model and the emission factors

The `ceda` pipeline builds the rest of the global multi-regional model and produces the published emission factors. It takes the U.S. components from a pinned `bedrock` release, adds the IO tables and emissions data for the Tier 1, Tier 2 and Tier 3 countries, maps them to the 405 common sectors with {term}`ABSR`, links the countries through bilateral trade, balances the multi-regional table with {term}`RAS`, and solves for the total requirements. It then calculates the emission factors, the regional and global averages, the factors for each year and at purchaser price, and the margin emission factors, and writes the release files (see [](../factors/calculation.md)). The pipeline grew out of the code behind CEDA and is maintained by Cornerstone. It is currently closed-source.

## How the code is checked

Both pipelines are tested automatically on every change, and their main outputs are compared with pinned reference results. See [](../validation/index.md#code-validation).

+++

:::{div}
:class: page-status
Applies to: 2026-rc.1 · Last reviewed: 2026-rc.1
:::
