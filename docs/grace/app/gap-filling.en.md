# Gap Filling

The GRACE record is missing 35 months: scattered single months, mostly between 2011 and 2017, and the 11 months between the end of GRACE and
the start of GRACE-FO (see [The GRACE Mission](../background/grace-mission.md#the-record-and-its-gaps)). The app can leave those months empty,
bridge them, or estimate them.

![The Gap filling control in the app's panel](../../static/images/grace/app-gap-fill-control.webp){ width="310" }

The **Gap filling** control in the panel sets what the chart does at months with no GRACE data:

- **None** breaks the line at every gap, so you can see exactly which months were observed.
- **Straight line** joins the months on either side of each gap. It only bridges the gap on the chart and estimates nothing.
- **Seasonal model** fills each gap with values estimated from the rest of the record, using a trend and seasonal cycle fitted to the
  observed months (see [Gap-Filling Method](../applications/gap-filling.md#method)). Filled months are drawn as a dashed line with open
  markers, and hovering over one shows its value.

The Northern Midwest Aquifer System has a strong seasonal cycle, which shows the difference between the three options well. With **None**,
each gap breaks the line, and the uncertainty band, so you can see where the record is missing: the scattered months between 2011 and 2017 and
the 11 months between GRACE and GRACE-FO:

![Northern Midwest Aquifer System GWSa with the line broken at each gap](../../static/images/grace/app-gap-fill-none.webp)

With **Straight line**, the 11 months between GRACE and GRACE-FO become a flat bridge from 9.5 cm in June 2017 to 10.0 cm in June 2018:

![Northern Midwest Aquifer System GWSa with the gaps bridged by straight lines](../../static/images/grace/app-gap-fill-line.webp)

With **Seasonal model**, the filled months carry on the region's annual cycle, rising to 12.8 cm in September 2017 and falling to 4.8 cm in
March 2018 before climbing to meet the first GRACE-FO month. The short gaps between 2011 and 2017 follow the observed peaks and troughs in the
same way:

![Northern Midwest Aquifer System GWSa with the gaps filled by the seasonal model](../../static/images/grace/app-gap-fill-seasonal.webp)

How much a fill differs from a straight line depends on the region. Much of the seasonal swing that GRACE sees is soil moisture and snow, which
are removed before GWSa is computed, so in many regions the groundwater cycle is small and the filled months look close to a straight line.

Some details of the app's fill:

- GWSa and TWSa are each filled from their own record. A filled GWSa value is therefore not exactly the filled TWSa minus the GLDAS terms for
  that month. The GLDAS layers have no gaps and are never filled.
- The app chooses the number and position of the trend breakpoints automatically.
- The uncertainty band is not drawn for filled months, because the error of a filled value comes from the model rather than from GRACE (see
  [How good is the fill?](../applications/gap-filling.md#how-good-is-the-fill)).
- The downloaded CSV always includes the filled values, in the `GWSa_filled` and `TWSa_filled` columns, with `GWSa_is_filled` and
  `TWSa_is_filled` marking the filled months (see [Downloading Data](downloading-data.md)). This holds whichever option the chart uses.

The model behind the fill, and tests of how well it works, are described in [Gap-Filling Method](../applications/gap-filling.md).
