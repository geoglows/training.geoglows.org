"""Conceptual water table fluctuation (WTF) method applied to a GWSa series."""
import math
from common import C, text, line, svg_doc, save, FONT

W, H = 1180, 500
L, R, T, B = 80, 760, 50, 420          # plot box
months = 18                             # previous peak (t=0) to a little after this year's peak


def X(t):
    return L + (t + 1) / (months + 1) * (R - L)


def Y(v):                               # vertical range fitted to the series and S_L below
    return T + (Y_TOP - v) / (Y_TOP - Y_BOT) * (B - T)


# Synthetic series from a linear reservoir: storage drains in proportion to its height above a base
# level, and a smooth recharge pulse arrives each wet season. Spun up over several years so the cycle
# is periodic, then cut from one wet-season peak (S_A, t = 0) to a few months past the next one.
K, BASE, DT = 0.03, -20.0, 0.01                 # drainage rate (1/month), base level (cm), step (months)


def recharge(t):
    m = t % 12
    return 4.0 * math.exp(-((m - 9.0) / 1.4) ** 2 / 2)


series, s, t = [], 0.0, 0.0
while t < 90:
    s += DT * (recharge(t) - K * (s - BASE))
    t += DT
    series.append((t, s))
peaks = [series[i] for i in range(1, len(series) - 1)
         if series[i][1] > series[i - 1][1] and series[i][1] >= series[i + 1][1] and series[i][0] > 36]
t0 = peaks[0][0]
pts = [(tt - t0, v) for tt, v in series if t0 <= tt <= t0 + 16]
step = max(1, len(pts) // 200)
pts = pts[::step]

SA = pts[0]
SB = min((p for p in pts if p[0] < 12), key=lambda p: p[1])
SP = max((p for p in pts if p[0] > SB[0]), key=lambda p: p[1])
# recession line: least-squares fit through the series from S_A to S_B; its slope is carried on from S_B
# to the peak time, as the app does
fit = [p for p in pts if p[0] <= SB[0]]
n = len(fit); mx = sum(p[0] for p in fit) / n; my = sum(p[1] for p in fit) / n
slope = sum((p[0] - mx) * (p[1] - my) for p in fit) / sum((p[0] - mx) ** 2 for p in fit)
icpt = my - slope * mx
SL = (SP[0], SB[1] + slope * (SP[0] - SB[0]))
tB, tP, tEnd = SB[0], SP[0], pts[-1][0]
span = max(p[1] for p in pts) - SL[1]
Y_TOP, Y_BOT = max(p[1] for p in pts) + 0.22 * span, SL[1] - 0.18 * span

out = []
# seasons
out += [f'<rect x="{X(0):.1f}" y="{T}" width="{X(tB) - X(0):.1f}" height="{B - T}" fill="#fdf6ec"/>',
        f'<rect x="{X(tB):.1f}" y="{T}" width="{X(tP) - X(tB):.1f}" height="{B - T}" fill="#eaf4fb"/>',
        f'<rect x="{X(tP):.1f}" y="{T}" width="{X(tEnd) - X(tP):.1f}" height="{B - T}" fill="#fdf6ec"/>',
        text((X(0) + X(tB)) / 2, T + 20, "dry season: storage drains", 12.5, fill="#9c6a1d", italic=True),
        text((X(tB) + X(tP)) / 2, T + 20, "wet season", 12.5, fill=C["blue"], italic=True)]
# axes
out += [line(L, B, R, B, "darkgray", 1.2), line(L, T, L, B, "darkgray", 1.2),
        f'<text x="0" y="0" transform="translate({L - 46},{(T + B) / 2}) rotate(-90)" font-family="{FONT}" '
        f'font-size="13" text-anchor="middle" fill="{C["darkgray"]}">GWSa (cm)</text>',
        text((L + R) / 2, B + 34, "time (months)", 13)]
# recession line: fitted from S_A to S_B (solid), projected from S_B to the peak time (dashed)
out.append(line(X(0), Y(icpt), X(tB), Y(icpt + slope * tB), "red", 2.2))
out.append(line(X(tB), Y(SB[1]), X(SL[0]), Y(SL[1]), "red", 2, dash="7 5"))
ang = math.degrees(math.atan2(Y(icpt + slope) - Y(icpt), X(1) - X(0)))
for lt, lab in [(tB * 0.5, "recession line, fitted"), (tB + (tP - tB) * 0.4, "projected from S<tspan font-size='9' baseline-shift='sub'>B</tspan>")]:
    ly_ = (Y(icpt + slope * lt) if lt <= tB else Y(SB[1] + slope * (lt - tB))) + 26
    out.append(text(X(lt), ly_, lab, 12.5, fill=C["red"],
                    style=f'transform="rotate({ang:.1f} {X(lt):.1f} {ly_:.1f})"'))
# series
poly = " ".join(f"{X(t):.1f},{Y(v):.1f}" for t, v in pts)
out.append(f'<polyline points="{poly}" fill="none" stroke="{C["navy"]}" stroke-width="3"/>')
# guide: S_B level across to the peak time
BX = X(tEnd) + 34                       # brackets sit right of the curve, reached by dotted guides
out.append(line(X(SB[0]), Y(SB[1]), BX, Y(SB[1]), "gray", 1.2, dash="2 4"))
out.append(line(X(SP[0]) + 8, Y(SP[1]), BX, Y(SP[1]), "gray", 1.2, dash="2 4"))
out.append(line(X(SL[0]) + 8, Y(SL[1]), BX, Y(SL[1]), "gray", 1.2, dash="2 4"))
# points
for (t, v), lab, col, dx, dy in [(SA, "S<tspan font-size='11' baseline-shift='sub'>A</tspan>", C["gray"], 0, -14),
                                  (SB, "S<tspan font-size='11' baseline-shift='sub'>B</tspan>", C["blue"], 0, 26),
                                  (SP, "S<tspan font-size='11' baseline-shift='sub'>P</tspan>", C["blue"], 0, -14),
                                  (SL, "S<tspan font-size='11' baseline-shift='sub'>L</tspan>", C["red"], -20, 6)]:
    out.append(f'<circle cx="{X(t):.1f}" cy="{Y(v):.1f}" r="6" fill="white" stroke="{col}" stroke-width="2.5"/>')
    out.append(f'<text x="{X(t) + dx:.1f}" y="{Y(v) + dy:.1f}" font-family="{FONT}" font-size="15" font-weight="bold" '
               f'text-anchor="middle" fill="{col}">{lab}</text>')
# brackets at peak time
bx = BX
for y0, y1, col, lab in [(Y(SP[1]), Y(SB[1]), "blue", "R<tspan font-size='11' baseline-shift='sub'>S</tspan>"),
                         (Y(SB[1]), Y(SL[1]), "red", "R<tspan font-size='11' baseline-shift='sub'>D</tspan>")]:
    out += [line(bx, y0, bx, y1, col, 2.2), line(bx - 7, y0, bx + 7, y0, col, 2.2), line(bx - 7, y1, bx + 7, y1, col, 2.2),
            f'<text x="{bx + 14}" y="{(y0 + y1) / 2 + 5:.1f}" font-family="{FONT}" font-size="15" font-weight="bold" fill="{C[col]}">{lab}</text>']
out.append(text(X(0), B + 18, "previous peak", 11.5, fill=C["gray"]))
out.append(text(X(tP), B + 18, "this year's peak", 11.5, fill=C["gray"]))

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
        eq(334, f"R1 (lower):  R{sub('S')} = S{sub('P')} − S{sub('B')}", 15, "bold", C["navy"]),
        eq(366, f"R2 (upper):  R{sub('S')} + R{sub('D')} = S{sub('P')} − S{sub('L')}", 15, "bold", C["navy"]),
        eq(412, "GWSa is already a depth of water, so no", 12.5, col=C["gray"]),
        eq(430, "specific yield is needed: R is in cm per year.", 12.5, col=C["gray"])]

print(save("wtf-concept", svg_doc(W, H, "\n".join(out), "Water table fluctuation method")))
