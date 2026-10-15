# Cornerstone EEIO model documentation

Source for the Cornerstone EEIO model docs, published at **https://docs.cornerstonedata.org/eeio/**.

The site explains the theory, assumptions, data, and validation behind the Cornerstone multi-regional EEIO model, and how to apply its emission factors. It is built with [MyST](https://mystmd.org) and served by GitHub Pages through the docs hub repo, [`cornerstone-data/cornerstone-data.github.io`](https://github.com/cornerstone-data/cornerstone-data.github.io).

## Preview locally

Requires Node.js 20 or later.

```bash
npm install -g mystmd   # or: pip install mystmd
myst start              # live preview at http://localhost:3000
myst build --html --strict   # the same build CI runs
```

## How changes go live

- **Pull requests** are built and previewed at `https://cornerstone-data.github.io/eeio-docs/pr-preview/pr-<number>/`, and links are checked.
- **Merges to `main`** are built with `BASE_URL=/eeio` and pushed into the hub repo's `eeio/` folder, which GitHub Pages serves within a minute or so.

## Layout

| Path | Contents |
|---|---|
| `myst.yml` | Site config, navigation, branding |
| `intro/`, `io/`, `ee/`, `factors/`, `validation/`, `benchmarking/`, `flag/` | Site sections |
| `reference/` | Glossary, notation, methods by country/version, data sources, further reading |
| `faq.md` | FAQs |
| `releases/` | One page per model release |
| `versions/` | Version records (one data file per release) |
| `figures/` | Hand-made diagrams, figure generator scripts, `figures.csv` inventory |
| `data/` | Small cached data extracts for figures |
| `references.bib` | Shared bibliography (keys match the `papers` repo) |
| `_parts/` | Navbar, footer, and custom CSS |

See [CONTRIBUTING.md](CONTRIBUTING.md) for page conventions.
