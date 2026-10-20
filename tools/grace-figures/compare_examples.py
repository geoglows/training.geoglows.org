"""Worked examples for the "Comparing the Two Datasets" pages.

Draws every case those pages argue from, with both datasets on the same axes:

  compare-agreement.png       four aquifers on four continents where the two agree
  compare-trend.png           four where GRACE falls and 2.2 stays nearly flat
  compare-amplitude.png       two where the timing agrees and the swing does not,
                              each with the total water and soil moisture cycles
                              the GRACE route subtracts
  compare-phase.png           six where the seasonal cycles run opposite
  compare-phase-mechanism.png why that happens, and the ratio that predicts it
                              across 322 aquifers
  compare-signal-size.png     correlation against how much water is moving,
                              over every shared land cell
  compare-artifact-ice.png    Greenland and Patagonia, where the loss is ice
  compare-artifact-water.png  the Amazon and the Amu Darya, where the swing and
                              the decline are surface water
  compare-artifact-frozen.png Siberia and northern Quebec, where it is frozen ground

Reads data/compare_*.csv and data/catalog_*.csv, written by
data/export_compare_series.py in webapp-grace-groundwater, which area-averages
each region exactly as the app's regional view does.

    python compare_examples.py
"""
from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import C, OUT

DATA = Path(__file__).resolve().parent / "data"
GRACE_C, G22_C = C["blue"], C["orange"]
SM_C, TW_C = C["green"], C["darkgray"]
MONTHS = ["J", "F", "M", "A", "M", "J", "J", "A", "S", "O", "N", "D"]
NAMES = ["January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"]

# Short labels for the figures. The region files carry the published names,
# which are too long for a panel title and sometimes misspelled.
LABEL = {
    "parecis": "Parecis Basin, Brazil",
    "taurus-zagros": "Taurus–Zagros, Iraq and Iran",
    "deccan": "Deccan Plateau, India",
    "khorat": "Khorat Plateau, Thailand and Laos",
    "central-valley": "Central Valley, California",
    "disi": "Saq–Ram (Disi), Jordan and Saudi Arabia",
    "veracruz": "Coastal Plain of Veracruz, Mexico",
    "tarim": "Tarim Basin, China",
    "senegalo-mauritanien": "Senegalo-Mauritanian Basin, West Africa",
    "nu-river": "Nu River Valley, China and Myanmar",
    "baltic-devonian": "Baltic Devonian, Latvia and Estonia",
    "western-mountain": "Western Mountain Aquifer, Israel and Palestine",
    "shebelle": "Shabelle Basin, Ethiopia and Somalia",
    "pilbara": "Pilbara Craton, Australia",
    "armorican": "Armorican Massif, France",
    "atlantic-coastal-plain": "N. Atlantic Coastal Plain, USA",
    "amazon": "Amazon Basin",
    "amu-darya": "Amu Darya, Aral Sea basin",
    "pascua": "Pascua Basin, Patagonia",
    "indigirka": "Indigirka Basin, Siberia",
    "george": "George River, northern Quebec",
    "greenland-cell": "66.5°N 36.5°W, east Greenland",
}

plt.rcParams.update({"font.family": "Helvetica", "font.size": 11})


def read(stem):
    df = pd.read_csv(DATA / f"compare_{stem}.csv", parse_dates=["date"])
    df["t"] = df["date"].dt.year + (df["date"].dt.month - 1) / 12.0
    df["month"] = df["date"].dt.month - 1
    return df


def note(ax, text, size=10):
    """A line of numbers above the axes, where it cannot land on a curve."""
    ax.text(0, 1.02, text, transform=ax.transAxes, fontsize=size,
            color=C["darkgray"], va="bottom")


def pair_r(df, c1, c2):
    """Correlation over the months both datasets report."""
    a, b = df[c1].to_numpy(float), df[c2].to_numpy(float)
    k = ~np.isnan(a) & ~np.isnan(b)
    return float(np.corrcoef(a[k], b[k])[0, 1])


def minus(x, fmt="{:+.2f}"):
    return fmt.format(x).replace("-", "−")


def detrend(df, col):
    y = df[col].to_numpy(float)
    k = ~np.isnan(y)
    return y - np.polyval(np.polyfit(df["t"][k], y[k], 1), df["t"])


def cycle(df, col):
    x, m = detrend(df, col), df["month"].to_numpy()
    c = np.array([np.nanmean(x[m == i]) for i in range(12)])
    return c - c.mean()


def trend(df, col):
    y = df[col].to_numpy(float)
    k = ~np.isnan(y)
    return np.polyfit(df["t"][k], y[k], 1)


def amp(c):
    return float(c.max() - c.min())


def series_panel(ax, df, title, legend=False, trends=False):
    """Both monthly groundwater records, optionally with their fitted lines."""
    ax.axhline(0, color=C["lightgray"], lw=1, zorder=0)
    ax.plot(df["t"], df["gw_a"], color=GRACE_C, lw=1.3, label="GRACE route")
    ax.plot(df["t"], df["gw_b"], color=G22_C, lw=1.3, label="GLDAS 2.2")
    if trends:
        for col, col_c in (("gw_a", GRACE_C), ("gw_b", G22_C)):
            sl, ic = trend(df, col)
            ax.plot(df["t"], sl * df["t"] + ic, color=col_c, lw=2.2, ls="--", alpha=0.75)
    ax.set_title(title, fontsize=11, pad=20, loc="left")
    ax.set_ylabel("cm")
    ax.spines[["top", "right"]].set_visible(False)
    if legend:
        ax.legend(frameon=False, fontsize=10, loc="lower left")


def cycle_panel(ax, df, title, legend=False):
    """The average seasonal cycle of both groundwater records."""
    ax.axhline(0, color=C["lightgray"], lw=1, zorder=0)
    ca, cb = cycle(df, "gw_a"), cycle(df, "gw_b")
    ax.plot(range(12), ca, color=GRACE_C, lw=2, marker="o", ms=3.5, label="GRACE route")
    ax.plot(range(12), cb, color=G22_C, lw=2, marker="o", ms=3.5, label="GLDAS 2.2")
    ax.set_xticks(range(12))
    ax.set_xticklabels(MONTHS)
    ax.set_title(title, fontsize=11, pad=20, loc="left")
    ax.set_ylabel("cm")
    ax.spines[["top", "right"]].set_visible(False)
    if legend:
        ax.legend(frameon=False, fontsize=10, loc="best")
    return ca, cb


def grid(stems, draw, shape, size, name, title, suptitle=None):
    fig, axes = plt.subplots(*shape, figsize=size)
    flat = np.atleast_1d(axes).ravel()
    for i, (ax, stem) in enumerate(zip(flat, stems)):
        draw(ax, read(stem), stem, i == 0)
    for ax in flat[len(stems):]:
        ax.set_visible(False)
    if suptitle:
        fig.suptitle(suptitle, fontsize=12, y=0.995)
    fig.tight_layout()
    save(fig, name)


def save(fig, name):
    png = OUT / f"{name}.png"
    fig.savefig(png, dpi=200, facecolor="white", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print(f"  {png.name}")


# ---------------------------------------------------------------- the figures

def agreement():
    def draw(ax, df, stem, first):
        series_panel(ax, df, LABEL[stem], legend=first)
        ca, cb = cycle(df, "gw_a"), cycle(df, "gw_b")
        note(ax, f"monthly r {pair_r(df, 'gw_a', 'gw_b'):.2f}   "
                 f"seasonal r {float(np.corrcoef(ca, cb)[0, 1]):.2f}   "
                 f"swing {amp(ca):.0f} and {amp(cb):.0f} cm")
    grid(["parecis", "taurus-zagros", "deccan", "khorat"], draw, (2, 2), (12, 7.5),
         "compare-agreement", "agreement")


def trend_figure():
    def draw(ax, df, stem, first):
        series_panel(ax, df, LABEL[stem], legend=first, trends=True)
        sa, sb = trend(df, "gw_a")[0], trend(df, "gw_b")[0]
        span = df["t"].iloc[-1] - df["t"].iloc[0]
        note(ax, f"{minus(sa)} against {minus(sb)} cm/yr   "
                 f"{minus(sa * span, '{:+.0f}')} against {minus(sb * span, '{:+.0f}')} cm "
                 f"over the record")
    grid(["central-valley", "disi", "veracruz", "tarim"], draw, (2, 2), (12, 7.5),
         "compare-trend", "trends")


def amplitude():
    """Two cases, each with the cycle pair and the subtraction behind it."""
    stems = ["senegalo-mauritanien", "nu-river"]
    fig, axes = plt.subplots(2, 2, figsize=(12, 7.5))
    for row, stem in enumerate(stems):
        df = read(stem)
        ca, cb = cycle_panel(axes[row][0], df, LABEL[stem], legend=(row == 0))
        note(axes[row][0], f"seasonal r {float(np.corrcoef(ca, cb)[0, 1]):.2f}   "
                           f"swing {amp(ca):.1f} against {amp(cb):.1f} cm "
                           f"({amp(cb) / amp(ca):.1f}×)")
        ax = axes[row][1]
        ax.axhline(0, color=C["lightgray"], lw=1, zorder=0)
        ct, cs = cycle(df, "tw_a"), cycle(df, "sm_a")
        ax.plot(range(12), ct, color=TW_C, lw=2, marker="o", ms=3.5, label="total water (TWSa)")
        ax.plot(range(12), cs, color=SM_C, lw=2, marker="o", ms=3.5, label="soil moisture (SMa)")
        ax.plot(range(12), ca, color=GRACE_C, lw=2, ls="--", label="what is left: groundwater")
        ax.set_xticks(range(12))
        ax.set_xticklabels(MONTHS)
        ax.set_ylabel("cm")
        ax.set_title("what the GRACE route subtracts", fontsize=11, pad=20, loc="left")
        ax.spines[["top", "right"]].set_visible(False)
        note(ax, f"total water swings {amp(ct):.1f} cm, soil moisture {amp(cs):.1f} cm, "
                 f"leaving {amp(ca):.1f} cm")
        if row == 0:
            ax.legend(frameon=False, fontsize=9, loc="lower left")
    fig.tight_layout()
    save(fig, "compare-amplitude")


def phase():
    def draw(ax, df, stem, first):
        ca, cb = cycle_panel(ax, df, LABEL[stem], legend=first)
        r = float(np.corrcoef(ca, cb)[0, 1])
        note(ax, f"peaks {NAMES[int(np.argmax(ca))]} against {NAMES[int(np.argmax(cb))]}   "
                 f"seasonal r {minus(r)}")
    grid(["baltic-devonian", "armorican", "western-mountain", "shebelle",
          "pilbara", "atlantic-coastal-plain"], draw, (3, 2), (12, 11),
         "compare-phase", "phase")


def phase_mechanism():
    """The subtraction that flips the cycle, and the ratio that predicts it."""
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.6))

    df = read("atlantic-coastal-plain")
    ax = axes[0]
    ax.axhline(0, color=C["lightgray"], lw=1, zorder=0)
    ct, cs, ca = cycle(df, "tw_a"), cycle(df, "sm_a"), cycle(df, "gw_a")
    ax.plot(range(12), ct, color=TW_C, lw=2, marker="o", ms=3.5, label="total water (TWSa)")
    ax.plot(range(12), cs, color=SM_C, lw=2, marker="o", ms=3.5, label="soil moisture (SMa)")
    ax.plot(range(12), ca, color=GRACE_C, lw=2.2, ls="--", label="what is left: groundwater")
    ax.set_xticks(range(12))
    ax.set_xticklabels(MONTHS)
    ax.set_ylabel("cm")
    ax.set_title("Northern Atlantic Coastal Plain: two large curves, one small remainder",
                 fontsize=11, pad=20, loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    note(ax, f"total water {amp(ct):.1f} cm, soil moisture {amp(cs):.1f} cm, "
             f"remainder {amp(ca):.1f} cm peaking in {NAMES[int(np.argmax(ca))]}")
    ax.legend(frameon=False, fontsize=9, loc="lower left")

    cat = pd.read_csv(DATA / "catalog_regions.csv")
    cat = cat[cat["amp_grace"] > 1.0]
    ax = axes[1]
    ax.axhline(0, color=C["lightgray"], lw=1, zorder=0)
    ax.axvline(1.0, color=C["lightgray"], lw=1, zorder=0)
    ax.scatter(cat["sm_over_tw"], cat["r_seasonal"], s=14, color=C["gray"],
               alpha=0.55, edgecolors="none")
    r = float(np.corrcoef(cat["sm_over_tw"], cat["r_seasonal"])[0, 1])
    marks = {"baltic-devonian": ("Baltic Devonian", (6, -10)),
             "western-mountain": ("Western Mountain", (-8, 10)),
             "shebelle": ("Shabelle", (6, 4)),
             "pilbara": ("Pilbara", (6, -3)),
             "armorican": ("Armorican", (6, -3)),
             "atlantic-coastal-plain": ("N. Atl. Coastal Plain", (6, 2)),
             "parecis": ("Parecis", (-34, 10)),
             "deccan": ("Deccan", (6, 4)),
             "khorat": ("Khorat", (10, -9))}
    for stem, (lab, off) in marks.items():
        d = read(stem)
        x = amp(cycle(d, "sm_a")) / amp(cycle(d, "tw_a"))
        y = float(np.corrcoef(cycle(d, "gw_a"), cycle(d, "gw_b"))[0, 1])
        ax.scatter([x], [y], s=34, color=C["red"], zorder=3, edgecolors="white", linewidths=0.8)
        ax.annotate(lab, (x, y), textcoords="offset points", xytext=off,
                    fontsize=8, color=C["red"])
    ax.set_xlabel("soil moisture swing ÷ total water swing")
    ax.set_ylabel("agreement of the two\nseasonal cycles (r)")
    ax.set_title(f"the ratio predicts the disagreement, across {len(cat)} aquifers",
                 fontsize=11, pad=20, loc="left")
    ax.set_xlim(0, 3.4)
    ax.spines[["top", "right"]].set_visible(False)
    note(ax, f"r = {minus(r, '{:+.2f}')} between the two axes; "
             "left of the line soil moisture swings less than total water")
    fig.tight_layout()
    save(fig, "compare-phase-mechanism")


def signal_size():
    """Correlation against how much water is actually moving, cell by cell."""
    cells = pd.read_csv(DATA / "catalog_cells.csv")
    fig, ax = plt.subplots(figsize=(9, 4.8))
    ax.axhline(0, color=C["lightgray"], lw=1, zorder=0)
    ax.scatter(cells["sd_grace"], cells["r"], s=3, color=C["gray"], alpha=0.25,
               edgecolors="none")
    edges = np.array([0, 2, 3, 5, 8, 12, 15, 25, 40, 1e9])
    xs, ys = [], []
    for lo, hi in zip(edges[:-1], edges[1:]):
        k = (cells["sd_grace"] >= lo) & (cells["sd_grace"] < hi)
        if k.sum() > 30:
            xs.append(float(np.median(cells["sd_grace"][k])))
            ys.append(float(np.median(cells["r"][k])))
    ax.plot(xs, ys, color=C["red"], lw=2.4, marker="o", ms=5, label="median by band")
    for x, lab in ((5, "5 cm"), (15, "15 cm")):
        ax.axvline(x, color=C["darkgray"], lw=1, ls=":")
        ax.text(x, -1.0, lab, fontsize=9, color=C["darkgray"], ha="center", va="bottom")
    ax.set_xscale("log")
    ax.set_xlim(0.5, 200)
    ax.set_xticks([1, 2, 5, 10, 20, 50, 100])
    ax.set_xticklabels(["1", "2", "5", "10", "20", "50", "100"])
    ax.minorticks_off()
    ax.set_ylim(-1.05, 1.05)
    ax.set_xlabel("how much the GRACE groundwater moves in that cell "
                  "(standard deviation, cm)")
    ax.set_ylabel("agreement of the two\nmonthly records (r)")
    ax.set_title("A low correlation where little water moves says nothing about either dataset",
                 fontsize=11, pad=22, loc="left")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, fontsize=10, loc="lower right")
    note(ax, f"{len(cells):,} shared 1° land cells; median r rises from "
             f"{np.median(cells['r'][cells['sd_grace'] < 5]):.2f} below 5 cm to "
             f"{np.median(cells['r'][cells['sd_grace'] > 15]):.2f} above 15 cm")
    fig.tight_layout()
    save(fig, "compare-signal-size")


def ice():
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))
    for ax, stem in zip(axes, ["greenland-cell", "pascua"]):
        df = read(stem)
        series_panel(ax, df, LABEL[stem], legend=(stem == "greenland-cell"))
        g = df["gw_a"].to_numpy(float)
        k = ~np.isnan(g)
        drop = (np.nanmean(g[k][:12]) - np.nanmean(g[k][-12:])) / 100.0
        extra = (f"   snow water runs {np.nanmean(df['swe_a']):.0f} cm above the baseline"
                 if stem == "greenland-cell" else
                 f"   {minus(trend(df, 'gw_a')[0], '{:+.1f}')} cm/yr")
        note(ax, f"GRACE route falls {drop:.1f} m over the record{extra}")
    fig.tight_layout()
    save(fig, "compare-artifact-ice")


def surface_water():
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))
    df = read("amazon")
    ca, cb = cycle_panel(axes[0], df, LABEL["amazon"], legend=True)
    note(axes[0], f"seasonal r {float(np.corrcoef(ca, cb)[0, 1]):.2f}   "
                  f"swing {amp(ca):.1f} against {amp(cb):.1f} cm   "
                  f"trends {minus(trend(df, 'gw_a')[0])} against {minus(trend(df, 'gw_b')[0])} cm/yr")
    df = read("amu-darya")
    series_panel(axes[1], df, LABEL["amu-darya"], trends=True)
    sa, sb = trend(df, "gw_a")[0], trend(df, "gw_b")[0]
    span = df["t"].iloc[-1] - df["t"].iloc[0]
    note(axes[1], f"{minus(sa)} against {minus(sb)} cm/yr   "
                  f"{minus(sa * span, '{:+.0f}')} against {minus(sb * span, '{:+.0f}')} cm "
                  f"over the record")
    fig.tight_layout()
    save(fig, "compare-artifact-water")


def frozen():
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.4))
    for ax, stem in zip(axes, ["indigirka", "george"]):
        df = read(stem)
        ca, cb = cycle_panel(ax, df, LABEL[stem], legend=(stem == "indigirka"))
        cw = cycle(df, "swe_a")
        ax.plot(range(12), cw, color=C["teal"], lw=1.8, ls=":", label="snow water (SWEa)")
        note(ax, f"swing {amp(ca):.1f} against {amp(cb):.1f} cm   "
                 f"snow water swings {amp(cw):.1f} cm")
        ax.legend(frameon=False, fontsize=9, loc="lower left")
    fig.tight_layout()
    save(fig, "compare-artifact-frozen")


if __name__ == "__main__":
    agreement()
    trend_figure()
    amplitude()
    phase()
    phase_mechanism()
    signal_size()
    ice()
    surface_water()
    frozen()
