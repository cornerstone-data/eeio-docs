"""Write the benchmarking results donut to figures/diagrams/benchmark-2026-rc1.png.

Redraws the slide-deck donut with the release's numbers. Each of the 88 benchmarked sectors falls in
one band by its gap, |model D - benchmark| / benchmark, with model D from the v1.0 release diagnostics
(cornerstone_2026_v0_7, ceda commit 03facf41):

- within 25% of the benchmark: 61 sectors
- 25-50% gap: 18 sectors
- 50% or more gap: 9 sectors

Percentages are rounded by largest remainder so they add to 100% (69%, 21%, 10%; exact shares are
69.3%, 20.5% and 10.2%).

Run from the repo root (needs matplotlib):
    uv run --with matplotlib python figures/scripts/benchmark_figures.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Circle, Wedge  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "diagrams"
TITLE, INK, MUTED = "#2F6F67", "#2C3746", "#6A727C"
BANDS = [  # (label, sectors, colour)
    ("Within 25% of benchmark", 61, "#2F5D8A"),
    ("25–50% gap", 18, "#D5D8DC"),
    ("50% or more gap", 9, "#7D848D"),
]
plt.rcParams.update({"font.family": ["Helvetica", "Arial", "DejaVu Sans"]})


def whole_percents(counts):
    """Round shares to whole percents that add to 100 (largest remainder)."""
    total = sum(counts)
    exact = [100 * c / total for c in counts]
    pcts = [int(e) for e in exact]
    by_remainder = sorted(range(len(counts)), key=lambda i: exact[i] - pcts[i], reverse=True)
    for i in by_remainder[: 100 - sum(pcts)]:
        pcts[i] += 1
    return pcts


def donut():
    counts = [n for _, n, _ in BANDS]
    total = sum(counts)
    pcts = whole_percents(counts)

    fig = plt.figure(figsize=(6.2, 5.7), dpi=200)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 620)
    ax.set_ylim(570, 0)
    ax.axis("off")

    ax.text(28, 26, "How Cornerstone compares to third-party references", color=TITLE, fontsize=14.5,
            fontweight="bold", va="center")

    cx, cy, r_out, r_in = 310, 231, 158, 103
    # The y axis runs top-down, so data angles turn clockwise on the page; -90 is 12 o'clock.
    start = -90.0
    for (_, n, colour) in BANDS:
        sweep = 360 * n / total
        ax.add_patch(Wedge((cx, cy), r_out, start, start + sweep, width=r_out - r_in, facecolor=colour,
                           edgecolor="white", linewidth=1.5))
        start += sweep

    ax.text(cx, cy - 18, f"{pcts[0]}%", color=BANDS[0][2], fontsize=34, fontweight="bold", ha="center",
            va="center")
    ax.text(cx, cy + 30, "within 25% of\nbenchmark", color=INK, fontsize=11, ha="center", va="center",
            linespacing=1.4)

    for i, ((label, _, colour), pct) in enumerate(zip(BANDS, pcts)):
        y = 431 + 32 * i
        ax.add_patch(Circle((37, y), 9, facecolor=colour, edgecolor="none"))
        ax.annotate(label, (65, y), color=INK, fontsize=12.5, va="center")
        ax.annotate(f" {pct}%", (1, 0.5), xycoords=ax.texts[-1], color=INK, fontsize=12.5,
                    fontweight="bold", va="center")

    ax.text(38, 531, f"Share of the {total} benchmarked sectors", color=MUTED, fontsize=10.5, va="center")
    fig.savefig(OUT / "benchmark-2026-rc1.png", facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    donut()
