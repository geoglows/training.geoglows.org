"""Data processing chain from NASA inputs to the app's storage anomaly grids."""
from common import C, text, line, svg_doc, save

W, H = 1200, 670
BODY, LEAD = 17, 25          # body text size and line spacing
HEAD = 36                    # box title bar height


def box(x, y, w, h, title, lines, col, fill="white"):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{col}" stroke-width="1.8"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="{HEAD}" rx="8" fill="{col}"/>',
           f'<rect x="{x}" y="{y + HEAD - 10}" width="{w}" height="10" fill="{col}"/>',
           text(x + w / 2, y + 25, title, 18, weight="bold", fill="white")]
    for i, s in enumerate(lines):
        indent = 62 if s.startswith("\t") else 0     # a leading tab continues an equation on the next line
        out.append(text(x + 14 + indent, y + HEAD + 28 + i * LEAD, s.lstrip("\t"), BODY, anchor="start"))
    return "\n".join(out)


def arrow(x1, y1, x2, y2, col="gray"):
    return line(x1, y1, x2 - 3, y2, col, 2.2, head=True)


out = [text(25, 42, "From satellite and model data to groundwater storage anomalies", 22, anchor="start",
            weight="bold", fill=C["navy"])]

TOP, BOTTOM, BH = 100, 285, 235
x1, w1 = 25, 270
x2, w2 = x1 + w1 + 40, 240
x3, w3 = x2 + w2 + 40, 250
x4, w4 = x3 + w3 + 40, 270

# column 1: inputs
out.append(text(x1, 86, "INPUTS (monthly)", 15, anchor="start", weight="bold", fill=C["gray"]))
out.append(box(x1, TOP, w1, 160, "GRACE / GRACE-FO", [
    "JPL mascon RL06.3 (CRI)",
    "TWS anomaly + σ",
    "0.5° grid (3° mascons)",
    "Relative to 2004–2009"], C["navy"]))
out.append(box(x1, BOTTOM, w1, BH, "GLDAS 2.1 models", [
    "Noah (0.25°)",
    "VIC (1°)",
    "CLSM (1°)",
    "Snow water equivalent,",
    "canopy water, soil",
    "moisture (all layers, ~2 m)"], C["teal"]))

# column 2: anomalies
out.append(text(x2, 86, "STEP 1", 15, anchor="start", weight="bold", fill=C["gray"]))
out.append(box(x2, BOTTOM, w2, BH, "Anomalies", [
    "Convert kg/m² to cm",
    "of water",
    "Regrid all models to 1°",
    "Subtract each cell's",
    "2004–2009 mean, so",
    "GLDAS anomalies share",
    "GRACE's baseline"], C["teal"]))

# column 3: ensemble
out.append(text(x3, 86, "STEP 2", 15, anchor="start", weight="bold", fill=C["gray"]))
out.append(box(x3, BOTTOM, w3, BH, "Model ensemble", [
    "SWEa, CANa, SMa =",
    "mean of the three",
    "models",
    "Uncertainty of each =",
    "standard deviation",
    "across the three models"], C["teal"]))

# column 4: water balance
out.append(text(x4, 86, "STEP 3", 15, anchor="start", weight="bold", fill=C["gray"]))
out.append(box(x4, TOP, w4, BOTTOM + BH - TOP, "Water balance (1°)", [
    "TWSa averaged to 1°",
    "",
    "GWSa = TWSa − (SWEa",
    "\t+ CANa + SMa)",
    "",
    "σGWSa = √(σ²TWSa",
    "\t+ σ²SWEa + σ²CANa",
    "\t+ σ²SMa)",
    "",
    "Errors treated as",
    "independent",
    ], C["orange"]))

# arrows
ya, yt = BOTTOM + BH / 2, TOP + 80
out += [arrow(x1 + w1, ya, x2, ya), arrow(x2 + w2, ya, x3, ya), arrow(x3 + w3, ya, x4, ya),
        arrow(x1 + w1, yt, x4, yt)]

# outputs strip
oy = BOTTOM + BH + 35
out += [f'<rect x="{x1}" y="{oy}" width="{x4 + w4 - x1}" height="90" rx="8" fill="{C["sky"]}" stroke="{C["lightgray"]}"/>',
        text(x1 + 20, oy + 36, "In the app", 18, anchor="start", weight="bold", fill=C["navy"]),
        text(x1 + 20, oy + 64, "Five layers, each ±1σ:", BODY, anchor="start"),
        text(255, oy + 36, "GWSa, SMa, SWEa, CANa on the 1° grid", BODY, anchor="start", fill=C["darkgray"]),
        text(255, oy + 64, "TWSa on the 0.5° grid, as JPL distributes it", BODY, anchor="start", fill=C["darkgray"]),
        text(680, oy + 36, "Monthly, April 2002 to the latest GRACE-FO release", BODY, anchor="start", fill=C["darkgray"]),
        text(680, oy + 64, "Units: cm of liquid water equivalent", BODY, anchor="start", fill=C["darkgray"])]

print(save("grace-processing", svg_doc(W, H, "\n".join(out), "GRACE Regional Analyst processing chain")))
