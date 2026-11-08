# Editing and Exporting

Measurements can be corrected or deleted in a table of a well's record or straight from the chart. Saved changes cannot be undone, so
back up first if you might want the original values again. In a Sample Data region, editing offers to copy the region to My Data, where
you can make the change.

## The measurement table

With one well selected, **View/Edit** in the chart panel opens **Edit Measurements**: every measurement of the current data type, by
date.

- To correct a value, type the new one in its box.
- To delete a measurement, click the bin at the end of its row. The row is struck through, and clicking the bin again restores it.
- **Save Changes** saves the edits and deletions together, and **Cancel** leaves the record as it was.

**Outlier threshold** highlights values far from the measurements around them in time. For each value, the app takes the measurements
within two years either side, or the six nearest when there are fewer, without the value itself. With their quartiles Q1 and Q3 and
interquartile range IQR = Q3 − Q1, the value is flagged when it is below Q1 − k·IQR or above Q3 + k·IQR. The slider sets k from 1 to 5,
3 to start with, and the count of flagged values is at the right.

![The measurement table of a well, with the outlier check](../../static/images/aquiferx/edit-table.webp){ width="704" }

Comparing each value with its neighbors in time keeps a long rise or decline from being flagged. The water table at the well above fell
from an elevation of 23 ft in 1960 to about 0 by 2000 and has stayed there, and the check flags 2 of its 61 values. The value of 0 in
January 1986, more than 9 ft below the values around it, is most likely a missing reading stored as zero: DWR's record gives the depth
to water that day as 140.1 ft, the same as the ground surface elevation. The other, 2.0 ft in November 2021, is only 2.2 ft above the
median of its neighbors, but five of the six lie within 0.7 ft of each other, so a small step stands out. With the slider at 4, only the
1986 value is flagged. A flagged value is a reading to look at on the chart, which may be a real event such as a pumping test, so check
before deleting it.

In a well read in two seasons, the check can flag ordinary readings. Well 901, in the 180/400 Foot Aquifer, is read each August, often
twice, and again in November or December, when the water level is about 38 ft higher. Most of the neighbors of a December reading are
then August readings, and the check flags some December readings, such as −19.9 ft on December 2, 1998, although the December readings
a year before and a year after are −28.5 and −28.3 ft.

## On the chart

![The menu of a measurement on the chart](../../static/images/aquiferx/edit-point-menu.webp){ align=right width="260" }

Right-click a measurement point on the chart for its menu:

- **Edit** opens a box with the date and value. Type the new value and press **Enter** or click **Save**.
- **Delete** asks you to confirm, then removes the measurement.

Each change is saved as soon as you make it. This is the quickest way to deal with a single bad reading you can see on the chart.

<div style="clear: both"></div>

## Removing data in bulk

Larger removals are made where the data came in or in the region tree:

- **Replace all**, when importing measurements, deletes the region's measurements of the types being imported (see
  [Measurements](measurements.md#measurements-already-in-the-region)).
- **Replace All**, when importing wells or aquifers, deletes the region's wells, measurements and, for aquifers, the aquifers too (see
  [Wells](wells.md#uploading-a-wells-file) and [Regions and Aquifers](regions-aquifers.md#adding-aquifers)).
- **Custom Data Types** deletes a custom type with all its measurements (see
  [Water Quality](water-quality.md#custom-data-types)).
- **Delete** in the menu of an aquifer or a region in the tree (see
  [Regions and Aquifers](regions-aquifers.md#changing-a-region)).

## Exporting

**Export CSV** in the chart panel downloads what the chart shows for the selected wells: one row per measurement, with its date as
YYYY-MM-DD, value, well ID, well name and aquifer ID, so the file can be imported again. The file is named after the first well and the
data type. With a gap-filling model open for one well, it downloads the model's monthly series instead (see Part 4).

To take a whole region elsewhere, use **Download** in the region's menu, or **Back up** for all of My Data. Both make a zip file of the
region's own files, which other software can read and Aquifer Analyst can restore (see
[Sample Data and My Data](../start/my-data.md#backing-up-and-restoring)).
