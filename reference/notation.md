---
title: Notation cheat sheet
---

:::{tip} Summary
The same few named variables are used on every page, in our data releases, and in our tools.
:::

In the multi-regional model, every row and column is a country–sector pair. `D` and `N` are the two results most users work with.

| Symbol | Name | In words | Units |
|---|---|---|---|
| `A` (`Adom`, `Aimp`) | Direct requirements | Inputs bought per dollar of a sector's output, split into domestic and imported | \$ / \$ |
| `L` | Total requirements (Leontief inverse) | All the output needed across the whole supply chain per dollar of final demand | \$ / \$ |
| `V` | Supply (Make) table | Production of each commodity by each domestic industry | \$ |
| `U` (`Udom`, `Uimp`) | Use table | Commodities bought by each industry as inputs, split into domestic and imported | \$ |
| `x` | Industry output | Total output of each industry: the row sums of `V` | \$ |
| `q` | Commodity output | Total domestic output of each commodity: the column sums of `V` | \$ |
| `y` (`ydom`, `yimp`) | Final demand | Purchases by households, government, investment, and exports, split into domestic and imported | \$ |
| `ynab` | Final demand for the national accounting balance | Final demand for domestic production: `ydom` plus exports | \$ |
| `E` | Emissions | Emissions of each gas by each sector, weighted by AR6 GWPs | kg CO₂e |
| `B` | Direct emission intensities | Emissions of each gas per dollar of a sector's own output, in CO₂e | kg CO₂e / \$ |
| `M` | Total emission intensities by gas | `B × L`: emissions of each gas across the supply chain per dollar, in CO₂e | kg CO₂e / \$ |
| **`D`** | **Direct emission factors** | `B` summed over gases: CO₂e emitted by the sector itself per dollar of output | kg CO₂e / \$ |
| **`N`** | **Total emission factors** | `D × L`, or `M` summed over gases: CO₂e across the whole supply chain per dollar of purchases | kg CO₂e / \$ |
| `A_margin` | Margin coefficients | Trade and transport margins paid to each margin sector per dollar of a commodity at producer price | \$ / \$ |
| `φ` | Producer share of purchaser price | `1 ÷ (1 + Σ A_margin)`: converts producer-price factors to purchaser price | \$ / \$ |
| `PI` | Price index | U.S. BEA chain-type price index for gross output, by sector (2017 = 100) | index |

:::{note} Draft
:class: dropdown
Team to confirm the final list and whether any others (e.g., value added, `U`/`V` tables) should be introduced (plan §2.4). To be redesigned as one visual card.
:::

+++

:::{div}
:class: page-status
Applies to: 2026-rc.1 · Last reviewed: 2026-rc.1
:::
