# Forecast Bias Correction

The **GEOGLOWS model** applies bias correction to its forecast data by assuming the forecast shares the same biases as the retrospective simulation. This process involves mapping forecasted streamflow values to a non-exceedance probability using the historical simulation's flow duration curve and then replacing the forecasted values with corresponding values from the observed flow duration curve.

![forecast_bias] (forecast-bias-correction.png)

This method helps improve forecast accuracy, particularly during earlier forecast lead times, aligning the data more closely with historical observations. However, improvements are limited by the assumption that the biases in forecast data are identical to those in the retrospective simulation​.

![kge](global_kge1.png)

![kge](global_kge2.png)

---

[02. Bias_Correction_Forecast_Data.pdf](https://drive.google.com/file/d/1CjsVCMkZjngEZt1k45dd4tgGTJREhi2D/view?usp=sharing)

This Colab notebook offers a step-by-step guide for performing bias correction on GEOGLOWS forecast values. It shows how to adjust forecasted streamflow values using historical observations, improving the accuracy of predictions and aligning the data with real-world measurements for better hydrological analysis: [02. Bias_Correction_GEOGloWS_ECMWF_Hydrological_Model_Forecast Colab.ipynb](https://colab.research.google.com/drive/1vXJNrCjef3G4KoCc1LlNm5T_mqLu20E_?usp=sharing)

---

## Validating an event after the fact

The **GEOGLOWS Global HydroViewer** is an essential tool for visualizing and accessing streamflow forecasts and historical data across the globe. This web-based application allows users to explore real-time streamflow conditions, analyze forecast trends, and review hydrological simulations for any river.
