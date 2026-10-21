# Explorar las diferencias en la aplicación

[Cómo se ven las diferencias](examples.md) recorre acuíferos concretos de uno en uno. La aplicación hace la misma aritmética para todas las
regiones de un conjunto a la vez, y para cada celda terrestre, coloreando el mapa con una comparación entre los dos conjuntos de datos en lugar
del valor de cualquiera de ellos.

## Cómo activarlo { #turning-it-on }

Una comparación necesita los dos conjuntos, así que la aplicación solo la ofrece mientras la **Displayed layer** (capa mostrada) es
**Groundwater Storage Anomaly (GWSa)**, la única magnitud que ambos conjuntos obtienen como producto propio. Con GWSa en pantalla, el desplegable
**Color by** (colorear por) del encabezado contiene cuatro opciones: la tendencia en GWSa, que trabaja sobre un conjunto a la vez, y tres
comparaciones.

| Color by | La pregunta que responde |
|:---|:---|
| GRACE vs GLDAS 2.2: trend difference | ¿discrepan los dos sobre la rapidez con que cambia el almacenamiento? |
| GRACE vs GLDAS 2.2: agreement | ¿ven los dos los mismos meses húmedos y los mismos meses secos? |
| GRACE vs GLDAS 2.2: seasonal swing | ¿coinciden los dos en cuánto oscila el ciclo anual? |

Cada una es un eje de desacuerdo, y un mapa de uno dice poco sobre los otros dos. Sobre los 322 contornos de acuíferos y cuencas que cubren los
datos publicados, las dos tendencias de la región mediana difieren en 0.27 cm/año a lo largo del registro, sus dos series mensuales correlacionan
a 0.69, y su ciclo estacional de GRACE oscila 0.73 veces lo que el de 2.2.

Elegir una comparación activa **Also show GLDAS 2.2** (mostrar también GLDAS 2.2) en el panel de control y lo mantiene activado, de modo que el
gráfico lleva ambas series para lo que selecciones a continuación. La vista regional colorea los contornos de las regiones, la vista global
colorea las celdas, y la medida sigue seleccionada al pasar de una a otra. [Análisis de tendencias y diferencias](../app/trends.md) da la
mecánica: los límites de las clases, el registro mínimo que necesita una región y cómo se promedian sus celdas.

## El mapa de diferencia de tendencia { #the-trend-difference-map }

![El conjunto Global Aquifers coloreado por la diferencia entre las tendencias de agua subterránea de cinco años de los dos conjuntos de datos](../../static/images/grace/app-diff-regions.webp)

Cada región o celda se colorea por la tendencia de GRACE menos la de 2.2 sobre la ventana del encabezado, en cm/año. GRACE es siempre el operando
izquierdo, sea cual sea el conjunto seleccionado en el panel, así que el signo de la diferencia nunca depende de otro control.

| Clase | Diferencia (cm/año) |
|:---|:---:|
| GRACE much lower (GRACE mucho menor) | menos de −1 |
| GRACE lower (GRACE menor) | −1 a −0.25 |
| Trends agree (las tendencias coinciden) | −0.25 a +0.25 |
| GRACE higher (GRACE mayor) | +0.25 a +1 |
| GRACE much higher (GRACE mucho mayor) | más de +1 |

El rojo marca los acuíferos donde la ruta de GRACE tiene el almacenamiento cayendo más rápido, que es el aplanamiento que expone
[Hasta dónde está validado](validation.md#22-flattens-trends): el modelo Catchment tras 2.2 no lleva bombeo, y el agotamiento llega a su
almacén de agua subterránea solo a través de la corrección mensual de GRACE, repartida entre todos los almacenes del modelo. El azul marca la
dirección contraria, donde GRACE tiene el almacenamiento subiendo más rápido. Sobre las 37 cuencas WHYMAP la tendencia de 2.2 es una mediana de
0.26 de la de GRACE donde el almacenamiento cae y de 0.33 donde sube, así que ambos colores son el mismo efecto.

La ventana importa aquí más que para una sola tendencia. Las ventanas cortas producen tendencias mayores, y la distancia entre los dos conjuntos
crece con ellas: sobre los contornos de Global Aquifers la diferencia típica más que se duplica, de 0.26 cm/año sobre todo el registro a 0.59
sobre los últimos cinco años. La clasificación lo sigue:

| Ventana | GRACE much lower | GRACE lower | Trends agree | GRACE higher | GRACE much higher |
|:---|:---:|:---:|:---:|:---:|:---:|
| últimos 5 años | 14 | 18 | 28 | 21 | 18 |
| últimos 10 años | 8 | 19 | 37 | 20 | 15 |
| últimos 15 años | 6 | 21 | 42 | 24 | 6 |
| últimos 20 años | 7 | 14 | 50 | 24 | 4 |
| todo el registro | 5 | 15 | 52 | 23 | 4 |

52 de los 99 acuíferos coinciden sobre todo el registro y 28 sobre los últimos cinco años. Ambas lecturas son correctas para su ventana. Una
región que cambia de clase al mover la ventana está diciendo que los dos conjuntos difieren sobre una oscilación reciente, que es un problema
menor que diferir sobre la dirección a largo plazo.

## El mapa de concordancia { #the-agreement-map }

![Los mismos acuíferos coloreados por la correlación entre las dos series mensuales de agua subterránea](../../static/images/grace/app-diff-agreement.webp)

La concordancia es la correlación de Pearson de las dos series mensuales, sobre los meses que ambos conjuntos reportan. Los meses que le faltan a
GRACE se descartan de ambos lados en lugar de rellenarse, así que el número no depende del ajuste de relleno de vacíos. Siempre se usa todo el
registro; el selector **Window** se atenúa, porque una correlación sobre cinco años plantea una pregunta distinta de una sobre veinte y la
respuesta corta es la más ruidosa de las dos.

| Clase | Correlación | Acuíferos del conjunto Global Aquifers |
|:---|:---:|:---:|
| Very close (muy estrecha) | más de 0.8 | 28 |
| Close (estrecha) | 0.6 a 0.8 | 30 |
| Partial (parcial) | 0.3 a 0.6 | 21 |
| Weak (débil) | 0 a 0.3 | 15 |
| Opposite (opuesta) | menos de 0 | 5 |

Lee este mapa junto al mapa de anomalías, no por separado. Una correlación baja donde se mueve poca agua no dice nada sobre ninguno de los dos
conjuntos: por debajo de unos 5 cm de variación en el agua subterránea de GRACE los dos correlacionan a una mediana de 0.19, y por encima de
unos 15 cm se asientan en torno a 0.77 por mucha más agua que haya en juego (ver
[Donde una correlación baja no significa nada](examples.md#where-a-low-correlation-means-nothing)). La clase marrón, donde los dos van opuestos,
es la que hay que tomar en serio, y tiene un mecanismo conocido: donde el ciclo de humedad del suelo de los modelos oscila tanto como el ciclo
medido de agua total, la resta tras la ruta de GRACE cancela la mayor parte de la señal de agua subterránea y lo que queda puede alcanzar su
máximo en la estación equivocada (ver [Donde los ciclos van opuestos](examples.md#where-the-cycles-run-opposite)).

Las clases débil y opuesta se sitúan sobre todo en latitudes altas en este mapa — las cuencas siberianas, los acuíferos bálticos —, que es el
término de nieve y no un acuífero: ningún modelo GLDAS guarda el suelo estacionalmente congelado como un almacén propio, así que un error en la
nieve de los modelos pasa directo al agua subterránea de la ruta de GRACE (ver
[Nieve y suelo congelado en latitudes altas](examples.md#snow-and-frozen-ground-at-high-latitude)).

## El mapa de amplitud estacional { #the-seasonal-swing-map }

![Los mismos acuíferos coloreados por el cociente de las amplitudes estacionales de los dos conjuntos de datos](../../static/images/grace/app-diff-swing.webp)

La amplitud es la altura del año medio desde su mes más bajo hasta el más alto, una vez retirada la tendencia a largo plazo, y este mapa colorea
cada región por la amplitud de GRACE dividida por la de 2.2. Es la misma magnitud que dibujan las figuras de las páginas de comparación, así que
el color de una región aquí y sus números allí concuerdan.

| Clase | Cociente | Acuíferos del conjunto Global Aquifers |
|:---|:---:|:---:|
| GRACE much flatter (GRACE mucho más plano) | menos de 0.5 | 16 |
| GRACE flatter (GRACE más plano) | 0.5 a 0.8 | 33 |
| Similar swing (amplitud parecida) | 0.8 a 1.25 | 22 |
| GRACE swings more (GRACE oscila más) | 1.25 a 2 | 11 |
| GRACE swings much more (GRACE oscila mucho más) | más de 2 | 8 |

El cociente de dos números pequeños es inestable, así que ambas amplitudes tienen que superar 1 cm para que una región se puntúe; nueve de los 99
acuíferos quedan por debajo y salen como **Insufficient data**, casi todos en el Sáhara, la península arábiga y Asia central, donde hay
demasiado poco ciclo anual como para tomar un cociente. De los 90 puntuados, 49 tienen el ciclo de GRACE más plano que el de 2.2 y 19 lo
tienen mayor — el patrón que muestran los casos de amplitud, con la oscilación de la ruta de GRACE recortada por la humedad del suelo que resta.
Los acuíferos donde GRACE oscila mucho más son sobre todo aquellos en los que está llevando algo que no es agua subterránea: un río, una llanura
de inundación, un embalse o un manto de nieve que los modelos no tienen (ver
[Diferencias que no son agua subterránea](examples.md#differences-that-are-not-groundwater)).

## Una celda no es una región { #a-cell-is-not-a-region }

La vista global responde las mismas tres preguntas por celda de 1°, y las respuestas salen mucho menos asentadas que las regionales:

| Proporción del conjunto en esta condición | Global Aquifers, 99 contornos | celdas de 1° |
|:---|:---:|:---:|
| diferencia de tendencia más allá de ±1 cm/año, últimos 5 años | 32% | 44% |
| correlación por debajo de 0 | 5% | 18% |
| amplitud estacional de GRACE más de 1.25 veces la de 2.2 | 21% | 45% |

Una de cada seis celdas terrestres tiene los dos registros yendo opuestos, donde lo hacen cinco de los 99 acuíferos, y casi la mitad de todas las
celdas tienen el ciclo de GRACE oscilando más que el de 2.2, donde el panorama regional es el contrario.

![Cada celda terrestre coloreada por la diferencia entre las tendencias de agua subterránea de cinco años de los dos conjuntos de datos](../../static/images/grace/app-diff-global.webp)

El mapa de arriba es lo que eso produce: moteado sobre casi toda la superficie terrestre, celdas rojas y azules alternándose en unos pocos
cientos de kilómetros, y el único bloque grande de **Trends agree** tendido sobre el Sáhara y la península arábiga, donde ninguno de los dos
registros se mueve mucho en cinco años.

Una sola celda lleva el ruido mes a mes que elimina un promedio de área, y del lado de GRACE lleva además el factor de ganancia aplicado a un
mascon de 3°, así que el valor de una celda descansa sobre la misma medición que el de sus vecinas (ver
[Resolución, fuga de señal y regiones pequeñas](../mission/resolution-and-leakage.md)). Lee los mapas de comparación globales para ver dónde
están los patrones grandes, y la vista regional para cualquier cosa que quieras decir sobre un acuífero concreto.

## Leer una región frente a su gráfico { #reading-a-region-against-its-chart }

![El Valle Central con la diferencia de tendencia activa: ambos conjuntos en el gráfico, cada uno con su recta ajustada sobre la ventana de cinco años](../../static/images/grace/app-diff-chart.webp)

Al hacer clic en una región, o en una celda de la vista global, se dibujan ambos conjuntos y se pone bajo el título del gráfico el número que
hay detrás del color de esa región. El Valle Central de arriba marca "GWSa trend difference +1.92 cm/yr (last 5 yr)", con las dos rectas
ajustadas de la leyenda en +3.40 y +1.43 cm/año: en los últimos cinco años ambos registros tienen el valle recuperándose de la sequía de
2021–2022 y GRACE lo tiene recuperándose más del doble de rápido. Sobre todo el registro ese mismo valle tiene a GRACE perdiendo 1.37 cm/año
frente a los 0.24 de 2.2 (ver [Donde difiere la tendencia](examples.md#where-the-trend-differs)), que es la lección de la ventana en una sola
región.

Bajo cualquiera de las dos medidas de tendencia cada serie recibe además su recta ajustada, discontinua. La concordancia y el cociente de
amplitudes no tienen recta que dibujar, así que el gráfico informa la medida bajo su título y deja las series lisas.

El número bajo el título es el número del mapa, así que puede diferir ligeramente de las dos pendientes de la leyenda. Colorear todas las
regiones de un conjunto a la vez promedia las celdas cuyos centros caen dentro de cada contorno, mientras que el gráfico de la región abierta usa
un promedio ponderado por solape de cada celda que el contorno toca (ver [Vista regional](../app/regional-view.md#which-cells-are-averaged)).

## Qué significa y qué no significa una gran diferencia { #what-a-large-difference-does-and-does-not-mean }

Una región coloreada en cualquiera de los dos extremos es una región que investigar. No es una barra de error, y ninguno de los dos conjuntos es
la verdad de la que el otro se aparta. Antes de tratar una gran diferencia como un resultado, haz las comprobaciones de
[Cuál usar](which-one-to-use.md#before-treating-a-large-difference-as-a-result): dibuja el agua de nieve, compara los dos totales, compara la
humedad del suelo frente al agua total, mira cuánta agua se mueve realmente, y pregúntate si un río, un lago o un embalse podrían explicarla.

Donde la evidencia sí apunta en una dirección, [Hasta dónde está validado](validation.md) dice hasta dónde. Dos comparaciones con pozos y un
estudio de 186 cuencas respaldan preferir GRACE para el tamaño de una tendencia y tratar la de 2.2 como aplanada. Nada comparable resuelve la
amplitud estacional, así que una región coloreada **GRACE much flatter** es un desacuerdo sobre cómo se reparte una estación húmeda entre el
suelo y el acuífero que hay debajo, sin ninguna medición independiente que diga qué reparto es el correcto.
