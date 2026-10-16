# Cálculo del Almacenamiento de Agua Subterránea

La aplicación llega al agua subterránea por dos caminos. El conjunto GRACE + GLDAS 2.1 resta el almacenamiento modelado de una medición de
gravedad. El conjunto GLDAS 2.2 lee un estado de modelo que GRACE ha corregido. Ambos reportan la misma magnitud sobre la misma línea base, y
aquí se dan los dos, seguidos de qué cubre la incertidumbre y cuándo preferir uno sobre el otro.

## El balance hídrico { #the-water-balance }

El almacenamiento total de agua es la suma de todos los almacenamientos de una columna de la Tierra: el equivalente de agua de la nieve (SWEa),
el agua retenida en el dosel vegetal (CANa), la humedad del suelo (SMa), el agua subterránea (GWSa) y el agua superficial en ríos, lagos y
embalses.

![Componentes del almacenamiento terrestre de agua](../../static/images/grace/grace-water-balance.png)

Los dos conjuntos de datos de la aplicación se apoyan en esta identidad, y los dos dejan fuera el agua superficial:

$$
\mathrm{TWSa} = \mathrm{SWEa} + \mathrm{CANa} + \mathrm{SMa} + \mathrm{GWSa}
$$

Así que cualquier cambio en el almacenamiento de agua superficial termina en la GWSa, en cualquiera de los dos conjuntos: ningún modelo de GLDAS
lleva ríos, lagos ni embalses tampoco. En la mayor parte del mundo los cambios de agua superficial son pequeños frente a los demás términos. En
regiones con grandes embalses, humedales o ríos con grandes crecidas (el Amazonas, el Ganges y el Brahmaputra, el mar Caspio, el lago Victoria,
el lago Volta), la GWSa incluye esos cambios y exagera la oscilación estacional del agua subterránea. En la Cuenca del Volta, por ejemplo, el
lago representa cerca de la mitad de la señal total de almacenamiento ([caso de estudio](../case-studies/volta.md)).

Lo que separa a las dos rutas es qué término se mide y cuál se despeja. La ruta 1 mide la TWSa con GRACE y reordena la identidad para obtener la
GWSa. La ruta 2 lee la GWSa de un modelo, y la TWSa es el total propio de ese mismo modelo.

## Ruta 1: GRACE menos GLDAS 2.1 { #route-1-grace-minus-gldas-21 }

GRACE mide el cambio total del agua almacenada en la columna, y los modelos de superficie terrestre estiman los tres términos que no son agua
subterránea lo bastante bien como para restarlos. Reordenando la identidad de arriba, el agua subterránea queda como el residuo:

$$
\mathrm{GWSa} = \mathrm{TWSa} - (\mathrm{SWEa} + \mathrm{CANa} + \mathrm{SMa})
$$

Nada en esta ruta modela el agua subterránea. Todo lo que GRACE pesó y que los tres términos del modelo no explican se reporta como agua
subterránea, lo que es la fuerza del método donde esos términos son pequeños y su debilidad donde no lo son.

### Los términos de GLDAS { #the-gldas-terms }

La aplicación toma el equivalente de agua de la nieve, el almacenamiento por intercepción del dosel y la humedad del suelo de cada uno de los
tres modelos de GLDAS 2.1 —Noah, VIC y el modelo Catchment, descritos en
[Los Modelos de Superficie Terrestre GLDAS](land-surface-models.md)—, los convierte de kg/m² a cm de agua y lleva los tres a la misma malla de 1°
(Noah se promedia de 0.25° a 1°). La anomalía de cada modelo es su valor menos la media de esa celda para 2004–2009, la misma línea base que
GRACE.

La humedad del suelo significa las capas sumadas para Noah y VIC, y el reservorio de la zona radicular para el modelo Catchment, cuyo reservorio
de perfil publicado traería consigo el agua subterránea del propio modelo
([por qué](land-surface-models.md#why-the-catchment-model-needs-separate-handling)).

Los tres modelos a menudo discrepan, en particular sobre la humedad del suelo profunda. En lugar de elegir uno, la aplicación los promedia:
SWEa, CANa y SMa son cada una la media de los tres modelos, y la dispersión entre los modelos (su desviación estándar) se usa como la
incertidumbre de cada término.

### Cadena de procesamiento { #processing-chain }

![La cadena de procesamiento de GRACE + GLDAS 2.1, desde las entradas publicadas hasta las cinco capas que ofrece la aplicación](../../static/images/grace/grace-processing.png)

La TWSa de GRACE se escala con los factores de ganancia a 0.5°, se promedia a 1° y se combina con el conjunto de modelos para obtener la GWSa en
una malla de 1°. La aplicación ofrece cinco capas: GWSa, SMa, SWEa y CANa a 1°, y TWSa a 0.5°, en la malla en la que la distribuye JPL. Usar 1°
para las capas derivadas sigue la práctica habitual de combinar GRACE con datos de modelos en la más gruesa de las dos mallas; reportar la GWSa
a 0.5° daría una impresión de detalle que ninguno de los dos conjuntos de datos tiene.

No se rellena ningún vacío. Cada valor mensual en la aplicación es el valor publicado por JPL, escalado como se describe más abajo, combinado
con el conjunto de GLDAS para ese mes. Los 35 meses que le faltan a GRACE faltan también aquí, y el relleno de vacíos de la aplicación actúa
sobre ellos solo en el gráfico (ver [Vacíos y Relleno de Vacíos](../mission/gap-filling.md)).

### Factores de ganancia { #gain-factors }

La solución mascon es nativamente de 3°, y el archivo de 0.5° repite el valor de cada mascon en todas las celdas que contiene —36 en el ecuador,
una mediana de 42 sobre tierra y más hacia los polos, donde un mascon de la misma área abarca más longitud—, así que la malla publicada por sí
sola no contiene ningún detalle más fino que un mascon. JPL distribuye en el mismo archivo una malla de **factores de ganancia** para recuperar
parte de ese detalle. Se obtienen pasando el modelo de superficie terrestre CLM por el mismo procesamiento que atraviesa GRACE y estimando,
celda por celda, el multiplicador que restituye la amplitud original del modelo. La corrección es una sola multiplicación, con el factor
constante en el tiempo:

$$
g'(x,y,t) = g(x,y,t) \times s(x,y)
$$

JPL no aplica este escalado antes de distribuir los datos; el GRACE-FO Level-3 Handbook indica que son los usuarios quienes deben aplicarlo, y su
propio ejemplo de agua subterránea sigue el mismo enfoque de TWSa menos GLDAS que usa esta aplicación, con la multiplicación como paso de
preprocesamiento. La aplicación aplica los factores a la TWSa a 0.5°, antes de promediarla a 1°, porque la estructura que añaden es más fina que
una celda de 1°.

La mayoría de los factores son cercanos a 1: el 84% de las celdas que reciben uno está entre 0.5 y 1.5. La aplicación dibuja 60,064 celdas a
0.5°, y una celda conserva el valor del mascon sin escalar en dos casos.

**Donde JPL no publica ningún factor.** Son 3,365 celdas, el 5.6% de la malla, y el 84% de ellas está al norte de 60°N. Los factores no están
pensados para el hielo, porque CLM no representa los casquetes de hielo ni los glaciares de montaña. JPL también deja el océano sin escalar, que
de todos modos elimina de la aplicación la máscara de tierra de GLDAS. La Antártida no llega a plantearse: GLDAS corre de 60°S hacia el norte,
así que la aplicación no tiene ninguna celda antártica.

**Donde el factor es implausible**, es decir cero o negativo, mayor que 3 o menor que 1/3. Son 790 celdas, el 1.3% de la malla, y es una regla
de la aplicación y no de JPL: el archivo marca todo su rango como válido y no fija ningún límite.

Lo que estas celdas tienen en común es que la regresión que produce el factor apenas tenía señal con la que trabajar, así que su pendiente es
inestable. Son costeras unas tres veces más a menudo que las celdas que se conservan (51% a menos de dos celdas del agua, frente al 19%) y
tienen nieve todo el año trece veces más a menudo (18.5% frente al 1.4%). Casi la mitad no es ni lo uno ni lo otro, y se sitúa en interiores
áridos —el Kalahari, el interior de Australia, el Karoo, el Atacama— donde la variación de almacenamiento de CLM es lo bastante pequeña como
para que el ajuste divida por casi nada. Hielo, costa y desierto son el mismo fallo en tres escenarios, y por eso un límite sobre el factor los
detecta donde una máscara de glaciares por sí sola no lo haría.

Los factores en estas celdas llegan hasta 24 y −1.35. Un factor negativo invierte el signo de la anomalía; un factor de 24 convirtió −292 cm en
−7048 cm en la isla de Ellesmere. En las cuencas áridas la exclusión es inocua en cualquier caso —cuatro de las 806 celdas de la Gran Cuenca
Artesiana, que mueven su serie 0.00 cm— porque una anomalía pequeña multiplicada por un factor malo sigue siendo pequeña.

Sí importa en al menos un lugar que un usuario notaría. Una de esas celdas cae dentro de la **Cuenca del Cáucaso Norte**, un acuífero de los
propios conjuntos de regiones de la aplicación. Aplicar todos los factores duplicó la serie de agua subterránea de esa cuenca: la desviación
estándar de su media pasó de 13.3 cm sin escalar a 23.5 cm, y queda en 13.6 cm cuando las celdas implausibles se dejan en paz. Casi toda esa
amplitud aparente eran unas pocas celdas degeneradas, no señal. La ganancia que los factores existen para restituir sobrevive a la regla: el
Valle Central de California la conserva entera, de 10.2 cm a 12.4 cm, y el Congo casi toda, de 7.6 cm sin escalar a 7.9 cm frente a 8.1 cm con
todos los factores aplicados.

Dos cuencas glaciares de los conjuntos de cuencas hidrográficas, Alsek y Santa Cruz, presentan una GWSa muy grande independientemente de lo que
se haga con los factores de ganancia. GRACE detecta ahí la pérdida de masa de hielo y GLDAS no modela glaciares, así que el balance hídrico la
atribuye al agua subterránea. Esos números son un artefacto del método, no del escalado.

Lo que los factores no hacen es convertir la malla de 0.5° en 36 mediciones independientes. El mascon subyacente sigue siendo una sola
estimación, y los factores redistribuyen su amplitud usando la idea que un modelo tiene de cómo varía el almacenamiento dentro de él. El handbook
es explícito en que los modelos que están detrás arrastran sesgos y «por lo general no incluyen el agua subterránea ni las actividades humanas en
sus simulaciones», así que un acuífero con bombeo intenso es precisamente donde la redistribución está menos informada por lo que se mide.

## Ruta 2: agua subterránea de GLDAS 2.2 { #route-2-groundwater-from-gldas-22 }

El modelo Catchment lleva el agua subterránea como un estado propio, y la ejecución de GLDAS 2.2 corrige ese estado cada mes asimilando la
anomalía del almacenamiento total de agua de GRACE. El agua subterránea llega por tanto como una variable publicada, `GWS_tavg`, y el cálculo es
una sola resta:

$$
\mathrm{GWSa}_{22} = \mathrm{GWS} - \overline{\mathrm{GWS}}_{2004\text{–}2009}
$$

La misma línea base 2004–2009 que GRACE, así que las anomalías de los dos conjuntos están sobre el mismo cero y pueden dibujarse en un solo eje.

La NASA publica 2.2 como campos diarios; la aplicación los promedia a meses calendario para que coincidan con el resto. Todo se convierte de
kg/m² a cm. El almacén de 0.25° guarda los valores con una centésima de centímetro, porque esa malla existe para regiones pequeñas donde medio
centímetro es parte de la señal y no hay dispersión de un conjunto donde esconderlo. Un almacén de 1°, promediado desde las mismas celdas que
usan los almacenes de GRACE, alimenta el mapa global con una décima de centímetro, lo que baja la primera vista de una capa de todo el mundo de
10.5 MB a 7.1 MB.

### La humedad del suelo, y por qué no es la que publica la NASA { #soil-moisture-and-why-it-is-not-what-nasa-publishes }

La humedad del suelo publicada del modelo Catchment ya contiene el agua subterránea. `SoilMoist_P_tavg` es todo el perfil desde la superficie
hacia abajo, y `SoilMoist_P − GWS` es positivo en todas partes: una mediana de 277 mm de agua situada por encima del nivel freático. El balance
propio del producto cierra con tres términos:

$$
\mathrm{TWS} = \mathrm{SoilMoist\_P} + \mathrm{SWE} + \mathrm{CanopInt}
$$

Ofrecida así, la SMa del conjunto 2.2 significaría algo distinto de la SMa del conjunto de GRACE, y las cinco capas no sumarían en el gráfico.
Por eso la aplicación guarda la SMa de 2.2 como la anomalía de `SoilMoist_P − GWS`, que es la humedad del suelo por encima del nivel freático.
Por la definición que la propia NASA da del agua subterránea del modelo, esa diferencia es el reservorio de la zona radicular, que es lo que el
promedio de modelos del conjunto de datos de GRACE toma del mismo modelo: ver
[por qué el modelo Catchment necesita un tratamiento aparte](land-surface-models.md#why-the-catchment-model-needs-separate-handling). Con esa
sustitución las cinco capas cierran exactamente:

$$
\mathrm{TWSa}_{22} = \mathrm{SWEa}_{22} + \mathrm{CANa}_{22} + \mathrm{SMa}_{22} + \mathrm{GWSa}_{22}
$$

Medido sobre el almacén publicado de 0.25°, el residuo más grande de todo el registro es de 0.02 cm, que son dos unidades de su propio redondeo.

### Qué hace y qué no hace la asimilación { #what-the-assimilation-does-and-does-not-do }

GRACE ve la columna entera y no puede distinguir a qué almacenamiento pertenece una discrepancia, así que el esquema reparte la corrección de
cada mes entre los estados del modelo, el agua subterránea incluida. El bombeo está ausente de la física del modelo y llega al estado de agua
subterránea solo a través de esta corrección.

Eso tiene consecuencias para leer una serie de 2.2.

El registro empieza en febrero de 2003, diez meses después del abril de 2002 de GRACE, porque es cuando se arrancó la ejecución asimiladora.

No falta ningún mes. Donde GRACE tiene un vacío el modelo sigue corriendo; simplemente queda sin corregir ese mes, así que la serie es continua
y nada marca dónde se interrumpió la corrección.

La malla es más fina que la corrección. Una celda de 0.25° es una celda del modelo, y la información de GRACE que le llegó venía de un mascon de
3°, así que las celdas vecinas difieren por lo que dice el modelo y no por lo que se midió: la misma advertencia que los factores de ganancia en
la otra ruta, llegando por otro camino.

## Incertidumbre { #uncertainty }

Cada capa del conjunto de datos de GRACE viene con una incertidumbre de una desviación estándar (1σ), que el gráfico de series temporales dibuja
como una banda alrededor de la línea:

- **TWSa:** la incertidumbre publicada por JPL para cada mascon y mes, multiplicada por el mismo factor de ganancia que los datos, de modo que
  la banda se mantiene en proporción al valor que describe.
- **SWEa, CANa, SMa:** la desviación estándar entre los tres modelos de GLDAS.
- **GWSa:** las cuatro combinadas, tratándolas como independientes:

$$
\sigma_{\mathrm{GWSa}} = \sqrt{\sigma_{\mathrm{TWSa}}^2 + \sigma_{\mathrm{SWEa}}^2 + \sigma_{\mathrm{CANa}}^2 + \sigma_{\mathrm{SMa}}^2}
$$

La banda de incertidumbre recoge el error de medición de GRACE y el desacuerdo entre modelos. No recoge los errores que comparten los tres
modelos, el efecto de dejar fuera el agua superficial, la fuga de señal desde fuera de una región (ver
[Resolución, Fuga de Señal y Regiones Pequeñas](../mission/resolution-and-leakage.md)) ni la incertidumbre de los propios factores de ganancia, que JPL no
publica. La incertidumbre real es mayor que la que muestra la banda.

Una advertencia sobre combinarlas: la incertidumbre de la TWSa de JPL es un error de medición, mientras que los tres términos de GLDAS son la
dispersión entre Noah, VIC y CLSM, que mide cuánto discrepan los modelos y no cuánto se equivocan. Sumarlas en cuadratura trata ambas cosas como
comparables. En la mayoría de las cuencas domina la dispersión entre modelos: en el Congo, 3.1 cm de GRACE frente a 5.7 cm combinados.

GLDAS 2.2 no lleva ninguna incertidumbre. Es una sola ejecución de un modelo y no un conjunto, así que no hay dispersión que tomar, y la NASA no
publica ningún error por mes para el producto. El gráfico no dibuja banda alguna para él. Ese silencio es la ausencia de una estimación; todo lo
que en [Los Modelos de Superficie Terrestre GLDAS](land-surface-models.md#accuracy-and-mixing-versions) hace que un modelo de superficie
terrestre se equivoque sigue aplicándose, sin que nada lo reporte.

## Cuál usar { #which-one-to-use }

Ninguno de los dos conjuntos gana en todas partes, y la costumbre útil es dibujar los dos y mirar dónde se separan.

**En la ruta de GRACE conviene apoyarse para saber cuánto cambió el almacenamiento.** Su agua subterránea se apoya en una medición de masa, y
los modelos entran solo como los términos que se restan. Donde los términos de GLDAS son pequeños frente a la señal de agua subterránea —la
mayoría de los acuíferos áridos y semiáridos—, muy poco de la respuesta depende de que los modelos acierten.

**A la ruta 2.2 hay que recurrir en una región pequeña**, porque se promedia en una malla de 0.25° donde la otra está en 1°, así que una cuenca
de unas pocas celdas de ancho queda descrita por dieciséis veces más celdas. Su registro continuo la hace además la serie más fácil de trabajar
año por año. Lo que compra es muestreo, no resolución: la información de GRACE que contiene siguió llegando a 3°.

**Para la recarga, preferir la ruta de GRACE.** Barbosa et al. (2025) aplicaron el método de fluctuación del nivel freático a ambos conjuntos en
la Cuenca del Volta y obtuvieron 17.4 y 36.1 cm/año con 2.2 frente a 5.8 y 10.7 cm/año con GRACE, mientras que los pozos daban una mediana de
10.4. Recomiendan 2.2 para tendencias y no para recarga (ver [Cuenca del Volta](../case-studies/volta.md)).

**La concordancia entre ambos vale más que cualquiera por separado.** Una medición y un modelo construido de forma independiente que dicen lo
mismo son difíciles de descartar. Donde discrepen, dibuja las componentes: una divergencia que vive en la SMa es un problema distinto de una que
vive en la TWSa.

El registro de 2.2 empieza diez meses después que el de GRACE, en febrero de 2003, y la solución de GRACE que hay detrás de 2.2 es la del CSR
mientras que las capas de GRACE de la propia aplicación son las del JPL. Ninguna de las dos cosas es un defecto de los datos; ambas aparecerán
cada vez que se superpongan los dos.

## Para qué sirve la GWSa { #what-gwsa-is-good-for }

La GWSa sirve mejor para responder preguntas regionales sobre dirección y tasa: ¿está disminuyendo el almacenamiento en este acuífero, a qué
velocidad, y se desaceleró la disminución después de un cambio de política o de una serie de años húmedos? No es adecuada para decisiones a la
escala de un campo de pozos o de un solo distrito de riego, y no dice nada sobre niveles de agua ni calidad del agua. Donde existan pozos de
monitoreo, compara la tendencia con el cambio de almacenamiento estimado a partir de los pozos; la concordancia entre ambos refuerza a los dos.

Eso vale para cualquiera de los dos conjuntos. Los dos son un cambio de almacenamiento promediado sobre un área mucho mayor que un campo de
pozos, los dos incluyen el agua superficial en el término de agua subterránea, y una comparación basada en pozos es la comprobación más fuerte
disponible para cualquiera de ellos.

## Referencias { #references }

- Rodell, M., et al. (2004). The Global Land Data Assimilation System. *Bulletin of the American Meteorological Society*, 85, 381–394.
  [doi:10.1175/BAMS-85-3-381](https://doi.org/10.1175/BAMS-85-3-381){:target="_blank"}
- Li, B., Rodell, M., Kumar, S., Beaudoing, H. K., Getirana, A., Zaitchik, B. F., et al. (2019). Global GRACE data assimilation for groundwater
  and drought monitoring: Advances and challenges. *Water Resources Research*, 55, 7564–7586.
  [doi:10.1029/2018WR024618](https://doi.org/10.1029/2018WR024618){:target="_blank"}
  La ejecución de GLDAS 2.2 que lee la segunda ruta.
- Barbosa, S. A., Jones, N. L., Williams, G. P., Teklu, H., Yidana, S. M., Pulla, S. T., et al. (2025). A Multi-Source Approach to Groundwater
  Storage and Recharge Assessment in the Volta Basin. *Science of the Total Environment*.
  [doi:10.1016/j.scitotenv.2025.180421](https://doi.org/10.1016/j.scitotenv.2025.180421){:target="_blank"}
  La comparación de las estimaciones de recarga de los dos conjuntos de datos; ver [Cuenca del Volta](../case-studies/volta.md).
- Datos de GLDAS en el NASA GES DISC: [Noah](https://disc.gsfc.nasa.gov/datasets/GLDAS_NOAH025_M_2.1/summary){:target="_blank"},
  [VIC](https://disc.gsfc.nasa.gov/datasets/GLDAS_VIC10_M_2.1/summary){:target="_blank"},
  [CLSM](https://disc.gsfc.nasa.gov/datasets/GLDAS_CLSM10_M_2.1/summary){:target="_blank"},
  [Catchment GRACE-DA1 2.2](https://disc.gsfc.nasa.gov/datasets/GLDAS_CLSM025_DA1_D_2.2/summary){:target="_blank"}
