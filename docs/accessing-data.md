# Accessing Data

## Hydrofabric
The GEOGLOWS Hydrofabric is a critical component that defines 
the spatial structure of watersheds, streams, and river networks
within the GEOGLOWS ECMWF Streamflow Service. It serves as the 
foundational layer used to link global runoff data to individual 
watersheds, enabling accurate streamflow forecasts at a 
local scale. The Hydrofabric is developed through a process 
of delineating watersheds and sub-basins globally, integrating 
both natural and human-altered drainage patterns.

This dataset allows GEOGLOWS to model streamflow behavior 
across different regions and supports the accurate routing 
of water through rivers and streams. By leveraging the 
Hydrofabric, users can access high-resolution streamflow 
data mapped to specific basins, allowing for tailored analysis 
and decision-making. The Hydrofabric is publicly accessible 
and can be visualized using tools like the GEOGLOWS 
HydroViewer, making it easy for researchers, engineers, 
and decision-makers to explore and utilize the data for 
their respective needs.

[Hydrofabric Presentation](https://drive.google.com/file/d/1mu3TXV_t-My3jGV0wBFi-2oEcuJsWmwp/view?usp=drive_link)

## Hydroviewer App
The GEOGLOWS Global HydroViewer is an essential tool for 
visualizing and accessing streamflow forecasts and 
historical data across the globe. This web-based application 
allows users to explore real-time streamflow conditions, 
analyze forecast trends, and review hydrological 
simulations for any river, helping decision-makers 
and researchers better understand water-related challenges. 
With easy-to-use visualization tools, users can assess 
discharge values and identify potential flood or drought 
risks. The HydroViewer supports informed decision-making 
in water resource management, disaster risk reduction, 
and climate resilience planning. Access the app at 
GEOGLOWS HydroViewer.

![image](images/img6.png)

[Hydroviewer Tutorial](https://drive.google.com/file/d/1uuzKFHy520o2Hby5t91_geSMVEeKnKW5/view?usp=drive_link)


## Programmatic Access

The GEOGLOWS ECMWF Streamflow Service offers programmatic access to 
streamflow data through a REST API, making it easy for users to 
integrate global hydrological data into their applications. By 
using this API, developers and researchers can retrieve historical 
and forecasted streamflow data in CSV format, enabling custom analysis 
and visualization. The API provides access to streamflow forecasts for 
over 7 million river segments worldwide, based on the GEOGLOWS Version 
2 dataset derived from the TanDEM-X Hydro dataset. Users can find 
detailed instructions on how to retrieve data, including identifying 
river numbers, through comprehensive tutorials and the GEOGLOWS Python 
package. For more details and documentation, visit [GEOGLOWS API Documentation][1]

[Programmatic Access Presentation][2]
[Programmatic Access Colab][3] 


[1]: https://geoglows.ecmwf.int/documentation
[2]: https://byu.sharepoint.com/:p:/r/sites/BYUHydroinformaticsLaboratory/Shared%20Documents/geoglows-training/GEOGLOWS%20Master%20Training%20Materials/Accessing%20GEOGLOWS%20Data/Programmatic%20Access%202.0.pptx?d=wb82414d8ae2640f0bb2bcb790a966b6d&csf=1&web=1&e=06SVks
[3]: https://colab.research.google.com/drive/19PiUTU2noCvNGr6r-1i9cv0YMduTxATs?authuser=1


## Data Download Directly from AWS

![image5](image5.png)

The GEOGLOWS Hydrological Model Version 2 allows users to download 
global streamflow data directly from AWS, providing access to both 
retrospective simulation data and 15-day streamflow forecasts. These 
datasets are hosted in S3 buckets, optimized for time series analysis
and bulk downloads. The retrospective data, derived from the ERA5 
reanalysis, spans over 80 years, while the forecast data leverages 
ECMWF ensemble predictions to offer insights into future streamflow 
conditions. Users can easily access and analyze these data using Python
and Jupyter notebooks, with detailed tutorials available. To get started,
use the following Colab notebooks:

1. Access [GEOGLOWS retrospective simulation data from AWS S3](https://colab.research.google.com/drive/19f8n-YMqGxL_qcn3aw5yv4oYUFFlB8IK)
2. Access [GEOGLOWS river forecast data from AWS S3](https://colab.research.google.com/drive/1tOuybiHK3HuxwL0MHDhGRbU65-yaolGs)

These resources make it easy for researchers and developers to 
integrate GEOGLOWS data into their own applications and analyses.
