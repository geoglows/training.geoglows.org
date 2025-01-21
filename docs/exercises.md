## Return periods, flow duration curves, and average flows

In hydrological analysis, return periods are used to estimate the probability of extreme events like floods. While the Weibull Distribution is often used to calculate return periods based on historical data, it is limited by the length of the data series and cannot predict events beyond the observed records. For the GEOGLOWS Model, the Gumbel Distribution is applied instead, as it better models extreme values and allows for extrapolation, making it possible to calculate return periods for events beyond the available data. 

Additionally, **Flow Duration Curves (FDCs)** are used to represent the percentage of time that streamflow is likely to equal or exceed certain flow rates, providing insights into the variability of water resources. The model also includes the analysis of daily seasonality to understand patterns of streamflow throughout the year, monthly seasonality to observe changes between months, and annual mean discharge to detect long-term trends. These analyses are critical for effective water resource management, flood forecasting, and understanding hydrological patterns. The following presentation gives more of a background on the return periods and flow duration curves. It shows the equations used in the GEOGLOWS Hydrologic Model to represent these things.

[Return_Periods-FDC-Average_Flows.pdf](https://drive.google.com/file/d/10Si933D0fxaUrJFmIJr-WdOyjOkm453m/view?usp=sharing)

To further explore the analysis of return periods, flow duration curves, and seasonal averages, we invite you to follow along with our interactive demonstration in the provided Google Colab notebook. This hands-on notebook will guide you through the process, using real data from the Tensift River in Morocco. You can access and run the notebook directly in your browser:  
  
 [Return_Periods-FDC-Average_Flows Colab.ipynb](https://colab.research.google.com/drive/1UngQNuvgQyzaj2fKDhHGWK4oATljaed-?usp=sharing)

---

## Interactive Learning
### Retrospective Data

To dive deeper into the analysis of retrospective data, return periods, flow duration curves, and seasonal averages, we have prepared an interactive Google Colab notebook. This notebook provides step-by-step guidance for conducting these analyses using real-world data from the San Juan River at Rancho La Trinidad in Costa Rica. It covers both retrospective data and statistical flow analysis, allowing you to engage with the data and methods discussed in this guide: [Retrospective Simulation Colab.ipynb](https://colab.research.google.com/drive/1P3yNvE1EoQ9U8emCsMkm18CSpKWahvc5?usp=sharing)

---

## Interactive Learning 
### Forecast Simulation

The Colab notebook provides an interactive guide on accessing and visualizing forecast data from the GEOGLOWS Model. It demonstrates how to retrieve streamflow forecasts, plot the data using Python libraries, and interpret key statistics for effective water resource management and planning: [Forecast Simulation Colab.ipynb](https://colab.research.google.com/drive/1C2-zkxGC7U280U2CRkSK2TbQD1nr2H1T?usp=drive_link)
