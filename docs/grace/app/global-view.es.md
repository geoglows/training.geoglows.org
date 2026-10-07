# Vista Global

## La vista global { #the-global-view }

Haz clic en **Global** para ver la capa mostrada en todas las celdas terrestres del mundo. La primera vez que la abres, la aplicación descarga
el registro completo de esa capa, lo que puede tardar un poco; después queda guardado en la caché de tu navegador.

![Vista global de la anomalía de almacenamiento de agua subterránea en septiembre de 2024](../../static/images/grace/app-global.webp)

Pulsa reproducir en el control de tiempo para animar el registro mes a mes. La vista global se reproduce más rápido que la vista regional,
unos cuatro meses por segundo, y vuelve al inicio al terminar. La animación hace fáciles de ver los grandes patrones: el descenso sostenido en el
norte de la India, Oriente Medio y la llanura del Norte de China, el aumento del almacenamiento en el Sahel desde aproximadamente 2010, y los años
húmedos y secos que recorren la Amazonía y el sur de África.

Cambia la **Displayed layer** para comparar componentes. La TWSa muestra el contorno en bloques de los mascons de 3° (ver
[La Misión GRACE](../background/grace-mission.md#the-mascon-solution-used-by-the-app)); la SWEa es casi cero en todas partes excepto en latitudes
altas y en montañas; la SMa muestra el humedecimiento y secado estacional de los suelos.

## Serie temporal de una sola celda { #time-series-for-a-single-cell }

Haz clic en cualquier celda terrestre para graficar su serie temporal. La ruta de navegación cambia a las coordenadas de la celda, y el gráfico
muestra los valores de la celda con la banda de incertidumbre de ±1σ. El gráfico funciona igual que para una región (ver
[Vista Regional](regional-view.md#the-time-series-chart)), y el CSV descargado para una celda lleva el nombre de sus coordenadas.

![Serie temporal de una sola celda de 1° en el centro de Irán](../../static/images/grace/app-global-cell.webp)

Una sola celda se revisa rápido, pero recuerda que GRACE resuelve unos 3°, así que la TWSa de la celda es la misma que la de sus vecinas dentro
del mismo mascon. Para una cuenca o un acuífero, usa la [vista regional](regional-view.md), que promedia todas las celdas de la región.

## Mapa de tendencias { #trend-map }

Con las tendencias activadas, la vista global colorea cada celda según su tendencia en lugar de la anomalía mensual, y la animación se oculta. La
leyenda cuenta las celdas de cada clase.

![Tendencia del almacenamiento de agua subterránea en los últimos cinco años, por celda](../../static/images/grace/app-global-trends.webp)

Ver [Análisis de Tendencias](trends.md) para saber cómo se calcula la tendencia y cómo elegir la ventana.
