"""Write the charts for the release candidate "Summary of changes" pages to images/.

Redrawn from the Doc "Change log" working draft so they read cleanly in the text: white background,
no title and no source line on the image (those live in the figure caption).

- summary-vs-useeio.png: US emission factor, USEEIO v1.4 to Cornerstone 2026, split into data updates
  and methodology changes (+0.4% and -1.2%; 0.2474 to 0.2454, -0.8% net).
- summary-vs-ceda.png: global emission factor, CEDA 2025 to Cornerstone 2026 (+5.8% and -27.5%;
  0.6942 to 0.5324, -23.3% net). The methodology bar is drawn to the stated end value.
- company-footprint-change-ceda.png: the same histogram against CEDA (median -14.0%); bar heights read
  off the draft, so approximate.
- drivers-vs-ceda.png: the drivers of the change against CEDA (percentages from the draft; the steps sum
  to -23.2% against the -23.3% net, and the last step is drawn to land on the end value).
- company-footprint-change.png: distribution of the change in the footprint of 400 corporate
  footprints against USEEIO (median -1.3%). Bar heights are relative and were read off the draft's
  histogram, so they are approximate; the y-axis is not labelled.
- drivers-vs-useeio.png: the drivers of the change against USEEIO (percentages from the draft). The
  steps do not sum to the net change stated in the draft; the last step is not forced to land on it.
- cement-ef.png: cement emission factor, USEEIO vs Cornerstone (4.35 and 5.21, values from the draft).

Run from the repo root (needs matplotlib):
    uv run --with matplotlib python figures/scripts/rc_summary_figures.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import Rectangle  # noqa: E402

OUT = Path(__file__).resolve().parents[2] / "images"
INK, MUTED = "#2C2C2A", "#5F5E5A"
BASE, END = "#B4B2A9", "#5F5E5A"
DATA, METHOD = "#D85A30", "#1D9E75"          # data update, methodology change
plt.rcParams.update({"font.family": ["Helvetica", "Arial", "DejaVu Sans"], "font.size": 11})


def clean(ax, left=False):
    for s in ("top", "right") + (() if left else ("left",)):
        ax.spines[s].set_visible(False)
    ax.spines["bottom"].set_color("#B4B2A9")
    if not left:
        ax.set_yticks([])
    ax.tick_params(axis="x", length=0, colors=INK)


def legend(ax, loc="lower right", anchor=(1.0, 1.0)):
    handles = [plt.Rectangle((0, 0), 1, 1, color=DATA), plt.Rectangle((0, 0), 1, 1, color=METHOD)]
    ax.legend(handles, ["Data update", "Methodology"], loc=loc, bbox_to_anchor=anchor, ncol=2, frameon=False,
              fontsize=10, labelcolor=INK, borderaxespad=0.2)


def summary(name, start_label, start, steps, end, net, size=(7.2, 3.9)):
    """steps: [(label, pct, colour)]; the last step is drawn to land on `end`."""
    fig, ax = plt.subplots(figsize=size, dpi=200)
    level = start
    ax.bar(0, start, color=BASE, width=0.6)
    ax.text(0, start * 1.015, f"{start:.4f}", ha="center", va="bottom", color=INK, fontweight="medium")
    xs, labels = [0], [start_label]
    for i, (label, pct, colour) in enumerate(steps, start=1):
        new = end if i == len(steps) else level + start * pct / 100
        lo, hi = min(level, new), max(level, new)
        ax.bar(i, hi - lo, bottom=lo, color=colour, width=0.6)
        ax.text(i, hi * 1.015, f"{pct:+.1f}%".replace("-", "−"), ha="center", va="bottom", color=colour, fontweight="medium")
        ax.plot([i - 0.7, i - 0.3], [level, level], color="#B4B2A9", lw=0.9, ls=(0, (3, 3)))
        level = new
        xs.append(i); labels.append(label)
    n = len(steps) + 1
    ax.plot([n - 0.7, n - 0.3], [level, level], color="#B4B2A9", lw=0.9, ls=(0, (3, 3)))
    ax.bar(n, end, color=END, width=0.6)
    ax.text(n, end * 1.015, f"{end:.4f}\n{net} net", ha="center", va="bottom", color=INK, fontweight="medium", linespacing=1.3)
    xs.append(n); labels.append("Cornerstone\n2026")
    ax.set_xticks(xs); ax.set_xticklabels(labels, fontsize=10)
    ax.set_ylim(0, start * 1.3)
    clean(ax); legend(ax)
    fig.tight_layout()
    fig.savefig(OUT / name, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def histogram(name, median, inside, outside, label_x, label_y, ymax):
    """inside/outside: [(centre of the 2.5-point bin in %, relative height read off the draft's histogram)]."""
    fig, ax = plt.subplots(figsize=(7.2, 3.3), dpi=200)
    ax.axvspan(-20, 20, color="#EFEDE6", zorder=0)
    ax.bar([x for x, _ in inside], [h for _, h in inside], width=2.3, color="#C9CAD1", zorder=2)
    ax.bar([x for x, _ in outside], [h if h > 2 else 3 for _, h in outside], width=2.3, color=METHOD, zorder=2)
    ax.axvline(median, color="#A33F2E", ls=(0, (4, 3)), lw=1.4, zorder=3)
    ax.axvline(0, color=INK, lw=0.8, zorder=3)
    ax.text(label_x, label_y, f"Median {median:.1f}%".replace("-", "−"), ha="right", va="center", color="#A33F2E", fontweight="medium")
    ax.text(0, -ymax * 0.16, "Within ±20%", ha="center", va="top", color=MUTED, fontsize=9.5)
    ax.set_xlim(-100, 100); ax.set_ylim(0, ymax)
    ax.set_xticks([-100, -50, -20, 0, 20, 50, 100])
    ax.set_xticklabels(["−100%", "−50%", "−20%", "0%", "+20%", "+50%", "+100%"], color=INK)
    clean(ax)
    fig.tight_layout()
    fig.savefig(OUT / name, facecolor="white")
    plt.close(fig)


def drivers(name, base_label, base, end, net, steps, bands, ylim, n_ticks_label=9, force_last=False):
    """steps: [(label, pct, colour, badge)]; bands: [(x0, x1, label, colour)]. The last step lands on `end` only with force_last."""
    fig, ax = plt.subplots(figsize=(9.6, 5.0), dpi=200)
    span = ylim[1] - ylim[0]
    for x0, x1, label, colour in bands:
        ax.add_patch(Rectangle((x0 + 0.04, ylim[0]), x1 - x0 - 0.08, span, fc=colour, ec="none", zorder=0))
        ax.text((x0 + x1) / 2, ylim[1] - span * 0.045, label, ha="center", va="center", color=MUTED, fontsize=9.5,
                fontweight="medium")
    ax.bar(0, base - ylim[0], bottom=ylim[0], color=BASE, width=0.6, zorder=2)
    ax.text(0, base + span * 0.012, f"{base:.4f}", ha="center", va="bottom", color=INK, fontweight="medium")
    level = base
    xs, labels = [0], [base_label]
    for i, (label, pct, colour, badge) in enumerate(steps, start=1):
        new = end if (force_last and i == len(steps)) else level + base * pct / 100
        lo, hi = min(level, new), max(level, new)
        ax.bar(i, max(hi - lo, span * 0.002), bottom=lo, color=colour, width=0.6, zorder=2)
        text = "~0%" if abs(pct) < 0.05 else f"{pct:+.1f}%".replace("-", "−")
        ax.text(i, hi + span * 0.012, text, ha="center", va="bottom", color=colour, fontweight="medium")
        if badge:
            ax.text(i + 0.36, hi + span * 0.03, str(badge), ha="center", va="center", color="white", fontsize=9, fontweight="medium",
                    bbox=dict(boxstyle="circle,pad=0.3", fc=INK, ec="none"), zorder=4)
        ax.plot([i - 0.7, i - 0.3], [level, level], color="#B4B2A9", lw=0.9, ls=(0, (3, 3)), zorder=1)
        level = new
        xs.append(i); labels.append(label)
    n = len(steps) + 1
    ax.plot([n - 0.7, n - 0.3], [level, level], color="#B4B2A9", lw=0.9, ls=(0, (3, 3)), zorder=1)
    ax.bar(n, end - ylim[0], bottom=ylim[0], color=END, width=0.6, zorder=2)
    ax.text(n, end + span * 0.012, f"{end:.4f}\n{net} net", ha="center", va="bottom", color=INK, fontweight="medium", linespacing=1.3)
    xs.append(n); labels.append("Cornerstone\n2026")
    ax.set_xticks(xs); ax.set_xticklabels(labels, fontsize=n_ticks_label)
    ax.set_xlim(-0.6, n + 0.6); ax.set_ylim(*ylim)
    ax.set_ylabel("kg CO$_2$e per 2024 USD", color=MUTED)
    ax.tick_params(axis="y", colors=MUTED, length=0)
    ax.grid(axis="y", color="#E8E6DF", lw=0.8, zorder=0)
    clean(ax, left=True); ax.spines["left"].set_visible(False)
    legend(ax)
    fig.tight_layout()
    fig.savefig(OUT / name, facecolor="white", bbox_inches="tight")
    plt.close(fig)


def drivers_useeio():
    steps = [("Model\nreconciliation", -3.5, METHOD, 1), ("US\ndata", 0.4, DATA, None),
             ("Nowcasting &\nfacility reported\ndata", -5.8, METHOD, 2), ("Trade\nimpact", 8.6, METHOD, 3),
             ("Benchmark-\ninformed\nimprovements", 0.2, METHOD, None)]
    bands = ((0.5, 3.5, "US MODEL", "#F1EEE8"), (3.5, 5.5, "GLOBAL MODEL (US PORTION)", "#E8EEEE"))
    drivers("drivers-vs-useeio.png", "Baseline\nUSEEIO v1.4", 0.2474, 0.2454, "−0.8%", steps, bands, (0.215, 0.262))


def drivers_ceda():
    steps = [("Model\nreconciliation", 0.0, METHOD, None), ("US\ndata", 0.1, DATA, None),
             ("Nowcasting &\nfacility reported\ndata", -0.7, METHOD, None), ("Bug\nfixes", -0.2, METHOD, None),
             ("UK & global\ntrade data", 0.0, DATA, None), ("China\ndata", 7.6, DATA, 1),
             ("Europe & other\nglobal data", -1.8, DATA, 2), ("ABSR", -11.0, METHOD, 3),
             ("Benchmark-\ninformed\nimprovements", -17.2, METHOD, 4)]
    bands = ((0.5, 3.5, "US MODEL", "#F1EEE8"), (3.5, 9.5, "GLOBAL MODEL", "#E8EEEE"))
    drivers("drivers-vs-ceda.png", "Baseline\nCEDA 2025", 0.6942, 0.5324, "−23.3%", steps, bands, (0.50, 0.80), 8.5, force_last=True)


def cement():
    fig, ax = plt.subplots(figsize=(6.2, 2.0), dpi=200)
    for y, (label, v, colour, bold) in enumerate((("USEEIO", 4.35, BASE, False), ("Cornerstone", 5.21, "#0F6E56", True))):
        ax.barh(y, v, color=colour, height=0.5)
        ax.text(v + 0.08, y, f"{v:.2f}", va="center", color=INK, fontweight="medium" if bold else "normal")
    ax.set_yticks([0, 1]); ax.set_yticklabels(["USEEIO", "Cornerstone"], color=INK)
    ax.invert_yaxis(); ax.set_xlim(0, 6.2)
    for s in ("top", "right", "bottom"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color("#B4B2A9"); ax.set_xticks([]); ax.tick_params(axis="y", length=0)
    fig.tight_layout()
    fig.savefig(OUT / "cement-ef.png", facecolor="white")
    plt.close(fig)


summary("summary-vs-useeio.png", "USEEIO\nv1.4 (US)", 0.2474, [("Data\nupdates", 0.4, DATA), ("Methodology\nchanges", -1.2, METHOD)], 0.2454, "−0.8%")
summary("summary-vs-ceda.png", "CEDA\n2025", 0.6942, [("Data\nupdates", 5.8, DATA), ("Methodology\nchanges", -27.5, METHOD)], 0.5324, "−23.3%")
histogram("company-footprint-change.png", -1.3,
          [(-16.3, 16), (-13.9, 19), (-11.3, 52), (-8.9, 93), (-6.2, 111), (-3.8, 100), (-1.5, 272), (1.2, 152),
           (3.6, 55), (6.2, 31), (8.6, 16), (11.3, 16), (13.7, 13), (16.0, 7), (18.7, 10)],
          [(-48.9, 1), (-33.8, 1), (-28.8, 4), (-24.0, 4), (-21.4, 7), (21.1, 4), (23.6, 7), (31.3, 1), (36.2, 1),
           (38.7, 1), (43.8, 1), (46.3, 1), (68.8, 1), (76.3, 1)], -4, 300, 330)
histogram("company-footprint-change-ceda.png", -14.0,
          [(-18.7, 231), (-16.3, 244), (-11.5, 211), (-9.0, 184), (-6.5, 184), (-4.0, 132), (-1.4, 310),
           (1.2, 5), (6.0, 5), (8.5, 5)],
          [(-38.8, 19), (-36.5, 12), (-34.2, 12), (-31.4, 19), (-28.9, 72), (-26.6, 98), (-24.0, 164), (-21.5, 164)],
          -16.5, 330, 350)
drivers_useeio(); drivers_ceda(); cement()
print("wrote", *(p.name for p in sorted(OUT.glob("*.png"))))
