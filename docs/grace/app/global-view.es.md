# Vista Global

## La vista global { #the-global-view }

Haz clic en **Global** para ver la capa mostrada en todas las celdas terrestres del mundo. La primera vez que la abres, la aplicación descarga
el registro completo de esa capa, lo que puede tardar un poco; después queda guardado en la caché de tu navegador.

El mapa global está en una malla de 1° para los dos conjuntos de datos, aunque GLDAS 2.2 sea nativamente de 0.25°. Una capa de 0.25° para todo
el mundo es un arreglo de 971 MB en el navegador para una sola variable, que ninguna cantidad de paciencia vuelve manejable. La malla más fina
se lee solo dentro de una región, donde hay un límite con el que recortarla; ver
[Vista Regional](regional-view.md#which-cells-are-averaged).

![Vista global de la anomalía de almacenamiento de agua subterránea en abril de 2002, el primer mes del registro](../../static/images/grace/app-global.webp)

Pulsa reproducir en el control de tiempo para animar el registro mes a mes. La vista global se reproduce más rápido que la vista regional,
unos cuatro meses por segundo, y vuelve al inicio al terminar. La animación hace fáciles de ver los grandes patrones: el descenso sostenido en el
norte de la India, Oriente Medio y la llanura del Norte de China, el aumento del almacenamiento en el Sahel desde aproximadamente 2010, y los años
húmedos y secos que recorren la Amazonía y el sur de África.

Cambia la **Displayed layer** para comparar componentes. En el conjunto de datos de GRACE, la TWSa sigue llevando la huella de los mascones de
3° incluso con los factores de ganancia aplicados (ver
[Cómo GRACE Mide el Almacenamiento de Agua](../mission/measuring-water-storage.md#the-mascon-solution-used-by-the-app)); la SWEa es casi cero en todas partes excepto en latitudes
altas y en montañas; la SMa muestra el humedecimiento y secado estacional de los suelos.

Cambia el **Dataset** para comparar las dos rutas hacia el agua subterránea en todo el mundo. Los patrones concuerdan en los lugares donde la
señal es grande —el norte de la India, la llanura del Norte de China, Oriente Medio— y esa concordancia significa algo, porque los dos se
obtuvieron de forma independiente. El mapa de 2.2 empieza en febrero de 2003 y no en abril de 2002 y tiene un valor en todos los meses, así que
su animación corre sin las pausas que los meses faltantes de GRACE dejan en la otra.

## Serie temporal de una sola celda { #time-series-for-a-single-cell }

Haz clic en cualquier celda terrestre para graficar su serie temporal. La ruta de navegación cambia a las coordenadas de la celda, y el gráfico
muestra los valores de la celda, con la banda de incertidumbre de ±1σ en el conjunto de datos de GRACE; GLDAS 2.2 no tiene banda (ver
[Vista Regional](regional-view.md#uncertainty)). El gráfico funciona igual que para una región (ver
[Vista Regional](regional-view.md#the-time-series-chart)), y el CSV descargado para una celda lleva el nombre de sus coordenadas.

![Serie temporal de una sola celda de 1° en el noroeste de Irán](../../static/images/grace/app-global-cell.webp)

Una sola celda se revisa rápido, pero recuerda que GRACE resuelve unos 3°, así que la TWSa de la celda se apoya en la misma medición que la de
sus vecinas dentro del mismo mascon. Los factores de ganancia dan a esas vecinas números distintos, y esa diferencia viene de un modelo de
superficie terrestre y no de GRACE (ver [Resolución, Fuga de Señal y Regiones Pequeñas](../mission/resolution-and-leakage.md)). La misma
advertencia vale para una celda de 2.2: su malla es más fina, pero la corrección de GRACE que hay detrás de su agua subterránea no lo es. Para
una cuenca o un acuífero, usa la [vista regional](regional-view.md), que promedia todas las celdas de la región.

## Mapas de tendencia y de diferencias { #trend-and-difference-maps }

Con el análisis activado, la vista global colorea cada celda con un único número para todo el registro en lugar de la anomalía mensual, y la
animación se oculta. La leyenda cuenta las celdas de cada clase. Una tendencia funciona en cualquiera de los dos conjuntos de datos; los
recuentos de celdas difieren, porque los dos tienen máscaras de tierra distintas y empiezan en años distintos.

![Tendencia del almacenamiento de agua subterránea en los últimos cinco años, por celda](../../static/images/grace/app-global-trends.webp)

Con el agua subterránea en pantalla, **Color by** ofrece además las tres comparaciones entre los dos conjuntos de datos, y cada una de ellas
colorea las mismas celdas según cuánto discrepan GRACE y GLDAS 2.2 ahí. Calcular una lee todo el registro de ambos conjuntos, así que tarda unos
segundos más que una tendencia.

![Cada celda terrestre coloreada por la diferencia entre las tendencias de agua subterránea de cinco años de los dos conjuntos de datos](../../static/images/grace/app-diff-global.webp)

Por celda esas comparaciones son ruidosas, como muestra el mapa de arriba. Úsalas para ver dónde están los patrones grandes y la vista regional
para decir algo sobre un acuífero concreto.

Ver [Análisis de Tendencias y Diferencias](trends.md) para saber cómo se calcula cada número y cómo elegir la ventana, y
[Explorar las diferencias en la aplicación](../compare/exploring.md) para saber cómo leer los mapas de comparación.
