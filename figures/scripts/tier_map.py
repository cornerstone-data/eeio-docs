"""Generate figures/diagrams/country-tiers-map.svg: a world map colored by country tier.

Usage:
    python figures/scripts/tier_map.py [path/to/ne_50m_admin_0_countries.geojson]

Tiers come from data/country_tiers.csv. Country outlines come from Natural Earth
1:50m admin-0 countries (public domain); the file is downloaded to a temp folder
if no path is given. Countries too small to see at this scale are drawn as dots.
"""

from __future__ import annotations

import csv
import json
import math
import os
import sys
import tempfile
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TIERS_CSV = os.path.join(ROOT, "data", "country_tiers.csv")
OUT_SVG = os.path.join(ROOT, "figures", "diagrams", "country-tiers-map.svg")
NE_URL = (
    "https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/"
    "geojson/ne_50m_admin_0_countries.geojson"
)

# One-hue ordinal ramp (darker = more detailed data), validated with the dataviz
# palette checker against the white page surface.
TIER_COLORS = {"0": "#0b3550", "1": "#175f8c", "2": "#2c8ec4", "3": "#72b8dc"}
NOT_MODELED = "#dcdcd8"
BORDER = "#ffffff"
TEXT = "#2c3746"
TEXT_2 = "#6a727c"

WIDTH = 960
MAP_TOP = 10
SIMPLIFY_PX = 0.35  # Douglas-Peucker tolerance in output pixels
DOT_IF_AREA_BELOW = 14.0  # px²: countries smaller than this also get a dot
DOT_R = 2.6


def equal_earth(lon: float, lat: float) -> tuple[float, float]:
    a1, a2, a3, a4 = 1.340264, -0.081106, 0.000893, 0.003796
    m = math.sqrt(3) / 2
    lam, phi = math.radians(lon), math.radians(lat)
    t = math.asin(m * math.sin(phi))
    t2, t6 = t * t, t**6
    x = lam * math.cos(t) / (m * (a1 + 3 * a2 * t2 + t6 * (7 * a3 + 9 * a4 * t2)))
    y = t * (a1 + a2 * t2 + t6 * (a3 + a4 * t2))
    return x, y


# Equal Earth extent: x in [-2.7064, 2.7064], y in [-1.3173, 1.3173]
X_MAX, Y_MAX = 2.7064, 1.3173
SCALE = (WIDTH - 20) / (2 * X_MAX)
Y_TOP = equal_earth(0, 84)[1]
Y_CUT = equal_earth(0, -58)[1]  # crop Antarctica and the far south
MAP_H = (Y_TOP - Y_CUT) * SCALE


def to_px(lon: float, lat: float) -> tuple[float, float]:
    x, y = equal_earth(lon, lat)
    return 10 + (x + X_MAX) * SCALE, MAP_TOP + (Y_TOP - y) * SCALE


def dp(points: list[tuple[float, float]], tol: float) -> list[tuple[float, float]]:
    if len(points) < 3:
        return points
    (x1, y1), (x2, y2) = points[0], points[-1]
    dx, dy = x2 - x1, y2 - y1
    norm = math.hypot(dx, dy) or 1e-12
    dmax, idx = 0.0, 0
    for i in range(1, len(points) - 1):
        px, py = points[i]
        d = abs(dy * px - dx * py + x2 * y1 - y2 * x1) / norm
        if d > dmax:
            dmax, idx = d, i
    if dmax > tol:
        return dp(points[: idx + 1], tol)[:-1] + dp(points[idx:], tol)
    return [points[0], points[-1]]


def ring_area(pts: list[tuple[float, float]]) -> float:
    return 0.5 * abs(
        sum(pts[i][0] * pts[i - 1][1] - pts[i - 1][0] * pts[i][1] for i in range(len(pts)))
    )


def iso_of(props: dict) -> str:
    for key in ("ISO_A3", "ISO_A3_EH", "ADM0_A3"):
        v = props.get(key)
        if v and v != "-99":
            return v
    return ""


def main() -> None:
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(tempfile.gettempdir(), "ne_50m_admin_0_countries.geojson")
    if not os.path.exists(src):
        urllib.request.urlretrieve(NE_URL, src)
    geo = json.load(open(src, encoding="utf-8"))

    tiers: dict[str, str] = {}
    with open(TIERS_CSV, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            tiers[row["iso3"]] = row["tier"]

    shapes: list[str] = []
    dots: list[str] = []
    found: set[str] = set()
    for feat in geo["features"]:
        iso = iso_of(feat["properties"])
        if iso == "ATA":
            continue
        tier = tiers.get(iso)
        fill = TIER_COLORS[tier] if tier else NOT_MODELED
        geom = feat["geometry"]
        polys = geom["coordinates"] if geom["type"] == "MultiPolygon" else [geom["coordinates"]]
        d_parts: list[str] = []
        total_area, best = 0.0, None
        for poly in polys:
            for ri, ring in enumerate(poly):
                pts = [to_px(lon, max(lat, -58)) for lon, lat in ring]
                if ri == 0:
                    a = ring_area(pts)
                    total_area += a
                    if best is None or a > best[0]:
                        best = (a, pts)
                # A closed ring starts and ends on the same point, so simplify it
                # as two open halves.
                mid = len(pts) // 2
                simp = dp(pts[: mid + 1], SIMPLIFY_PX)[:-1] + dp(pts[mid:], SIMPLIFY_PX)
                if len(simp) < 3:
                    continue
                d_parts.append("M" + "L".join(f"{x:.1f},{y:.1f}" for x, y in simp) + "Z")
        if tier:
            found.add(iso)
        name = feat["properties"].get("NAME", iso)
        label = f"{name}: Tier {tier}" if tier else f"{name}: not modeled separately"
        if d_parts:
            shapes.append(
                f'<path d="{"".join(d_parts)}" fill="{fill}"><title>{label}</title></path>'
            )
        if tier and total_area < DOT_IF_AREA_BELOW and best:
            pts = best[1]
            cx = sum(p[0] for p in pts) / len(pts)
            cy = sum(p[1] for p in pts) / len(pts)
            dots.append(
                f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{DOT_R}" fill="{fill}" '
                f'stroke="{BORDER}" stroke-width="0.8"><title>{label}</title></circle>'
            )

    missing = sorted(set(tiers) - found)
    if missing:
        print("Not found in Natural Earth (not drawn):", ", ".join(missing))

    counts = {t: sum(1 for v in tiers.values() if v == t) for t in "0123"}
    legend_items = [
        (TIER_COLORS["0"], "Tier 0", "United States"),
        (TIER_COLORS["1"], "Tier 1", f"National tables ({counts['1']})"),
        (TIER_COLORS["2"], "Tier 2", f"FIGARO or ICIO ({counts['2']})"),
        (TIER_COLORS["3"], "Tier 3", f"Proxy tables ({counts['3']})"),
        (NOT_MODELED, "Not modeled", "Part of rest of world"),
    ]
    ly = MAP_TOP + MAP_H + 30
    legend: list[str] = []
    col_w = (WIDTH - 20) / len(legend_items)
    for i, (color, head, sub) in enumerate(legend_items):
        x = 10 + i * col_w
        legend.append(f'<rect x="{x:.0f}" y="{ly - 14:.0f}" width="18" height="18" rx="3" fill="{color}"/>')
        legend.append(
            f'<text x="{x + 25:.0f}" y="{ly:.0f}" font-size="17" fill="{TEXT}">'
            f'<tspan font-weight="700">{head}</tspan>'
            f'<tspan x="{x + 25:.0f}" dy="21" font-size="15" fill="{TEXT_2}">{sub}</tspan></text>'
        )
    height = ly + 36

    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {WIDTH} {height:.0f}" '
        f'width="{WIDTH}" height="{height:.0f}" '
        f'font-family="DM Sans, Segoe UI, Helvetica, Arial, sans-serif" role="img" '
        f'aria-label="World map of countries colored by data tier">\n'
        f'<rect width="{WIDTH}" height="{height:.0f}" fill="#ffffff"/>\n'
        f'<g stroke="{BORDER}" stroke-width="0.5" stroke-linejoin="round">\n'
        + "\n".join(shapes)
        + "\n</g>\n<g>\n"
        + "\n".join(dots)
        + "\n</g>\n"
        + "\n".join(legend)
        + "\n</svg>\n"
    )
    with open(OUT_SVG, "w", encoding="utf-8", newline="\n") as f:
        f.write(svg)
    print(f"Wrote {OUT_SVG} ({os.path.getsize(OUT_SVG) / 1024:.0f} KB), {len(dots)} dots")


if __name__ == "__main__":
    main()
