"""Data processing chain from NASA inputs to the app's storage anomaly grids."""
from common import C, text, line, svg_doc, save

W, H = 1200, 520


def box(x, y, w, h, title, lines, col, fill="white", tsize=14):
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="8" fill="{fill}" stroke="{col}" stroke-width="1.6"/>',
           f'<rect x="{x}" y="{y}" width="{w}" height="28" rx="8" fill="{col}"/>',
           f'<rect x="{x}" y="{y + 18}" width="{w}" height="10" fill="{col}"/>',
           text(x + w / 2, y + 19, title, tsize, weight="bold", fill="white")]
    for i, s in enumerate(lines):
        out.append(text(x + 12, y + 50 + i * 19, s, 12.5, anchor="start"))
    return "\n".join(out)


def arrow(x1, y1, x2, y2, col="gray"):
    return line(x1, y1, x2 - 3, y2, col, 2, head=True)


out = [text(30, 34, "From satellite and model data to groundwater storage anomalies", 17, anchor="start",
            weight="bold", fill=C["navy"])]

# column 1: inputs
x1, w1 = 30, 260
out.append(text(x1, 70, "INPUTS (monthly)", 12, anchor="start", weight="bold", fill=C["gray"]))
out.append(box(x1, 82, w1, 118, "GRACE / GRACE-FO", [
    "JPL mascon solution RL06.3 (CRI)",
    "Total water storage anomaly + σ",
    "0.5° grid (3° mascons)",
    "Already relative to 2004–2009"], C["navy"]))
out.append(box(x1, 222, w1, 156, "GLDAS 2.1 land surface models", [
    "Noah (0.25°)",
    "VIC (1°)",
    "CLSM (1°)",
    "Snow water equivalent, canopy water,",
    "soil moisture (all layers, ~2 m)"], C["teal"]))

# column 2: anomalies
x2, w2 = 350, 240
out.append(text(x2, 70, "STEP 1", 12, anchor="start", weight="bold", fill=C["gray"]))
out.append(box(x2, 222, w2, 156, "Anomalies", [
    "Convert kg/m² to cm of water",
    "Put all models on a 1° grid",
    "Subtract each cell's 2004–2009",
    "mean, so GLDAS anomalies share",
    "GRACE's baseline"], C["teal"]))

# column 3: ensemble
x3, w3 = 650, 240
out.append(text(x3, 70, "STEP 2", 12, anchor="start", weight="bold", fill=C["gray"]))
out.append(box(x3, 222, w3, 156, "Model ensemble", [
    "SWEa, CANa, SMa = mean of the",
    "three models",
    "Uncertainty of each = standard",
    "deviation across the three",
    "models"], C["teal"]))

# column 4: water balance
x4, w4 = 950, 220
out.append(text(x4, 70, "STEP 3", 12, anchor="start", weight="bold", fill=C["gray"]))
out.append(box(x4, 82, w4, 296, "Water balance (1°)", [
    "TWSa averaged to 1°",
    "",
    "GWSa = TWSa − SWEa",
    "\u00a0" * 13 + "− CANa − SMa",
    "",
    "σGWSa = √(σ²TWSa + σ²SWEa",
    "\u00a0" * 13 + "+ σ²CANa + σ²SMa)",
    "",
    "Errors treated as",
    "independent",
    ], C["orange"]))

# arrows
out += [arrow(x1 + w1, 300, x2, 300), arrow(x2 + w2, 300, x3, 300), arrow(x3 + w3, 300, x4, 300),
        f'<path d="M{x1 + w1},{140} L{x4 - 3},{140}" fill="none" stroke="{C["gray"]}" stroke-width="2" '
        f'marker-end="url(#ah-gray)"/>']

# outputs strip
oy = 420
out += [f'<rect x="30" y="{oy}" width="1140" height="70" rx="8" fill="{C["sky"]}" stroke="{C["lightgray"]}"/>',
        text(50, oy + 28, "In the app", 14, anchor="start", weight="bold", fill=C["navy"]),
        text(50, oy + 50, "Five layers, each with ±1σ:", 12.5, anchor="start"),
        text(300, oy + 28, "GWSa, SMa, SWEa, CANa on the 1° grid", 13.5, anchor="start", fill=C["darkgray"]),
        text(300, oy + 50, "TWSa on the 0.5° grid, as JPL distributes it", 13.5, anchor="start", fill=C["darkgray"]),
        text(700, oy + 28, "Monthly, April 2002 to the latest GRACE-FO release", 13.5, anchor="start", fill=C["darkgray"]),
        text(700, oy + 50, "Units: cm of liquid water equivalent", 13.5, anchor="start", fill=C["darkgray"])]

print(save("grace-processing", svg_doc(W, H, "\n".join(out), "GRACE Regional Analyst processing chain")))
