# Cálculo del Almacenamiento de Agua Subterránea

## El balance hídrico { #the-water-balance }

GRACE mide el cambio total del agua almacenada en una columna de la Tierra. Para aislar el agua subterránea, la aplicación resta las partes de ese
total que pueden estimarse por otros medios:

![Componentes del almacenamiento terrestre de agua](../../static/images/grace/grace-water-balance.png)

La TWSa es la suma de las anomalías de todos los almacenamientos de la columna: el equivalente de agua de la nieve (SWEa), el agua retenida en el
dosel vegetal (CANa), la humedad del suelo (SMa), el agua subterránea (GWSa) y el agua superficial en ríos, lagos y embalses. Los modelos de
superficie terrestre estiman bien los tres primeros. Al restarlos queda el agua subterránea:

$$
\mathrm{GWSa} = \mathrm{TWSa} - (\mathrm{SWEa} + \mathrm{CANa} + \mathrm{SMa})
$$

La aplicación deja el agua superficial fuera del balance, así que cualquier cambio en el almacenamiento de agua superficial termina en la GWSa. En
la mayor parte del mundo los cambios de agua superficial son pequeños frente a los demás términos. En regiones con grandes embalses, humedales o
ríos con grandes crecidas (el Amazonas, el Ganges y el Brahmaputra, el mar Caspio, el lago Victoria, el lago Volta), la GWSa incluye esos cambios
y exagera la oscilación estacional del agua subterránea. En la Cuenca del Volta, por ejemplo, el lago representa cerca de la mitad de la señal
total de almacenamiento ([caso de estudio](../case-studies/volta.md)).

## Modelos de superficie terrestre GLDAS { #gldas-land-surface-models }

El Sistema Global de Asimilación de Datos Terrestres (GLDAS) de la NASA ejecuta modelos de superficie terrestre forzados con precipitación,
radiación y meteorología observadas para estimar cuánta agua almacena la superficie terrestre cada mes. La aplicación usa tres modelos de GLDAS
versión 2.1, que difieren en cómo representan las capas del suelo y la escorrentía:

| Modelo | Malla | Humedad del suelo utilizada |
|---|---|---|
| Noah | 0.25° | cuatro capas, 0–200 cm |
| VIC (Variable Infiltration Capacity) | 1° | tres capas, profundidades variables según la ubicación |
| CLSM (Catchment Land Surface Model) | 1° | perfil total del suelo |

De cada modelo la aplicación toma el equivalente de agua de la nieve, el almacenamiento por intercepción del dosel y la humedad del suelo, los
convierte de kg/m² a cm de agua y lleva los tres modelos a la misma malla de 1° (Noah se promedia de 0.25° a 1°). La anomalía de cada modelo es su
valor menos la media de esa celda para 2004–2009, la misma línea base que GRACE.

Los tres modelos a menudo discrepan, en particular sobre la humedad del suelo profunda. En lugar de elegir uno, la aplicación los promedia: SWEa,
CANa y SMa son cada una la media de los tres modelos, y la dispersión entre los modelos (su desviación estándar) se usa como la incertidumbre de
cada término.

## Cadena de procesamiento { #processing-chain }

![Cadena de procesamiento de GRACE Regional Analyst](../../static/images/grace/grace-processing.png)

La TWSa de GRACE se promedia de 0.5° a 1° y se combina con el conjunto de modelos para obtener la GWSa en una malla de 1°. La aplicación ofrece
cinco capas: GWSa, SMa, SWEa y CANa a 1°, y TWSa a 0.5° tal como la distribuye JPL. Usar 1° para las capas derivadas sigue la práctica habitual
de combinar GRACE con datos de modelos en la más gruesa de las dos mallas; reportar la GWSa a 0.5° daría una impresión de detalle que ninguno de
los dos conjuntos de datos tiene.

No se rellena ningún vacío. Cada valor mensual en la aplicación es el valor publicado por JPL, escalado como se describe más abajo,
combinado con el conjunto de GLDAS para ese mes.

### Factores de ganancia { #gain-factors }

La solución mascon es nativamente de 3°, y el archivo de 0.5° repite el valor de cada mascon en sus 36 celdas, así que la malla publicada por sí
sola no contiene ningún detalle más fino que un mascon. JPL distribuye en el mismo archivo una malla de **factores de ganancia** para recuperar
parte de ese detalle. Se obtienen pasando el modelo de superficie terrestre CLM por el mismo procesamiento que atraviesa GRACE y estimando, celda
por celda, el multiplicador que restituye la amplitud original del modelo. La corrección es una sola multiplicación, con el factor constante en el
tiempo:

$$
g'(x,y,t) = g(x,y,t) \times s(x,y)
$$

JPL no aplica este escalado antes de distribuir los datos; el GRACE-FO Level-3 Handbook indica que son los usuarios quienes deben aplicarlo, y su
propio ejemplo de agua subterránea sigue el mismo enfoque de TWSa menos GLDAS que usa esta aplicación, con la multiplicación como paso de
preprocesamiento. La aplicación aplica los factores a la TWSa a 0.5°, antes de promediarla a 1°, porque la estructura que añaden es más fina que
una celda de 1°.

La mayoría de los factores son cercanos a 1: cerca del 83% está entre 0.5 y 1.5. Una celda conserva el valor del mascon sin escalar en dos casos.

**Donde JPL no publica ningún factor.** Eso es el océano, que de todos modos elimina la máscara de tierra de GLDAS, y el hielo: toda la Antártida
y el 18% de la tierra al norte de 60°N. Los factores no están pensados para el hielo, porque CLM no representa los casquetes de hielo ni los
glaciares de montaña. Esto abarca el 5.6% de las celdas que dibuja la aplicación.

**Donde el factor es implausible**, es decir cero o negativo, o mayor que 3. Son 1,604 celdas en la malla de 0.5°, el 0.74% del total, y es una
regla de la aplicación y no de JPL: el archivo marca todo su rango como válido y no fija ningún límite.

Lo que estas celdas tienen en común es que la regresión que produce el factor apenas tenía señal con la que trabajar, así que su pendiente es
inestable. Son costeras unas tres veces más a menudo que las celdas que se conservan (51% a menos de dos celdas del agua, frente al 19%) y tienen
nieve todo el año trece veces más a menudo (18.5% frente al 1.4%). Casi la mitad no es ni lo uno ni lo otro, y se sitúa en interiores áridos —el
Kalahari, el interior de Australia, el Karoo, el Atacama— donde la variación de almacenamiento de CLM es lo bastante pequeña como para que el
ajuste divida por casi nada. Hielo, costa y desierto son el mismo fallo en tres escenarios, y por eso un límite sobre el factor los detecta donde
una máscara de glaciares por sí sola no lo haría.

Los factores en estas celdas llegan hasta 24 y −1.35. Un factor negativo invierte el signo de la anomalía; un factor de 24 convirtió −292 cm en
−7048 cm en la isla de Ellesmere. En las cuencas áridas la exclusión es inocua en cualquier caso —cuatro de las 806 celdas de la Gran Cuenca
Artesiana, que mueven su serie 0.00 cm— porque una anomalía pequeña multiplicada por un factor malo sigue siendo pequeña.

Sí importa en al menos un lugar que un usuario notaría. Una de esas celdas cae dentro de la **Cuenca del Cáucaso Norte**, un acuífero de los
propios conjuntos de regiones de la aplicación. Aplicar todos los factores duplicó la serie de agua subterránea de esa cuenca: la desviación
estándar de su media pasó de 13.3 cm sin escalar a 23.5 cm, y queda en 13.6 cm cuando las celdas implausibles se dejan en paz. Casi toda esa
amplitud aparente eran unas pocas celdas degeneradas, no señal. La ganancia que los factores existen para restituir sobrevive a la regla: el Valle
Central de California la conserva entera, de 10.2 cm a 12.4 cm, y el Congo casi toda, de 7.6 cm sin escalar a 7.9 cm frente a 8.1 cm con todos
los factores aplicados.

Dos cuencas glaciares de los conjuntos de cuencas hidrográficas, Alsek y Santa Cruz, presentan una GWSa muy grande independientemente de lo que
se haga con los factores de ganancia. GRACE detecta ahí la pérdida de masa de hielo y GLDAS no modela glaciares, así que el balance hídrico la
atribuye al agua subterránea. Esos números son un artefacto del método, no del escalado.

Lo que los factores no hacen es convertir la malla de 0.5° en 36 mediciones independientes. El mascon subyacente sigue siendo una sola
estimación, y los factores redistribuyen su amplitud usando la idea que un modelo tiene de cómo varía el almacenamiento dentro de él. El handbook
es explícito en que los modelos que están detrás arrastran sesgos y «por lo general no incluyen el agua subterránea ni las actividades humanas en
sus simulaciones», así que un acuífero con bombeo intenso es precisamente donde la redistribución está menos informada por lo que se mide.

## Incertidumbre { #uncertainty }

Cada capa de la aplicación viene con una incertidumbre de una desviación estándar (1σ), que el gráfico de series temporales dibuja como una banda
alrededor de la línea:

- **TWSa:** la incertidumbre publicada por JPL para cada mascon y mes, multiplicada por el mismo factor de ganancia que los datos, de modo que
  la banda se mantiene en proporción al valor que describe.
- **SWEa, CANa, SMa:** la desviación estándar entre los tres modelos de GLDAS.
- **GWSa:** las cuatro combinadas, tratándolas como independientes:

$$
\sigma_{\mathrm{GWSa}} = \sqrt{\sigma_{\mathrm{TWSa}}^2 + \sigma_{\mathrm{SWEa}}^2 + \sigma_{\mathrm{CANa}}^2 + \sigma_{\mathrm{SMa}}^2}
$$

La banda de incertidumbre recoge el error de medición de GRACE y el desacuerdo entre modelos. No recoge los errores que comparten los tres
modelos, el efecto de dejar fuera el agua superficial, la fuga de señal desde fuera de una región (ver
[Resolución, Fuga de Señal y Regiones Pequeñas](resolution-and-leakage.md)) ni la incertidumbre de los propios factores de ganancia, que JPL no
publica. La incertidumbre real es mayor que la que muestra la banda.

Una advertencia sobre combinarlas: la incertidumbre de la TWSa de JPL es un error de medición, mientras que los tres términos de GLDAS son la
dispersión entre Noah, VIC y CLSM, que mide cuánto discrepan los modelos y no cuánto se equivocan. Sumarlas en cuadratura trata ambas cosas como
comparables. En la mayoría de las cuencas domina la dispersión entre modelos: en el Congo, 3.1 cm de GRACE frente a 5.7 cm combinados.

## Para qué sirve la GWSa { #what-gwsa-is-good-for }

La GWSa sirve mejor para responder preguntas regionales sobre dirección y tasa: ¿está disminuyendo el almacenamiento en este acuífero, a qué
velocidad, y se desaceleró la disminución después de un cambio de política o de una serie de años húmedos? No es adecuada para decisiones a la
escala de un campo de pozos o de un solo distrito de riego, y no dice nada sobre niveles de agua ni calidad del agua. Donde existan pozos de
monitoreo, compara la tendencia de GRACE con el cambio de almacenamiento estimado a partir de los pozos; la concordancia entre ambos refuerza a
los dos.

## Referencias { #references }

- Rodell, M., et al. (2004). The Global Land Data Assimilation System. *Bulletin of the American Meteorological Society*, 85, 381–394.
  [doi:10.1175/BAMS-85-3-381](https://doi.org/10.1175/BAMS-85-3-381){:target="_blank"}
- Datos de GLDAS en el NASA GES DISC: [Noah](https://disc.gsfc.nasa.gov/datasets/GLDAS_NOAH025_M_2.1/summary){:target="_blank"},
  [VIC](https://disc.gsfc.nasa.gov/datasets/GLDAS_VIC10_M_2.1/summary){:target="_blank"},
  [CLSM](https://disc.gsfc.nasa.gov/datasets/GLDAS_CLSM10_M_2.1/summary){:target="_blank"}
