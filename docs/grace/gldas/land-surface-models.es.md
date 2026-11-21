# Los Modelos de Superficie Terrestre GLDAS

Todo lo que muestra la aplicación que no sea una medición de gravedad viene de GLDAS. El conjunto GRACE + GLDAS 2.1 usa tres modelos de GLDAS
para quitar la nieve, el agua del dosel y la humedad del suelo de lo que miden los satélites. El conjunto GLDAS 2.2 lee el agua subterránea
directamente de una cuarta ejecución de GLDAS. Esta página trata de qué son esos modelos y qué pueden y no pueden representar;
[Cálculo del Almacenamiento de Agua Subterránea](deriving-groundwater.md) da ambos cálculos completos.

## Qué es GLDAS { #what-gldas-is }

El Sistema Global de Asimilación de Datos Terrestres de la NASA produce campos globales de estados y flujos de la superficie terrestre
forzando modelos de superficie terrestre con meteorología observada (Rodell et al., 2004). Los modelos corren **sin acoplamiento**, es decir
que no están acoplados a una atmósfera: la meteorología es un dato de entrada y la tarea del modelo es seguir a dónde va el agua y la energía
una vez que llegan al suelo. GLDAS los ejecuta a través del Land Information System (Kumar et al., 2006).

Los productos que lee la aplicación cubren de 60°S a 90°N y todas las longitudes, en mallas de 1° y 0.25°. La Antártida queda fuera del
dominio, y por eso el mapa global termina en 60°S. GLDAS publica salidas cada 3 horas y diarias, y medias mensuales construidas a partir de
ellas; la aplicación usa las medias mensuales.

La versión 2 de GLDAS se divide en tres partes, y las diferencias entre ellas importan para cómo trata la aplicación a cada una:

| | Forzamiento | Modelos | Periodo | Observaciones asimiladas |
|---|---|---|---|---|
| **GLDAS-2.0** | conjunto meteorológico de Princeton | Noah, VIC, Catchment | 1948–2014 | ninguna |
| **GLDAS-2.1** | NOAA GDAS, GPCP, AGRMET | Noah, VIC, Catchment | 2000–presente | ninguna |
| **GLDAS-2.2** | análisis IFS del ECMWF | solo Catchment | 2003–presente | almacenamiento total de agua de GRACE |

GLDAS-2.0 termina en 2014 y la aplicación no lo usa, salvo que las otras dos versiones arrancaron de su estado y no desde cero. GLDAS-2.0 y
2.1 son de **bucle abierto**: los modelos corren solo con su forzamiento y ninguna observación los corrige por el camino. GLDAS-2.2 es el único
producto de la familia que asimila datos.

## Qué calcula un modelo de superficie terrestre { #what-a-land-surface-model-computes }

El balance de abajo es el mismo en todas las versiones de GLDAS. Lo que cambia entre ellas es qué almacenamientos existen y cuáles toma la
aplicación, y el pie de la figura lo indica para cada una.

![Los almacenamientos y flujos que lleva un modelo de superficie terrestre GLDAS para cada celda de la malla, y lo que aporta a la aplicación cada versión de GLDAS](../../static/images/grace/gldas-water-cycle.png)

Para cada celda y cada paso de tiempo, el modelo toma la meteorología sobre la superficie y resuelve un balance de agua y energía por debajo de
ella. Llegan la lluvia y la nieve. Parte de la lluvia queda retenida en las hojas y se evapora de vuelta; la nieve se acumula y más tarde se
funde; lo que llega al suelo se infiltra, baja por el suelo y vuelve a salir como evaporación, transpiración, escorrentía superficial o drenaje.
Lo que no ha salido al final del paso es almacenamiento, y pasa al paso siguiente.

Los cuatro almacenamientos son la base de la aplicación: el agua del dosel, el equivalente de agua de la nieve, la humedad del suelo y el agua
subterránea. Los tres primeros existen en todos los modelos de GLDAS y los usan ambos conjuntos de datos de la aplicación. El agua subterránea
existe solo en el modelo Catchment, y por eso llega a la aplicación únicamente a través de GLDAS 2.2. Cada almacenamiento se reporta como una
profundidad de agua líquida en kg/m², que equivale a un milímetro, o a una décima de centímetro; la aplicación los convierte todos a
centímetros para poder sumarlos y restarlos con GRACE.

Lo que los modelos dejan fuera acaba en el agua subterránea de la aplicación:

**Sin bombeo ni riego.** GLDAS simula el ciclo natural del agua. Nada en el modelo extrae agua de un acuífero, así que una ejecución de GLDAS
por sí sola no puede producir el agotamiento que es el tema central de esta aplicación. Por eso la ruta 2.1 resta los modelos de una medición y
la ruta 2.2 tiene que asimilar una.

**Sin agua superficial.** No hay ríos, lagos ni embalses. En una cuenca donde un gran embalse se llena y se vacía, ese cambio se cuenta en otra
parte, que en la práctica es el agua subterránea.

**Sin glaciares ni casquetes de hielo.** Ninguno de los modelos de GLDAS los tiene, así que en Groenlandia, en partes del Ártico y en el suelo
permanentemente congelado del Himalaya el equivalente de agua de la nieve se acumula sin límite. La documentación de la NASA para GLDAS versión 2
lo dice sin rodeos y aconseja enmascarar esas celdas.

[Cómo se ven las diferencias](../compare/examples.md) muestra lo que produce cada una de estas tres carencias sobre el mapa.

### Los datos de forzamiento { #the-forcing-data }

Un modelo de superficie terrestre no calcula nada sobre la meteorología; se le entrega la meteorología y resuelve qué hace el suelo con ella.
GLDAS suministra siete campos en cada paso de tiempo:

| Campo | Variable | Unidades |
|---|---|---|
| Tasa de precipitación total | `Rainf_f_tavg` | kg m⁻² s⁻¹ |
| Temperatura del aire | `Tair_f_inst` | K |
| Humedad específica | `Qair_f_inst` | kg kg⁻¹ |
| Presión en superficie | `Psurf_f_inst` | Pa |
| Velocidad del viento | `Wind_f_inst` | m s⁻¹ |
| Radiación de onda corta descendente | `SWdown_f_tavg` | W m⁻² |
| Radiación de onda larga descendente | `LWdown_f_tavg` | W m⁻² |

La precipitación es lo que más importa para el almacenamiento, y es el campo que cada versión de GLDAS trata de forma distinta:

| | Campos atmosféricos | Precipitación | Radiación |
|---|---|---|---|
| **GLDAS-2.0** | conjunto global de forzamiento de Princeton (Sheffield et al., 2006) | Princeton | Princeton |
| **GLDAS-2.1** | análisis GDAS de la NOAA (Derber et al., 1991) | GPCP v1.3 diario, desagregado a 3 horas | AGRMET, ahora GALWEM |
| **GLDAS-2.2** | análisis operativo IFS del ECMWF | IFS del ECMWF | IFS del ECMWF |

La fuente de radiación de 2.1 cambió bajo los pies de la aplicación: AGRMET se construía sobre el World-Wide Merged Cloud Analysis de la Fuerza
Aérea, que dejó de producirse el 8 de junio de 2025, así que desde el 9 de junio de 2025 GLDAS 2.1 se fuerza con la radiación GALWEM del Met
Office del Reino Unido. Los meses anteriores y posteriores a esa fecha se produjeron con entradas de radiación distintas, lo que es una razón
más de que la banda de incertidumbre sea la dispersión entre modelos y no un error publicado.

Dos consecuencias más del forzamiento que conviene llevar a la lectura de los datos. GLDAS 2.1 corrió solo con GDAS y GPCP desde enero de 2000
hasta que se añadió AGRMET el 1 de marzo de 2001, así que sus primeros meses no están forzados igual que el resto; el registro de la aplicación
empieza en abril de 2002 y queda libre de eso. Y como el forzamiento de 2.2 es del ECMWF, cuya licencia no permite a la NASA redistribuirlo, el
producto 2.2 no publica ningún campo meteorológico: se puede ver qué hizo el modelo, pero no qué se le dijo.

Los modelos tampoco llevan encaminamiento entre celdas de la malla. Noah y VIC tratan cada celda como una columna independiente. El modelo
Catchment es la excepción dentro de una celda: divide la tierra en cuencas hidrológicas delimitadas a partir de datos de elevación y
redistribuye el agua dentro de cada una según la topografía (Koster et al., 2000; Ducharne et al., 2000).

## Los tres modelos de GLDAS 2.1 { #the-three-models-of-gldas-21 }

GLDAS 2.1 empezó el 1 de enero de 2000 desde el estado de GLDAS-2.0, forzado como describe la tabla anterior. Ejecuta tres modelos, que
difieren sobre todo en cómo llevan el agua del suelo:

| Modelo | Malla | Humedad del suelo que usa la aplicación |
|---|---|---|
| Noah 3.6 | 0.25° | cuatro capas, 0–200 cm |
| VIC 4.1.2 | 1° | tres capas, profundidades variables según la ubicación |
| Catchment (CLSM-F2.5) | 1° | zona radicular, 0–100 cm |

Ninguno de los tres lleva un almacenamiento de agua subterránea que la aplicación pueda usar. Noah y VIC no tienen ninguno: el agua que drena
por debajo de la capa inferior sale de la columna como flujo base y el modelo deja de seguirla. El modelo Catchment sí lleva agua subterránea,
pero corriendo en bucle abierto no tiene manera de saber del bombeo, así que su agua subterránea sigue a la lluvia y a poco más.

Los tres modelos a menudo discrepan, y la humedad del suelo profunda es donde más. La aplicación los promedia en lugar de elegir uno, lo que
obliga a trabajar en la más gruesa de las tres mallas, la de 1° ([cómo](deriving-groundwater.md#the-gldas-terms)).

### Por qué el modelo Catchment necesita un tratamiento aparte { #why-the-catchment-model-needs-separate-handling }

Noah y VIC reportan la humedad del suelo por capas de profundidad, así que la aplicación suma las capas. El modelo Catchment no tiene capas.
Reporta tres reservorios, y la documentación de la NASA para GLDAS versión 2 es explícita en que están anidados: el perfil incluye la zona
radicular, y la zona radicular incluye la superficie.

| Reservorio | Profundidad | Variable |
|---|---|---|
| Superficie | 0–2 cm | `SoilMoist_S_inst` |
| Zona radicular | 0–100 cm | `SoilMoist_RZ_inst` |
| Perfil | hasta el lecho rocoso, variable celda a celda | `SoilMoist_P_inst` |

El reservorio del perfil baja por debajo del nivel freático, así que contiene el agua subterránea del modelo junto con su humedad del suelo. La
NASA define el agua subterránea del modelo Catchment a partir de ese hecho:

$$
\mathrm{GWS} = \mathrm{TWS} - \mathrm{RootZone} - \mathrm{SWE} - \mathrm{CanopInt}
$$

El almacenamiento total de agua del modelo es el agua de su perfil más la nieve más el dosel, lo que cierra con 5×10⁻⁴ mm en los archivos
publicados. Sustituyendo eso, el agua subterránea queda como la diferencia entre los dos reservorios:

$$
\mathrm{GWS} = \mathrm{SoilMoist\_P} - \mathrm{RootZone}
$$

En el conjunto de la superficie terrestre esa diferencia contiene una mediana de 746 mm de agua: más del triple de lo que contiene la zona
radicular misma.

Por eso la aplicación toma la zona radicular para el modelo Catchment y deja el perfil en paz. Meter el perfil en el término de humedad del
suelo entregaría el agua subterránea del modelo al lado equivocado del balance hídrico: se restaría de lo que midió GRACE, cuando el agua
subterránea es justamente la cantidad que se está despejando. Basta con que un tercio del conjunto lleve agua subterránea en su término de
humedad del suelo para amortiguar el resultado en todas partes.

Esto también alinea los dos conjuntos de datos entre sí. La ruta 2.2 parte del mismo modelo y resta su agua subterránea del perfil, y por la
identidad de arriba `SoilMoist_P − GWS` *es* la zona radicular. Las capas de humedad del suelo de ambos conjuntos describen por tanto el mismo
reservorio del mismo modelo.

Lo que el cambio no arregla es la profundidad. Noah suma 0–200 cm, la zona radicular de Catchment se detiene en 100 cm y las dos capas
inferiores de VIC varían según la ubicación, así que el conjunto sigue promediando tres columnas de suelo distintas. Esa es una discrepancia
ordinaria entre modelos, del tipo que la dispersión entre ellos está ahí para expresar, y es cosa distinta de contar el agua subterránea como
humedad del suelo.

## GLDAS 2.2 y la corrección de GRACE { #gldas-22-and-the-grace-correction }

![Cómo difieren las rutas 2.1 y 2.2 hacia el agua subterránea](../../static/images/grace/gldas-2.1-vs-2.2.png)

GLDAS 2.2 es un único producto diario: el modelo Catchment a 0.25°, arrancado el 1 de febrero de 2003 desde el estado de Catchment de
GLDAS-2.0.

Lo que lo hace distinto es que la anomalía del almacenamiento total de agua medida por GRACE se asimila en la ejecución (Li et al., 2019), a
través de la maquinaria de asimilación del Land Information System (Kumar et al., 2016). El modelo Catchment se eligió para esto por cómo
maneja el agua bajo la superficie: lleva un déficit de agua de la cuenca que hace de equivalente de la profundidad al nivel freático, así que el
agua subterránea es un estado que el modelo propaga en lugar de una cantidad que se infiere después. Eso es lo que le da a la asimilación un
lugar donde poner una corrección.

GRACE mide la columna entera y no puede ver a qué almacenamiento pertenece una discrepancia, así que el esquema distribuye la corrección de cada
mes entre los almacenamientos del modelo, el agua subterránea incluida. El agotamiento por bombeo llega al estado de agua subterránea de 2.2
solo por esta vía. La física del modelo sigue sin tener pozos.

La solución de GRACE que se asimila en 2.2 es el producto de mascones del **CSR** (Save et al., 2012, 2016), mientras que las capas de GRACE de
la propia aplicación usan los mascones del **JPL**. Las dos rutas hacia el agua subterránea no se apoyan por tanto en la misma solución de
GRACE, y no coincidirán exactamente ni siquiera donde ambas funcionen bien.

## La salida, y de dónde la toma la aplicación { #output-and-where-the-app-gets-it }

GLDAS publica con pasos de 3 horas y diarios, con medias mensuales construidas a partir de los archivos de 3 horas. Lo que existe difiere según
la versión, y la aplicación toma el valor mensual en cualquier caso:

| | Publicado como | Resoluciones | La aplicación lee |
|---|---|---|---|
| **GLDAS-2.0** | 3 horas, diario, mensual | 1°, 0.25° | nada |
| **GLDAS-2.1** | 3 horas, mensual | 1°, 0.25° | los archivos mensuales |
| **GLDAS-2.2** | solo diario | 0.25° | los archivos diarios, promediados a meses calendario |

Los archivos de 2.1 vienen del archivo GES DISC como NetCDF-4, uno por modelo y por mes: `GLDAS_NOAH025_M.2.1`, `GLDAS_VIC10_M.2.1` y
`GLDAS_CLSM10_M.2.1`. Se necesita una cuenta de Earthdata Login para descargarlos, y también son accesibles por Earthdata Search, OPeNDAP,
THREDDS y el subsetter de GES DISC.

GLDAS 2.2 no tiene producto mensual, así que la aplicación construye uno. Lee la colección diaria `GLDAS_CLSM025_DA1_D.2.2` a través de Google
Earth Engine, que lleva los mismos campos, promedia cada mes calendario y guarda el resultado. Por eso el registro de 2.2 en la aplicación es
mensual como todo lo demás y no diario.

Las dos versiones van por detrás del presente: el flujo de producción principal de 2.1 de tres a cuatro meses, el de 2.2 de dos a seis, porque
espera el campo de GRACE que asimila. Cada una tiene además un flujo temprano a unos 1.5 meses, que para 2.2 significa ninguna asimilación de
GRACE. La aplicación lee los flujos principales, así que el mes más reciente que muestra tiene algunos meses y todos los meses de 2.2 que
contiene están corregidos.

## Exactitud, y mezclar versiones { #accuracy-and-mixing-versions }

La NASA enumera cuatro fuentes de error en las estimaciones de GLDAS: la incertidumbre del forzamiento meteorológico, que es peor en latitudes
altas, a gran altitud y donde las estaciones meteorológicas son escasas; las representaciones simplificadas de procesos complejos en los
modelos; los errores en los parámetros de superficie terrestre que describen la vegetación, los suelos y la elevación; y la calibración
insuficiente de los parámetros del modelo. Ninguna de ellas se reporta como un número junto a los datos, y por eso la banda de incertidumbre de
la aplicación para la ruta 2.1 se construye a partir de la dispersión entre los tres modelos y no de nada que publique la NASA.

La NASA también advierte contra unir las versiones de GLDAS en una sola serie temporal: sus conjuntos de forzamiento están sesgados unos
respecto a otros, y la asimilación cambia tanto los estados como los flujos en 2.2. La aplicación nunca los empalma. Cada conjunto de datos es
su propio registro de principio a fin, y cuando se muestran los dos en un gráfico se dibujan como series separadas. Sí comparten la línea base
2004–2009, que es lo que los pone en un cero común y hace legible la comparación; lo que se mantiene aparte son los registros, no el periodo de
referencia.

## Referencias { #references }

- Rodell, M., Houser, P. R., Jambor, U., Gottschalck, J., Mitchell, K., Meng, C.-J., et al. (2004). The Global Land Data Assimilation System.
  *Bulletin of the American Meteorological Society*, 85(3), 381–394.
  [doi:10.1175/BAMS-85-3-381](https://doi.org/10.1175/BAMS-85-3-381){:target="_blank"}

- Li, B., Rodell, M., Kumar, S., Beaudoing, H. K., Getirana, A., Zaitchik, B. F., et al. (2019). Global GRACE data assimilation for groundwater
  and drought monitoring: Advances and challenges. *Water Resources Research*, 55, 7564–7586.
  [doi:10.1029/2018WR024618](https://doi.org/10.1029/2018WR024618){:target="_blank"}
  El estudio del que salió GLDAS 2.2, y la referencia de lo que la asimilación le hace al agua subterránea.

- Kumar, S. V., Zaitchik, B. F., Peters-Lidard, C., Rodell, M., Reichle, R., Li, B., et al. (2016). Assimilation of gridded GRACE terrestrial
  water storage estimates in the North American Land Data Assimilation System. *Journal of Hydrometeorology*, 17(7), 1951–1972.
  [doi:10.1175/JHM-D-15-0157.1](https://doi.org/10.1175/JHM-D-15-0157.1){:target="_blank"}

- Koster, R. D., Suarez, M. J., Ducharne, A., Stieglitz, M., and Kumar, P. (2000). A catchment-based approach to modeling land surface processes
  in a general circulation model: 1. Model structure. *Journal of Geophysical Research*, 105(D20), 24809–24822.
  [doi:10.1029/2000JD900327](https://doi.org/10.1029/2000JD900327){:target="_blank"}

- Ducharne, A., Koster, R. D., Suarez, M. J., Stieglitz, M., and Kumar, P. (2000). A catchment-based approach to modeling land surface processes
  in a general circulation model: 2. Parameter estimation and model demonstration. *Journal of Geophysical Research*, 105(D20), 24823–24838.
  [doi:10.1029/2000JD900328](https://doi.org/10.1029/2000JD900328){:target="_blank"}

- Rui, H., and Beaudoing, H. (2025). *README Document for NASA GLDAS Version 2 Data Products*. NASA GES DISC.
  [hydro1.gesdisc.eosdis.nasa.gov](https://hydro1.gesdisc.eosdis.nasa.gov/data/GLDAS/GLDAS_CLSM025_DA1_D.2.2/doc/README_GLDAS2.pdf){:target="_blank"}
  La documentación propia de la NASA para los productos GLDAS, y la fuente del forzamiento, los periodos de registro, las versiones de los
  modelos y las advertencias de esta página. Su sección «Data Interpretation» es de donde vienen el anidamiento de los tres reservorios de
  humedad del suelo del modelo Catchment y la definición de su almacenamiento de agua subterránea.

- Datos de GLDAS en el NASA GES DISC: [Noah](https://disc.gsfc.nasa.gov/datasets/GLDAS_NOAH025_M_2.1/summary){:target="_blank"},
  [VIC](https://disc.gsfc.nasa.gov/datasets/GLDAS_VIC10_M_2.1/summary){:target="_blank"},
  [CLSM](https://disc.gsfc.nasa.gov/datasets/GLDAS_CLSM10_M_2.1/summary){:target="_blank"},
  [Catchment GRACE-DA1 2.2](https://disc.gsfc.nasa.gov/datasets/GLDAS_CLSM025_DA1_D_2.2/summary){:target="_blank"}
