# Retrospective Data & Validation

## Retrospective Data

![image4](image4.png)

The retrospective simulation in the GEOGLOWS Model is a deterministic 
dataset with daily resolution, providing historical streamflow data. 
Version 1 of the model covers the period from 1979 to the present, while
Version 2 extends the dataset back to 1940, offering over 84 years of 
historical data. This simulation is based on the ERA5 reanalysis, which 
is updated weekly, ensuring that the lag between real-time and historical 
data remains minimal. The retrospective data is essential for calculating 
return periods, understanding long-term hydrological trends, and placing 
current streamflow forecasts in a historical context.

[Retrospective Data](https://drive.google.com/file/d/147febiNAZhg0XSrFSwjBfKPvO8FLEBdo/view?usp=sharing)

## Return periods, flow duration curves, daily/monthly/annual average flows
In hydrological analysis, return periods are used to estimate the probability of 
extreme events like floods. While the Weibull Distribution is often used to 
calculate return periods based on historical data, it is limited by the length 
of the data series and cannot predict events beyond the observed records. For 
the GEOGLOWS Model, the Gumbel Distribution is applied instead, as it better 
models extreme values and allows for extrapolation, making it possible to 
calculate return periods for events beyond the available data. Additionally, 
Flow Duration Curves (FDCs) are used to represent the percentage of time that 
streamflow is likely to equal or exceed certain flow rates, providing insights 
into the variability of water resources. The model also includes the analysis of
daily seasonality to understand patterns of streamflow throughout the year, 
monthly seasonality to observe changes between months, and annual mean 
discharge to detect long-term trends. These analyses are critical for effective
water resource management, flood forecasting, and understanding hydrological patterns.

[Return Periods](https://drive.google.com/file/d/1skirRgypzaD_6P-sZ2IDZ3tYPEXWaZr1/view?usp=sharing)

To further explore the analysis of return periods, flow duration curves, 
and seasonal averages, we invite you to follow along with our interactive 
demonstration in the provided Google Colab notebook. This hands-on notebook 
will guide you through the process, using real data from the Wabi Uetmal River 
in Ethiopia. You can access and run the notebook directly in your browser:

[Retrospective Demonstration Notebook](https://colab.research.google.com/drive/1zYcKoCN_Ljc1znBP87FthZ1uIeDDGazc?usp=sharing)

## Observed Data- Hydroserver

We have collected observed discharge data from gauging stations worldwide, 
spanning diverse hydrological environments across 113 countries. This data 
was sourced through a combination of projects, including NASA GEOGLOWS, 
NASA SERVIR (SERVIR-Hindu Kush Himalaya, SERVIR-Mekong, and SERVIR-Amazonia), 
and the Global Runoff Data Centre (GRDC), along with direct contributions from 
national water resource agencies such as IDEAM (Colombia), ANA (Brazil), INAMHI 
(Ecuador), SENAMHI (Peru), INAMEH (Venezuela), INDRHI (Dominican Republic), BOM 
(Australia), WSC (Canada), and USGS (United States), among others. Each gauging 
station is accompanied by metadata, including Station ID, Station Name, Latitude, 
Longitude, and, in some cases, Stream Name. The station network is connected to 
the stream network through a Reach ID, assigned based on the station's proximity 
to the stream. The data is stored and managed using HydroServer, a platform built 
on the Hydrologic Information System (HIS) for collecting, managing, and sharing 
hydrological time series data. The observed data is accessible via [HydroServer](https://hydroserver.geoglows.org/).

[Hydroserver Presentation](https://drive.google.com/file/d/13QBqi0RuFJqRXi-I25_hEm3RsbOIZFSX/view?usp=sharing)

## Validation Exercises and Results
To validate the GEOGLOWS Model, we selected gauging stations that are connected 
to the GEOGLOWS Model stream network and meet specific criteria. These criteria 
include stations paired with a GEOGLOWS reach ID, stations with at least one year 
of data, and stations with records available after January 1, 1979, which aligns 
with the start date of version 1 of the model. With the release of version 2, 
which extends the retrospective simulation back to January 1, 1940, we are now 
able to include a larger set of stations for validation. The performance of the 
GEOGLOWS retrospective simulation is assessed using the Kling-Gupta Efficiency 
(KGE) metric, which decomposes into three components: bias, variability, and 
correlation. This validation process ensures that the model's simulations are 
consistent with observed streamflow data, providing reliable information for 
water resource management and hydrological studies.

![image](img11.png)


