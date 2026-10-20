---
title: "The IO model: overview"
---

:::{tip} Summary
Cornerstone uses standardized national input-output tables to represent production recipes and it links them with trade data, thus representing domestic and international supply chains.
:::

## Preparing the IO tables

Every country enters the model as a national IO table, but countries don't all start from the same kind of table. The first step is to collect the best available table for each country and record where it came from: the source, version, year, valuation, and sector detail. Which table we start from depends on the country's {term}`tier <Country tier>`: the U.S. starts from {term}`Make and Use tables <Make/Use framework>` for 2024 that Cornerstone produces, after {term}`redefinitions <Redefinitions>` and following BEA's 2017 detailed schema, while other countries start from national statistical agency tables, {term}`FIGARO` or {term}`ICIO`, or a template. See [](country-tiers.md) for what each tier starts from.

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

The direct requirements tables turn the Supply and Use tables into recipes: the inputs needed to make \$1 of each commodity. They take three steps.

1. **Inputs per dollar of industry output.** Divide each industry's column of domestic use by its output `x`.
2. **Market shares.** Divide each commodity's column of the Supply table by its output `q`. This gives the share of each commodity made by each industry.
3. **Combine.** Multiply the two to get inputs per dollar of each *commodity*. Doing this with domestic use gives `Adom`; doing it with imported use gives `Aimp`.

For the math, see the [Cornerstone U.S. methods working paper](https://github.com/cornerstone-data/papers/blob/published/us-methods/us-methods.md#treatment-of-economic-data-and-iot-construction).

:::{note} Draft
:class: dropdown
The linked working paper describes U.S. model v0.2. Update it to the current release (nowcast tables, 405-sector schema, the multi-region model) and update this link.
:::

`Adom` and `Aimp` add up to the total direct requirements `A`. A column of `A` is the input recipe for \$1 of that commodity, split by where the inputs come from.

Tables that are already symmetric, with the same sectors on rows and columns, skip step 2: their domestic and imported use are divided by output directly. This applies to the Tier 1 and Tier 2 tables.

## Final demand and output (`y_nab`)

Final demand in the Use table includes purchases of imports. To match domestic production, we need final demand for *domestic* products only. We call this `y_nab`, the final demand for the national accounting balance: domestic final demand for domestic products (`ydom`) plus exports.

Here `ydom` is what households, government, and investment buy from domestic producers, and `yimp` is what they buy from abroad. Imports not bought by industries go to final users, so `yimp` is total imports less the row sums of `Uimp`. Exports are the country's own production, so they count toward `y_nab` in full.

With `y_nab`, the model reproduces the country's commodity output: running `y_nab` through the domestic supply chain (the Leontief inverse of `Adom`) gives back `q`. This is a check that the tables, `Adom`, and `y_nab` are consistent.

## From single-country tables to the multi-region model

:::{figure} ../figures/diagrams/io-mrio-blocks.svg
:label: fig-mrio-blocks
:alt: A block matrix with countries as both rows and columns. Diagonal blocks are each country's domestic direct requirements Adom. Off-diagonal blocks are imports from the row country to the column country. A side panel shows Country 2's imported direct requirements Aimp being multiplied by trade shares by origin and product, giving separate blocks of imports from Country 1, Country 3, and the rest of the world.
The {term}`MRIO` direct requirements table. Each country's domestic inputs sit on the diagonal; its imported inputs are spread down its column by country of origin.
:::

Each country's tables say how much of its inputs are imported, but not where they come from. The multi-region model links the countries so that a supply chain can be followed across borders.

1. **Put every country in one table.** The 65 countries in Tiers 0 to 2 each get their own block, so `A` is a 65 × 65 grid of country blocks, each 405 × 405 sectors. Each country's `Adom` sits on the diagonal. A country's column holds everything its industries buy; the rows say which country sold it.
2. **Split imports by origin.** Each country's `Aimp` is spread down its column using bilateral trade data ({term}`BACI`): for each product, the share the country imports from each origin. Products the trade data don't cover, mostly services, use origin shares from {term}`FIGARO` or {term}`ICIO`. Imported final demand (`yimp`) is split the same way.
3. **Add the rest of the world.** Imports from countries outside the table come from a rest-of-world region. Its domestic input structure is pooled from the tables of Colombia, Mexico, Türkiye, and Chile. It is added as one more block, making `A` a 66 × 66 grid of country blocks. This region is separate from the template used for Tier 3 countries' own factors (see [](country-tiers.md)).
4. **Balance.** The whole table is balanced with {term}`RAS`, so that each country's sales to all users, at home and abroad, add up to its output. This makes small adjustments to the import coefficients.
5. **Solve.** The total requirements (`L`) are calculated for the whole table at once, so supply chains that cross several borders are captured in full (see [below](#total-requirements)).

The other 83 of the model's 148 countries (Tier 3) are linked to this table more simply; see [](country-tiers.md).

(total-requirements)=
## Total requirements (`L`)

`A` shows only a sector's direct suppliers. Take \$1 of furniture. Its column of `A` lists what the furniture maker buys to make it: lumber, hardware, electricity, transport. These are the **first tier** of the supply chain.

Each of those suppliers has its own column in `A`. The sawmill buys logs, fuel, and machinery; the power plant buys fuel and equipment. These purchases are the **second tier**. Each supplier's column is scaled by how much of it the first tier needs: if the furniture maker buys 20 cents of lumber for each \$1 of furniture, the sawmill's whole recipe is multiplied by 0.20. The second-tier suppliers have their own suppliers, the third tier, scaled again by what the second tier needs, and so on, without end. In the multi-region model the trace crosses borders: a second-tier supplier may be a steel mill in another country.

Each tier is smaller than the one before, because every dollar of output pays for value added (wages, taxes, profits) as well as purchases. So the tiers add up to a finite total: everything produced, anywhere in the supply chain, to deliver \$1 of each commodity to a final user. Written out, that total is `I + A + A² + A³ + …`, where `I` is the \$1 of the commodity itself, `A` the first tier, `A²` the second, and so on.

There is a simple way to calculate this infinite sum all at once: a special inverse of `A`, `(I − A)⁻¹`, called the Leontief inverse after the economist Wassily Leontief. That is why the result is called `L`. A column of `L` shows the total output needed from every sector, in every country, for \$1 of final demand for that commodity.

:::{note}
The tiers here are rounds of suppliers in a supply chain. They are not the same as the {term}`country tiers <Country tier>`, which describe the data available for each country.
:::

### What the model can and can't trace

`L` follows supply chains through the 65 countries in the multi-region table and the rest-of-world region. The 83 Tier 3 countries are not separate parts of that table, so supply chains can't be traced to them one by one.

| Question | Can the model answer it? |
|---|---|
| How much of a U.S. product's supply chain is in China, Germany, or Korea? | Yes. Each of the 65 countries has its own part of the table. |
| How much is in Kenya or Egypt specifically? | No. Imports from all Tier 3 countries are grouped into the rest-of-world region. |
| Do the emissions traced to the rest of the world reflect those countries? | Not directly. The region's input recipe and emission intensities come from Colombia, Mexico, Türkiye, and Chile. |
| Where do a Tier 3 country's own supply chains lead? | Only to its own economy and to its imports as a whole, which are approximated with China's supply chains. |

:::{important} Key assumptions
:class: dropdown
**Industry technology**

- **Assumption:** An industry uses the same input recipe for everything it makes, its primary product and any secondary products alike. This is what lets the market shares (`V` ÷ `q`) turn industry recipes into commodity recipes.
- **Why we make it:** It is the standard assumption for building commodity-by-commodity tables from Supply and Use tables, and unlike the alternative (commodity technology) it never produces negative requirements.
- **How it affects results:** A secondary product takes on its producer's recipe. Using U.S. tables after {term}`redefinitions <Redefinitions>` keeps secondary products, and so this effect, small.
- **Alternatives or sensitivity tested:** *To be written.*

**Import proportionality**

- **Assumption:** Within a country, every buyer of a product gets the same mix of origins. If a country imports 30% of its steel from Korea, every industry that buys imported steel gets 30% of it from Korea.
- **Why we make it:** Trade data record which countries trade each product, but not which industry buys the imports.
- **How it affects results:** An industry that in reality buys mostly from one origin gets the national average mix instead. Where origins differ a lot in emission intensity, this can move that industry's factors.
- **Alternatives or sensitivity tested:** *To be written.*

**The rest of the world looks like four proxy economies**

- **Assumption:** The rest-of-world region stands in for every country outside the multi-region table, including all Tier 3 countries, as a source of imports. Its input recipe and emission intensities are pooled from Colombia, Mexico, Türkiye, and Chile. It buys nothing from other regions, so a supply chain that reaches it stays there.
- **Why we make it:** Countries outside the table have no linked IO tables of their own, and these four are the lower-income OECD economies in the table.
- **How it affects results:** Imports from Tier 3 countries carry the proxy economies' emission intensities rather than their own. Supply chains can't be traced to individual Tier 3 countries, or onward from the rest of the world to other regions.
- **Alternatives or sensitivity tested:** *To be written.*

**Shares still apply when data years differ**

- **Assumption:** The IO tables, trade shares, and gap-fill shares come from different years (for example, 2024 trade data with IO tables from 2018 to 2023). We assume the input recipes and origin shares from each source's data year still describe the 2024 economy.
- **Why we make it:** National tables, multi-regional databases, and trade data are published on different schedules, and we use the most recent of each.
- **How it affects results:** Where an economy's structure or trading partners changed between the data year and 2024, the model reflects the earlier pattern. The years used for each country are listed in [](../reference/methods-by-country.md).
- **Alternatives or sensitivity tested:** *To be written.*
:::


## Learn more

- **From the field:** Supply, Use, and IO tables in national accounts [@unitednationsHandbookSupplyUse2018]; the standard textbook on IO analysis [@millerInputoutputAnalysisFoundations2022]; how the U.S. IO accounts are built [@beaConceptsMethodsUS2009]
- **Cornerstone papers:** [Methodology for Cornerstone U.S. Model](https://github.com/cornerstone-data/papers/blob/published/us-methods/us-methods.md) (working paper; describes v0.2, update pending)
- **Code:** *to be added*

+++

:::{div}
:class: page-status
Applies to: RC · Last reviewed: RC
:::
