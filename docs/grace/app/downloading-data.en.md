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

For example:

```text
Date,GWSa,GWSa_upper,GWSa_lower,TWSa,TWSa_upper,TWSa_lower,SMa,...
2002-04-01,-2.406,4.184,-8.996,-4.961,1.683,-11.604,-2.584,...
2002-05-01,-2.238,1.684,-6.160,-5.182,-1.284,-9.081,-2.976,...
```

The file has one row for every month from April 2002 to the latest release. In months with no GRACE data, the `GWSa` and `TWSa` cells are blank,
while the GLDAS layers (`SMa`, `SWEa`, `CANa`) still have values, because the land surface models run every month. The **Fill gaps** setting
does not change the file.

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

The CSV is the starting point for the analyses in Part 3:

- [Filling Gaps](../applications/gap-filling.md) estimates the missing months, which many analyses need.
- [Estimating Recharge](../applications/recharge-wtf.md) applies the water table fluctuation method to the filled series.
