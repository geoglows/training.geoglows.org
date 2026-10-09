# Vista Regional

## La página de inicio { #the-landing-page }

La aplicación abre en la vista regional, que muestra los contornos de todas las regiones del conjunto de regiones activo. El conjunto
predeterminado es Global Aquifers. Cada contorno se colorea según la tendencia del almacenamiento de agua subterránea en los últimos cinco años, y
la leyenda en la esquina superior derecha cuenta las regiones de cada clase de tendencia (ver [Análisis de Tendencias](trends.md)). Haz clic en
**Hide trends** para mostrar solo los contornos.

![La vista regional al abrirse, con el conjunto Global Aquifers clasificado por la tendencia del almacenamiento de agua subterránea](../../static/images/grace/app-home.webp)

Desde aquí puedes:

- desplazar y acercar el mapa; los nombres de las regiones aparecen al acercarte lo suficiente (desactívalos con **Show region names**)
- cambiar a otro conjunto de regiones, o filtrar la lista de nombres, en la sección **Regions** del panel de control
- cambiar la **Displayed layer** o la **Window** de tendencia para reclasificar todas las regiones a la vez, por ejemplo para ver qué acuíferos
  han perdido almacenamiento total de agua en los últimos 20 años
- abrir una región para analizarla, como se describe a continuación

En esta página, la ruta de navegación del encabezado dice **Home**. Después de abrir una región, haz clic en **Home** o en el botón **Regions**
para volver.

## Elegir una región { #choosing-a-region }

Hay tres formas de abrir una región para analizarla:

1. Haz clic en su contorno en el mapa, o en su nombre en la lista del panel de control.
2. Sube un límite desde un archivo GeoJSON.
3. Dibuja un polígono en el mapa.

### Conjuntos de regiones predefinidos { #preset-region-sets }

Elige un conjunto en la lista desplegable bajo **Regions**. Escribe en **Filter regions…** para acotar la lista.

| Conjunto de regiones | Regiones | Fuente |
|---|---|---|
| Global Aquifers | 99 | Compilado por el equipo de GEOGLOWS a partir de varias fuentes, con los vacíos completados con los conjuntos de WHYMAP e IGRAC de abajo |
| Large Aquifer Systems (WHYMAP) | 37 | Large Aquifer Systems of the World, WHYMAP (BGR/UNESCO) |
| Transboundary Aquifers (IGRAC) | 155 | Transboundary Aquifers of the World 2025, UNESCO-IHP / IGRAC (CC BY-SA 3.0 IGO) |
| Principal Aquifers, USA (USGS) | 31 | Principal Aquifers of the United States, U.S. Geological Survey |
| Major River Basins (GRDC) | 456 | Major River Basins of the World, Global Runoff Data Centre (solo uso no comercial) |
| My Regions | las tuyas | Regiones que has subido |

La atribución del conjunto activo se muestra debajo de la lista. Cítala si publicas resultados basados en ese conjunto.

### Subir una región { #uploading-a-region }

Haz clic en **Upload**, elige o arrastra un archivo GeoJSON (`.geojson` o `.json`, de hasta 50 MB), dale un nombre a la región y haz clic en
**Analyze**.

![El cuadro de diálogo Upload Region](../../static/images/grace/app-upload.webp){ width="510" }

El archivo debe contener entidades Polygon o MultiPolygon en longitud y latitud WGS 84, que es el estándar de GeoJSON. Si tiene más de una
entidad, se fusionan en una sola región. Los huecos de los polígonos se ignoran.

!!! tip "Convertir un shapefile"
    La aplicación solo lee GeoJSON. Para convertir un shapefile, ábrelo en QGIS, haz clic derecho en la capa, elige
    **Export → Save Features As…**, fija el formato en GeoJSON y el SRC en EPSG:4326. [mapshaper.org](https://mapshaper.org){:target="_blank"}
    hace lo mismo en el navegador: importa juntos los archivos `.shp`, `.dbf` y `.prj` y exporta como GeoJSON. Simplificar primero un límite muy
    detallado reduce el tamaño del archivo sin cambiar el resultado, ya que las celdas de la malla miden 1°.

Las regiones subidas se guardan en **My Regions**, donde puedes volver a abrirlas o eliminarlas con la × junto al nombre. Se almacenan solo en tu
navegador: no se comparten con nadie y no aparecerán en otra computadora ni en otro navegador.

### Dibujar una región { #drawing-a-region }

Selecciona **My Regions** en la lista desplegable de conjuntos de regiones y luego haz clic en **Draw a polygon** en el mapa. Haz clic para
colocar cada vértice y doble clic para terminar. La aplicación analiza el polígono de inmediato. Los polígonos dibujados no se guardan; sube un
archivo si quieres conservar una región.

## Interpretar los resultados { #reading-the-results }

Cuando abres una región, el mapa se acerca a ella y muestra las celdas de anomalía de la capa mostrada dentro de su límite, y el gráfico muestra la
serie temporal promedio de la región (ver [El gráfico de series temporales](#the-time-series-chart)).

![Análisis regional de una región subida sobre Punjab y Haryana, India](../../static/images/grace/app-upload-result.webp)

### Qué celdas se promedian { #which-cells-are-averaged }

El promedio regional usa todas las celdas de la malla que tienen al menos el 35% de su área dentro de la región, y pondera cada una por el área de
superposición. Las celdas que quedan mayormente fuera de la región se excluyen; las celdas del borde cuentan en proporción a la parte que queda
dentro.

![Cómo promedia la aplicación las celdas sobre una región](../../static/images/grace/grace-region-averaging.png)

La TWSa se promedia en su malla de 0.5° y las demás capas en su malla de 1°, cada una con sus propios pesos de superposición. Una región más
pequeña que aproximadamente el 35% de una celda puede no tener ninguna celda que cumpla el criterio; usa una región más grande o haz clic en la
celda en la [vista global](global-view.md).

### Mostrar la malla { #showing-the-grid }

Activa **Show cell boundaries** y **Show mascon boundaries** para ver cómo se relaciona la región con la malla y con la resolución real de GRACE:

![Límites de celdas y de mascons sobre el Sistema Acuífero Iullemeden-Irhazer](../../static/images/grace/app-region-boundaries.webp)

Aquí la región abarca partes de varios mascons (en morado), así que su promedio se basa en varios valores independientes de GRACE. Una región
dentro de un solo mascon está sujeta a la [fuga de señal](../background/resolution-and-leakage.md) descrita en la sección de fundamentos.

## El gráfico de series temporales { #the-time-series-chart }

El gráfico debajo del mapa representa el promedio de la región para cada mes en cm de equivalente de agua líquida, con el cero (la media de
2004–2009) dibujado como una línea continua. Arrastra el divisor entre el mapa y el gráfico para darle más espacio al gráfico.

![Gráfico de series temporales de GWSa del Sistema Acuífero Northern Midwest, con los vacíos rellenados por el modelo estacional y la tendencia de 5 años](../../static/images/grace/app-recharge-button.webp)

Pasa el cursor sobre el gráfico para leer los valores de un mes. La línea roja discontinua marca el mes que se muestra en el mapa y se mueve a
medida que avanzas o reproduces el control de tiempo.

### Incertidumbre { #uncertainty }

Cuando se grafica un solo componente, una banda sombreada muestra ±1σ. La banda se promedia sobre las celdas igual que los valores, lo que trata
los errores de celdas vecinas como totalmente correlacionados. Es la opción prudente: errores que se cancelan en parte entre celdas darían una
banda más estrecha. La banda se oculta cuando se grafican varios componentes, para que el gráfico siga siendo legible.

### Comparar componentes { #comparing-components }

El gráfico siempre representa la **Displayed layer**. Marca otros componentes bajo **Time series** en el panel de control para añadirlos en los
mismos ejes:

| Componente | Fuente | Qué muestra |
|---|---|---|
| TWSa | GRACE | toda el agua de la columna: agua subterránea, humedad del suelo, nieve, dosel y agua superficial |
| GWSa | TWSa menos las tres capas de GLDAS | agua subterránea, con el agua superficial incluida |
| SMa | GLDAS | humedad del suelo |
| SWEa | GLDAS | equivalente de agua de la nieve |
| CANa | GLDAS | agua retenida en el dosel vegetal |

[Cálculo del Almacenamiento de Agua Subterránea](../background/deriving-groundwater.md) explica cómo encajan las capas entre sí.

![GWSa comparada con TWSa y SMa para el Sistema Acuífero Iullemeden-Irhazer](../../static/images/grace/app-chart-compare.webp)

Comparar componentes muestra qué impulsa la señal del agua subterránea. En el ejemplo de arriba, la humedad del suelo (verde) tiene un ciclo
estacional marcado pero ninguna tendencia de largo plazo, mientras que el almacenamiento total de agua (naranja) y el agua subterránea (azul)
suben juntos desde aproximadamente 2010, así que el aumento del almacenamiento total corresponde al agua subterránea.

### Relleno de vacíos { #gap-filling }

GRACE no tiene datos para 35 meses del registro, así que la TWSa y la GWSa tienen vacíos; las capas de GLDAS tienen un valor cada mes. El control
**Gap filling** define cómo dibuja el gráfico los vacíos:

- **None** corta la línea en cada vacío.
- **Straight line** une los meses a ambos lados de cada vacío.
- **Seasonal model** estima los meses faltantes a partir de una tendencia y un ciclo estacional ajustados al propio registro de la región, y los
  dibuja como una línea discontinua con marcadores huecos, como en el gráfico de arriba.

El ajuste solo cambia el gráfico. La Parte 3 compara las tres opciones en [Vacíos en el Registro](../gap-filling/gaps.md) y luego presenta el
método completo.

### Líneas de tendencia { #trend-lines }

Mientras las tendencias están activas (**Analyze trends** en el encabezado), cada componente graficado recibe su tendencia ajustada como una línea
discontinua sobre la ventana de tendencia, y la leyenda da su pendiente, por ejemplo "GWSa trend −0.29 cm/yr (last 5 yr)". Ver
[Análisis de Tendencias](trends.md).

### Análisis de recarga { #recharge-analysis }

Con **Seasonal model** seleccionado, aparece un botón **Recharge Analysis** encima del gráfico. Abre una página que estima la recarga anual de
agua subterránea a partir de la serie de GWSa rellenada con el método de fluctuación del nivel freático. El análisis siempre usa la GWSa,
cualquiera que sea la capa mostrada. La Parte 4 lo describe, comenzando con [El Método WTF](../recharge/wtf-method.md).

### Descargar los datos { #downloading-the-data }

**Download CSV** guarda los valores mensuales de los cinco componentes para la región, con sus límites de ±1σ y las series de TWSa y GWSa con los
vacíos rellenados, independientemente de qué componentes estén graficados y de qué opción de relleno esté seleccionada.
[Descarga de Datos](downloading-data.md) enumera las columnas y muestra cómo convertir los valores en volúmenes.
