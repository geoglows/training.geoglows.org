## Overview

There are 6.25 million river segments modeled in the GEOGLOWS V2 datasets. These numbers are unique to the TDX-Hydro dataset and are different from
numbers in any other stream dataset and previous versions of the model. All ID numbers are 9 digits. As a reference, this table provides IDs of some 
major rivers and their general locations.

| ID Number        | Select Rivers and General Locations |
| ---------------- | ----------------------------------- |
| 760_021_611      | Mississippi, USA                    |
| 160_064_246      | Nile, East Africa                   |
| 710_462_910      | Colorado, USA & Mexico              |
| 441_057_380      | Ganges, India                       |
| 430_157_411      | Mekong, Vietnam                     |
| 210_406_913      | Tiber, Italy                        |
| 621_010_293      | Amazon, Brazil                      |
| 130_747_391      | Congo, D.R. Congo                   |
| 640_255_644      | Parana, Argentina                   |

!!! warning "Users migrating from V1"
    RFS v2 is derived from a different source Digital Elevation Model (DEM) than v1 and has significantly more modeled streams. Because of the higher
    resolution and changes in placements of river channels, it is not possible to provide a mapping of all version 1 numbers to v2 numbers. We have 
    outlined some steps below to map an old ID to a GEOGLOWS 2 ID.

[//]: # (todo add image)
Example Comparison of GEOGLOWS 1 vs GEOGLOWS 2 Streams

Left: GEOGLOWS Version 1's stream network (similar to hydrosheds). Notice how the river centerlines do not line up exactly with the rivers in the
satellite imagery. Right: GEOGLOWS Version 2's stream network (derived from TDX Hydro). More streams are included and river centerlines are more
aligned to the streams in the imagery. This river network is at a higher spatial resolution allowing for lines which more smoothly follow river paths
compared to the more jagged or blocky looking lines on the left.

## Step 1: Find the watershed group of your stream
For computation and data organization purposes, data are broken into groups of watersheds. These were referred to as "regions" in V1 and followed
major watersheds and some political boundaries. There were 13 regions in V1. In V2, there are more of these groups and are identified with a 3 digit
number. We call these "vector processing units" or VPU in order to share the same terminology used by other similar modeling projects. There are 125
divisions in V2. Below we have the GEOGLOWS 1 regions mapped to all the applicable GEOGLOWS 2 VPU numbers.

First, find the region your river is part of using the table and maps. Next, download all V2 VPUs or only the ones specifically applicable to the
watersheds you need. Use the Dataset Reference page on this site to find links for dataset downloads. For example, if you had a river in the East Asia
region, download the V2 VPUs 401 to 406.

GEOGLOWS V1 Region Boundaries

[//]: # (todo add image)


GEOGLOWS V2 VPU Boundaries

[//]: # (todo add image)

## Step 2: Comparison with GIS
Load the old network into your GIS software of choice. Identify the stream in the old network, either by querying the attribute table of the network
or by visually locating the stream. The image on the right shows the Central America region loaded in QGIS. A stream was selected in red using the
Select tool, and zoomed in by right clicking the network name in the Layers panel and selecting "Zoom to Layer(s)"

Load the VPU(s) into the GIS. The new network will appear, and new prospective rivers should appear in the same area as the selected stream. If none
appear in the area of the selected stream, it may be that you need to download another VPU region. Consult the VPU boundary map and download any
additional regions. The image shows that the VPU region 718 has been loaded (orange).

In this example, it is fairly intuitive that stream should map to the new stream that is closest to it. The image to right shows the new stream
selected in red that most closely matches the old stream.

By selecting the VPU region layer in the Layers panel, and then selecting the new stream using the "Identify Features Tool", we can obtain the new id.
The image on the right shows the attributes of the stream. The new ID is labeled as the "TDXHydroLinkNo." Other useful attributes can be seen in this
panel.

While this process is usually straightforward, there are some areas where more work is required to correctly map an old stream to a new stream. Below
on the left is the old network in blue and the new network in green, with the old stream we want to map highlighted in red. On the right, a potential
new stream is highlighted in red. This appears to be a logic choice, but more inspection is warranted. By checking the attribute tables for both
features, it is revealed that the drainage area upstream of the old stream is roughly 6000 sq. km, while the proposed new stream has a drainage area
of about 200 sq. km, which indicates that our selection is probably incorrect.

Old stream selected

New proposed stream selected

Below, the map has been zoomed out. After carefully tracing the paths of the old stream and the new streams to the main trunk, it becomes clear that
the new network routes the main river to a different outlet. This suggests that the stream selected in the right picture is the correct one. An
inspection of the attribute table reveals that this new selection has a drainage area of about 5300 sq. km, which better matches our expectations.

Old stream selected

New correct stream selected