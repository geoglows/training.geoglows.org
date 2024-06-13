# Validating Flood Events 

This part of the workshop will show you how to validate the 
GEOGloWS ECMWF Streamflow Services short-term forecast in any 
flood event in any place in the world. You will compare observed 
data with simulated forecasts for a flood event to see how well 
the forecast performs.

Example data is provided to complete this workshop. If you would like to perform 
the validation for a different flood event, you will need:

The set of reach_ids which you want to use for the analysis.

The observed streamflow during the flood event corresponding to the set of reach_ids.

The record of forecasts starting at least 15 days before the flood event 
(the length of one forecast) to at least a couple of days after the event was finished.

Optional: The historical observed streamflow corresponding to the set of reach_ids.

## Step 1: Get Forecast Record
The first step is getting the record of forecasts after a flood event has occurred.

This [Google Colab notebook][1] will allow you to download the forecast data.
[1]: https://colab.research.google.com/drive/1y2eVRJpfcdISB25U0lCBZ7z6up14wswg

After running this notebook, you will find a folder in your Google Drive called ‘Forecast_Validation’ 
containing a folder for each of the reach_ids that you used. Within these folders is a file with the forecast 
for each day that a forecast was available.

For the example followed in this tutorial, you will need to use the forecast data available here:
#these links do not work:)

## Step 2: Compare Observed Data with Forecasts

## Step 3: Reorganizing the Forecast Data

## Step 4: Comparing Days-in-Advance Forecasts with Observed Data


#most of this information is taken from https://training.geoglows.org/en/latest/content/streamflow-model/forecast-skill-evaluation.html#