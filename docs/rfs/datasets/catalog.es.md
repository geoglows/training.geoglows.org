## Resumen

Existen tres tipos principales de conjuntos de datos fluviales proporcionados por el Sistema de Pronóstico de Ríos (River Forecast System). Todos estos datos están disponibles de forma gratuita.

1. **Hidrografía**: Datos GIS sobre las ubicaciones de ríos y cuencas hidrográficas en todo el mundo.
2. **Simulación retrospectiva**: Datos horarios de caudal desde enero de 1940.
3. **Pronósticos**: Pronósticos de caudal a 15 días generados cada día a la medianoche.

[River Forecast System v2](https://www.geoglows.org){:target="_blank"} © 2024 por [Dr. Riley Hales](https://hales.app){:target="_blank"} tiene licencia bajo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/){:target="_blank"}

## Tabla de conjuntos de datos

Todos los conjuntos de datos de RFS V2 son patrocinados por el Programa de Patrocinio de Datos Abiertos de AWS. Esto permite que los datos estén disponibles públicamente y sin costo. **No necesitas** una cuenta de AWS, tarjeta de crédito, ni un nombre de usuario o contraseña para utilizar este servicio. Lee más en el [Registro de Datos Abiertos](https://registry.opendata.aws/geoglows-v2/) y en el [Intercambio de Datos de AWS](https://aws.amazon.com/marketplace/pp/prodview-aboaljwcz64zs).

Los datos se almacenan en 2 buckets. El primero contiene archivos de configuración del modelo, datos GIS, simulaciones retrospectivas y otros datos que son esencialmente estáticos. El segundo bucket contiene los pronósticos diarios producidos por RFS.

- Pronósticos: [http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html](http://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html){:target="_blank"}
- GIS + Retro: [https://rfs-v2.s3-us-west-2.amazonaws.com/index.html](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html){:target="_blank"}

| Conjunto de Datos                        | Formato(s) de Archivo | URI y Ruta del Bucket                                                                                                                         | Región AWS |
|------------------------------------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------|
| Pronósticos Diarios                      | Zarr                   | [s3://geoglows-v2-forecasts/](https://geoglows-v2.s3-website-us-west-2.amazonaws.com/index.html){:target="_blank"}                          | us-west-2  |
| Hidrografía - VPUs                       | GeoPackage (sqlite)    | [s3://rfs-v2/hydrography/](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#hydrography/){:target="_blank"}                             | us-west-2  |
| Hidrografía - Global                     | GeoPackage (sqlite)    | [s3://rfs-v2/hydrography-global/](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#hydrography-global/){:target="_blank"}               | us-west-2  |
| Hidrografía - Tablas Suplementarias      | Parquet                | [s3://rfs-v2/tables/](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#tables/){:target="_blank"}                                       | us-west-2  |
| Retrospectivo - Promedio Horario         | Zarr                   | [s3://rfs-v2/retrospective/hourly.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}              | us-west-2  |
| Retrospectivo - Promedio Diario          | Zarr                   | [s3://rfs-v2/retrospective/daily.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}               | us-west-2  |
| Retrospectivo - Promedio Mensual         | Zarr                   | [s3://rfs-v2/retrospective/monthly-timeseries.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}  | us-west-2  |
| Retrospectivo - Promedio Anual           | Zarr                   | [s3://rfs-v2/retrospective/yearly-timeseries.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}   | us-west-2  |
| Retrospectivo - Máximos Anuales          | Zarr                   | [s3://rfs-v2/retrospective/yearly-maximums.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}     | us-west-2  |
| Retrospectivo - Periodos de Retorno      | Zarr                   | [s3://rfs-v2/retrospective/return-periods.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}      | us-west-2  |
| Retrospectivo - Curvas de Duración de Caudal | Zarr               | [s3://rfs-v2/retrospective/fdc.zarr](https://rfs-v2.s3-us-west-2.amazonaws.com/index.html#retrospective/){:target="_blank"}                | us-west-2  |

## Código y Referencias Técnicas

- Preparación de post-procesamiento TDX-Hydro para modelado hidrológico: [https://github.com/geoglows/tdxhydro-postprocessing](https://github.com/geoglows/tdxhydro-postprocessing){:target="_blank"}
- Scripts para el cálculo de pronósticos: [https://github.com/geoglows/geoglows_ecflow](https://github.com/geoglows/geoglows_ecflow){:target="_blank"}
- Scripts de actualización semanal retrospectiva: [https://github.com/geoglows/retrospective-update](https://github.com/geoglows/retrospective-update){:target="_blank"}
- Paquete de Python `river-route` para enrutamiento tipo Matrix Muskingum: [https://github.com/rileyhales/river-route](https://github.com/rileyhales/river-route){:target="_blank"}

## Descarga de datos desde la línea de comandos (recomendado)

La forma más rápida de descargar datos de RFS es utilizando la Interfaz de Línea de Comandos (CLI) de AWS. Si no estás familiarizado con la programación o herramientas de línea de comandos, por favor salta a la siguiente sección sobre cómo descargar datos con un navegador web.

Usar la CLI permite descargar datos más rápidamente que a través del navegador y es recomendable para descargar grandes volúmenes de datos. Consulta las instrucciones de AWS para descargar datos desde S3. Es posible que necesites agregar el parámetro `--no-sign-request` en tus comandos de copia o sincronización.

## Descarga de datos con un navegador web

La forma más simple de explorar los conjuntos de datos RFS V2 es mediante los sitios web que permiten navegar por los datos disponibles. Esta no es la forma más rápida. Para un mejor rendimiento al descargar datos, se recomienda usar las instrucciones de la línea de comandos.

RFS permite a los usuarios descargar datos de caudal global directamente desde AWS. Esto proporciona acceso tanto a los datos de simulación retrospectiva como a los pronósticos de caudal a 15 días. Estos conjuntos de datos se alojan en buckets de S3, optimizados para el análisis de series temporales y descargas masivas.

Los usuarios pueden acceder y analizar fácilmente estos datos usando **Python** y **Jupyter Notebooks**, con tutoriales detallados disponibles.

![Collab](../../static/images/image5.png)

Los siguientes notebooks de Google Colab demuestran cómo acceder a los datos desde el bucket de AWS usando Python:

- [Acceder a datos de simulación retrospectiva de RFS desde AWS S3](https://colab.research.google.com/drive/19f8n-YMqGxL_qcn3aw5yv4oYUFFlB8IK)
- [Acceder a datos de pronóstico fluvial de RFS desde AWS S3](https://colab.research.google.com/drive/1tOuybiHK3HuxwL0MHDhGRbU65-yaolGs)
