# Esri Living Atlas Layer

Esri hosts an **ArcGIS Living Atlas of the World**. It includes maps, apps, and data layers which can help researchers easily access data. They host a GEOGLOWS layer as part of this program. This allows GEOGLOWS stream data to be loaded into ArcGIS or QGIS without needing to download the entire dataset. The image below shows the stream layer loaded into QGIS.

![screenshot](imagen.png)


The layer is an animation layer that shows the first 10 days of the 15-day GEOGLOWS forecast data. The streams are colored based on if they exceed a given return period and are therefore in high flow. 

Some things that a user can do with this layer:

- Forecast data can be viewed sequentially over time because of the slider incorporated in the app. A user can look at the streams in 3-hour windows. The color of the streams will change if the stream experiences high flow during this time.
- Features can be identified by clicking on the map. Preconfigured pop-ups will show that include river names from OpenStreetMap.

More information about the web map layer can be found here: [Esri Living Atlas GEOGLOWS Layer](https://www.arcgis.com/home/item.html?id=8f0573e0c0b9491dbeafde9c72ccf02b)
