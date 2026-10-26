---
title: "Why we benchmark"
label: benchmarking-hub
---

:::{tip} Summary
Validation ensures the model’s parts mathematically check out. Benchmarking asks whether emissions and economic data line up with real-world conditions, by comparing our direct emission factors to independent sources.
:::

Both [](../validation/index.md) and benchmarking feed the same loop into the next release: build → validate → benchmark → investigate → methodology change.

## What we compare

To benchmark our model, we compare direct emission factors to independent sources. We usually do not benchmark full supply chain (cradle-to-gate) factors as matching scope across sources is much harder.

:::{important} Direct factors, not full supply chains
The comparisons on this page are about what each sector emits itself (`D`), not the full upstream intensity (`N`).
:::

## Kinds of sources we compare against

| Kind of source | What it usually is | Why it’s useful |
|---|---|---|
| National inventories and accounts | Official country reports of emissions and economic output | Closest match to "total emissions for a sector ÷ total sales of that sector" |
| Government factor databases | Official numbers on how much a plant or activity emits | Measured or regulated; good for electricity, cement, steel, and similar |
| International datasets | Cross-country emissions and energy statistics | Easy to compare across countries; strong for large emitting sectors |
| Peer-reviewed studies | Academic papers on sector or product emissions | Independent of our model; check that they measure the same thing |
| Other EEIO / multi-country models | Similar models from other teams | Same *kind* of number we publish; strongest when they don’t reuse our inputs |
| Industry association studies | Sector-wide studies from trade groups | Useful physical intensities; often need care converting to “per dollar” |
| Product declarations (EPDs) | Emissions for a specific product | Good for one product; usually too narrow for a whole national sector |
| Company reports | Sustainability or ESG reports from firms | Helpful when one company dominates a sector; weak as a country average |
| Simple derived estimates | Emissions per tonne or kWh divided by a market price | Easy to find, but often not comparable to our per-dollar factors |
| Reviews and secondary web pages | Summaries that quote other studies | Starting points only; follow them back to the original source |

:::{tip} Prefer like-for-like denominators
The strongest comparisons already look like emissions divided by national-accounts output. Estimates built from a market price or a company’s revenue are different objects unless they are restated to match that same scope and denominator.
:::

## What benchmarking can lead to

1. **Sharper benchmark** — The comparison isn’t quite like-for-like in scope or assumptions, so we adjust the external number to match what the model measures.
2. **Model improvement** — The gap points to a place to improve the model (for example, bringing in additional data).
3. **Documented, valid difference** — The model and the benchmark are measuring different things on purpose; we maintain the model and record why they diverge.

:::{note}
These three outcomes are the point of the exercise. Benchmarking is not a single pass/fail score for the whole model.
:::

## Challenges in assessing a fair comparison

### Scope and boundary (what emissions count)

- Direct only vs full life cycle (purchased power, upstream fuels)
- Territorial vs residence accounting (especially international transport)
- Whether related activities count in this sector or elsewhere (for example a steel mill’s own power plant, or coke making counted with steel vs with chemicals)
- Whole industry vs one product line (for example steel mills vs re-rollers)

### What “per dollar” means

- National-accounts output (our basis) vs a market price route (e.g.,mass × price). Price routes often look higher.
- Producer vs purchaser prices; mill gate vs retail
- Company revenue is not the same as sector output
- Commodity vs industry output; private vs government producers; blended products under one label

:::{important} Output route vs price route
Many apparent disagreements come from the denominator, not from missing emissions. We divide official emissions by the sector’s gross output from national accounts. A common alternative divides physical intensity (for example grams per kWh) by a retail price. Retail prices carry taxes and margins that output does not, and sales between firms inside the sector are missing from a price-based denominator while emissions are counted once, so the price route almost always looks larger.
:::

### Currency and year

- Converting to USD and to the model’s dollar year
- Emissions year often lags the dollar year — a small gap is not always agreement
- Which price index is used to rebase

### Sector definitions

- Broad foreign categories vs our finer sectors
- Re-scoping with shares adds assumptions
- Same name, different contents (for example heat counted with electricity; private fleets vs for-hire trucking)

## How we judge agreement

The goal is not an exact match to one external number. It is whether our estimate aligns with the **preponderance of the evidence**, after fair scope and dollar treatment.

## Results for this release

*Headline counts and a figure will be added for the RC.* See [](../releases/rc.md) for the release summary once those numbers are in.

:::{seealso} Related
Internal accounting checks live on [](../validation/index.md). Version-specific headlines will also appear in the [](../releases/index.md).
:::

+++

:::{div}
:class: page-status
Applies to: 2026-rc.1 · Last reviewed: 2026-rc.1
:::
