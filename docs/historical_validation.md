# Historical Validation

### Introduction
These historical validation workshops will showcase some of the validation work 
we have done in different pilot regions. More importantly, these workshops will guide 
you on how you can use your own local observations to evaluate the performance of 
the model for your rivers.

<!--the presentation linked here was no longer found!-->

[Historical Validation Google Colab Notebook][1]

[1]: https://colab.research.google.com/drive/14u9aMkf7_SnRdlmner5LdmG_ZfvrAGkL

The ERA-5 reanalysis precipitation data that have been bias corrected by the Global Precipitation Climatology Project (GPCP). It is converted into runoff using the HTESSEL model. After that, the runoff is resampled performing an area-weighted grid-to-vector downscaling for the runoff computation. The GEOGloWS ECMWF streamflow services (GESS) computes a cumulative runoff volume at each time step as an incremental contribution for each sub-basin. GESS then uses the routing application for parallel computation of discharge (RAPID) model to route these inputs through the stream network (Qiao et al., 2019; Snow et al., 2016). GESS uses the historic simulation to define the return periods and uses these return periods as thresholds for flood alerts (Sanchez Lozano et al., 2021).

Decision-makers are worried about the accuracy and uncertainty of hydrologic model outcomes. Results do not need to be perfect, but they need to be reliable and accurate enough to give decision-makers the confidence to use them. The model accuracy is typically evaluated by comparing simulation results to observed data.

Hydrostats is an open-source software package designed to support hydrologic model evaluation. It supports both visual analysis and error metrics calculation. Hydrostats contains tools for preprocessing data, visualizing data, calculating error metrics on observed and predicted time series, and forecast validation. The visual analysis contains different options such as, hydrographs, daily and monthly seasonality, scatter plots, histograms comparison, and quantile-quantile plots. For error metrics calculation, It contains over 70 error metrics, with many metrics specific to the field of hydrology (Roberts et al., 2018).

In this tutorial, we will show how to validate the GEOGloWS ECMWF Streamflow Service historical simulation using the HydroStats Tethys app.

## Obtain Data

## Open the Statistics Calculator App

## Visualization



<!--most of this information is taken from https://training.geoglows.org/en/latest/content/streamflow-model/historical-validation.html-->