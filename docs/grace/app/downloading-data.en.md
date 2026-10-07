# Downloading Data

## Downloading a CSV

With a region or a cell selected, click **Download CSV** in the upper right of the chart panel. The file contains the monthly values of all
five layers for that region or cell, whichever ones are plotted. It is named `grace_gwsa_data.csv` for a region (the middle part follows the
displayed layer) or `grace_cell_<lat>_<lon>_data.csv` for a single cell.

| Column | Contents |
|---|---|
| `Date` | First day of the month, `YYYY-MM-DD` |
| `GWSa`, `TWSa`, `SMa`, `SWEa`, `CANa` | Area-weighted mean anomaly for the month, cm of liquid water equivalent |
| `<layer>_upper`, `<layer>_lower` | The mean plus and minus 1σ |
| `GWSa_filled`, `TWSa_filled` | The same series with its gaps filled by the seasonal model; equal to the observed value in every other month |
| `GWSa_is_filled`, `TWSa_is_filled` | 1 in months the seasonal model filled, 0 otherwise |

For example, the start of the gap between missions for the Northern Midwest Aquifer System:

```text
Date,GWSa,GWSa_upper,GWSa_lower,GWSa_filled,GWSa_is_filled,TWSa,...
2017-06-01,9.529,14.913,4.146,9.529,0,12.536,...
2017-07-01,,,,11.146,1,,...
2017-08-01,,,,12.694,1,,...
```

The file has one row for every month from April 2002 to the latest release. In months with no GRACE data, the `GWSa` and `TWSa` cells are blank,
while the GLDAS layers (`SMa`, `SWEa`, `CANa`) still have values, because the land surface models run every month. The `_filled` columns
supply a value for those months (see [Gap Filling](gap-filling.md)). They are written whatever the **Gap filling** setting, so
the file is the same however the chart is drawn.

Excel, Google Sheets, Python and R all read the file directly, and the ISO dates need no conversion (in pandas, use
`pd.read_csv(path, parse_dates=["Date"])`). To get
the uncertainty σ back from the bounds, take `(upper − lower) / 2`.

## Converting to volume

The anomalies are depths of water averaged over the region. Multiply by the region's area to get a volume:

```text
ΔV (km³) = GWSa (cm) × Area (km²) / 100,000
```

For example, a GWSa of −12 cm over a 400,000 km² aquifer is 12 × 400,000 / 100,000 = 4.8 km³ (4,800 million m³) less water than the 2004–2009
average. The change between two dates is the difference of their anomalies times the area, and a trend in cm/yr times the area gives a rate of
loss or gain in km³/yr.

Use the area of the region as you defined it. For an uploaded region, a GIS can report the polygon's area; compute it in an equal-area
projection, not in degrees.

## What to do next

The CSV is the starting point for analyses outside the app. To estimate recharge, use the app's [Recharge Analysis](../recharge/opening.md),
which runs the water table fluctuation method on the filled series and has its own CSV download. The
[Gap-Filling Method](../gap-filling/method.md) describes how the `GWSa_filled` and `TWSa_filled` columns are estimated.
