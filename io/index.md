---
title: "The IO model: overview"
---

:::{tip} 
Cornerstone uses standardized national input-output tables to represent production recipes and it links them with trade data, thus representing domestic and international supply chains.
:::

## Preparing the IO tables

Every country enters the model as a national IO table, but countries don't all start from the same kind of table. The first step is to collect the best available table for each country and record where it came from: the source, version, year, valuation, and sector detail. Which table we start from depends on the country's {term}`tier <Country tier>`: the U.S. starts from Cornerstone's nowcast {term}`Make and Use tables <Make/Use framework>` for 2024, after {term}`redefinitions <Redefinitions>` and following BEA's 2017 detailed schema, while other countries start from national statistical agency tables, {term}`FIGARO` or the {term}`OECD ICIO`, or a template. See [](country-tiers.md) for what each tier starts from.

The detailed U.S. structure sets the model's common sector list, and it is used to split other countries' coarser sectors (see {term}`ABSR`). Sector lists and currencies are reconciled in the later steps: mapping to the common sector list, linking with trade data, and balancing.

## What's in the tables

:::{figure} ../figures/diagrams/io-supply-use.svg
:label: fig-supply-use
:alt: Two block diagrams. The Supply table has industries as rows and commodities as columns, with row sums giving industry output x, column sums giving commodity output q, and a row of imports below. The Use table has commodities as rows, with industry columns and final demand columns, value added below the industry columns, and industry column sums giving industry output x.
The Supply and Use tables. Supply shows who makes each commodity; Use shows who buys it and what each industry adds in value. The Make table (\*) is a variant of Supply that leaves imports to the Use table.
:::

An economy's IO accounts come as a pair of tables.

**Supply** (`V`) records the production of each commodity by each domestic industry, plus imports of each commodity. The **Make** table, used for the U.S., is a variant: it has the same production block but no imports row. Imports appear instead in the Use table's final demand, as a negative column. Either way, the production block gives two output totals:

- **Industry output** `x`: the sum across an industry's row, which is everything the industry makes, including secondary products.
- **Commodity output** `q`: the sum down a commodity's column, which is everything domestic industries make of that commodity. Adding imports gives the total supply of the commodity.

**Use** (`U` and `y`) records who buys each commodity:

- **Intermediate use** (`U`): the commodities each industry buys as inputs.
- **Final demand** (`y`): the commodities bought by final users, namely households, government, investment, and exports.
- **Value added**: below each industry's inputs, its wages, taxes on production, and profits.

The two tables balance. For each commodity, total supply equals total use. For each industry, inputs plus value added equal the industry's output `x`.

## Domestic and imported use

:::{figure} ../figures/diagrams/io-domestic-imported.svg
:label: fig-domestic-imported
:alt: The Use table equals a domestic use table plus an imported use table. Domestic use has Udom for industries and ydom plus exports for final demand, which together form y_nab. Imported use has Uimp for industries and yimp for final demand.
The Use table is split into domestic and imported use, for industries and final users alike.
:::

A purchase can come from a domestic producer or from abroad, and the two lead to different supply chains. So the Use table is split in two:

- **Domestic use** (`Udom`, `ydom`): commodities bought from domestic producers.
- **Imported use** (`Uimp`, `yimp`): commodities bought from producers in other countries.

`U = Udom + Uimp`. Final demand splits the same way, with exports on the domestic side: `y = ydom + exports + yimp`. Imported use is later traced back to the countries that made the imports, using trade data. How each country's tables arrive at this split is described in [](country-tiers.md).

## From tables to direct requirements (`A`)

:::{figure} ../figures/diagrams/io-tables-to-a.svg
:label: fig-tables-to-a
:alt: Domestic use divided by industry output, times the Supply table divided by commodity output, equals Adom. The same steps with imported use give Aimp.
Domestic and imported direct requirements are built from the same two steps.
:::

The direct requirements tables turn the Supply and Use tables into recipes: the inputs needed to make $1 of each commodity. They take three steps.

1. **Inputs per dollar of industry output.** Divide each industry's column of domestic use by its output `x`.
2. **Market shares.** Divide each commodity's column of the Supply table by its output `q`. This gives the share of each commodity made by each industry.
3. **Combine.** Multiply the two to get inputs per dollar of each *commodity*:

$$
A_{dom} = \left(U_{dom}\,\hat{x}^{-1}\right)\left(V\,\hat{q}^{-1}\right)
\qquad
A_{imp} = \left(U_{imp}\,\hat{x}^{-1}\right)\left(V\,\hat{q}^{-1}\right)
$$

Here $\hat{x}^{-1}$ and $\hat{q}^{-1}$ divide each column by that sector's output. `Adom` and `Aimp` add up to the total direct requirements `A`. A column of `A` is the input recipe for $1 of that commodity, split by where the inputs come from.

Tables that are already symmetric, with the same sectors on rows and columns, skip step 2: their domestic and imported use are divided by output directly. This applies to the Tier 1 and Tier 2 tables.

## Final demand and output (`y_nab`)

Final demand in the Use table includes purchases of imports. To match domestic production, we need final demand for *domestic* products only. We call this `y_nab`, the final demand for the national accounting balance:

$$
y_{nab} = y_{dom} + \text{exports} = y - y_{imp}
$$

Here `ydom` is what households, government, and investment buy from domestic producers, and `yimp` is what they buy from abroad. Imports not bought by industries go to final users, so `yimp` is total imports less the row sums of `Uimp`. Exports are the country's own production, so they count toward `y_nab` in full.

With `y_nab`, the model reproduces the country's commodity output: $q = L_{dom}\, y_{nab}$, where $L_{dom} = (I - A_{dom})^{-1}$ is the domestic Leontief inverse. This is a check that the tables, `Adom`, and `y_nab` are consistent.

:::{note} Draft placeholder
:class: dropdown
Plan §3.2.1 · target: **RC (Oct 27)**


**Planned content**

- What data go in, what comes out, and how the pieces fit

**Key visuals**

- 🖼 Pipeline: national tables + trade data → common schema → balanced MRIO → `A`/`L`
:::

:::{important} Key assumptions
:class: dropdown
**Industry technology**

- **Assumption:** An industry uses the same input recipe for everything it makes, its primary product and any secondary products alike. This is what lets the market shares (`V` ÷ `q`) turn industry recipes into commodity recipes.
- **Why we make it:** It is the standard assumption for building commodity-by-commodity tables from Supply and Use tables, and unlike the alternative (commodity technology) it never produces negative requirements.
- **How it affects results:** A secondary product takes on its producer's recipe. Using U.S. tables after {term}`redefinitions <Redefinitions>` keeps secondary products, and so this effect, small.
- **Alternatives or sensitivity tested:** *To be written.*
:::

:::{seealso} Checks we run
*The validation behind this part of the model. See [Validation](#validation-hub).*
:::

## Learn more

- **From the field:** *to be added*
- **Cornerstone papers:** *to be added*
- **Code:** *to be added*

+++

:::{div}
:class: page-status
Applies to: RC · Last reviewed: RC
:::
