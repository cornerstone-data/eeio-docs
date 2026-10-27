# Writing pages

Every page follows the same pattern so readers know where to look.

1. **"Summary"** tip box at the top: one or two sentences on what the page covers.
2. **Visual first:** lead with a diagram or chart, then the explanation.
3. Plain language. Use the variable names in [reference/notation.md](reference/notation.md) (`A`, `L`, `B`, `D`, `N`, …) and define terms in [reference/glossary.md](reference/glossary.md). Link a term with `` {term}`MRIO` ``.
4. Methods pages carry a **Key assumptions** box. Each assumption uses the card: *Assumption · Why we make it · How it affects results · Alternatives or sensitivity tested.*
5. End with **Learn more** in three groups: *From the field*, *Cornerstone papers*, *Code*. Cite with `[@key]` using keys from `references.bib`.
6. Describe the model as **one model**: organize by what it does, and don't name code repositories in page text.
7. **Version-aware:** describe the current release only. When a method changes, add a callout such as "Changed in v0.6: … (previously …; see release notes)", and update the page-status line at the bottom (`Applies to: …`).

Placeholder pages contain a collapsed **Draft placeholder** note listing the planned content and visuals. Delete it once the page is written.

Before opening a PR, run `myst build --html --strict` locally; CI runs the same build.
