"""Write figures/diagrams/release-lifecycle.svg: the Cornerstone EEIO version lifecycle (option 2).

Hand-drawn schematic (no data source). A new methodology version about every two years;
each gets 3+ years of annual maintenance and data updates, then 2 years of extended support.
Run from the repo root:
    python3 figures/scripts/release_lifecycle.py
"""
from pathlib import Path

OUT = Path(__file__).resolve().parents[1] / "diagrams" / "release-lifecycle.svg"
W, H = 680, 334
INK, MUTED, LINE = "#2C2C2A", "#5F5E5A", "#888780"
TEAL = dict(fill="#E1F5EE", stroke="#0F6E56", ink="#085041", mark="#1D9E75")
GRAY = dict(fill="#F1EFE8", stroke="#5F5E5A", ink="#444441")
CORAL = dict(fill="#FAECE7", stroke="#993C1D")

X0, PY = 170, 39.1
x = lambda year: round(X0 + (year - 2026) * PY, 1)

els = []
add = els.append


def text(px, py, s, cls="ts", anchor="start", fill=None):
    f = f' fill="{fill}"' if fill else ""
    add(f'<text class="{cls}" x="{px}" y="{py}" text-anchor="{anchor}" dominant-baseline="central"{f}>{s}</text>')


def rect(px, py, w, h, c, rx=0):
    add(f'<rect x="{px}" y="{py}" width="{w}" height="{h}" rx="{rx}" fill="{c["fill"]}" stroke="{c["stroke"]}" stroke-width="1"/>')


def marker(cx, cy):
    add(f'<circle cx="{cx}" cy="{cy}" r="5" fill="#FFFFFF" stroke="{TEAL["mark"]}" stroke-width="1.5"/>')


# time axis
add(f'<line x1="{X0}" y1="236" x2="{x(2038)}" y2="236" stroke="{LINE}" stroke-width="1"/>')
for yr in range(2026, 2039):
    add(f'<line x1="{x(yr)}" y1="236" x2="{x(yr)}" y2="242" stroke="{LINE}" stroke-width="1"/>')
    text(x(yr), 254, yr, "ts", "middle")

# one row per version
for i, yr in enumerate((2026, 2028, 2030, 2032)):
    cy = 48 + 52 * i
    s, m, e = x(yr), x(yr + 3), x(yr + 5)
    text(40, cy, f"{yr} methods", "th")
    rect(s, cy - 17, round(m - s, 1), 34, TEAL, rx=3)
    text(round((s + m) / 2 + 4, 1), cy - 7, "Annual updates", "ts", "middle", fill=TEAL["ink"])
    for k in range(3):
        marker(round(s + PY * (k + 0.5), 1), cy + 8)
    rect(m, cy - 17, round(e - m, 1), 34, GRAY, rx=3)
    text(round((m + e) / 2, 1), cy, "2 years", "ts", "middle", fill=GRAY["ink"])
    add(f'<circle cx="{s}" cy="{cy}" r="8" fill="{CORAL["fill"]}" stroke="{CORAL["stroke"]}" stroke-width="1"/>')

text(381, 48, "About 5 years of support per version")
add(f'<line x1="{x(2026)}" y1="74" x2="{x(2028)}" y2="74" stroke="{LINE}" stroke-width="1"/>')
for yr in (2026, 2028):
    add(f'<line x1="{x(yr)}" y1="69" x2="{x(yr)}" y2="79" stroke="{LINE}" stroke-width="1"/>')
text(round((x(2026) + x(2028)) / 2, 1), 88, "~2 years", "ts", "middle")

# legend
rect(40, 278, 14, 12, TEAL, rx=2); text(62, 284, "Maintenance and data updates, 3+ years")
rect(330, 278, 14, 12, GRAY, rx=2); text(352, 284, "Extended support, 2 years")
add(f'<circle cx="47" cy="306" r="7" fill="{CORAL["fill"]}" stroke="{CORAL["stroke"]}" stroke-width="1"/>')
text(62, 306, "Large methodology update: a new version")
marker(337, 306); text(352, 306, "Annual update, every October")

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img">
<title>Cornerstone version lifecycle: a new methodology version about every two years, each with three years of annual updates and two years of extended support</title>
<desc>About every two years a new version with a large methodology update is released. Each version gets at least three years of maintenance with an annual data update every October, then two years of extended support, so companies can adopt a version and rely on about five years of support.</desc>
<style>
text{{font-family:Helvetica,Arial,sans-serif}}
.th{{font-size:14px;font-weight:500;fill:{INK}}} .ts{{font-size:12px;fill:{MUTED}}}
</style>
<rect width="{W}" height="{H}" fill="#FFFFFF"/>
{chr(10).join(els)}
</svg>
'''
OUT.write_text(svg, encoding="utf-8")
print("wrote", OUT)
