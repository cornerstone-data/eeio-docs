"""Write figures/diagrams/release-cycle.svg: the Cornerstone EEIO development and release cycle.

Hand-drawn schematic (no data source). Run from the repo root:
    python3 figures/scripts/release_cycle.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "diagrams" / "release-cycle.svg"
W, H = 680, 376

INK, MUTED, LINE = "#2C2C2A", "#5F5E5A", "#888780"
PURPLE = dict(fill="#EEEDFE", stroke="#534AB7", ink="#3C3489", line="#7F77DD", tint="#F6F5FF")
TEAL = dict(fill="#E1F5EE", stroke="#0F6E56", ink="#085041", tint="#F2FAF6")
CORAL = dict(fill="#FAECE7", stroke="#993C1D", line="#D85A30")
GRAY = dict(fill="#F1EFE8", stroke="#5F5E5A")

els = []
add = els.append


def text(x, y, s, cls="t", anchor="start", fill=None):
    f = f' fill="{fill}"' if fill else ""
    add(f'<text class="{cls}" x="{x}" y="{y}" text-anchor="{anchor}" dominant-baseline="central"{f}>{s}</text>')


def rect(x, y, w, h, fill, stroke, rx=8, sw=1):
    add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')


def dot(cx, cy, r, c):
    add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c["fill"]}" stroke="{c["stroke"]}" stroke-width="1"/>')


def right_arrow(x1, x2, y, color=LINE):
    add(f'<line x1="{x1}" y1="{y}" x2="{x2 - 6}" y2="{y}" stroke="{color}" stroke-width="1.5"/>')
    add(f'<polygon points="{x2},{y} {x2 - 8},{y - 4.5} {x2 - 8},{y + 4.5}" fill="{color}"/>')


def down_arrow(x, y1, y2, color=LINE):
    add(f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2 - 6}" stroke="{color}" stroke-width="1.5"/>')
    add(f'<polygon points="{x},{y2} {x - 4.5},{y2 - 8} {x + 4.5},{y2 - 8}" fill="{color}"/>')


# predecessors merge into Cornerstone EEIO
rect(40, 80, 84, 40, GRAY["fill"], GRAY["stroke"]); text(82, 100, "USEEIO", "th", "middle")
rect(40, 204, 84, 40, GRAY["fill"], GRAY["stroke"]); text(82, 224, "CEDA", "th", "middle")
right_arrow(124, 146, 100); right_arrow(124, 146, 224)
rect(148, 24, 98, 282, "#FFFFFF", LINE)
text(197, 156, "Cornerstone", "th", "middle"); text(197, 174, "EEIO", "th", "middle")

# lane 1: research version
LX, LW = 264, 376
rect(LX, 24, LW, 88, PURPLE["tint"], PURPLE["stroke"], rx=10)
text(LX + 14, 44, "Research version", "th", fill=PURPLE["ink"])
text(LX + LW - 14, 44, "Tests new science", "ts", "end", fill=PURPLE["stroke"])
text(LX + 14, 62, "Continuously updated, with many releases", "ts", fill=PURPLE["stroke"])
add(f'<line x1="{LX + 14}" y1="92" x2="{LX + LW - 14}" y2="92" stroke="{PURPLE["line"]}" stroke-width="2"/>')
for cx in (284, 310, 336, 362, 382, 436, 462, 488, 512, 556, 582, 604, 620):
    dot(cx, 92, 6, PURPLE)
right_arrow(248, 262, 68, PURPLE["line"])

# lane 2: corporate version
rect(LX, 158, LW, 148, TEAL["tint"], TEAL["stroke"], rx=10)
text(LX + 14, 178, "Corporate version", "th", fill=TEAL["ink"])
text(LX + LW - 14, 178, "For targets and reporting", "ts", "end", fill=TEAL["stroke"])
text(LX + 14, 196, "One release every October, stable methods", "ts", fill=TEAL["stroke"])
right_arrow(248, 262, 229, TEAL["stroke"])
bands = [(272, "2026"), (396, "2031"), (520, "2036")]
for x0, yr in bands:
    rect(x0, 208, 114, 88, "#FFFFFF", LINE)
    text(x0 + 57, 224, f"{yr} methods", "th", "middle")
    text(x0 + 57, 241, "Stable 5 years", "ts", "middle")
    for k in range(5):
        cx = x0 + 22 + 17.5 * k
        dot(cx, 262, 8, CORAL) if k == 0 else dot(cx, 262, 5.5, TEAL)
    text(x0 + 22, 283, yr, "ts", "middle")
    text(x0 + 92, 283, str(int(yr) + 4), "ts", "middle")

# proven science: research into the major updates
for x0 in (396, 520):
    down_arrow(x0 + 14, 116, 154, CORAL["line"])
    text(x0 + 24, 135, "Proven science", "ts")

text(340, 328, "Each October release: data updates, bug fixes and small improvements", "ts", "middle")

# legend
dot(46, 356, 6, PURPLE); text(58, 356, "Research release", "ts")
dot(196, 356, 5.5, TEAL); text(208, 356, "Annual release", "ts")
dot(332, 356, 8, CORAL); text(346, 356, "Major update, every 5 years", "ts")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">
<title>USEEIO and CEDA merge into Cornerstone EEIO, which follows a research version and a corporate version from 2026 to 2040</title>
<desc>USEEIO and CEDA merge into the Cornerstone EEIO. The research version is updated continuously with many releases. The corporate version is released every October and keeps its methodology stable for five years. Every five years a major update brings proven science from the research version into a new set of methods.</desc>
<style>
text{{font-family:Helvetica,Arial,sans-serif}}
.t{{font-size:14px;fill:{INK}}} .th{{font-size:14px;font-weight:500;fill:{INK}}} .ts{{font-size:12px;fill:{MUTED}}}
</style>
<rect width="{W}" height="{H}" fill="#FFFFFF"/>
{chr(10).join(els)}
</svg>
'''
OUT.write_text(svg, encoding="utf-8")
print("wrote", OUT)
