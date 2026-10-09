# Análisis de Tendencias

## Clasificación de tendencias { #trend-classification }

**Analyze trends** colorea el contorno de cada región (en la vista regional) o cada celda de la malla (en la vista global) según la tasa a la que
la capa mostrada ha estado subiendo o bajando. Las tendencias están activadas al abrir la aplicación; haz clic en **Hide trends** para
desactivarlas.

![Acuíferos del conjunto Global Aquifers clasificados según la tendencia de su almacenamiento de agua subterránea en los últimos cinco años](../../static/images/grace/app-home.webp)

En la vista regional, arriba, cada acuífero o cuenca recibe una tendencia a partir del promedio de sus celdas (ver
[Vista Regional](regional-view.md#the-landing-page)). Esa es la mejor guía para un acuífero en particular.

![Tendencia del almacenamiento de agua subterránea en los últimos cinco años para cada celda de 1°, en la vista global](../../static/images/grace/app-global-trends.webp)

La vista global, arriba, clasifica las 15,159 celdas terrestres, así que muestra dónde está cambiando el almacenamiento sin importar los límites
de los acuíferos: aumenta en el Sahel y África Oriental, y disminuye en gran parte de Oriente Medio, el norte de la India y Brasil.

La tendencia es la pendiente de una recta ajustada por mínimos cuadrados a los valores mensuales dentro de la ventana de tendencia, en cm por año.
Los meses sin datos de GRACE se omiten, no se rellenan. Una región o celda necesita al menos 24 meses con datos dentro de la ventana para
clasificarse; de lo contrario se muestra como **Insufficient data** (datos insuficientes).

| Clase | Tendencia (cm/año) |
|---|---|
| Extreme decline (descenso extremo) | menos de −2 |
| Decline (descenso) | −2 a −0.5 |
| Static (estable) | −0.5 a +0.5 |
| Increase (aumento) | +0.5 a +2 |
| Extreme increase (aumento extremo) | más de +2 |

La leyenda cuenta las regiones o celdas de cada clase. Como referencia, una tendencia de −2 cm/año sostenida sobre 100,000 km² equivale a una
pérdida de 2 km³ de agua al año.

## La ventana de tendencia { #the-trend-window }

El selector **Window** del encabezado fija cuánto retrocede el ajuste desde el mes más reciente: 5, 10, 15 o 20 años, o **All** para todo el
registro desde 2002. La clasificación y la leyenda se actualizan cuando lo cambias.

En la mayoría de las regiones el almacenamiento oscila entre años húmedos y secos, así que una ventana corta puede captar una sola oscilación en
lugar de la dirección de largo plazo. En el Valle Central de California, el almacenamiento de agua subterránea disminuyó desde 2002 hasta la
sequía de 2021–2022, y luego se recuperó en parte tras el invierno muy húmedo de 2022–2023. La tendencia de 5 años es un aumento; la de 20 años es
un descenso. Ambas son correctas para sus ventanas. Revisa la serie temporal antes de sacar conclusiones de una clase de tendencia, y compara más
de una ventana.

## Línea de tendencia en el gráfico { #trend-line-on-the-chart }

Cuando hay una región o celda seleccionada y las tendencias están activadas, el gráfico añade la recta ajustada como una línea discontinua sobre
la ventana de tendencia, y la leyenda indica la pendiente, por ejemplo "GWSa trend +2.25 cm/yr (last 5 yr)". Cada componente graficado tiene su
propia línea de tendencia.

## Cómo se calcula la clasificación de las regiones { #how-the-region-classification-is-computed }

Para clasificar a la vez todas las regiones de un conjunto, la aplicación promedia las celdas cuyos centros caen dentro de cada región, ponderadas
por el coseno de la latitud. Esto es más rápido que el promedio ponderado por superposición que se usa para el gráfico de una región seleccionada
(ver [Vista Regional](regional-view.md#which-cells-are-averaged)), y los dos pueden diferir ligeramente en regiones pequeñas o angostas. La
tendencia de la leyenda del gráfico es la calculada a partir de la serie del gráfico. Una región demasiado pequeña para contener el centro de
alguna celda se clasifica usando la celda situada en su centro.
