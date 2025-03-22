# Using the GEOGLOWS Hydroviewer

The GEOGLOWS Hydroviewer is a tool for visualizing and accessing streamflow forecasts and historical data across the globe. This web-based application
allows users to explore real-time streamflow conditions, analyze forecast trends, and review hydrological simulations for any river, helping
decision-makers and researchers better understand water-related challenges. With easy-to-use visualization tools, users can assess discharge values
and identify potential flood or drought risks. The HydroViewer supports informed decision-making in water resource management, disaster risk
reduction, and climate resilience planning. Access the app at [GEOGLOWS Hydroviewer](https://hydroviewer.geoglows.org/).

![Hydroviewer](../../static/images/hydroviewer.png)

## Stream Visualization

The Hydroviewer highlights streams where flows are expected to exceed return periods, using the following color-coded legend:

![Legend for Return Periods](../../static/images/river-legend.png)

This allows users to quickly identify rivers experiencing high flows.

**Map Features:**

1. **Zoom Levels**:
    - At the global level, only the largest streams are displayed.
    - As users zoom in, more streams become visible within their area of interest.
2. **Interactive River Selection**:
    - Clicking on a river displays retrospective and forecast data for that stream.
    - The river ID is shown for easy reference.
3. **Direct River ID Entry**:
    - If the river ID is known, users can directly enter it into the application to view the data.

Users can download **plots** and **.csv files** for streams of interest.

# Selecting Data

At the global level, only the largest streams are shown. More streams become visible as a user zooms in on the map and their area of interest. If you
are not accurate enough in your click, a warning will show asking you to zoom in more and be more precise when clicking the river segment.

Once you have selected the streams, a pop-up window will appear with the river name, ID, and two graphs: the forecasted and retrospective streamflow
data.

![loaded-datat](../../static/images/loaded-graph.png)

Plots and `.csv` files can be downloaded for streams of interest by selecting the camera icon in the corner of the plot.

## Previous Forecast Data

By default, when you click on a stream, the 15-day forecast from the current day will be displayed. However, if you would like, you can see a forecast
from a previous day by choosing a date from the date dropdown menu.

![calendar](../../static/images/calendar-forecast.png)

## Retrospective Data

By default, you will view 10 years of retrospective data, but this can be adjusted using the grey sliders at the bottom. The entire retrospective
dataset, dating back to 1940, can be accessed this way.

![Retrospective Data](../../static/images/retrospective-variable.png)

## Entering a River ID

If a user already knows the river ID for their stream of interest, they can directly enter the river ID into the application to view the data.

1. Get the chart pop-up window open either by selecting the chart icon in the upper right corner or by it being open from a previous river selection.
2. Click on **“Enter River ID”** in the top middle of the pop-up window.
3. Type in any river ID (for example, this reach ID is for the Magdalena River in Colombia: `610363879`) and click **“OK”**.
4. The forecast and retrospective data will reload and will be displayed for the new river in the pop-up window.

## Filtering Data

Data can also be filtered:

- Click on the **filter** button on the left-hand side to bring up the filtering options.
- There, you will find options to filter based on:
    - River country
    - VPU number
    - River outlet country

This will only show rivers that meet these criteria on the map.

![filter](../../static/images/filtered-streams.png)
