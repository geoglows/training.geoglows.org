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

GEOGLOWS Data can be accessed through the use of an API at [this link][1]

![image](image2.png)

The following presentation outlines the process of using the web browser interface to access data, as well as briefly outlines the 
method of using the geoglows python package to do the same thing. 

[Programmatic Access][2]

This [Google Colab][3] notebook holds the code to access geoglows data. 


[1]: https://geoglows.ecmwf.int/documentation#/default/get_dates
[2]: https://byu.sharepoint.com/:p:/r/sites/BYUHydroinformaticsLaboratory/Shared%20Documents/geoglows-training/GEOGLOWS%20Master%20Training%20Materials/Accessing%20GEOGLOWS%20Data/Programmatic%20Access%202.0.pptx?d=wb82414d8ae2640f0bb2bcb790a966b6d&csf=1&web=1&e=06SVks
[3]: https://colab.research.google.com/drive/19PiUTU2noCvNGr6r-1i9cv0YMduTxATs?authuser=1


## Bulk Data Download

![image5](image5.png)

This Colab Notebook defines the process for downloading data from AWS.

[Forecast Data](https://colab.research.google.com/drive/1tOuybiHK3HuxwL0MHDhGRbU65-yaolGs?usp=sharing)

Most GEOGLOWS data can be downloaded from the web browser. Links to these datasets are given at the [Available Data](https://data.geoglows.org/available-data) page.

Go to [data.geoglows.org](data.geoglows.org) for instructions. 