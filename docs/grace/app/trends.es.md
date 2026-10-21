# Análisis de Tendencias y Diferencias

## Qué hace el análisis { #what-the-analysis-does }

**Analyze**, en el encabezado, colorea el contorno de cada región, en la vista regional, o cada celda de la malla, en la vista global, con un
único número que resume todo el registro, en lugar del valor del mes que marca el control de tiempo. El análisis está activado al abrir la
aplicación; **Hide** lo desactiva y devuelve el mapa a la anomalía mensual.

**Color by** (colorear por), junto al botón, elige ese número. Una medida trabaja sobre el conjunto de datos que esté seleccionado, y tres
comparan los dos conjuntos entre sí:

| Color by | Qué calcula | Ambos conjuntos | Ventana |
|:---|:---|:---:|:---:|
| Trend in GWSa | la pendiente por mínimos cuadrados de los valores mensuales, en cm/año | no | sí |
| GRACE vs GLDAS 2.2: trend difference | la pendiente de GRACE menos la de 2.2 | sí | sí |
| GRACE vs GLDAS 2.2: agreement | la correlación de Pearson de las dos series mensuales | sí | no |
| GRACE vs GLDAS 2.2: seasonal swing | la amplitud estacional de GRACE dividida por la de 2.2 | sí | no |

La entrada de tendencia nombra lo que esté en pantalla, así que dice **Trend in GWSa** en la capa por defecto y **Trend in SMa** en humedad del
suelo. Las tres comparaciones solo aparecen mientras se muestra agua subterránea (GWSa), porque es la única magnitud que ambos conjuntos obtienen
por derecho propio: la humedad del suelo, la nieve y el agua de dosel de la ruta 2.1 vienen de los tres modelos de superficie terrestre, sin
GRACE dentro, así que llamar "GRACE vs GLDAS 2.2" a una comparación contra ellas nombraría un conjunto que no está en ella.

Toda medida necesita al menos 24 meses con datos en la ventana, y las tres comparaciones necesitan 24 meses que reporten ambos conjuntos; una
región o celda con menos aparece como **Insufficient data** (datos insuficientes). [Explorar las diferencias en la
aplicación](../compare/exploring.md) cubre qué
significan las tres comparaciones, los límites de sus clases y cómo leerlas. El resto de esta página trata de la tendencia.

## Clasificación de tendencias { #trend-classification }

Bajo **Trend in GWSa**, o la tendencia de lo que esté en pantalla, cada región o celda se colorea según la tasa a la que esa capa ha estado
subiendo o bajando.

![Acuíferos del conjunto Global Aquifers clasificados según la tendencia de su almacenamiento de agua subterránea en los últimos cinco años](../../static/images/grace/app-home.webp)

En la vista regional, arriba, cada acuífero o cuenca recibe una tendencia a partir del promedio de sus celdas (ver
[Vista Regional](regional-view.md#the-landing-page)). Esa es la mejor guía para un acuífero en particular.

![Tendencia del almacenamiento de agua subterránea en los últimos cinco años para cada celda de 1°, en la vista global](../../static/images/grace/app-global-trends.webp)

La vista global, arriba, clasifica todas las celdas terrestres —15,159 en la malla de 1° del conjunto de datos de GRACE y 17,346 en la de
GLDAS 2.2, que lleva una máscara de tierra algo mayor—, así que muestra dónde está cambiando el almacenamiento sin importar los límites de los
acuíferos: aumenta en el Sahel y África Oriental, y disminuye en gran parte de Oriente Medio, el norte de la India y Brasil.

La tendencia es la pendiente de una recta ajustada por mínimos cuadrados a los valores mensuales dentro de la ventana, en cm por año. Los meses
sin datos de GRACE se omiten en lugar de rellenarse, lo que afecta solo al conjunto de datos de GRACE; GLDAS 2.2 tiene un valor en todos los
meses.

Las tendencias se calculan sobre el conjunto de datos que esté seleccionado, así que la clasificación cambia al cambiar de conjunto. Dos
diferencias importan al comparar los dos mapas. GLDAS 2.2 empieza en febrero de 2003 frente al abril de 2002 de GRACE, así que la ventana
**All** cubre diez meses menos. Y una tendencia de 2.2 es una tendencia en un estado de modelo que GRACE corrige cada mes, que hereda la
resolución de GRACE por fina que parezca la malla del modelo.

| Clase | Tendencia (cm/año) |
|---|---|
| Extreme decline (descenso extremo) | menos de −2 |
| Decline (descenso) | −2 a −0.5 |
| Static (estable) | −0.5 a +0.5 |
| Increase (aumento) | +0.5 a +2 |
| Extreme increase (aumento extremo) | más de +2 |

La leyenda cuenta las regiones o celdas de cada clase. Como referencia, una tendencia de −2 cm/año sostenida sobre 100,000 km² equivale a una
pérdida de 2 km³ de agua al año.

### Factores de ganancia y magnitud de las tendencias { #gain-factors-and-trend-magnitudes }

Esta sección trata del conjunto de datos de GRACE. GLDAS 2.2 no se ve afectado: no se le aplica ningún factor de ganancia, y la solución de
GRACE que se asimila en él es la del CSR y no la del JPL.

La TWSa que sirve la aplicación tiene aplicados los factores de ganancia de JPL (ver
[Cálculo del Almacenamiento de Agua Subterránea](../gldas/deriving-groundwater.md#gain-factors)), y esos factores pasan directamente a las
tendencias, porque un multiplicador constante sobre una serie temporal multiplica su pendiente. JPL acompaña este uso de una advertencia: los
factores están dominados por el ciclo anual, y el GRACE-FO Level-3 Handbook dice que «pueden introducir sesgos en bandas de frecuencia distintas
de la componente anual, en particular en las tendencias de largo plazo», para las que harían falta factores obtenidos por núcleo de promediado.
Para este producto no se publican tales factores, así que la aplicación aplica los estándar en todo momento y reporta un solo valor de GWSa en
todas partes, en lugar de un número para el mapa y otro distinto para la tendencia.

En la práctica esto mueve muy poco la mayoría de las tendencias. En la ventana de cinco años con que abre la aplicación, la tendencia de agua
subterránea de la celda mediana se desplaza 0.12 cm/año y la magnitud mediana de la tendencia pasa de 0.95 a 0.93 cm/año; sobre todo el registro
el desplazamiento mediano es de 0.05 cm/año. Cerca del 15% de las celdas cruza un límite de clase en cinco años, y el 10% sobre todo el registro;
casi todas ellas son celdas que ya estaban cerca de las líneas de ±0.5 o ±2 cm/año, donde un cambio pequeño de pendiente mueve la etiqueta. Las
excepciones son celdas glaciares, en Svalbard, Nueva Zembla y los campos de hielo de la Patagonia, donde se aplica un factor grande a una señal
de hielo enorme y la tendencia puede moverse decenas de cm por año. Esas celdas nunca fueron agua subterránea. Trata una clase como un resumen y
no como una medición, y lee juntas la magnitud de la tendencia y la serie temporal.

## La ventana de análisis { #the-analysis-window }

El selector **Window** del encabezado fija cuánto retrocede el ajuste desde el mes más reciente: 5, 10, 15 o 20 años, o **All** para todo el
registro desde 2002. La clasificación y la leyenda se actualizan cuando lo cambias.

La concordancia y la amplitud estacional usan siempre todo el registro, así que el selector se atenúa con esas dos. Una correlación sobre cinco
años plantea una pregunta distinta de una sobre veinte, y un ciclo estacional estimado a partir de cinco años descansa sobre cinco valores por
mes del calendario. El ajuste se conserva mientras el selector está atenuado y vuelve cuando regresas a una tendencia.

En la mayoría de las regiones el almacenamiento oscila entre años húmedos y secos, así que una ventana corta puede captar una sola oscilación en
lugar de la dirección de largo plazo. En el Valle Central de California, el almacenamiento de agua subterránea disminuyó desde 2002 hasta la
sequía de 2021–2022, y luego se recuperó en parte tras el invierno muy húmedo de 2022–2023. La tendencia de 5 años es un aumento; la de 20 años es
un descenso. Ambas son correctas para sus ventanas. Revisa la serie temporal antes de sacar conclusiones de una clase de tendencia, y compara más
de una ventana.

## Rectas ajustadas en el gráfico { #fitted-lines-on-the-chart }

Cuando hay una región o celda seleccionada y se muestra una tendencia, el gráfico añade la recta ajustada como una línea discontinua sobre la
ventana, y la leyenda indica la pendiente, por ejemplo "GWSa trend +2.25 cm/yr (last 5 yr)". Cada componente graficado tiene su propia línea de
tendencia.

La diferencia de tendencia dibuja ambos ajustes, uno por conjunto, e informa bajo el título del gráfico el número con el que se coloreó el mapa.
La concordancia y la amplitud estacional no tienen recta que dibujar, así que el gráfico no muestra ninguna e informa la medida bajo su título.

## Cómo se calcula la clasificación de las regiones { #how-the-region-classification-is-computed }

Para clasificar a la vez todas las regiones de un conjunto, bajo cualquiera de las cuatro medidas, la aplicación promedia las celdas cuyos
centros caen dentro de cada región, ponderadas
por el coseno de la latitud. Esto es más rápido que el promedio ponderado por superposición que se usa para el gráfico de una región seleccionada
(ver [Vista Regional](regional-view.md#which-cells-are-averaged)), y los dos pueden diferir ligeramente en regiones pequeñas o angostas. La
tendencia de la leyenda del gráfico, y la medida bajo el título del gráfico, se calculan a partir de la serie del propio gráfico. Una región
demasiado pequeña para contener el centro de
alguna celda se clasifica usando la celda situada en su centro.
