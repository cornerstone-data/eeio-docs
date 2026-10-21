"""Write the three charts on the release candidate page to images/.

Redrawn from the Practitioners Forum Roundtable 2 deck so they read cleanly in the text: white
background, no title and no source line on the image (those live in the figure caption).

- rc-factor-comparison.png: emission factors, Cornerstone 2026 vs CEDA 2025 and vs USEEIO v1.4.
  Step sizes are the slide labels; the methodology bar is drawn to the stated end value.
- rc-china-battery.png: China battery production. Totals are the slide labels. The split by
  battery type is read off the slide graphic, so it is approximate.
- rc-germany-power.png: Germany's power factor, share of the change from a cleaner grid vs prices.

Run from the repo root (needs matplotlib):
    uv run --with matplotlib python figures/scripts/rc_figures.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).resolve().parents[2] / "images"
INK, MUTED = "#2C2C2A", "#5F5E5A"
BASE, END, UP, DOWN = "#B4B2A9", "#5F5E5A", "#D85A30", "#1D9E75"
DARK_TEAL, LIGHT_TEAL = "#0F6E56", "#9FE1CB"
plt.rcParams.update({"font.family": ["Helvetica", "Arial", "DejaVu Sans"], "font.size": 11})


def clean(ax, bottom=True):
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#B4B2A9")
    ax.set_yticks([])
    ax.tick_params(axis="x", length=0, colors=INK)
    if not bottom:
        ax.spines["bottom"].set_visible(False)


def panel(ax, start_label, start, steps, end_label, end, net):
    """steps: [(label, pct)] in order; the last step is drawn to land on `end`."""
    level = start
    xs, labels = [0], [start_label]
    ax.bar(0, start, color=BASE, width=0.62)
    ax.text(0, start * 1.015, f"{start:.4f}", ha="center", va="bottom", color=INK, fontweight="medium")
    prev_top = start
    for i, (label, pct) in enumerate(steps, start=1):
        new = level + start * pct / 100
        if i == len(steps):
            new = end
        lo, hi = min(level, new), max(level, new)
        ax.bar(i, hi - lo, bottom=lo, color=UP if pct > 0 else DOWN, width=0.62)
        txt = f"{pct:+.1f}%".replace("-", "−")
        ax.text(i, hi * 1.015, txt, ha="center", va="bottom", color=UP if pct > 0 else DOWN, fontweight="medium")
        ax.plot([i - 0.69, i - 0.31], [level, level], color="#B4B2A9", lw=0.9, ls=(0, (3, 3)))
        level = new
        xs.append(i); labels.append(label)
    n = len(steps) + 1
    ax.plot([n - 0.69, n - 0.31], [level, level], color="#B4B2A9", lw=0.9, ls=(0, (3, 3)))
    ax.bar(n, end, color=END, width=0.62)
    ax.text(n, end * 1.015, f"{end:.4f}\n{net} net", ha="center", va="bottom", color=INK, fontweight="medium", linespacing=1.3)
    xs.append(n); labels.append(end_label)
    ax.set_xticks(xs); ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylim(0, start * 1.28)
    clean(ax)


def comparison():
    fig, axes = plt.subplots(1, 2, figsize=(11, 3.7), dpi=200)
    panel(axes[0], "CEDA\n2025", 0.6957, [("Data\nupdates", 6.3), ("Methodology\nchanges", -28.6)],
          "Cornerstone\n2026", 0.5281, "−24.1%")
    panel(axes[1], "USEEIO\nv1.4 (US)", 0.2474, [("Data\nupdates", -4.2), ("Methodology\nchanges", 3.3)],
          "Cornerstone\n2026", 0.2448, "−1.0%")
    fig.tight_layout(w_pad=3)
    fig.savefig(OUT / "rc-factor-comparison.png", facecolor="white")
    plt.close(fig)


def china():
    fig, ax = plt.subplots(figsize=(6, 4), dpi=200)
    data = {"2020": (150, 232), "2023": (946, 237)}  # (lithium-ion, lead-acid) GWh, approximate split
    for x, (yr, (li, pb)) in enumerate(data.items()):
        ax.bar(x, pb, color=LIGHT_TEAL, width=0.5)
        ax.bar(x, li, bottom=pb, color=DARK_TEAL, width=0.5)
        ax.text(x, li + pb + 20, f"{li + pb:,} GWh", ha="center", va="bottom", fontweight="medium", color=INK)
    ax.text(1.29, 237 + 946 / 2, "Lithium-ion", va="center", color=DARK_TEAL, fontweight="medium")
    ax.text(1.29, 237 / 2, "Lead-acid", va="center", color="#3C8F77", fontweight="medium")
    ax.set_xticks([0, 1]); ax.set_xticklabels(list(data), fontsize=11)
    ax.set_xlim(-0.5, 1.95); ax.set_ylim(0, 1350)
    clean(ax)
    fig.tight_layout()
    fig.savefig(OUT / "rc-china-battery.png", facecolor="white")
    plt.close(fig)


def germany():
    fig, ax = plt.subplots(figsize=(8, 1.7), dpi=200)
    ax.barh(0, 25, color=DARK_TEAL, height=0.5)
    ax.barh(0, 75, left=25, color=LIGHT_TEAL, height=0.5)
    ax.text(12.5, 0, "~25%", ha="center", va="center", color="white", fontweight="medium")
    ax.text(62.5, 0, "~75%", ha="center", va="center", color=DARK_TEAL, fontweight="medium")
    ax.text(0, -0.5, "Cleaner grid", ha="left", va="top", color=DARK_TEAL, fontweight="medium")
    ax.text(100, -0.5, "Higher prices", ha="right", va="top", color="#3C8F77", fontweight="medium")
    ax.text(0, 0.42, "Share of the 60% fall in Germany's power factor", ha="left", va="bottom", color=MUTED, fontsize=10)
    ax.set_xlim(0, 100); ax.set_ylim(-0.95, 0.85); ax.axis("off")
    fig.tight_layout()
    fig.savefig(OUT / "rc-germany-power.png", facecolor="white")
    plt.close(fig)


comparison(); china(); germany()
print("wrote", *(p.name for p in sorted(OUT.glob("rc-*.png"))))
