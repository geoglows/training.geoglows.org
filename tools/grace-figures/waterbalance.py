"""Terrestrial water storage components and the groundwater water balance."""
import random
from common import C, text, line, svg_doc, save, FONT

W, H = 1180, 560
random.seed(4)

SOIL = "#b08d57"
SOIL_BG = "#e8d5b0"
AQ = "#7fb3d5"
AQ_BG = "#cfe3f1"
ROCK = "#c9c9c9"
CAN = "#4f8a3c"
SNOW = "#ffffff"

X0, X1 = 40, 640
SKY0, SURF, SOILB, WT, AQB, BOT = 60, 230, 300, 340, 470, 510


SM_DEPTH = 30                # soil moisture band thickness below the surface (drawing units)
LAKE_L, LAKE_R, LAKE_D = X0 + 440, X0 + 575, 34
LAKE_LEVEL = SURF + 5


def bez(p0, p1, p2, p3, n=40):
    return [((1 - t) ** 3 * p0[0] + 3 * (1 - t) ** 2 * t * p1[0] + 3 * (1 - t) * t ** 2 * p2[0] + t ** 3 * p3[0],
             (1 - t) ** 3 * p0[1] + 3 * (1 - t) ** 2 * t * p1[1] + 3 * (1 - t) * t ** 2 * p2[1] + t ** 3 * p3[1])
            for t in (i / n for i in range(n + 1))]


def surface_points():
    # mountain at left, plain, then a lake basin with gently sloping banks
    lm = (LAKE_L + LAKE_R) / 2
    pts = bez((X0, SURF - 90), (X0 + 60, SURF - 150), (X0 + 120, SURF - 150), (X0 + 170, SURF - 70))
    pts += bez((X0 + 170, SURF - 70), (X0 + 200, SURF - 20), (X0 + 240, SURF), (X0 + 300, SURF))[1:]
    pts += [(LAKE_L, SURF)]
    pts += bez((LAKE_L, SURF), (LAKE_L + 30, SURF), (lm - 40, SURF + LAKE_D), (lm, SURF + LAKE_D))[1:]
    pts += bez((lm, SURF + LAKE_D), (lm + 40, SURF + LAKE_D), (LAKE_R - 30, SURF), (LAKE_R, SURF))[1:]
    pts += [(X1, SURF)]
    return pts


def poly(pts):
    return "M" + " L".join(f"{x:.1f},{y:.1f}" for x, y in pts)


def surf_y(x, pts):
    for (xa, ya), (xb, yb) in zip(pts, pts[1:]):
        if xa <= x <= xb:
            return ya + (yb - ya) * (x - xa) / (xb - xa) if xb > xa else ya
    return pts[-1][1]


SP = surface_points()
sp = poly(SP)
band = SP + [(x, y + SM_DEPTH) for x, y in reversed(SP)]

out = []
out.append(f'<clipPath id="xs"><rect x="{X0}" y="{SKY0}" width="{X1 - X0}" height="{BOT - SKY0}" rx="10"/></clipPath>')
out.append('<g clip-path="url(#xs)">')
out.append(f'<rect x="{X0}" y="{SKY0}" width="{X1 - X0}" height="{BOT - SKY0}" fill="{C["sky"]}"/>')
# unsaturated zone, soil moisture band along the surface, aquifer, bedrock
out.append(f'<path d="{sp} L{X1},{BOT} L{X0},{BOT} Z" fill="#efe6d4"/>')
out.append(f'<path d="{poly(band)} Z" fill="{SOIL_BG}"/>')
out.append(f'<path d="{poly([(x, y + SM_DEPTH) for x, y in SP])}" fill="none" stroke="{C["groundline"]}" '
           f'stroke-width="1" stroke-dasharray="4 4"/>')
out.append(f'<path d="M{X0},{WT} C{X0 + 200},{WT - 6} {X0 + 400},{WT + 4} {X1},{WT - 2} L{X1},{AQB} L{X0},{AQB} Z" fill="{AQ_BG}"/>')
out.append(f'<rect x="{X0}" y="{AQB}" width="{X1 - X0}" height="{BOT - AQB}" fill="{ROCK}"/>')
# texture dots
for _ in range(260):
    x = random.uniform(X0, X1); y = random.uniform(WT + 6, AQB - 4)
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.6" fill="{AQ}"/>')
n = 0
while n < 150:
    x = random.uniform(X0, X1)
    y = surf_y(x, SP) + random.uniform(4, SM_DEPTH - 3)
    out.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="1.5" fill="{SOIL}" opacity="0.7"/>')
    n += 1
# water table
out.append(f'<path d="M{X0},{WT} C{X0 + 200},{WT - 6} {X0 + 400},{WT + 4} {X1},{WT - 2}" fill="none" stroke="{C["blue"]}" stroke-width="2"/>')
wx = X0 + 120
out.append(f'<path d="M{wx - 8},{WT - 15} L{wx + 8},{WT - 15} L{wx},{WT - 4} Z" fill="{C["blue"]}"/>')
out.append(line(wx - 6, WT - 1, wx + 6, WT - 1, "blue", 1.2))
# lake: the basin below a level water surface
lake = [(x, y) for x, y in SP if LAKE_L - 1 <= x <= LAKE_R + 1 and y >= LAKE_LEVEL]
out.append(f'<path d="M{lake[0][0]:.1f},{LAKE_LEVEL} {poly(lake)[1:].replace("M", "L")} L{lake[-1][0]:.1f},{LAKE_LEVEL} Z" '
           f'fill="#4a90d9"/>')
out.append(line(lake[0][0], LAKE_LEVEL, lake[-1][0], LAKE_LEVEL, "blue", 1.5))
lm = (LAKE_L + LAKE_R) / 2
for dx, w in [(-28, 22), (12, 16), (-6, 10)]:
    yy = LAKE_LEVEL + (6 if w != 10 else 13)
    out.append(f'<line x1="{lm + dx:.1f}" y1="{yy}" x2="{lm + dx + w:.1f}" y2="{yy}" stroke="white" stroke-width="1.5" '
               f'stroke-linecap="round" opacity="0.6"/>')
# surface
out.append(f'<path d="{sp}" fill="none" stroke="{C["groundline"]}" stroke-width="2"/>')
# snow cap: the mountain shape clipped above a zigzag snow line
zz = " ".join(f"L{X0 + 30 + 16 * k},{SURF - (112 if k % 2 else 100)}" for k in reversed(range(9)))
out.append(f'<clipPath id="snowclip"><path d="M{X0},{SKY0} L{X0 + 200},{SKY0} L{X0 + 200},{SURF - 100} {zz} L{X0},{SURF - 100} Z"/></clipPath>')
out.append(f'<path d="{sp} L{X1},{BOT} L{X0},{BOT} Z" fill="{SNOW}" stroke="#a0aec0" stroke-width="1" clip-path="url(#snowclip)"/>')
# trees
for tx, s in [(X0 + 330, 1.0), (X0 + 372, 0.8), (X0 + 590, 0.9)]:
    out.append(f'<rect x="{tx - 3 * s:.1f}" y="{SURF - 30 * s:.1f}" width="{6 * s:.1f}" height="{30 * s:.1f}" fill="#7a5c3a"/>')
    out.append(f'<ellipse cx="{tx}" cy="{SURF - 46 * s:.1f}" rx="{24 * s:.1f}" ry="{28 * s:.1f}" fill="{CAN}"/>')
    for dx, dy in [(-8, -8), (6, -2), (-2, 8)]:
        out.append(f'<path d="M{tx + dx * s:.1f},{SURF - (52 - dy) * s - 4:.1f} q3,5 0,7 q-3,-2 0,-7 z" fill="{C["lightblue"]}"/>')
out.append('</g>')
out.append(f'<rect x="{X0}" y="{SKY0}" width="{X1 - X0}" height="{BOT - SKY0}" rx="10" fill="none" stroke="{C["lightgray"]}"/>')


def tag(x, y, label, col, anchor="start"):
    w = len(label) * 7.6 + 16
    bx = x if anchor == "start" else x - w
    return (f'<rect x="{bx:.1f}" y="{y - 15}" width="{w:.1f}" height="22" rx="4" fill="white" opacity="0.9" stroke="{col}"/>'
            + text(bx + w / 2, y + 1, label, 13, weight="bold", fill=col))


out += [tag(X0 + 160, SKY0 + 26, "Snow water equivalent (SWE)", C["navy"]),
        line(X0 + 175, SKY0 + 34, X0 + 120, SURF - 118, "navy", 1),
        tag(X0 + 290, SURF - 92, "Canopy water (CAN)", CAN),
        tag(X0 + 330, SURF + 66, "Surface water (assumed small)", C["blue"]),
        line(lm + 10, SURF + 51, lm + 10, SURF + LAKE_D - 6, "blue", 1),
        tag(X0 + 14, SURF + 14, "Soil moisture (SM)", "#8a6a37"),
        line(X0 + 150, SURF - 1, X0 + 178, surf_y(X0 + 178, SP) + SM_DEPTH / 2, "darkgray", 1),
        tag(X0 + 14, WT + 66, "Groundwater (GWS)", C["navy"]),
        text(X0 + 150, WT - 10, "water table", 12, anchor="start", fill=C["blue"], italic=True),
        text(X0 + 300, SURF + SM_DEPTH + 16, "~2 m soil column", 11, anchor="start", fill="#8a6a37", italic=True),
        text(X0 + (X1 - X0) / 2, BOT - 12, "bedrock", 11, fill=C["darkgray"], italic=True)]

# brace: GRACE senses the whole column
bx = X1 + 22
out += [f'<path d="M{bx},{SKY0 + 10} q12,0 12,12 L{bx + 12},{(SKY0 + BOT) / 2 - 12} q0,12 12,12 q-12,0 -12,12 '
        f'L{bx + 12},{BOT - 22} q0,12 -12,12" fill="none" stroke="{C["orange"]}" stroke-width="2.5"/>']
tx = bx + 40
ym = (SKY0 + BOT) / 2
out += [f'<text x="0" y="0" transform="translate({bx + 44},{ym}) rotate(-90)" font-family="{FONT}" font-size="14" '
        f'font-weight="bold" text-anchor="middle" fill="{C["orange"]}">GRACE senses the whole column (TWS)</text>']

# equations on the right
ex = bx + 80
out += [text(ex, 110, "GRACE measures the total:", 14, anchor="start", weight="bold", fill=C["navy"]),
        f'<text x="{ex}" y="140" font-family="{FONT}" font-size="17" fill="{C["darkgray"]}">'
        f'TWSa = SWEa + CANa + SMa + GWSa</text>',
        text(ex, 200, "GLDAS land surface models", 14, anchor="start", weight="bold", fill=C["navy"]),
        text(ex, 220, "(mean of Noah, VIC and CLSM) supply:", 14, anchor="start", weight="bold", fill=C["navy"]),
        f'<text x="{ex}" y="250" font-family="{FONT}" font-size="17" fill="{C["darkgray"]}">SWEa, CANa, SMa</text>',
        text(ex, 310, "Groundwater is the remainder:", 14, anchor="start", weight="bold", fill=C["navy"]),
        f'<rect x="{ex - 10}" y="322" width="420" height="44" rx="8" fill="{C["sky"]}" stroke="{C["blue"]}" stroke-width="1.5"/>',
        f'<text x="{ex + 4}" y="351" font-family="{FONT}" font-size="18" font-weight="bold" fill="{C["navy"]}">'
        f'GWSa = TWSa − (SWEa + CANa + SMa)</text>',
        text(ex, 400, "Each term is an anomaly (suffix “a”): the", 13, anchor="start"),
        text(ex, 418, "departure from its 2004–2009 mean, in cm", 13, anchor="start"),
        text(ex, 436, "of liquid water equivalent.", 13, anchor="start")]

print(save("grace-water-balance", svg_doc(W, H, "\n".join(out), "Terrestrial water storage components")))
