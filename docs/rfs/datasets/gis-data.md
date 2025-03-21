# GIS Data

## Terms and Vocabulary

- **Hydrography**: GIS datasets of hydrological features such as streams, confluence points, catchment boundaries, watershed boundaries, lake
  boundaries, and other features.
- **Hydrofabric**: hydrography.
- **TanDEM-X**: A SAR satellite mission from the German Aerospace Center (DLR) and Airbus Defence and Space. It is used to produce a 12-meter digital
  elevation model which is the highest accuracy and resolution global product of its kind. It is not publicly available but the Copernicus Glo30 and
  FABDEM products derived from it are.
- **TDX-Hydro**: A stream centerline and catchment boundary dataset produced by the National Geospatial Intelligence Agency in 2023. The streams are
  delineated from 12-meter TanDEM-X elevation data using TauDEM with extensive elevation preprocessing and stream centerline location correction
  post-processing.
- **TauDEM**: A terrain analysis tool used to delineate streams and catchments from elevation data.
- **VPU**: Vector Processing Unit. A group of 1 or more complete watersheds put together to make smaller pieces of the global hydrography dataset for
  convenience in distributing data, dividing computations, and making maps.

---

## Overview

The RFS hydrography is a modification of the TDX-Hydro streams and catchments dataset. It comes from proprietary TanDEM-X 12-m elevation data. The GIS
data used in RFS is available for users to download and use for their own purposes. This dataset is referred to as hydrography, hydrofabric, or river
network. It is vector data with points and lines with coordinates, not grid data, and it includes four main components:

- The exact **stream center lines** used in RFS. Each stream has a unique 9 number ID which is referred to as a reachID, link number, or stream ID.
  This is the file called "streams_{vpu}.gpkg".
- The **catchment boundaries** used RFS. There are the boundaries around each of the streamlines and represent the area connected to that streamline.
  It is identified using the same link number as the stream center lines. This is the file called "catchments_{vpu}.spatialite". Each stream
  centerline corresponds to exactly one unique catchment boundary.
- The **connection points** used in RFS where different stream centerlines connect. Each point has the an attribute called DSLINKNO which represents
  the one downstream link number for each of the points. It has another attribute called USLINKNOs. This is a comma seperated list of the link numbers
  upstream of the nexus point. This is the file called "nexus_{vpu}.gpkg".
- The **merged lake catchments** used in RFS to represent the locations of lakes. Stream catchments that were identified through GIS searching to be
  part of a lake were merged to present the lakes. Therefore, it will have a different shape than the actual lake boundary based on the shapes of the
  merged stream catchments. This is the file called "lakes_{vpu}.gpkg".

---

## Modifications to TDX-Hydro

There were some slight modifications made to the TDX-Hydro dataset when creating the GEOGLOWS stream network. This is not a comprehensive list; more
details are available
at [https://data.geoglows.org/dataset-descriptions/gis-streams-and-catchments](https://data.geoglows.org/dataset-descriptions/gis-streams-and-catchments).

- Regions in the far north and south were excluded, along with some small islands, because runoff datasets may not be as accurate in these regions,
  and there is less interest.
- Streams that had no length and no upstream/downstream segments were removed along with their associated catchments.
- Streams with no length but with upstream and downstream segments were removed with their associated catchments, and the upstream and/or downstream
  segments were modified to preserve the connectivity of the network.
- For many of the regions, headwater streams were dissolved with the downstream segments.
- Small watersheds that did not represent real flowing streams were often dropped.

---

## VPUs

The GIS data are divided into 125 smaller pieces, VPUs. This makes the large quantity of data easier to manage and access. Each VPU represents one or
more complete watersheds.

![image](../../static/images/vpu-boundary.png)

The VPU boundaries are also available for download to help identify which VPU includes a user's area of interest. The other GIS data sets should be
downloaded based on the VPU of interest and are downloaded as an entire VPU.

---

## Available Metadata

The V2 streams have the following attributes, which come from the TauDEM delineation process. For more explanation of these attributes, please
check [here](https://hydrology.usu.edu/taudem/taudem5/help53/StreamReachAndWatershed.html).

*For modified features, this value was not recomputed and should not be trusted.*

- **LINKNO** - A river ID number unique to the TDXHydro delineation. In TDXHydro v1, this is not globally unique. In future versions, this will be the
  same as geoglowsID.
- **DSLINKNO** - The ID of the river immediately downstream of the segment represented on that row.
- **strmOrder** - The Strahler stream order.*
- **USContArea** - The total drainage area upstream of the most upstream point (i.e., the inlet) of this segment.*
- **DSContArea** - The total drainage area upstream of the most downstream point (i.e., the outlet) of this segment.
- **LengthGeodesucMaters** - Geodesic length in meters of the river segment.

V2 streams also have the following additional attributes added by the GEOGLOWS modelers:

- **TDXHydroRegion** - The original TDX regional group number of which this stream is part.
- **TopologicalOrder** - The topological order of a stream, from headwater to outlet.
- **Musk_k** - The Muskingum k parameter.
- **Musk_x** - The Muskingum x parameter.
- **TerminalNode** - This number is the TDXHydroLinkNo of the eventual outlet of this stream's watershed.
- **VPUCode** - A three-digit number representing which VPU region this stream belongs to.
