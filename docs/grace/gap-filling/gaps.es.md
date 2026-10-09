# Vacíos en el Registro

## Meses faltantes { #missing-months }

Al registro de GRACE le faltan 35 meses: meses sueltos, la mayoría entre 2011 y 2017, y los 11 meses entre el fin de GRACE y el inicio
de GRACE-FO (consulta [La Misión GRACE](../background/grace-mission.md#the-record-and-its-gaps)). TWSa y GWSa tienen vacíos en esos
meses. Las capas de GLDAS (SMa, SWEa y CANa) provienen de modelos de superficie terrestre que se ejecutan todos los meses, así que no tienen vacíos.

El análisis de tendencias de la aplicación omite los meses faltantes. Los análisis que trabajan año por año necesitan un valor para cada mes. En el
[Análisis de Recarga](../recharge/wtf-method.md), por ejemplo, un mes faltante en un pico o un valle estacional cambia el resultado de ese año. La aplicación
estima los meses faltantes con un modelo estacional, siguiendo el enfoque de Barbosa et al. (2022). Esta página muestra las opciones de la aplicación, y
[El Modelo Estacional](seasonal-model.md) presenta el método: el modelo, cómo se ajusta, cómo se calculan los valores rellenados y qué tan precisos
son.

## El control Gap filling { #the-gap-filling-control }

El control **Gap filling** (relleno de vacíos) del panel define qué hace el gráfico en los meses faltantes:

![El control Gap filling en el panel de la aplicación](../../static/images/grace/app-gap-fill-control.webp){ width="310" }

- **None** corta la línea en cada vacío, para que veas exactamente qué meses se observaron.
- **Straight line** une los meses a ambos lados de cada vacío. Solo cubre el vacío en el gráfico y no estima nada.
- **Seasonal model** estima cada mes faltante a partir de una tendencia y un ciclo estacional ajustados a los meses observados. Los meses rellenados se dibujan
  con una línea discontinua y marcadores huecos, y al pasar el cursor sobre uno se muestra su valor. Esta opción también agrega el botón **Recharge Analysis** encima del
  gráfico (consulta [Apertura del Análisis](../recharge/opening.md)).

El Sistema Acuífero del Norte del Medio Oeste (Northern Midwest Aquifer System), que tiene un ciclo estacional marcado, muestra la diferencia entre las tres opciones. Con **None**:

![GWSa del Northern Midwest Aquifer System con la línea cortada en cada vacío](../../static/images/grace/app-gap-fill-none.webp)

Con **Straight line**, los 11 meses entre las misiones se convierten en un puente plano:

![GWSa del Northern Midwest Aquifer System con los vacíos unidos por líneas rectas](../../static/images/grace/app-gap-fill-line.webp)

Con **Seasonal model**, los meses rellenados continúan el ciclo anual de la región:

![GWSa del Northern Midwest Aquifer System con los vacíos rellenados por el modelo estacional](../../static/images/grace/app-gap-fill-seasonal.webp)

La banda de incertidumbre no se dibuja en los meses rellenados, porque el error de un valor rellenado proviene del modelo y no de GRACE (consulta
[Precisión del relleno](seasonal-model.md#fill-accuracy)).

## Valores rellenados en el CSV { #filled-values-in-the-csv }

El CSV descargado siempre incluye los valores rellenados, en las columnas `GWSa_filled` y `TWSa_filled`, con `GWSa_is_filled` y
`TWSa_is_filled` marcando los meses rellenados, sin importar qué opción use el gráfico (consulta [Descarga de Datos](../app/downloading-data.md)).

## Referencia { #reference }

Barbosa, S. A., Pulla, S. T., Williams, G. P., Jones, N. L., Mamane, B., and Sanchez, J. L. (2022). Evaluating groundwater storage change and
recharge using GRACE data: A case study of aquifers in Niger, West Africa. *Remote Sensing*, 14(7), 1532.
[doi:10.3390/rs14071532](https://doi.org/10.3390/rs14071532){:target="_blank"}
