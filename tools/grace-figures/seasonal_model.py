"""Seasonal model figures for the Northern Midwest Aquifer System.

Refits the app's gap-fill model (src/gapFill.js in webapp-grace-groundwater) to the observed GWSa in
data/northern_midwest_filled.csv, with the same constraints, grid search and BIC rule, and draws:

  seasonal-decomposition.png  observed series, trend, seasonal cycle and residual, stacked
  seasonal-levels.png         the twelve monthly levels of the seasonal cycle
  seasonal-breakpoints.png    the best trend with 0, 1, 2 and 3 breakpoints, and the BIC of each
  seasonal-gap-correction.png the residual correction across the gap between the missions
  seasonal-gap-correction-cv.png  the same for the Central Valley (data/central_valley_gwsa.csv, an app export),
                              where the correction tilts across the gap
"""
import itertools
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from common import C, OUT

END_BUFFER, MIN_SEGMENT, GRID_STEP, MIN_BIC_DROP = 48, 36, 3, 10



def design(bps, tt, mm):
    return np.column_stack([tt, *[np.maximum(tt - b, 0) for b in bps], *[(mm == k).astype(float) for k in range(12)]])


def fit_series(values, months):
    """The app's seasonal model for one monthly series (NaN where GRACE is missing), one row per month.

    Returns the best fit for 0-3 breakpoints, the one the BIC rule keeps, and its trend, monthly levels and residual.
    """
    obs = ~np.isnan(values)
    t_all = np.arange(len(values))
    t, mon, y = t_all[obs], months[obs], values[obs]
    n = len(y)

    def fit(bps):
        beta, *_ = np.linalg.lstsq(design(bps, t, mon), y, rcond=None)
        r = y - design(bps, t, mon) @ beta
        rss = r @ r
        return dict(bps=list(bps), beta=beta, rss=rss, bic=n * np.log(rss / n) + (1 + 2 * len(bps) + 12) * np.log(n))

    def valid(b):
        return b[0] - t[0] >= END_BUFFER and t[-1] - b[-1] >= END_BUFFER and all(
            b[i] - b[i - 1] >= MIN_SEGMENT for i in range(1, len(b)))

    def best(k):
        if k == 0:
            return fit([])
        cands = range(t[0] + END_BUFFER, t[-1] - END_BUFFER + 1, GRID_STEP)
        b = min((fit(c) for c in itertools.combinations(cands, k) if valid(c)), key=lambda f: f["rss"])
        improved = True
        while improved:
            improved = False
            for i in range(k):
                for s in (-1, 1):
                    trial = list(b["bps"])
                    trial[i] += s
                    if valid(trial) and (f := fit(trial))["rss"] < b["rss"] - 1e-9:
                        b, improved = f, True
        return b

    def parts(f):
        """Trend and seasonal levels, shifted so the cycle averages zero."""
        k = len(f["bps"])
        trend = design(f["bps"], t_all, months)[:, :1 + k] @ f["beta"][:1 + k]
        levels = f["beta"][1 + k:]
        off = levels.mean()
        return trend + off, levels - off

    fits = [best(k) for k in range(4)]
    chosen = 0
    for k in range(1, 4):
        if fits[k]["bic"] <= fits[chosen]["bic"] - MIN_BIC_DROP:
            chosen = k
    trend, levels = parts(fits[chosen])
    seasonal = levels[months]
    return dict(fits=fits, chosen=chosen, parts=parts, trend=trend, levels=levels, seasonal=seasonal,
                resid=values - trend - seasonal, obs=obs)


d = pd.read_csv(Path(__file__).parent / "data" / "northern_midwest_filled.csv")
d["date"] = pd.to_datetime(d.month)
cal = d.date.dt.month.values - 1
m = fit_series(d.observed.values, cal)
fits, chosen, parts, trend, levels, seasonal, resid, obs = (m[k] for k in
                                                            ("fits", "chosen", "parts", "trend", "levels", "seasonal",
                                                             "resid", "obs"))
model = fits[chosen]
assert np.allclose(trend + seasonal, d.trend + d.seasonal, atol=1e-3), "refit differs from the app's fill"
bp_dates = [d.date[b] for b in model["bps"]]

plt.rcParams.update({"font.family": "Helvetica", "font.size": 11})
GAP = (pd.Timestamp("2017-06-15"), pd.Timestamp("2018-05-15"))
xlim = (d.date.iloc[0] - pd.Timedelta(days=60), d.date.iloc[-1] + pd.Timedelta(days=60))


def tidy(ax, grid=True):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    if grid:
        ax.grid(axis="y", color=C["lightgray"], lw=0.8)


def breaks(ax):
    for b in bp_dates:
        ax.axvline(b, color=C["teal"], lw=0.8, ls=":", alpha=0.8)


def label(ax, s):
    ax.text(0.005, 0.97, s, transform=ax.transAxes, ha="left", va="top", fontsize=11.5, weight="bold", color=C["darkgray"])


def observed_line(ax, **kw):
    # NaN breaks the line at each missing month
    ax.plot(d.date, d.observed, color=C["navy"], lw=1.3, **kw)
    # a month with gaps on both sides has no segment to draw, so mark it
    lone = obs & ~np.r_[False, obs[:-1]] & ~np.r_[obs[1:], False]
    ax.plot(d.date[lone], d.observed[lone], "o", color=C["navy"], ms=2.5, **kw)


# --- 1. decomposition ---------------------------------------------------------------------------------------------
fig, axs = plt.subplots(4, 1, figsize=(11, 9), dpi=200, sharex=True,
                        gridspec_kw=dict(height_ratios=[1.3, 1.3, 1, 1], hspace=0.18))
ax = axs[0]
observed_line(ax)
label(ax, "Observed GWSa,  y")
lo = min(np.nanmin(d.observed), trend.min()) - 2
hi = max(np.nanmax(d.observed), trend.max()) + 4
ax = axs[1]
ax.plot(d.date, trend, color=C["teal"], lw=2.2)
breaks(ax)
label(ax, "Trend,  T")
for b in bp_dates:
    ax.text(b + pd.Timedelta(days=45), hi - 1, f"{b:%b %Y}", va="top", ha="left", fontsize=9, color=C["teal"])
ax = axs[2]
ax.plot(d.date, seasonal, color=C["orange"], lw=1.4)
label(ax, "Seasonal cycle,  S")
ax = axs[3]
ax.axhline(0, color=C["gray"], lw=0.8)
ax.plot(d.date, resid, color=C["gray"], lw=1.1)
lone = obs & ~np.r_[False, obs[:-1]] & ~np.r_[obs[1:], False]
ax.plot(d.date[lone], resid[lone], "o", color=C["gray"], ms=2.5)
label(ax, "Residual,  r = y − T − S")
for ax in axs[:2]:
    ax.set_ylim(lo, hi)
s_lim = max(np.abs(seasonal).max(), np.nanmax(np.abs(resid))) + 1.5
for ax in axs[2:]:
    ax.set_ylim(-s_lim, s_lim)
for ax in axs:
    ax.axvspan(*GAP, color=C["lightgray"], alpha=0.7, lw=0)
    ax.set_ylabel("cm")
    tidy(ax)
axs[-1].set_xlim(*xlim)
fig.align_ylabels(axs)
fig.savefig(OUT / "seasonal-decomposition.png", facecolor="white", bbox_inches="tight", pad_inches=0.15)
plt.close(fig)

# --- 2. monthly levels --------------------------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(7.5, 3.4), dpi=200)
names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
cols = [C["orange"] if v >= 0 else C["blue"] for v in levels]
ax.bar(names, levels, color=cols, width=0.7)
ax.axhline(0, color=C["darkgray"], lw=0.9)
for i, v in enumerate(levels):
    ax.text(i, v + (0.25 if v >= 0 else -0.25), f"{v:+.1f}".replace("-", "−"), ha="center", va="bottom" if v >= 0 else "top", fontsize=9,
            color=C["darkgray"])
ax.set_ylabel("S (cm)")
ax.set_ylim(levels.min() - 1.4, levels.max() + 1.4)
tidy(ax)
ax.tick_params(axis="x", length=0)
fig.tight_layout()
fig.savefig(OUT / "seasonal-levels.png", facecolor="white", bbox_inches="tight", pad_inches=0.15)
plt.close(fig)

# --- 3. breakpoint counts -----------------------------------------------------------------------------------------
fig, axs = plt.subplots(2, 2, figsize=(11, 6.4), dpi=200, sharex=True, sharey=True)
for k, (ax, f) in enumerate(zip(axs.flat, fits)):
    tr, _ = parts(f)
    observed_line(ax, alpha=0.45)
    ax.plot(d.date, tr, color=C["teal"] if k == chosen else C["red"], lw=2.2)
    for b in f["bps"]:
        ax.axvline(d.date[b], color=C["gray"], lw=0.8, ls=":")
    word = "breakpoint" if k == 1 else "breakpoints"
    head = f"{k} {word}:  BIC {f['bic']:.0f}"
    if k:
        drop = fits[k - 1]["bic"] - f["bic"]
        head += f"  (−{drop:.0f})" if drop > 0 else f"  (+{-drop:.0f})"
    ax.set_title(head, loc="left", fontsize=11.5, weight="bold" if k == chosen else "normal",
                 color=C["teal"] if k == chosen else C["darkgray"])
    tidy(ax)
for ax in axs[:, 0]:
    ax.set_ylabel("GWSa (cm)")
axs[0, 0].set_xlim(*xlim)
fig.tight_layout()
fig.savefig(OUT / "seasonal-breakpoints.png", facecolor="white", bbox_inches="tight", pad_inches=0.15)
plt.close(fig)

# --- 4. gap correction --------------------------------------------------------------------------------------------
def pointer(axis, s, xy, off, col):
    """A label set off in clear space, with a pointer line to its point."""
    axis.annotate(s, xy, xytext=off, textcoords="offset points", ha="center", va="center", fontsize=16, color=col,
                  arrowprops=dict(arrowstyle="-", color=col, lw=0.9, shrinkA=4, shrinkB=4))


def corr_area(axis, x, upper, base):
    for where, col in ((upper >= base, C["green"]), (upper < base, C["red"])):
        axis.fill_between(x, base, upper, where=where, interpolate=True, facecolor=col, alpha=0.18, lw=0, zorder=1)
        axis.fill_between(x, base, upper, where=where, interpolate=True, facecolor="none", edgecolor=col, hatch="////",
                          lw=0, alpha=0.6, zorder=1)


def gap_figure(name, dates, observed, ts, resid, filled, a_date, c_date, start, end, offsets):
    """The residual correction across the gap between the observed months a and c."""
    win = (dates >= start) & (dates <= end)
    a, c = np.flatnonzero(dates == a_date)[0], np.flatnonzero(dates == c_date)[0]
    r_line = np.interp(np.arange(a, c + 1), [a, c], [resid[a], resid[c]])
    fig, (ax, axr) = plt.subplots(2, 1, figsize=(9, 5.8), dpi=200, sharex=True,
                                  gridspec_kw=dict(height_ratios=[2.2, 1], hspace=0.12))
    # shade from a to c, the observed months that bound the gap
    for x in (ax, axr):
        x.axvspan(dates[a], dates[c], color=C["lightgray"], alpha=0.7, lw=0)
    ax.plot(dates[win], observed[win], color=C["navy"], lw=1.5, marker="o", ms=3.5, label="Observed, y", zorder=4)
    ax.plot(dates[win], ts[win], color=C["orange"], lw=1.4, ls=(0, (4, 3)), label="Model alone, T + S")
    # a and c are observed months, so only the months between them get the filled marker
    ax.plot(dates[a:c + 1], filled[a:c + 1], color=C["red"], lw=2, marker="o", ms=4, mfc="white",
            markevery=range(1, c - a), label="Filled, T + S + correction", zorder=3)
    # the correction: the area between the fill and the model alone, matched in the residual panel by the area
    # between the interpolated residual and zero, green where it raises the fill and red where it lowers it
    span = dates[a:c + 1]
    corr_area(ax, span, filled[a:c + 1], ts[a:c + 1])
    corr_area(axr, span, r_line, np.zeros_like(r_line))
    ax.set_ylabel("GWSa (cm)")
    ax.legend(loc="lower left", frameon=False, ncol=3, fontsize=9.5)
    pointer(ax, "$a$", (dates[a], observed[a]), offsets["a"], C["navy"])
    pointer(ax, "$c$", (dates[c], observed[c]), offsets["c"], C["navy"])
    tidy(ax)
    lo, hi = min(np.nanmin(observed[win]), ts[win].min()), max(np.nanmax(observed[win]), ts[win].max())
    ax.set_ylim(lo - 0.35 * (hi - lo), hi + 0.2 * (hi - lo))
    axr.axhline(0, color=C["gray"], lw=0.8)
    axr.plot(dates[win], resid[win], color=C["gray"], lw=1.1, marker="o", ms=3)
    axr.plot(dates[a:c + 1], r_line, color=C["red"], lw=2, ls=(0, (4, 3)))
    pointer(axr, "$r_a$", (dates[a], resid[a]), offsets["ra"], C["red"])
    pointer(axr, "$r_c$", (dates[c], resid[c]), offsets["rc"], C["red"])
    rlo, rhi = np.nanmin(resid[win]), np.nanmax(resid[win])
    axr.text(dates[(a + c) // 2], rhi + 0.15 * (rhi - rlo), "correction, interpolated from $r_a$ to $r_c$", ha="center",
             fontsize=11, color=C["red"])
    axr.set_ylabel("Residual (cm)")
    axr.set_ylim(rlo - 0.3 * (rhi - rlo), rhi + 0.35 * (rhi - rlo))
    tidy(axr)
    fig.align_ylabels((ax, axr))
    fig.savefig(OUT / f"{name}.png", facecolor="white", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)


# Northern Midwest: the gap between the missions, where r_a and r_c happen to be almost equal
gap_figure("seasonal-gap-correction", d.date.values, d.observed.values, trend + seasonal, resid, d.filled.values,
           np.datetime64("2017-06-01"), np.datetime64("2018-06-01"), np.datetime64("2016-09-01"),
           np.datetime64("2019-03-01"), dict(a=(-45, 40), c=(-45, 45), ra=(40, -38), rc=(-40, -38)))

# Central Valley: the same gap, where the two residuals differ by about 9 cm and the correction tilts
cv = pd.read_csv(Path(__file__).parent / "data" / "central_valley_gwsa.csv", parse_dates=["Date"])
first, last = cv.GWSa.first_valid_index(), cv.GWSa.last_valid_index()
cv = cv.loc[first:last].reset_index(drop=True)
mc = fit_series(cv.GWSa.values, cv.Date.dt.month.values - 1)
cv_ts = mc["trend"] + mc["seasonal"]
gap = cv.GWSa_is_filled == 1
r = np.where(np.isnan(cv.GWSa.values), np.nan, mc["resid"])
fill = cv_ts + pd.Series(r).interpolate().values
assert np.allclose(fill[gap], cv.GWSa_filled[gap], atol=2e-3), "Central Valley refit differs from the app's fill"
gap_figure("seasonal-gap-correction-cv", cv.Date.values, cv.GWSa.values, cv_ts, r, np.where(gap, fill, cv.GWSa.values),
           np.datetime64("2017-06-01"), np.datetime64("2018-06-01"), np.datetime64("2016-09-01"),
           np.datetime64("2019-03-01"), dict(a=(45, 14), c=(-45, 40), ra=(40, -30), rc=(-50, -22)))

print("breakpoints", [f"{b:%Y-%m}" for b in bp_dates], "BIC", [round(f["bic"], 1) for f in fits], "chosen", chosen)
