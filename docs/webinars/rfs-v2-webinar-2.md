---
webinar:
  title: "2. GEOGLOWS Model Formulation"
  date: "23 September 2025"
  youtube_id: "jw1CNAMhQ6A"
  video_width_max: "720"
  presenter: "Dr. Riley Hales"

  description: "Riley Hales presented an overview of the River Forecast System (RFS) model version two, explaining its inputs from ECMWF and NGA via TDX hydro, and its processing to determine water flow, which is then sent to AWS and Esri. He detailed enhancements in stream and catchment data derived from TDX hydro, improving accuracy and reducing stream count for efficiency, and clarified the meteorological and land surface model details, including data from ECMWF and runoff calculations. Michael Souffront and Riley Hales discussed future improvements, such as handling water movement through lakes and reservoir operations, and Riley Hales clarified that ERA5 precipitation data is available directly from the Copernicus Data Store (CDS)."

  about_the_author: "**Riley Hales** is a researcher in hydrology and river hydraulics emphasizing in numerical modeling. His research focuses on building large numerical models in hydraulics and hydrology; both physical, and statistical or machine learning models. His areas of expertise includes hydrology, hydraulics, machine learning, remote sensing, high performance computing, geographic information systems, web development, and decision support tools. He received his doctoral degree in Civil Engineering from Brigham Young University. Dr Hales is the Technical Director of GEOGLOWS where he has built two generations of the River Forecast System, a global hydrologic model providing forecast and hindcast river discharge predictions at 7 million river reaches worldwide. RFS data services around 40 million annual data downloads, or averaging over 100k per day. He has provided hydrologic capacity building and training in more than a dozen countries in Central and South America, Africa, the Middle East, and South Asia. RFS data is used by the local water and disaster management agencies in these countries use for many applications including flood preparation, early warning systems, agricultural planning, water quality monitoring, and training data for machine learning workflows."
---

# {{ webinar.title }}

**Presenter:** {{ webinar.presenter }}  
**Date:** {{ webinar.date }}

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: {{ webinar.video_width_max }}px; margin: 0 auto;">
  <iframe
    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
    src="https://www.youtube-nocookie.com/embed/{{ webinar.youtube_id }}?controls=1&start=0"
    title="{{ webinar.title }}"
    frameborder="0"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
    referrerpolicy="strict-origin-when-cross-origin" 
    allowfullscreen>
  </iframe>
</div>

## **Description:**

{{ webinar.description }}

## **About the Author**

{{ webinar.about_the_author }}
