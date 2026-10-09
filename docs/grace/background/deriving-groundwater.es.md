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

No se aplican factores de ganancia ni de escala a los datos de GRACE, y no se rellena ningún vacío. Cada valor mensual en la aplicación es el
valor publicado por JPL combinado con el conjunto de GLDAS para ese mes.

## Incertidumbre { #uncertainty }

Cada capa de la aplicación viene con una incertidumbre de una desviación estándar (1σ), que el gráfico de series temporales dibuja como una banda
alrededor de la línea:

- **TWSa:** la incertidumbre publicada por JPL para cada mascon y mes.
- **SWEa, CANa, SMa:** la desviación estándar entre los tres modelos de GLDAS.
- **GWSa:** las cuatro combinadas, tratándolas como independientes:

$$
\sigma_{\mathrm{GWSa}} = \sqrt{\sigma_{\mathrm{TWSa}}^2 + \sigma_{\mathrm{SWEa}}^2 + \sigma_{\mathrm{CANa}}^2 + \sigma_{\mathrm{SMa}}^2}
$$

La banda de incertidumbre recoge el error de medición de GRACE y el desacuerdo entre modelos. No recoge los errores que comparten los tres
modelos, el efecto de dejar fuera el agua superficial ni la fuga de señal desde fuera de una región (ver
[Resolución, Fuga de Señal y Regiones Pequeñas](resolution-and-leakage.md)), así que la incertidumbre real es mayor que la que muestra la banda.

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
