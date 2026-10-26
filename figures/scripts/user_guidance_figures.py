"""Write the two graphics on the User guidance page to images/.

- user-guidance-ef-by-country.png: 2026 producer-price factor for management consulting (sector 541610)
  in six locations, kg CO2e per USD, from the 2026-rc.1 release workbook.
- user-guidance-worked-example.png: GBP 10,000 of UK management consulting taken to kg CO2e, using the
  0.0449 kg CO2e per USD factor and the 2026 rate of 0.74283 GBP per USD (0.0449 / 0.74283 = 0.0604).

Run from the repo root (needs matplotlib):
    uv run --with matplotlib python figures/scripts/user_guidance_figures.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

OUT = Path(__file__).resolve().parents[2] / "images"
INK, MUTED, GRID = "#1F2933", "#5B6770", "#E3E7EA"
BASE, HI = "#A9BFCC", "#1F5F8B"
plt.rcParams["font.family"] = "DejaVu Sans"

# Chart 1: EF by location
data = [("China", 0.315), ("India", 0.137), ("Global average", 0.0948),
        ("United Kingdom", 0.0449), ("United States", 0.0391), ("France", 0.0390)]
fig, ax = plt.subplots(figsize=(8, 3.6), dpi=200)
labels = [d[0] for d in data][::-1]; vals = [d[1] for d in data][::-1]
cols = [HI if l == "United Kingdom" else BASE for l in labels]
bars = ax.barh(labels, vals, color=cols, height=0.62)
for b, v in zip(bars, vals):
    ax.text(v + 0.006, b.get_y() + b.get_height()/2, f"{v:.3g}" if v>=0.1 else f"{v:.4f}".rstrip("0") if False else (f"{v:.3f}" if v>=0.1 else f"{v:.4f}"), va="center", fontsize=10, color=INK)
ax.set_xlim(0, 0.36)
ax.set_xlabel("kg CO₂e per USD (2026, producer price)", fontsize=9, color=MUTED)
ax.xaxis.grid(True, color=GRID, lw=0.8); ax.set_axisbelow(True)
for s in ("top", "right", "left"): ax.spines[s].set_visible(False)
ax.spines["bottom"].set_color(GRID)
ax.tick_params(axis="y", length=0, labelsize=10, labelcolor=INK)
ax.tick_params(axis="x", labelsize=9, labelcolor=MUTED, colors=GRID)
fig.tight_layout(); fig.savefig(str(OUT / "user-guidance-ef-by-country.png"), facecolor="white"); plt.close(fig)

# Chart 2: worked example flow
fig, ax = plt.subplots(figsize=(10, 2.7), dpi=200)
ax.set_xlim(0, 101); ax.set_ylim(0, 27); ax.axis("off")
boxes = [
    ("£10,000", "Management consulting,\nUnited Kingdom, 2026", "Your spend", BASE, INK),
    ("0.0449", "kg CO₂e per USD", "Emission factor", BASE, INK),
    ("0.0604", "kg CO₂e per £\n(0.0449 ÷ 0.74283)", "Factor in pounds", BASE, INK),
    ("604 kg", "CO₂e\n(0.60 t)", "Emissions", HI, "white"),
]
w, gap, x = 18, 9.2, 1
for i, (big, small, tag, fc, tc) in enumerate(boxes):
    ax.add_patch(FancyBboxPatch((x, 3), w, 18, boxstyle="round,pad=0,rounding_size=1.5",
                                fc=fc if fc == HI else "#EEF3F6", ec=fc, lw=1.4))
    ax.text(x + w/2, 24.2, tag, ha="center", va="center", fontsize=9, color=MUTED)
    ax.text(x + w/2, 15.2, big, ha="center", va="center", fontsize=16, fontweight="bold", color=tc)
    ax.text(x + w/2, 8.2, small, ha="center", va="center", fontsize=8, color=tc if fc == HI else MUTED, linespacing=1.3)
    if i < 3:
        ax.text(x + w + gap/2, 15, ["look up", "÷ 0.74283", "× £10,000"][i], ha="center", va="center", fontsize=7, color=MUTED)
        ax.add_patch(FancyArrowPatch((x + w + 0.6, 11.5), (x + w + gap - 0.6, 11.5), arrowstyle="-|>",
                                     mutation_scale=12, color=MUTED, lw=1.4))
    x += w + gap
ax.text(1 + 2*(w+gap) + w + gap/2 + 0.0, 0.0, "", fontsize=1)
fig.savefig(str(OUT / "user-guidance-worked-example.png"), facecolor="white", bbox_inches="tight", pad_inches=0.1); plt.close(fig)
