#!/usr/bin/env python3
"""
Draw the figures that have a source, in the visual grammar of the GRACE set.

Most diagrams under docs/static/images/grace/diagrams were committed as SVG with
no source, so correcting a label meant redrawing one by hand. These are
generated: a number or a wording changes here and both the SVG and the PNG
follow. Each is written as SVG and rendered to PNG at 2x, which is what the
committed GRACE PNGs are.

Usage:
    uv run --with cairosvg python tools/make_figures.py
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
    W, H = 1200, 800
    b = [text(25, 42, "What a GLDAS land surface model computes for one cell", 22, "bold", "start", NAVY),
         text(25, 68, "Every GLDAS model solves this budget each time step. What differs between versions is which stores "
                      "exist and which the app reads,", 16, "normal", "start", GRAY),
         text(25, 90, "and that is set out at the foot of the figure. Every store is a depth of water in kg/m², "
                      "which is the same as a millimetre.", 16, "normal", "start", GRAY)]

    # Forcing across the top.
    b.append(text(25, 134, "METEOROLOGICAL FORCING", 15, "bold", "start", GRAY))
    forcing = ["Precipitation", "Radiation", "Air temperature", "Humidity", "Wind", "Pressure"]
    for i, f in enumerate(forcing):
        b.append(chip(25 + i * 196, 148, 180, 40, f, BLUE, "#ebf4fb"))
    for i in range(6):
        b.append(arrow(115 + i * 196, 190, 115 + i * 196, 218, "blue", BLUE, 2.0))

    # The column of stores.
    b.append(text(25, 254, "STORES  (carried from one time step to the next)", 15, "bold", "start", GRAY))
    stores = [
        (TEAL,  "Canopy water", "CanopInt", "Rain caught on leaves before it reaches the ground", "both"),
        (BLUE,  "Snowpack", "SWE", "Snow held as water equivalent; melts into the soil", "both"),
        (GOLD,  "Soil moisture", "SoilMoist", "Surface, root zone and whole profile", "both"),
        (ORANGE, "Groundwater", "GWS", "Below the water table", "2.2 only"),
    ]
    for i, (c, label, var, note, which) in enumerate(stores):
        y = 270 + i * 86
        b.append(f'<rect x="25" y="{y}" width="640" height="72" rx="8" fill="white" stroke="{c}" stroke-width="1.8"/>')
        b.append(f'<rect x="25" y="{y}" width="10" height="72" rx="4" fill="{c}"/>')
        b.append(text(50, y + 30, label, 19, "bold", "start", NAVY))
        b.append(text(50, y + 55, note, 16, "normal", "start", DARK))
        b.append(text(560, y + 30, var, 17, "bold", "end", c))
        tag = "in both versions" if which == "both" else "GLDAS 2.2 only"
        tagc = GRAY if which == "both" else ORANGE
        b.append(text(560, y + 55, tag, 14, "bold", "end", tagc))
        if i < 3:
            b.append(arrow(345, y + 72, 345, y + 86, "gray", GRAY, 2.0))

    # Fluxes out, to the right.
    b.append(text(720, 254, "FLUXES OUT", 15, "bold", "start", GRAY))
    fluxes = [(GREEN, "Evapotranspiration", "Evap", "From canopy, bare soil and plants"),
              (GRAY, "Surface runoff", "Qs", "Storm runoff that never infiltrates"),
              (ORANGE, "Baseflow", "Qsb", "Drainage out of the groundwater store")]
    for i, (c, label, var, note) in enumerate(fluxes):
        y = 270 + i * 86
        b.append(f'<rect x="720" y="{y}" width="455" height="72" rx="8" fill="white" stroke="{c}" stroke-width="1.8"/>')
        b.append(text(740, y + 30, label, 19, "bold", "start", NAVY))
        b.append(text(740, y + 55, note, 16, "normal", "start", DARK))
        b.append(text(1160, y + 30, var, 17, "bold", "end", c))
        b.append(arrow(668, y + 36, 716, y + 36, "gray", GRAY, 2.0))

    # What each version gives the app. Two columns, with a rule between them so
    # a line from one cannot be read as part of the other.
    b.append(panel(25, 630, 1150, 150))
    b.append(f'<line x1="600" y1="652" x2="600" y2="758" stroke="{LIGHT}" stroke-width="2"/>')
    b.append(text(45, 678, "GLDAS 2.1  —  three models, run blind", 18, "bold", "start", TEAL))
    for i, line in enumerate([
            "The app takes CanopInt, SWE and SoilMoist from Noah, VIC and",
            "the Catchment model and averages the three. It takes no",
            "groundwater: Noah and VIC have no such store, and with nothing",
            "assimilated the Catchment model's follows rainfall alone."]):
        b.append(text(45, 706 + i * 23, line, 15))
    b.append(text(625, 678, "GLDAS 2.2  —  Catchment model, corrected by GRACE", 18, "bold", "start", BLUE))
    for i, line in enumerate([
            "TWS = CanopInt + SWE + SoilMoist. Groundwater is not added",
            "again: in the Catchment model it lies inside the soil profile.",
            "GWS is published as its own variable, and the app reads it",
            "directly as groundwater."]):
        b.append(text(625, 706 + i * 23, line, 15))
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
    b.append(text(160, 644, "2.1 route: 1°, except TWSa at 0.5°, with an uncertainty band, and 35 months missing with GRACE", 16))
    b.append(text(160, 670, "2.2 route: 0.25° in a region and 1° globally, no band, no missing months", 16))
    svg("gldas-2.1-vs-2.2", "GLDAS 2.1 and 2.2 compared", W, H, "\n".join(b))


# ------------------------------------------------------------- processing chain
def processing_chain():
    """
    The GRACE + GLDAS 2.1 chain. Redrawn from the hand-authored original to add
    the gain factors, which the pipeline had never applied and the figure
    therefore never showed.
    """
    W, H = 1200, 700
    COL, GAP = 265, 30
    xs = [25, 320, 615, 910]
    b = [text(25, 42, "From satellite and model data to groundwater storage anomalies", 22, "bold", "start", NAVY),
         text(25, 68, "The GRACE + GLDAS 2.1 route. GLDAS 2.2 reaches groundwater without any of this; see the "
                      "page text.", 16, "normal", "start", GRAY)]

    for i, label in enumerate(["INPUTS (monthly)", "STEP 1", "STEP 2", "STEP 3"]):
        b.append(text(xs[i], 112, label, 15, "bold", "start", GRAY))

    b.append(card(xs[0], 126, COL, 190, "GRACE / GRACE-FO", [
        "JPL mascon RL06.3 (CRI)", "TWS anomaly + \u03c3", "0.5\u00b0 grid (3\u00b0 mascons)",
        "Relative to 2004\u20132009",
    ], NAVY, 16, 24))
    b.append(card(xs[1], 126, COL, 190, "Gain factors", [
        "Multiply TWSa and its \u03c3", "by JPL's factor for the cell,", "at 0.5\u00b0, before averaging",
        "Factors outside (0, 3] are", "left unapplied",
    ], GOLD, 16, 24))
    b.append(card(xs[0], 346, COL, 230, "GLDAS 2.1 models", [
        "Noah (0.25\u00b0)", "VIC (1\u00b0)", "CLSM (1\u00b0)", "Snow water equivalent,",
        "canopy water, soil", "moisture (all layers)",
    ], TEAL, 16, 24))
    b.append(card(xs[1], 346, COL, 230, "Anomalies", [
        "Convert kg/m\u00b2 to cm", "Regrid all models to 1\u00b0", "Subtract each cell's",
        "2004\u20132009 mean, so GLDAS", "shares GRACE's baseline",
    ], TEAL, 16, 24))
    b.append(card(xs[2], 346, COL, 230, "Model ensemble", [
        "SWEa, CANa, SMa =", "mean of the three models", "Uncertainty of each =",
        "standard deviation", "across the three",
    ], TEAL, 16, 24))
    b.append(card(xs[3], 126, COL, 450, "Water balance (1\u00b0)", [
        "Scaled TWSa averaged to 1\u00b0", "", "GWSa = TWSa \u2212 (SWEa", "        + CANa + SMa)", "",
        "\u03c3GWSa = \u221a(\u03c3\u00b2TWSa", "        + \u03c3\u00b2SWEa + \u03c3\u00b2CANa", "        + \u03c3\u00b2SMa)", "",
        "Errors treated as", "independent",
    ], ORANGE, 16, 24))

    b.append(arrow(xs[0] + COL, 221, xs[1] - 3, 221))
    b.append(arrow(xs[1] + COL, 170, xs[3] - 3, 170))
    b.append(arrow(xs[0] + COL, 461, xs[1] - 3, 461))
    b.append(arrow(xs[1] + COL, 461, xs[2] - 3, 461))
    b.append(arrow(xs[2] + COL, 461, xs[3] - 3, 461))

    b.append(panel(25, 606, 1150, 80))
    b.append(text(45, 640, "In the app", 18, "bold", "start", NAVY))
    b.append(text(45, 668, "Five layers, each \u00b11\u03c3:", 16))
    b.append(text(255, 640, "GWSa, SMa, SWEa, CANa on the 1\u00b0 grid", 16))
    b.append(text(255, 668, "TWSa on the 0.5\u00b0 grid, with the gain factors applied", 16))
    b.append(text(700, 640, "Monthly, April 2002 to the latest GRACE-FO release", 16))
    b.append(text(700, 668, "Units: cm of liquid water equivalent", 16))
    svg("grace-processing", "GRACE Regional Analyst processing chain", W, H, "\n".join(b))


if __name__ == "__main__":
    water_cycle()
    versions()
    processing_chain()
