# Descripción General de GRACE Regional Analyst

## Qué hace la aplicación { #what-the-app-does }

GRACE Regional Analyst sigue cómo ha cambiado el almacenamiento de agua subterránea desde 2002 en cualquier región del mundo. Reporta una
anomalía de almacenamiento de agua subterránea: cuánta agua más o menos hay almacenada bajo tierra en un mes dado respecto al promedio de
2004–2009, expresada como una lámina de agua líquida en centímetros.

Llega a ese número por dos caminos distintos, y lleva los dos.

**GRACE + GLDAS 2.1** parte de la columna total de agua pesada por los satélites GRACE y GRACE Follow-On de la NASA y resta la nieve, el agua
del dosel y la humedad del suelo estimadas por tres modelos de superficie terrestre. Lo que queda es el agua subterránea. El registro empieza en
abril de 2002, y la parte que más importa —el cambio de almacenamiento mismo— está medida y no modelada.

**GLDAS 2.2** lee el agua subterránea de un solo modelo de superficie terrestre, el modelo Catchment de la NASA, que lleva el agua subterránea
como un estado propio y se corrige cada mes asimilando GRACE. El registro empieza en febrero de 2003, no le falta ningún mes y se ofrece a 0.25°
dentro de una región, cuatro veces más fino en cada dirección que el otro conjunto de datos, que es lo que hace manejables las cuencas más
pequeñas.

Ninguno de los dos es la respuesta correcta en todas partes, y discrepan de maneras informativas, así que la aplicación dibuja los dos en un
mismo gráfico. [Cálculo del Almacenamiento de Agua Subterránea](gldas/deriving-groundwater.md) da los dos cálculos completos y dice dónde vale
la pena confiar en cada uno.

La mayoría de los acuíferos tienen muy pocos pozos de monitoreo, o pozos con demasiados vacíos, como para afirmar con confianza si el
almacenamiento está subiendo o bajando en todo el sistema. GRACE observa todos los acuíferos de la Tierra, cada mes, con el mismo instrumento. Su
resolución es gruesa, de unos 300 km, por lo que es adecuado para acuíferos, cuencas y países y no para campos de pozos individuales, pero a esa
escala ofrece un registro consistente del cambio de almacenamiento donde hay poca información más.

![GRACE Regional Analyst, vista regional del Sistema Acuífero Iullemeden-Irhazer](../static/images/grace/app-region.webp)

La aplicación es gratuita y funciona en un navegador web en
[apps.geoglows.org/grace-anomalies](https://apps.geoglows.org/grace-anomalies){:target="_blank"}. Con ella puedes:

- cambiar entre los dos conjuntos de datos, o dibujar los dos en el mismo gráfico para compararlos
- animar mapas mensuales de anomalías de agua subterránea, agua total, humedad del suelo, nieve y agua en el dosel vegetal para todo el planeta
- elegir un acuífero o una cuenca hidrográfica de uno de cinco conjuntos de regiones publicados, subir tu propio límite en GeoJSON o dibujarlo en el mapa
- graficar la serie temporal promediada sobre el área de esa región, con su banda de incertidumbre cuando el conjunto de datos tiene una, y comparar los componentes del almacenamiento
- clasificar regiones o celdas de la malla según la tendencia del almacenamiento en los últimos 5, 10, 15 o 20 años, o en todo el registro
- rellenar los meses que le faltan a GRACE con un modelo estacional ajustado al registro propio de la región
- estimar la recarga anual de agua subterránea con el método de fluctuación del nivel freático
- descargar los valores mensuales de cualquier región o celda como archivo CSV para tu propio análisis

## Qué cubre esta capacitación { #what-this-training-covers }

**La Parte 1, La Misión GRACE,** trata de la medición: qué es, hasta dónde se la puede llevar y dónde tiene huecos:

- [Cómo GRACE Mide el Almacenamiento de Agua](mission/measuring-water-storage.md): cómo dos satélites miden los cambios en la gravedad de la
  Tierra y qué es una anomalía mensual de almacenamiento de agua.
- [Resolución, Fuga de Señal y Regiones Pequeñas](mission/resolution-and-leakage.md): qué puede y qué no puede resolver GRACE, y cómo trabajar
  con regiones más pequeñas que su huella.
- [Vacíos y Relleno de Vacíos](mission/gap-filling.md): los 35 meses que le faltan al registro, las opciones de la aplicación y el modelo
  estacional detrás del relleno **Seasonal model**: cómo se ajusta, cómo se calculan los valores rellenados y qué tan precisos son.

**La Parte 2, GLDAS,** trata de los modelos, que aportan todo lo que hay en la aplicación que no sea una medición de gravedad:

- [Los Modelos de Superficie Terrestre GLDAS](gldas/land-surface-models.md): qué es GLDAS, qué calcula un modelo de superficie terrestre, los
  tres modelos detrás del conjunto 2.1 y qué cambia la asimilación de GRACE en 2.2.
- [Cálculo del Almacenamiento de Agua Subterránea](gldas/deriving-groundwater.md): las dos rutas hacia el agua subterránea, los factores de
  ganancia aplicados a los datos de GRACE y cómo se estima la incertidumbre.

**La Parte 3, Uso de la Aplicación,** recorre la interfaz: [la disposición](app/interface.md), [la vista regional](app/regional-view.md),
[la vista global](app/global-view.md), [el análisis de tendencias](app/trends.md) y [la descarga de datos](app/downloading-data.md).

**La Parte 4, Análisis de Recarga,** estima la recarga anual de agua subterránea con el método de fluctuación del nivel freático:
[el método](recharge/wtf-method.md) aplicado a datos de GRACE, luego [la apertura del análisis](recharge/opening.md) y la revisión de la
serie, [los años hidrológicos y la selección de puntos](recharge/picks.md), y [los resultados](recharge/results.md).

**La Parte 5, Casos de Estudio,** resume tres estudios publicados por el equipo de Brigham Young University que desarrolló la aplicación y su
predecesora, la GRACE Groundwater Subsetting Tool (GGST). Cada uno combina el balance hídrico de GRACE y GLDAS de la aplicación con otros datos:
[la estimación de la recarga en Níger](case-studies/niger.md), donde los pozos son escasos, [la consideración de un gran embalse en la Cuenca
del Volta](case-studies/volta.md), y [la corrección de la fuga de señal en el Valle Central de California](case-studies/central-valley.md),
un valle angosto con bombeo intenso.

## Historia { #history }

GRACE Regional Analyst reemplaza a la GRACE Groundwater Subsetting Tool (GGST), una aplicación de Tethys Platform desarrollada en Brigham Young
University dentro del proyecto NASA SERVIR West Africa (2019–2023) y usada en talleres de capacitación en África Occidental, Jordania y Palestina.
La nueva aplicación conserva el método de GGST para separar el agua subterránea del almacenamiento total de agua y añade la clasificación de
tendencias, límites publicados de acuíferos y cuencas, regiones dibujadas por el usuario, el análisis de recarga y el conjunto de datos GLDAS 2.2
junto al anterior. Funciona completamente en el navegador, leyendo los datos procesados directamente desde el almacenamiento en la nube, así que
no necesitas cuenta ni inicio de sesión.

## Lecturas adicionales { #further-reading }

Estos artículos establecieron a GRACE como herramienta para monitorear el almacenamiento de agua subterránea en grandes acuíferos:

- Rodell, M., Velicogna, I., and Famiglietti, J. S. (2009). Satellite-based estimates of groundwater depletion in India. *Nature*, 460,
  999–1002. [doi:10.1038/nature08238](https://doi.org/10.1038/nature08238){:target="_blank"}
- Famiglietti, J. S., et al. (2011). Satellites measure recent rates of groundwater depletion in California's Central Valley. *Geophysical
  Research Letters*, 38, L03403. [doi:10.1029/2010GL046442](https://doi.org/10.1029/2010GL046442){:target="_blank"}
- Famiglietti, J. S. (2014). The global groundwater crisis. *Nature Climate Change*, 4, 945–948.
  [doi:10.1038/nclimate2425](https://doi.org/10.1038/nclimate2425){:target="_blank"}
- Thomas, A. C., Reager, J. T., Famiglietti, J. S., and Rodell, M. (2014). A GRACE-based water storage deficit approach for hydrological
  drought characterization. *Geophysical Research Letters*, 41, 1537–1545.
  [doi:10.1002/2014GL059323](https://doi.org/10.1002/2014GL059323){:target="_blank"}
