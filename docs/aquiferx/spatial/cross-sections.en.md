# Cross Sections

A cross section is a profile of the maps along a straight line: the water table's elevation from one end of the line to the other, on
the date shown. As the date changes, the profile changes with it, so playing the maps shows the water table rising or falling along
the line.

![A cross section across the Escalante Valley-Beryl-Enterprise maps](../../static/images/aquiferx/map-section.webp)

## Drawing a section

With a set of maps open, click **Cross Section** on the card at the top right of the map. The pointer becomes a crosshair:

1. Click where the line starts. A dashed line follows the pointer from there.
2. Click where it ends.

**Esc** before the second click cancels. The line is drawn with its ends labeled A and A′, and an arrow at each end that points the
way you look at the profile: with A on your left and A′ on your right. The panel below the map opens on the **Cross Section** tab,
titled *Cross Section A–A′* with the line's length.

The button then reads **Clear Cross Section**, which removes the line and the tab. Closing the maps, or opening another set, clears it
too. To draw a different line, clear the first.

## The profile

The chart gives the elevation along the line against the distance from A, in the region's unit. It is sampled at 200 points evenly
spaced along the line, each the bilinear interpolation of the four cell centers around it. Where the line runs outside the aquifer's
outline, the profile has a gap. Pointing at the chart gives the date, the distance and the elevation, and the date shown is also at the
top right of the tab.

The elevation axis spans the lowest to the highest value along the line on any date of the set, and stays fixed as the date changes.
Drag the slider or play the maps, and the profile drops where the water table fell and rises where it recovered.

The section in the figure runs 26.6 miles up the Escalante Valley-Beryl-Enterprise aquifer, from its southwest end to its northeast.
In March 1941 the water table fell along it from 5,140 ft at A to 5,092 ft at A′. By March 1999 it had dropped 75 to 93 ft along the
first 11 miles and little near A′, and the profile rose from 5,057 ft at A to 5,092 ft at A′: the water table's slope along the valley
had reversed.

The profile is of the water table maps alone. It does not show the ground surface or the aquifer's base, and between the wells it
carries the interpolation's shape (see [Interpolation Methods](interpolation.md)). Wells near the line show where the profile rests on
readings: turn on **Active Wells** to see which wells have a value on the date shown (see [Viewing the Maps](maps.md#what-the-map-shows)).
