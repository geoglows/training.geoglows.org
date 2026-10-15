#!/usr/bin/env python3
"""
Draw the two GLDAS figures, in the same visual grammar as the GRACE diagrams.

The older diagrams in docs/static/images/grace/diagrams were committed as SVG
with no source; these have one, so a number or a label can be corrected without
redrawing. Each figure is written as SVG and rendered to PNG at 2x, which is
what the committed GRACE PNGs are.

Usage:
    uv run --with cairosvg python tools/make_gldas_figures.py
"""

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "docs/static/images/grace"
SVG_DIR, PNG_DIR = ROOT / "diagrams", ROOT

NAVY, BLUE, TEAL, ORANGE, GRAY = "#1f3a5f", "#2b6cb0", "#2c7a7b", "#dd6b20", "#718096"
DARK, LIGHT, PANEL, GOLD, GREEN = "#4a5568", "#e2e8f0", "#f7fafc", "#d69e2e", "#68a063"
FONT = "Helvetica, Arial, sans-serif"

HEADS = {"navy": NAVY, "blue": BLUE, "teal": TEAL, "orange": ORANGE, "gray": GRAY,
         "darkgray": DARK, "gold": GOLD, "green": GREEN}


def marker_defs():
    return "<defs>\n" + "\n".join(
        f'<marker id="ah-{n}" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" '
        f'orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{c}"/></marker>'
        for n, c in HEADS.items()) + "\n</defs>"


def text(x, y, s, size=17, weight="normal", anchor="start", fill=DARK):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return (f'<text x="{x}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" '
            f'text-anchor="{anchor}" fill="{fill}">{s}</text>')


def card(x, y, w, h, title, lines, color, line_size=17, lead=25):
    """A titled box: coloured header bar, white body, one line of text per entry."""
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="white" stroke="{color}" stroke-width="1.8"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="36" rx="8" fill="{color}"/>',
           f'<rect x="{x}" y="{y + 26}" width="{w}" height="10" fill="{color}"/>',
           text(x + w / 2, y + 25, title, 18, "bold", "middle", "white")]
    for i, line in enumerate(lines):
        out.append(text(x + 14, y + 64 + i * lead, line, line_size))
    return "\n".join(out)


def chip(x, y, w, h, label, color, fill="white", size=16):
    return "\n".join([
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{color}" stroke-width="1.6"/>',
        text(x + w / 2, y + h / 2 + 5, label, size, "normal", "middle", DARK)])


def arrow(x1, y1, x2, y2, head="gray", color=GRAY, width=2.2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{width}" '
            f'stroke-linecap="round"{d} marker-end="url(#ah-{head})"/>')


def panel(x, y, w, h):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{PANEL}" stroke="{LIGHT}"/>'


def svg(name, title, width, height, body):
    doc = (f'<?xml version="1.0" encoding="UTF-8"?>\n'
           f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
           f'viewBox="0 0 {width} {height}">\n<title>{title}</title>\n{marker_defs()}\n'
           f'<rect width="{width}" height="{height}" fill="white"/>\n' + body + "\n</svg>\n")
    (SVG_DIR / f"{name}.svg").write_text(doc, encoding="utf-8")
    import cairosvg
    cairosvg.svg2png(bytestring=doc.encode("utf-8"), write_to=str(PNG_DIR / f"{name}.png"), scale=2)
    print(f"wrote {name}.svg and {name}.png ({width * 2}x{height * 2})")


# ---------------------------------------------------------------- water cycle
def water_cycle():
    W, H = 1200, 760
    b = [text(25, 42, "What a GLDAS land surface model computes for one cell", 22, "bold", "start", NAVY),
         text(25, 68, "Water enters as precipitation, is held in four stores, and leaves as evaporation or runoff. "
                      "The model solves this budget every time step.", 16, "normal", "start", GRAY)]

    # Forcing across the top.
    b.append(text(25, 112, "METEOROLOGICAL FORCING", 15, "bold", "start", GRAY))
    forcing = ["Precipitation", "Radiation", "Air temperature", "Humidity", "Wind", "Pressure"]
    for i, f in enumerate(forcing):
        b.append(chip(25 + i * 196, 126, 180, 40, f, BLUE, "#ebf4fb"))
    for i in range(6):
        b.append(arrow(115 + i * 196, 168, 115 + i * 196, 196, "blue", BLUE, 2.0))

    # The column of stores.
    b.append(text(25, 232, "STORES  (what the model carries from one step to the next)", 15, "bold", "start", GRAY))
    stores = [
        (TEAL,  "Canopy water", "CanopInt", "Rain caught on leaves before it reaches the ground"),
        (BLUE,  "Snowpack", "SWE", "Snow held as water equivalent; melts into the soil"),
        (GOLD,  "Soil moisture", "SoilMoist", "Surface, root zone and whole profile"),
        (ORANGE, "Groundwater", "GWS", "Below the water table — Catchment model only"),
    ]
    for i, (c, label, var, note) in enumerate(stores):
        y = 248 + i * 86
        b.append(f'<rect x="25" y="{y}" width="640" height="72" rx="8" fill="white" stroke="{c}" stroke-width="1.8"/>')
        b.append(f'<rect x="25" y="{y}" width="10" height="72" rx="4" fill="{c}"/>')
        b.append(text(50, y + 30, label, 19, "bold", "start", NAVY))
        b.append(text(50, y + 55, note, 16, "normal", "start", DARK))
        b.append(text(650, y + 30, var, 17, "bold", "end", c))
        if i < 3:
            b.append(arrow(345, y + 72, 345, y + 86, "gray", GRAY, 2.0))

    # Fluxes out, to the right.
    b.append(text(720, 232, "FLUXES OUT", 15, "bold", "start", GRAY))
    fluxes = [(GREEN, "Evapotranspiration", "Evap", "From canopy, bare soil and plants"),
              (GRAY, "Surface runoff", "Qs", "Storm runoff that never infiltrates"),
              (ORANGE, "Baseflow", "Qsb", "Drainage out of the groundwater store")]
    for i, (c, label, var, note) in enumerate(fluxes):
        y = 248 + i * 86
        b.append(f'<rect x="720" y="{y}" width="455" height="72" rx="8" fill="white" stroke="{c}" stroke-width="1.8"/>')
        b.append(text(740, y + 30, label, 19, "bold", "start", NAVY))
        b.append(text(740, y + 55, note, 16, "normal", "start", DARK))
        b.append(text(1160, y + 30, var, 17, "bold", "end", c))
        b.append(arrow(668, y + 36, 716, y + 36, "gray", GRAY, 2.0))

    # The budget, and what the app takes from it.
    b.append(panel(25, 608, 1150, 128))
    b.append(text(45, 644, "The storage the app reads", 18, "bold", "start", NAVY))
    b.append(text(45, 676, "TWS  =  CanopInt + SWE + SoilMoist", 18, "bold", "start", TEAL))
    b.append(text(45, 706, "Each is a depth of water, in kg/m² — the same as mm, a tenth of a centimetre.", 16))
    b.append(text(560, 676, "Groundwater is not added again: in the Catchment model it lies inside the soil", 16))
    b.append(text(560, 706, "profile. Noah and VIC have no groundwater store at all.", 16))
    svg("gldas-water-cycle", "What a GLDAS land surface model computes", W, H, "\n".join(b))


# ------------------------------------------------------------------ 2.1 vs 2.2
def versions():
    W, H = 1200, 700
    b = [text(25, 42, "Two ways to the same quantity", 22, "bold", "start", NAVY),
         text(25, 68, "The app carries both. One subtracts models from a measurement; the other reads a model "
                      "that has been corrected by that measurement.", 16, "normal", "start", GRAY)]

    b.append(text(25, 112, "GLDAS 2.1  —  open loop, no assimilation", 15, "bold", "start", TEAL))
    b.append(card(25, 128, 560, 240, "Three models, run blind", [
        "Noah 3.6 (0.25°), VIC 4.1.2 (1°), CLSM-F2.5 (1°)",
        "Forcing: NOAA GDAS analysis, GPCP precipitation,",
        "AGRMET (now GALWEM) radiation",
        "No observation is assimilated — the models run from",
        "their forcing alone, so nothing tells them about pumping",
        "January 2000 to present",
    ], TEAL))
    b.append(card(25, 392, 560, 196, "Groundwater by subtraction", [
        "GRACE measures the whole column, TWSa",
        "The models supply the parts that are not",
        "groundwater, and the rest is what is left",
    ], ORANGE))
    b.append(text(45, 556, "GWSa = TWSa − (SWEa + CANa + SMa)", 19, "bold", "start", ORANGE))
    b.append(arrow(305, 368, 305, 388, "gray", GRAY))

    b.append(text(615, 112, "GLDAS 2.2  —  GRACE assimilated", 15, "bold", "start", BLUE))
    b.append(card(615, 128, 560, 240, "One model, corrected monthly", [
        "Catchment (CLSM-F2.5) only, 0.25°",
        "Forcing: ECMWF IFS operational analysis",
        "Assimilates the GRACE total water storage anomaly",
        "(CSR mascons) through the Land Information System,",
        "which is what puts pumping into the groundwater state",
        "February 2003 to present",
    ], BLUE))
    b.append(card(615, 392, 560, 196, "Groundwater read straight out", [
        "The Catchment model carries groundwater as a",
        "state, so GWS is a published variable and the",
        "anomaly is taken from it directly",
    ], ORANGE))
    b.append(text(635, 556, "GWSa = GWS − its 2004–2009 mean", 19, "bold", "start", ORANGE))
    b.append(arrow(895, 368, 895, 388, "gray", GRAY))

    b.append(panel(25, 612, 1150, 72))
    b.append(text(45, 644, "In the app", 18, "bold", "start", NAVY))
    b.append(text(160, 644, "2.1 route: 1° everywhere, with an uncertainty band, and 35 months missing with GRACE", 16))
    b.append(text(160, 670, "2.2 route: 0.25° in a region and 1° globally, no band, no missing months", 16))
    svg("gldas-2.1-vs-2.2", "GLDAS 2.1 and 2.2 compared", W, H, "\n".join(b))


if __name__ == "__main__":
    water_cycle()
    versions()
