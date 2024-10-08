# Forecast Data

## Ensembles

## Statistics
## Initialization
## Bias Correction from Historical Data
## Validation


This part of the workshop will show you how to validate the 
GEOGloWS ECMWF Streamflow Services short-term forecast in any 
flood event in any place in the world. You will compare observed 
data with simulated forecasts for a flood event to see how well 
the forecast performs.

Example data is provided to complete this workshop. If you would like to perform 
the validation for a different flood event, you will need:

* The set of reach_ids which you want to use for the analysis.

* The observed streamflow during the flood event corresponding to the set of reach_ids.

* The record of forecasts starting at least 15 days before the flood event 
(the length of one forecast) to at least a couple of days after the event was finished.

* Optional: The historical observed streamflow corresponding to the set of reach_ids.

## Step 1: Get Forecast Record
The first step is getting the record of forecasts after a flood event has occurred.

This [Google Colab notebook][4] will allow you to download the forecast data.

[4]: https://colab.research.google.com/drive/1y2eVRJpfcdISB25U0lCBZ7z6up14wswg

After running this notebook, you will find a folder in your Google Drive called ‘Forecast_Validation’ 
containing a folder for each of the reach_ids that you used. Within these folders is a file with the forecast 
for each day that a forecast was available.

For the example followed in this tutorial, you will need to use the forecast data available here:
<!--these links do not work:)-->

## Step 2: Compare Observed Data with Forecasts

The second step in validating the performance of the GESS forecast during flood events is comparing the observed values with the original forecast datasets. First, you will need to save the observed streamflow data for the high flow event of interest to your Google Drive in the correct format. All of the observed data should be in the folder on your Google Drive called ‘Forecast_Validation/Country/’ (for this example the country is Honduras, so it would be ‘Forecast_Validation/Honduras/’). The observed data file for each station should be named in this format: ‘{station name}_RT_Q_orig.csv’

The observed data files should be in the same format as the example file below. The left column should contain the datetime (format: yyyy-mm-dd hh:mm:ss) with the column header “Datetime.” The right column should contain streamflow with units of m3/s and the column header “Streamflow (m3/s).”

In this example we are following the GEOGloWS ECMWF Streamflow Services (GESS) Forecast Validation for the Eta and Iota Hurricanes in the stations HDRPV-Jicaro (951603) and HDRPV-Maragua (951795) in Honduras. The data needed for the example is available here:

The following Colab notebook will help to plot the original forecast launched every day and the observed data for the same datasets. The Colab notebook is available here: https://colab.research.google.com/drive/1VMs50wKE55TBn8tWTimc69s1rNaom8SI
## Step 3: Reorganizing the Forecast Data

The third step is reorganizing the forecast as a function of days-in-advance. This will help us understand how far in advance the GEOGloWS ECMWF Streamflow Services forecasts accurately predict flow. Tables 1 and 2 illustrate how the data will be reorganized. After reorganizing the data, we can create visuals and compute metrics that show how accurate the forecasts are 1 day in advance, 2 days in advance, 3 days in advance, etc.

## Step 4: Comparing Days-in-Advance Forecasts with Observed Data

![image](screenshot.png)

<!--most of this information is taken from https://training.geoglows.org/en/latest/content/streamflow-model/forecast-skill-evaluation.html#-->