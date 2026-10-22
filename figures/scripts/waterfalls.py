"""Write the two release-candidate waterfall charts to figures/diagrams/.

Source: the Practitioners Forum Roundtable 2 deck (slide 25). The USEEIO driver chart is now drawn by rc_summary_figures.py. Steps are the percentage
changes shown on the slides, converted to kg CO2e per USD against each baseline. The listed steps
do not sum exactly to the net change on the slides, so the remainder is drawn as "Other" until the
science team confirms the attribution.

Run from the repo root (needs matplotlib):
    uv run --with matplotlib python figures/scripts/waterfalls.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

OUT = Path(__file__).resolve().parents[1] / "diagrams"
INK, MUTED = "#2C2C2A", "#5F5E5A"
UP, DOWN, TOTAL, OTHER = "#D85A30", "#1D9E75", "#5F5E5A", "#B4B2A9"
plt.rcParams.update({"font.family": ["Helvetica", "Arial", "DejaVu Sans"], "font.size": 11,
                     "svg.fonttype": "none"})

CHARTS = {
    "waterfall-vs-ceda": dict(
        title="Global production-weighted emission factor: Cornerstone 2026 vs. CEDA 2025",
        ylabel="kg CO$_2$e per 2024 USD",
        base_label="CEDA\n2025", base=0.6957, end_label="Cornerstone\n2026", end=0.5281,
        steps=[("Model\nreconciliation", 0.0), ("US\ndata", 0.1), ("Nowcasting &\nfacility\ndata", -0.7),
               ("Bug\nfixes", -0.4), ("UK & global\ntrade data", 0.0), ("China\ndata", 7.8),
               ("Europe &\nother global\ndata", -1.6), ("ABSR", -10.7), ("Benchmark-\ninformed\nimprovements", -19.0)],
        ylim=(0.50, 0.76), net="−24.1% net",
    ),
}


def draw(name, c):
    labels, bottoms, heights, colors, texts = [], [], [], [], []
    level = c["base"]
    labels.append(c["base_label"]); bottoms.append(0); heights.append(c["base"]); colors.append(TOTAL)
    texts.append((c["base"], f'{c["base"]:.4f}'))
    for label, pct in c["steps"]:
        delta = c["base"] * pct / 100
        new = level + delta
        labels.append(label); bottoms.append(min(level, new)); heights.append(abs(delta))
        colors.append(UP if delta > 0 else DOWN)
        txt = "~0%" if pct == 0 else f"{pct:+.1f}%".replace("-", "−")
        texts.append((max(level, new), txt))
        level = new
    labels.append(c["end_label"]); bottoms.append(0); heights.append(c["end"]); colors.append(TOTAL)
    texts.append((c["end"], f'{c["end"]:.4f}\n({c["net"]})'))

    fig, ax = plt.subplots(figsize=(11, 5.6), dpi=170)
    xs = range(len(labels))
    bars = ax.bar(xs, heights, bottom=bottoms, color=colors, width=0.62, zorder=3)
    pos = c["base"]
    levels = [c["base"]]
    for _, pct in c["steps"]:
        pos += c["base"] * pct / 100; levels.append(pos)
    for i in range(len(levels)):
        ax.plot([i + 0.31, i + 1 - 0.31], [levels[i], levels[i]], color="#B4B2A9", lw=0.8, zorder=2)
    span = c["ylim"][1] - c["ylim"][0]
    for x, (y, t) in zip(xs, texts):
        ax.text(x, y + span * 0.012, t, ha="center", va="bottom", color=INK, fontsize=11, fontweight="medium")
    ax.set_xticks(list(xs)); ax.set_xticklabels(labels, fontsize=9, color=INK)
    ax.set_ylim(*c["ylim"]); ax.set_ylabel(c["ylabel"], color=MUTED)
    ax.tick_params(axis="y", colors=MUTED, length=0); ax.tick_params(axis="x", length=0)
    ax.grid(axis="y", color="#E8E6DF", lw=0.8, zorder=0)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#B4B2A9")
    fig.tight_layout()
    for ext in ("png", "svg"):
        fig.savefig(OUT / f"{name}.{ext}", facecolor="white")
    plt.close(fig)
    print(name, "baseline", c["base"], "end", c["end"], "last step level", round(levels[-1], 4))


for n, c in CHARTS.items():
    draw(n, c)
