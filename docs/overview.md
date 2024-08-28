# What is GEOGLOWS? 

![image](image3.png)

## Overview
The GEOGLOWS (Global Earth Observations Global Water Sustainability) initiative is a collaborative effort aimed at improving global water sustainability through advanced hydrological forecasting and data analysis. Leveraging the power of Earth observations, numerical weather predictions, and supercomputing, GEOGLOWS provides actionable information on streamflow status and outlook for every river worldwide. By making decades of historical climatological flow data and future forecasts easily accessible, GEOGLOWS supports informed decision-making in water resource management, disaster risk reduction, and climate adaptation. This global service enables countries and organizations to enhance their understanding of water-related challenges and implement effective solutions, ultimately contributing to a more sustainable and resilient future.

The presentation linked below provides deeper insights into the scope and impact of GEOGLOWS.

[GEOGLOWS V2 Overview](https://byu.sharepoint.com/:p:/r/sites/BYUHydroinformaticsLaboratory/Shared%20Documents/geoglows-training/GEOGLOWS%20Master%20Training%20Materials/What%20is%20GEOGLOWS/GEOGLOWS%20V2%20Overview%202024%20Updated.pptx?d=wc965db49aec247ac9ac4070e689c1078&csf=1&web=1&e=S3eqbe)

## History
The GEOGLOWS initiative, established under the framework of the Group on Earth Observations (GEO), has its roots in a commitment to integrate Earth observation data to enhance global water sustainability. The journey began in 2014 at the GEO Plenary in Geneva, where the need for coordinated water data management became evident. With support from partners such as NASA, ECMWF, and regional organizations, GEOGLOWS evolved from early efforts in the Dominican Republic to a broader application of global hydrological modeling. By leveraging advanced technologies, including the ECMWF’s global weather forecasts and cutting-edge cloud computing, GEOGLOWS pioneered global streamflow forecasting services. These services provide critical information to support decision-making in water management, helping to mitigate the impacts of floods, droughts, and other water-related challenges. Over time, the initiative has expanded its reach, integrating local and regional hydrological insights, and fostering collaborations across continents to address the complex issues of water scarcity and disaster preparedness.

The presentation below offers a deeper insight into the history and impact of GEOGLOWS.

[GEOGLOWS History](https://byu.sharepoint.com/:p:/r/sites/BYUHydroinformaticsLaboratory/Shared%20Documents/geoglows-training/GEOGLOWS%20Master%20Training%20Materials/What%20is%20GEOGLOWS/GEOGLOWS%20History%20Updated.pptx?d=wca370acd764f41b58c139a29a10f5044&csf=1&web=1&e=RKovEW)

## Model Formulation
The GEOGLOWS model leverages the Hydrology Tiled ECMWF Scheme for Surface Exchanges over Land (HTESSEL) alongside the ECMWF Integrated Forecast System (IFS) to conduct detailed calculations of water and energy balances within grid cells. HTESSEL simulates how land surfaces respond to atmospheric conditions, estimating critical variables such as surface and sub-surface runoff for both operational ensemble forecasts and retrospective simulations. The model employs varying spatial resolutions for its runoff files, including approximately 25 km for historical ERA-5 data, 16 km for low-resolution ensemble members, and 8 km for high-resolution forecasts. By intersecting grid lines with specific basins and applying runoff depth values, the model calculates water volumes over different time periods, which are then routed through the stream network using the Muskingum method with the RAPID algorithm. This approach provides valuable discharge data for hydrological analysis and decision-making.

The presentation below offers a deeper insight into the model formulation of the GEOGLOWS Model.

[Model Formulation](https://byu.sharepoint.com/:p:/r/sites/BYUHydroinformaticsLaboratory/Shared%20Documents/geoglows-training/GEOGLOWS%20Master%20Training%20Materials/What%20is%20GEOGLOWS/Model%20formulation_JLSL_updated.pptx?d=w6dfed72c2099467984d82899c77da881&csf=1&web=1&e=VGwJ9C)

## Understanding GEOGLOWS Data
* ### Hydrofabric
The GEOGLOWS ECMWF Streamflow Service leverages a Hydrologic Modeling as a Service (HMaaS) approach, centralizing cyberinfrastructure, expertise, and state-of-the-art forecasting capabilities to provide reliable streamflow data. Instead of requiring local agencies to manage and compute vast amounts of data independently, GEOGLOWS streamlines the process by using ensemble meteorological forecasts from ECMWF, processed through the HTESSEL land surface model. This generates global runoff data, which is mapped to GEOGLOWS watersheds and routed through river networks using the RAPID model to produce 15-day forecasts. Additionally, the ERA-5 retrospective historical data spanning over 80 years is used to derive return periods, placing current forecasts in a meaningful historical context. These streamflow forecasts are accessible via web mapping services and APIs, facilitating the development of customized applications tailored to address local water management challenges such as flooding, drought, and water security

* ### Map
The GEOGloWS ECMWF Streamflow Model can be easily explored using a mapping service developed in collaboration with Esri (see: https://hydroviewer.geoglows.org/). The web map allows users to visualize current streamflow conditions worldwide, with line thickness indicating discharge magnitude and line color showing if and when a river's discharge exceeds the threshold for a specific return period. The app also lets you select a specific stream to view both the forecast and historical simulation data for that river.

* ### Retrospective Data
* ### Forecasts

## Stories of Application

The presentation below outlines success stories wherein GEOGLOWS resources
have been employed effectively for the use of those in need. 

[Stories](https://byu.sharepoint.com/:p:/r/sites/BYUHydroinformaticsLaboratory/Shared%20Documents/geoglows-training/GEOGLOWS%20Master%20Training%20Materials/What%20is%20GEOGLOWS/GEOGloWS%20-%20Stories.pptx?d=web302a8f8f774b8caa227fe40c05d4c0&csf=1&web=1&e=kpz1f7) *this still needs to be updated to the correct format*


## Joining GEOGLOWS
Join the user group on Google Groups where you can get updates, ask the community, and stay connected!  
[Join the group!](https://groups.google.com/g/geoglows)

If you are a GEOGLOWS User, please take our survey here:

 * [English Survey](https://forms.gle/eZr1nARB5L2kvMGy9)
 * [Español Survey](https://forms.gle/gjUedjP74PVb368w5)
