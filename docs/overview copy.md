# What is GEOGLOWS? 

![image](image3.png)

## Overview
The GEOGLOWS (Global Earth Observations Global Water Sustainability) 
initiative is a collaborative effort aimed at improving global 
water sustainability through advanced hydrological forecasting 
and data analysis. Leveraging the power of Earth observations, 
numerical weather predictions, and supercomputing, GEOGLOWS 
provides actionable information through our hydrologic model, the River Forecast System (RFS). RFS provides streamflow status and 
outlook for every river worldwide. By making decades of 
historical climatological flow data and future forecasts 
easily accessible, RFS supports informed decision-making
in water resource management, disaster risk reduction, and 
climate adaptation. This global service enables countries 
and organizations to enhance their understanding of 
water-related challenges and implement effective solutions, 
ultimately contributing to a more sustainable and 
resilient future.

## History
The GEOGLOWS initiative, established under the framework
of the Group on Earth Observations (GEO), has its roots 
in a commitment to integrate Earth observation data to 
enhance global water sustainability. The journey began 
in 2014 at the GEO Plenary in Geneva, where the need for 
coordinated water data management became evident. With 
support from partners such as NASA, ECMWF, and regional 
organizations, GEOGLOWS evolved from early efforts in the 
Dominican Republic to a broader application of global 
hydrological modeling. By leveraging advanced technologies, 
including the ECMWF’s global weather forecasts and cutting-edge
cloud computing, GEOGLOWS pioneered global streamflow 
forecasting services in the creation of the model that is now known as RFS. These services provide critical 
information to support decision-making in water management,
helping to mitigate the impacts of floods, droughts, and
other water-related challenges. Over time, the initiative
has expanded its reach, integrating local and regional 
hydrological insights, and fostering collaborations 
across continents to address the complex issues of 
water scarcity and disaster preparedness.

## Model Formulation
The GEOGLOWS model leverages the Hydrology Tiled ECMWF Scheme for Surface Exchanges over Land (HTESSEL) alongside the ECMWF Integrated Forecast System (IFS) to conduct detailed calculations of water and energy balances within grid cells. HTESSEL simulates how land surfaces respond to atmospheric conditions, estimating critical variables such as surface and sub-surface runoff for both operational ensemble forecasts and retrospective simulations. The model employs varying spatial resolutions for its runoff files, including approximately 25 km for historical ERA-5 data, 16 km for low-resolution ensemble members, and 8 km for high-resolution forecasts. By intersecting grid lines with specific basins and applying runoff depth values, the model calculates water volumes over different time periods, which are then routed through the stream network using the Muskingum method with the RAPID algorithm. This approach provides valuable discharge data for hydrological analysis and decision-making.

## River Forecast System Training
To learn more about our model, RFS, continue with out training under the River Forecast System portion of this website. This training is broken down into 3 main sections, each having different sub sections within them. We recommend you start with the first section (Available Data) before progressing to the second section (Accessing Data). The third section (Skills and Examples) is a more advanced section designed for people looking to complete specific tasks using the RFS data who already have a good understanding of the first two sections. As you are learning about the data, there is also a website available with more information on how to download and use the RFS data: https://data.geoglows.org/. This is a great resource once you have a basic understanding of the data. Here is a brief overview of what you can expect to learn: 
 
1. **Available Data** - This section details the available datasets from RFS. It is divided into 3 sections:  
    - **a. GIS Data** - Learn about the hydrography data used in the RFS, including stream centerlines, catchment boundaries, and their unique identifiers, derived from high-resolution elevation products.  
    - **b. Retrospective River Discharge** - Explore over 85 years of daily average streamflow data, derived from meteorological reanalysis and updated weekly, offering insights into historical river discharge.  
    - **c. Forecast River Discharge** - Understand daily river flow forecasts with a 51-member ensemble providing detailed predictions at 3-hour intervals, including uncertainty ranges for better planning.  

2. **Accessing Data** - This section explains how the previously described data can be accessed and downloaded using 4 different techniques. Each section will detail a different technique:  
    - **a. A Data Catalog** - This section explains the data catalog available through AWS buckets.  
    - **b. A Data Service** - This section describes how to use our REST API to access GEOGLOWS data.  
    - **c. A Web Map** - This section explains the Esri Living Atlas map layer that can be loaded into any GIS software (ArcGIS or QGIS).  
    - **d. A Web App** - This section introduces you to the HydroViewer, which is our web application that allows for easy visualization and download of data globally.  

3. **Skills and Examples** - This section explains more advanced techniques that can be used when using the data for specific purposes.  
    - **a. Accessing and Interpreting Data** - This section includes Google Colab notebooks that show you how to use the GEOGLOWS Python package to make and customize your streamflow plots.  
    - **b. Bias Correction and SABER Overview** - This section gives a brief overview of bias correction and a technique called SABER that applies bias correction to other areas.  
    - **c. Bias Correction for Forecast Data** - This section provides a notebook that goes through examples of bias-correcting the forecast data.  


## Stories of Application

GEOGLOWS has been instrumental in transforming water management 
and disaster response across the globe. From helping predict 
floods and droughts in Nepal, to improving transboundary flow 
forecasts in Bangladesh, GEOGLOWS empowers local agencies with 
the tools to make life-saving decisions. In the Dominican Republic, 
GEOGLOWS enhances capacity for hydrological challenges, including 
flood risk and irrigation management. The service has extended 
early warning lead times in Malawi and has been crucial in 
managing reservoir releases during hurricanes in Honduras. 
These real-world applications demonstrate the global impact 
of GEOGLOWS in addressing critical water-related challenges. 
For more in-depth stories of how GEOGLOWS is making a difference 
worldwide, visit [GEOGLOWS Stories](https://stories.geoglows.org/home).

## Joining GEOGLOWS
Are you interested in being part of the global GEOGLOWS community? 
By joining, you can stay updated with the latest developments, collaborate 
with experts, and access valuable resources related to hydrological forecasting 
and water sustainability.

To join the GEOGLOWS network, simply sign up for our Google Group:
[Join the group!](https://groups.google.com/g/geoglows)

By becoming a member, you will be part of a growing community 
focused on advancing global water sustainability and streamflow forecasting.

