#!/usr/bin/env python3
"""
Retake the app screenshots used in the GRACE training.

They have to be remade whenever the interface changes or the data is rebuilt,
and doing it by hand means putting the app into a dozen particular states and
cropping each one the same way as last time. This drives a headless Chromium
instead, so a rebuild is a re-run.

It needs the app's dev server running on the branch being documented:

    cd ../webapp-grace-groundwater && npm run dev

Then, from this repository:

    uv run --with playwright --with pillow python tools/make_screenshots.py
    uv run --with playwright --with pillow python tools/make_screenshots.py home panel

Playwright's own Chromium is used rather than the browser on this machine,
which is subject to whatever policies it has been given and cannot always reach
a local server.

Output is .webp at the sizes the pages already use: 1800 wide for a whole
window, narrower crops for single controls.
"""

import io
import os
import sys
from pathlib import Path

from PIL import Image
from playwright.sync_api import Page, sync_playwright

APP = os.environ.get("APP_URL", "http://127.0.0.1:5173/")
OUT = Path(__file__).resolve().parent.parent / "docs/static/images/grace"

WIDTH, HEIGHT = 1800, 1125
# The regions the captions already name, so a retake keeps saying what the
# surrounding text says it shows.
REGION = "Iullemeden-Irhazer Aquifer System"      # the regional-view examples
SEASONAL = "Northern Midwest Aquifer System"      # strong annual cycle: gaps, recharge
CENTRAL_VALLEY = "California Central Valley"      # the leakage and poor-candidate examples
VOLTA = ("igrac-tba", "Volta Basin")              # a published basin with a case study behind it
SETTLE = 2500          # after an interaction that redraws the map
LOAD = 6000            # after one that fetches a variable it has not read yet


# ---------------------------------------------------------------- plumbing
def save(page_or_locator, name: str, **kw) -> None:
    """Shoot, then write the .webp the pages reference. Quality 82 keeps a full
    window near the 130 KB the committed files sit at, with no visible loss on
    the thin lines a chart is made of."""
    png = page_or_locator.screenshot(**kw)
    img = Image.open(io.BytesIO(png)).convert("RGB")
    dest = OUT / f"{name}.webp"
    img.save(dest, "WEBP", quality=82, method=6)
    print(f"  wrote {dest.name}  {img.width}x{img.height}  {dest.stat().st_size // 1024} KB")


def open_app(pw, width=WIDTH, height=HEIGHT, scale=1) -> tuple:
    """A whole window is shot at 1800x1125 and scale 1. A single control is shot
    at scale 2, because the pages display those small and a 1x crop of a 320px
    panel is soft at any width."""
    browser = pw.chromium.launch()
    page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=scale)
    page.goto(APP, wait_until="networkidle", timeout=120_000)
    page.wait_for_timeout(LOAD)
    return browser, page


def pick_region(page: Page, name: str = REGION, region_set: str | None = None) -> None:
    if region_set:
        page.locator("#region-set-select").select_option(region_set)
        page.wait_for_timeout(SETTLE)
    page.locator("#region-filter").fill(name.split()[0])
    page.wait_for_timeout(400)
    page.locator("#region-list").get_by_text(name, exact=True).first.click()
    page.wait_for_selector("#timeseries-plot canvas", timeout=60_000)
    # Leave the list as the app opens it, so the shot is not of a filtered list.
    page.locator("#region-filter").fill("")
    page.wait_for_timeout(LOAD)


def go_global(page: Page) -> None:
    page.locator("#global-view-button").click()
    page.wait_for_timeout(LOAD * 2)


def trends_off(page: Page) -> None:
    if "Hide" in page.locator("#trends-button").inner_text():
        page.locator("#trends-button").click()
        page.wait_for_timeout(LOAD)


# ------------------------------------------------------------------- shots
def shot_home(pw) -> None:
    """The landing page: regional view, trends on, nothing selected."""
    b, pg = open_app(pw)
    save(pg, "app-home")
    b.close()


def shot_panel(pw) -> None:
    """The whole control panel. It fills the window height, so the window sets
    how much of the region list comes with it."""
    b, pg = open_app(pw, height=1180, scale=2)
    save(pg.locator("aside.rfs-panel"), "app-panel")
    b.close()


def shot_header(pw) -> None:
    b, pg = open_app(pw, scale=2)
    save(pg, "app-header", clip={"x": 320, "y": 0, "width": 1480, "height": 52})
    b.close()


def shot_settings(pw) -> None:
    b, pg = open_app(pw)
    pg.locator("#settings-button").click()
    pg.wait_for_timeout(SETTLE)
    save(pg, "app-settings")
    b.close()


def shot_region(pw) -> None:
    b, pg = open_app(pw)
    pick_region(pg)
    save(pg, "app-region")
    b.close()


def shot_region_result(pw) -> None:
    """What a region looks like once analyzed, for Reading the results.

    A published basin rather than a drawn box: the section is about reading an
    ordinary result, and the Volta has a case study behind it.
    """
    b, pg = open_app(pw)
    pick_region(pg, VOLTA[1], region_set=VOLTA[0])
    save(pg, "app-region-result")
    b.close()


def shot_region_boundaries(pw) -> None:
    b, pg = open_app(pw)
    pick_region(pg)
    pg.locator("#border-toggle").check()
    pg.locator("#mascon-toggle").check()
    pg.wait_for_timeout(SETTLE)
    save(pg, "app-region-boundaries", clip={"x": 320, "y": 0, "width": 1480, "height": 766})
    b.close()


def shot_chart_compare(pw) -> None:
    """GWSa with TWSa and SMa on the same axes."""
    b, pg = open_app(pw)
    pick_region(pg)
    for key in ("TWSa", "SMa"):
        pg.locator(f"#series-toggles input[data-series='{key}']").check()
        pg.wait_for_timeout(LOAD)
    save(pg, "app-chart-compare", clip={"x": 320, "y": 780, "width": 1480, "height": 345})
    b.close()


def shot_global(pw) -> None:
    b, pg = open_app(pw)
    go_global(pg)
    trends_off(pg)
    save(pg, "app-global")
    b.close()


def shot_global_trends(pw) -> None:
    b, pg = open_app(pw)
    go_global(pg)
    save(pg, "app-global-trends")
    b.close()


def shot_global_cell(pw) -> None:
    b, pg = open_app(pw)
    go_global(pg)
    trends_off(pg)
    # Central Iran, which the existing caption names.
    pg.mouse.click(1255, 330)
    pg.wait_for_selector("#timeseries-plot canvas", timeout=60_000)
    pg.wait_for_timeout(LOAD)
    save(pg, "app-global-cell")
    b.close()


def shot_time_control(pw) -> None:
    b, pg = open_app(pw, scale=2)
    pick_region(pg)
    save(pg.locator("#time-control"), "app-time-control")
    b.close()


def shot_gap_fill_control(pw) -> None:
    b, pg = open_app(pw, scale=2)
    save(pg.locator("#gap-fill-control"), "app-gap-fill-control")
    b.close()


def shot_gap_fills(pw) -> None:
    """The same chart under each of the three gap-filling options."""
    b, pg = open_app(pw)
    pick_region(pg, SEASONAL)
    chart = {"x": 320, "y": 780, "width": 1480, "height": 345}
    for value, name in [("none", "app-gap-fill-none"),
                        ("line", "app-gap-fill-line"),
                        ("seasonal", "app-gap-fill-seasonal")]:
        # The radio sits behind its own label span, so a real click lands on the
        # span; force skips the actionability check rather than the event.
        pg.locator(f"#gap-fill-control input[value='{value}']").check(force=True)
        pg.wait_for_timeout(SETTLE)
        save(pg, name, clip=chart)
    b.close()


def _open_recharge(pw, region=SEASONAL):
    """A region with its gaps filled, then the recharge page over it."""
    b, pg = open_app(pw)
    pick_region(pg, region)
    pg.locator("#gap-fill-control input[value='seasonal']").check(force=True)
    pg.wait_for_timeout(SETTLE)
    return b, pg


def shot_recharge_button(pw) -> None:
    b, pg = _open_recharge(pw)
    save(pg, "app-recharge-button", clip={"x": 320, "y": 780, "width": 1480, "height": 345})
    b.close()


def _enter_recharge(pg) -> None:
    pg.get_by_role("button", name="Recharge Analysis").click()
    pg.wait_for_selector(".rc-view", timeout=60_000)
    pg.wait_for_timeout(LOAD)


def shot_recharge_pages(pw) -> None:
    """The blocks of the recharge page, each cropped to what its caption names.

    The page has three numbered sections: the seasonality check, the water years
    with their picks, and recharge by year. Each shot is one block inside one of
    them, taken by class rather than by position so a reordering does not
    silently swap two images.
    """
    b, pg = _open_recharge(pw)
    _enter_recharge(pg)
    sec = pg.locator(".rc-section")
    save(sec.nth(0), "app-recharge-seasonality")                       # the whole check
    save(sec.nth(1).locator(".rc-chart-box").first, "app-recharge-picks")
    save(sec.nth(1).locator(".rc-editor").first, "app-recharge-editor")
    save(sec.nth(2).locator(".rc-summary").first, "app-recharge-summary")
    save(sec.nth(2).locator(".rc-chart-box").first, "app-recharge-chart")
    save(sec.nth(2).locator(".rc-table-wrap").first, "app-recharge-table")
    b.close()


def shot_recharge_verdict_cv(pw) -> None:
    """The Central Valley, whose seasonality check comes back poor."""
    b, pg = _open_recharge(pw, CENTRAL_VALLEY)
    _enter_recharge(pg)
    save(pg.locator(".rc-verdict-title").first.locator("xpath=.."), "app-recharge-verdict-cv")
    b.close()


# A box over Punjab and Haryana, which is what the uploaded-region caption
# names. Written to a temp file because the dialog takes a file, not a string.
PUNJAB = """{"type":"FeatureCollection","features":[{"type":"Feature","properties":{"name":
"Punjab and Haryana"},"geometry":{"type":"Polygon","coordinates":[[[74.0,29.5],[77.5,29.5],
[77.5,32.3],[74.0,32.3],[74.0,29.5]]]}}]}"""


def _upload_file() -> str:
    path = Path(os.environ.get("TMPDIR", "/tmp")) / "punjab-haryana.geojson"
    path.write_text(PUNJAB)
    return str(path)


def shot_upload(pw) -> None:
    """The Upload Region dialog, with a file chosen."""
    b, pg = open_app(pw)
    pg.locator("#upload-button").click()
    pg.locator("#upload-file-input").set_input_files(_upload_file())
    pg.locator("#upload-region-name").fill("Punjab and Haryana")
    pg.wait_for_timeout(SETTLE)
    save(pg, "app-upload")
    b.close()


def shot_upload_result(pw) -> None:
    """The same region analyzed, which is what the regional-view page shows."""
    b, pg = open_app(pw)
    pg.locator("#upload-button").click()
    pg.locator("#upload-file-input").set_input_files(_upload_file())
    pg.locator("#upload-region-name").fill("Punjab and Haryana")
    pg.wait_for_timeout(SETTLE)
    pg.locator("#upload-submit").click()
    pg.wait_for_selector("#timeseries-plot canvas", timeout=90_000)
    pg.wait_for_timeout(LOAD)
    save(pg, "app-upload-result")
    b.close()


def shot_central_valley(pw) -> None:
    b, pg = open_app(pw)
    pick_region(pg, CENTRAL_VALLEY)
    save(pg, "app-central-valley", clip={"x": 320, "y": 0, "width": 1480, "height": 925})
    b.close()


SHOTS = {
    "home": shot_home,
    "panel": shot_panel,
    "header": shot_header,
    "settings": shot_settings,
    "region": shot_region,
    "region-result": shot_region_result,
    "region-boundaries": shot_region_boundaries,
    "chart-compare": shot_chart_compare,
    "global": shot_global,
    "global-trends": shot_global_trends,
    "global-cell": shot_global_cell,
    "time-control": shot_time_control,
    "gap-fill-control": shot_gap_fill_control,
    "gap-fills": shot_gap_fills,
    "recharge-button": shot_recharge_button,
    "recharge-pages": shot_recharge_pages,
    "recharge-verdict-cv": shot_recharge_verdict_cv,
    "central-valley": shot_central_valley,
    "upload": shot_upload,
    "upload-result": shot_upload_result,
}


def main() -> None:
    wanted = sys.argv[1:] or list(SHOTS)
    unknown = [w for w in wanted if w not in SHOTS]
    if unknown:
        raise SystemExit(f"Unknown shot(s): {', '.join(unknown)}\nKnown: {', '.join(SHOTS)}")
    with sync_playwright() as pw:
        for name in wanted:
            print(f"{name} ...")
            SHOTS[name](pw)


if __name__ == "__main__":
    main()
