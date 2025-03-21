# Forecast Bias Correction

RFS applies bias correction to its forecast data by assuming the forecast shares the same biases as the retrospective simulation. This process involves mapping forecasted streamflow values to a non-exceedance probability using the historical simulation's flow duration curve and then replacing the forecasted values with corresponding values from the observed flow duration curve.

![forecasts](../../static/images/forecast-bias-correction.png)

This method helps improve forecast accuracy, particularly during earlier forecast lead times, aligning the data more closely with historical observations. However, improvements are limited by the assumption that the biases in forecast data are identical to those in the retrospective simulation​. The following images show how the KGE values improved for the forecasted model after applying the bias correction techniques.

![kge](../../static/images/global_kge1.png)

![kge](../../static/images/global_kge2.png)

---

[Bias_Correction_Forecast_Data.pdf](https://drive.google.com/file/d/1CjsVCMkZjngEZt1k45dd4tgGTJREhi2D/view?usp=sharing)

This Colab notebook offers a step-by-step guide for performing bias correction on GEOGLOWS forecast values. It shows how to adjust forecasted streamflow values using historical observations, improving the accuracy of predictions and aligning the data with real-world measurements for better hydrological analysis:  
  
[Bias_Correction_GEOGloWS_ECMWF_Hydrological_Model_Forecast Colab.ipynb](https://colab.research.google.com/drive/1vXJNrCjef3G4KoCc1LlNm5T_mqLu20E_?usp=sharing)
