"""Worked examples for the "Comparing the Two Datasets" pages.

Draws the regional cases the pages argue from, with both datasets on the same
axes:

  compare-agreement.png   Guarani Aquifer System, where the two agree
  compare-amplitude.png   Senegalo-Mauritanian Basin, same timing, 3x the swing
  compare-phase.png       Northern Atlantic Coastal Plain, cycles half a year apart,
                          and the soil moisture cycle that causes it
  compare-trend.png       California Central Valley, GRACE falling four times as fast
  compare-artifact-ice.png     east Greenland, where the loss is the ice sheet
  compare-artifact-amazon.png  Amazon Basin, where the swing is the floodplain

Reads data/compare_*.csv, written by data/export_compare_series.py in
webapp-grace-groundwater, which area-averages each region exactly as the app's
regional view does.

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


def note(ax, text):
    """A line of numbers above the axes, where it cannot land on a curve."""
    ax.text(0, 1.02, text, transform=ax.transAxes, fontsize=10,
            color=C["darkgray"], va="bottom")


def pair_r(df, c1, c2):
    """Correlation over the months both datasets report."""
    a, b = df[c1].to_numpy(float), df[c2].to_numpy(float)
    k = ~np.isnan(a) & ~np.isnan(b)
    return float(np.corrcoef(a[k], b[k])[0, 1])


def minus(x, fmt="{:+.2f}"):
    return fmt.format(x).replace("-", "\u2212")

plt.rcParams.update({"font.family": "Helvetica", "font.size": 11})


def read(stem):
    df = pd.read_csv(DATA / f"compare_{stem}.csv", parse_dates=["date"])
    df["t"] = np.arange(len(df)) / 12.0
    df["month"] = df["date"].dt.month - 1
    return df


def detrend(df, col):
    """The series with its straight-line trend removed, as the climatology needs."""
    v = df[col].to_numpy(float)
    k = ~np.isnan(v)
    return v - np.polyval(np.polyfit(df["t"][k], v[k], 1), df["t"])


def cycle(df, col):
    """Average seasonal cycle: mean of each calendar month, trend removed, centred."""
    d = detrend(df, col)
    c = np.array([np.nanmean(d[df["month"] == m]) for m in range(12)])
    return c - c.mean()


def trend(df, col):
    v = df[col].to_numpy(float)
    k = ~np.isnan(v)
    return np.polyfit(df["t"][k], v[k], 1)


def amp(c):
    return float(c.max() - c.min())


def style(ax, ylabel="GWSa (cm)"):
    ax.set_ylabel(ylabel)
    ax.grid(alpha=0.25, linewidth=0.6)
    ax.axhline(0, color=C["gray"], linewidth=0.8, zorder=1)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)


def cycle_axes(ax, title):
    ax.set_xticks(range(12))
    ax.set_xticklabels(MONTHS)
    ax.set_xlim(-0.4, 11.4)
    ax.set_title(title, fontsize=11, loc="left", pad=22)


def series_axes(ax, df, title):
    ax.set_xlim(df["date"].iloc[0], df["date"].iloc[-1])
    ax.set_title(title, fontsize=11, loc="left", pad=22)


def save(fig, name):
    fig.savefig(OUT / name, facecolor="white", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print(f"  {name}")


# ---------------------------------------------------------------- agreement --
def agreement():
    df = read("guarani")
    ga, gb = cycle(df, "gw_a"), cycle(df, "gw_b")
    r = np.corrcoef(ga, gb)[0, 1]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 3.6), dpi=200,
                                   gridspec_kw={"width_ratios": [2.1, 1]})
    ax1.plot(df["date"], df["gw_a"], color=GRACE_C, linewidth=1.3, label="GRACE route")
    ax1.plot(df["date"], df["gw_b"], color=G22_C, linewidth=1.3, label="GLDAS 2.2")
    series_axes(ax1, df, "Guarani Aquifer System: the two records month by month")
    style(ax1)
    note(ax1, f"monthly r = {pair_r(df, 'gw_a', 'gw_b'):.2f} over the months both report")
    ax1.legend(frameon=False, loc="lower left", fontsize=10, ncol=2)

    ax2.plot(range(12), ga, color=GRACE_C, linewidth=2, marker="o", markersize=3.5)
    ax2.plot(range(12), gb, color=G22_C, linewidth=2, marker="o", markersize=3.5)
    cycle_axes(ax2, "Average seasonal cycle")
    style(ax2, "")
    note(ax2, f"swing {amp(ga):.1f} against {amp(gb):.1f} cm, seasonal r = {r:.2f}")
    save(fig, "compare-agreement.png")


# ---------------------------------------------------------------- amplitude --
def amplitude():
    df = read("senegalo-mauritanien")
    ga, gb = cycle(df, "gw_a"), cycle(df, "gw_b")
    sm, tw = cycle(df, "sm_a"), cycle(df, "tw_a")
    r = np.corrcoef(ga, gb)[0, 1]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 3.6), dpi=200)
    ax1.plot(range(12), ga, color=GRACE_C, linewidth=2, marker="o", markersize=4,
             label=f"GRACE route, {amp(ga):.1f} cm")
    ax1.plot(range(12), gb, color=G22_C, linewidth=2, marker="o", markersize=4,
             label=f"GLDAS 2.2, {amp(gb):.1f} cm")
    cycle_axes(ax1, "Senegalo-Mauritanian Basin: groundwater cycle")
    style(ax1)
    ax1.legend(frameon=False, loc="upper left", fontsize=10)
    note(ax1, f"same timing, seasonal r = {r:.2f}; 2.2 swings {amp(gb) / amp(ga):.1f} times as far")

    ax2.plot(range(12), tw, color=TW_C, linewidth=2, marker="o", markersize=4,
             label=f"total water, {amp(tw):.1f} cm")
    ax2.plot(range(12), sm, color=SM_C, linewidth=2, marker="o", markersize=4,
             label=f"soil moisture, {amp(sm):.1f} cm")
    cycle_axes(ax2, "What the GRACE route subtracts")
    style(ax2, "cm")
    ax2.legend(frameon=False, loc="upper left", fontsize=10)
    note(ax2, f"soil moisture swings {amp(sm) / amp(tw):.2f} of total water")
    save(fig, "compare-amplitude.png")


# -------------------------------------------------------------------- phase --
def phase():
    df = read("atlantic-coastal-plain")
    ga, gb = cycle(df, "gw_a"), cycle(df, "gw_b")
    sm, tw = cycle(df, "sm_a"), cycle(df, "tw_a")
    r = np.corrcoef(ga, gb)[0, 1]
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10.5, 3.6), dpi=200)
    ax1.plot(range(12), ga, color=GRACE_C, linewidth=2, marker="o", markersize=4,
             label="GRACE route")
    ax1.plot(range(12), gb, color=G22_C, linewidth=2, marker="o", markersize=4,
             label="GLDAS 2.2")
    for c, col in ((ga, GRACE_C), (gb, G22_C)):
        ax1.axvline(int(np.argmax(c)), color=col, linewidth=1, linestyle=":", alpha=0.8)
    cycle_axes(ax1, "Northern Atlantic Coastal Plain: groundwater cycle")
    style(ax1)
    ax1.legend(frameon=False, loc="lower left", fontsize=10)
    note(ax1, f"peaks in {NAMES[int(np.argmax(ga))]} against {NAMES[int(np.argmax(gb))]}, "
              f"seasonal r = {minus(r)}")

    ax2.plot(range(12), tw, color=TW_C, linewidth=2, marker="o", markersize=4,
             label=f"total water, {amp(tw):.1f} cm")
    ax2.plot(range(12), sm, color=SM_C, linewidth=2, marker="o", markersize=4,
             label=f"soil moisture, {amp(sm):.1f} cm")
    ax2.plot(range(12), ga, color=GRACE_C, linewidth=1.6, linestyle="--",
             label="what is left: GRACE groundwater")
    cycle_axes(ax2, "Why: the subtraction leaves almost nothing")
    style(ax2, "cm")
    ax2.legend(frameon=False, loc="lower left", fontsize=9.5)
    note(ax2, f"soil moisture swings {amp(sm) / amp(tw):.2f} of total water")
    save(fig, "compare-phase.png")


# -------------------------------------------------------------------- trend --
def trend_figure():
    df = read("central-valley")
    fig, ax = plt.subplots(figsize=(10.5, 3.8), dpi=200)
    for col, colour, label in (("gw_a", GRACE_C, "GRACE route"), ("gw_b", G22_C, "GLDAS 2.2")):
        slope, intercept = trend(df, col)
        ax.plot(df["date"], df[col], color=colour, linewidth=1.2, alpha=0.65)
        ax.plot(df["date"], slope * df["t"] + intercept, color=colour, linewidth=2.6,
                label=f"{label}, {minus(slope)} cm/yr")
    series_axes(ax, df, "California Central Valley: the same aquifer, two depletion rates")
    style(ax)
    ax.legend(frameon=False, loc="lower left", fontsize=10)
    save(fig, "compare-trend.png")


# ---------------------------------------------------------------- artifacts --
def ice():
    df = read("greenland-cell")
    fig, ax = plt.subplots(figsize=(7.5, 3.6), dpi=200)
    ax.plot(df["date"], df["gw_a"] / 100, color=GRACE_C, linewidth=1.3, label="GRACE route")
    ax.plot(df["date"], df["gw_b"] / 100, color=G22_C, linewidth=1.3, label="GLDAS 2.2")
    series_axes(ax, df, "66.5°N 36.5°W, east Greenland: no aquifer here")
    style(ax, "GWSa (m)")
    note(ax, f"mean snow water {np.nanmean(abs(df['swe_a'])):.0f} cm; "
             f"the GRACE route loses {abs(df['gw_a'].iloc[-1] / 100):.0f} m of \u201cgroundwater\u201d")
    ax.legend(frameon=False, loc="lower left", fontsize=10)
    save(fig, "compare-artifact-ice.png")


def amazon():
    df = read("amazon")
    ga, gb = cycle(df, "gw_a"), cycle(df, "gw_b")
    ta, tb = trend(df, "gw_a")[0], trend(df, "gw_b")[0]
    fig, ax = plt.subplots(figsize=(7.5, 3.6), dpi=200)
    ax.plot(range(12), ga, color=GRACE_C, linewidth=2, marker="o", markersize=4,
            label=f"GRACE route, {amp(ga):.1f} cm swing, {minus(ta)} cm/yr")
    ax.plot(range(12), gb, color=G22_C, linewidth=2, marker="o", markersize=4,
            label=f"GLDAS 2.2, {amp(gb):.1f} cm swing, {minus(tb)} cm/yr")
    cycle_axes(ax, "Amazon Basin: the river in the groundwater layer")
    style(ax)
    note(ax, f"same timing, seasonal r = {np.corrcoef(ga, gb)[0, 1]:.2f}; "
             "the two disagree on the sign of the trend")
    ax.legend(frameon=False, loc="lower left", fontsize=10)
    save(fig, "compare-artifact-amazon.png")


if __name__ == "__main__":
    print("drawing:")
    agreement()
    amplitude()
    phase()
    trend_figure()
    ice()
    amazon()
