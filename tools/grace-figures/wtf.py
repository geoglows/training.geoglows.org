"""Conceptual water table fluctuation (WTF) method applied to a GWSa series."""
import math
from common import C, text, line, svg_doc, save, FONT

W, H = 1180, 500
L, R, T, B = 80, 760, 50, 420          # plot box
months = 18                             # previous peak (t=0) to a little after this year's peak


def X(t):
    return L + (t + 1) / (months + 1) * (R - L)


def Y(v):                               # v in cm, range -8 .. 6
    return T + (6 - v) / 14 * (B - T)


# synthetic series: peak at t=0, recession to t=8, wet-season rise to t=12, recession after
def gw(t):
    if t <= 8:
        return 4 - 0.75 * t + 0.25 * math.sin(t)             # recession
    if t <= 12:
        s = (t - 8) / 4
        b = 4 - 0.75 * 8 + 0.25 * math.sin(8)
        return b + (5 - b) * (1 - (1 - s) ** 2)
    return 5 - 0.7 * (t - 12)


pts = [(t / 4, gw(t / 4)) for t in range(0, 4 * 16 + 1)]
SA = (0, gw(0))
SB = (8, gw(8))
SP = (12, gw(12))
slope = (SB[1] - SA[1]) / (SB[0] - SA[0])
SL = (12, SA[1] + slope * 12)

out = []
# seasons
out += [f'<rect x="{X(0):.1f}" y="{T}" width="{X(8) - X(0):.1f}" height="{B - T}" fill="#fdf6ec"/>',
        f'<rect x="{X(8):.1f}" y="{T}" width="{X(12) - X(8):.1f}" height="{B - T}" fill="#eaf4fb"/>',
        f'<rect x="{X(12):.1f}" y="{T}" width="{X(16) - X(12):.1f}" height="{B - T}" fill="#fdf6ec"/>',
        text((X(0) + X(8)) / 2, T + 20, "dry season: storage drains", 12.5, fill="#9c6a1d", italic=True),
        text((X(8) + X(12)) / 2, T + 20, "wet season", 12.5, fill=C["blue"], italic=True)]
# axes
out += [line(L, B, R, B, "darkgray", 1.2), line(L, T, L, B, "darkgray", 1.2),
        f'<text x="0" y="0" transform="translate({L - 46},{(T + B) / 2}) rotate(-90)" font-family="{FONT}" '
        f'font-size="13" text-anchor="middle" fill="{C["darkgray"]}">GWSa (cm)</text>',
        text((L + R) / 2, B + 34, "time (months)", 13)]
# recession line extended
out.append(line(X(SA[0]), Y(SA[1]), X(SL[0]), Y(SL[1]), "red", 2, dash="7 5"))
out.append(text(X(5.2), Y(SA[1] + slope * 5.2) + 34, "recession line, extended", 12.5, fill=C["red"],
                style=f'transform="rotate({math.degrees(math.atan2(Y(SA[1] + slope) - Y(SA[1]), X(1) - X(0))):.1f} {X(5.2):.1f} {Y(SA[1] + slope * 5.2) + 34:.1f})"'))
# series
poly = " ".join(f"{X(t):.1f},{Y(v):.1f}" for t, v in pts)
out.append(f'<polyline points="{poly}" fill="none" stroke="{C["navy"]}" stroke-width="3"/>')
# guide: S_B level across to the peak time
out.append(line(X(SB[0]), Y(SB[1]), X(12) + 40, Y(SB[1]), "gray", 1.2, dash="2 4"))
# points
for (t, v), lab, col, dx, dy in [(SA, "S<tspan font-size='11' baseline-shift='sub'>A</tspan>", C["gray"], 0, -14),
                                  (SB, "S<tspan font-size='11' baseline-shift='sub'>B</tspan>", C["blue"], 0, 26),
                                  (SP, "S<tspan font-size='11' baseline-shift='sub'>P</tspan>", C["blue"], 0, -14),
                                  (SL, "S<tspan font-size='11' baseline-shift='sub'>L</tspan>", C["red"], -20, 6)]:
    out.append(f'<circle cx="{X(t):.1f}" cy="{Y(v):.1f}" r="6" fill="white" stroke="{col}" stroke-width="2.5"/>')
    out.append(f'<text x="{X(t) + dx:.1f}" y="{Y(v) + dy:.1f}" font-family="{FONT}" font-size="15" font-weight="bold" '
               f'text-anchor="middle" fill="{col}">{lab}</text>')
# brackets at peak time
bx = X(12) + 40
for y0, y1, col, lab in [(Y(SP[1]), Y(SB[1]), "blue", "R<tspan font-size='11' baseline-shift='sub'>S</tspan>"),
                         (Y(SB[1]), Y(SL[1]), "red", "R<tspan font-size='11' baseline-shift='sub'>D</tspan>")]:
    out += [line(bx, y0, bx, y1, col, 2.2), line(bx - 7, y0, bx + 7, y0, col, 2.2), line(bx - 7, y1, bx + 7, y1, col, 2.2),
            f'<text x="{bx + 14}" y="{(y0 + y1) / 2 + 5:.1f}" font-family="{FONT}" font-size="15" font-weight="bold" fill="{C[col]}">{lab}</text>']
out.append(text(X(0), B + 18, "previous peak", 11.5, fill=C["gray"]))
out.append(text(X(12), B + 18, "this year's peak", 11.5, fill=C["gray"]))

# legend / equations on the right
ex = 820
eq = lambda y, s, size=15, weight="normal", col=None: (
    f'<text x="{ex}" y="{y}" font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="{col or C["darkgray"]}">{s}</text>')
sub = lambda s: f"<tspan font-size='10' baseline-shift='sub'>{s}</tspan>"
out += [eq(70, "Picks for one water year", 15, "bold", C["navy"]),
        eq(98, f"S{sub('A')}  previous wet-season peak", 13),
        eq(120, f"S{sub('B')}  lowest point before the rise", 13),
        eq(142, f"S{sub('P')}  this wet season's peak", 13),
        eq(164, f"S{sub('L')}  where storage would have been", 13),
        eq(182, "      at the peak with no recharge", 13),
        eq(226, "Recharge", 15, "bold", C["navy"]),
        eq(256, f"R{sub('S')} = S{sub('P')} − S{sub('B')}   (visible rise)", 14, col=C["blue"]),
        eq(282, f"R{sub('D')} = S{sub('B')} − S{sub('L')}   (drainage offset)", 14, col=C["red"]),
        f'<rect x="{ex - 10}" y="304" width="340" height="80" rx="8" fill="{C["sky"]}" stroke="{C["blue"]}"/>',
        eq(334, f"Method 1:  R = R{sub('S')}", 15, "bold", C["navy"]),
        eq(366, f"Method 2:  R = R{sub('S')} + R{sub('D')} = S{sub('P')} − S{sub('L')}", 15, "bold", C["navy"]),
        eq(412, "GWSa is already a depth of water, so no", 12.5, col=C["gray"]),
        eq(430, "specific yield is needed: R is in cm per year.", 12.5, col=C["gray"])]

print(save("wtf-concept", svg_doc(W, H, "\n".join(out), "Water table fluctuation method")))
