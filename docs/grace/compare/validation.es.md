# Hasta dónde está validado

[Cuál usar](which-one-to-use.md) hace recomendaciones. Esta página dice sobre qué se apoyan, para que pueda juzgar cuánto peso dar a cada una.

## Qué establece la comparación de estas páginas { #what-the-comparison-on-these-pages-establishes }

Las cifras de [Por qué difieren los dos conjuntos](why-they-differ.md) y [Cómo se ven las diferencias](examples.md) salen de comparar los dos
conjuntos publicados entre sí. Eso establece cómo difieren, en cuánto y a través de qué término. No resuelve nada sobre cuál está más cerca del
nivel freático, porque en esa comparación ninguno se contrasta con niveles de agua en ninguna parte.

Que dos conjuntos discrepen dice que al menos uno está equivocado. No dice cuál.

## Dónde se ha consultado realmente a los pozos { #where-wells-have-actually-been-consulted }

Dos estudios han comparado estos conjuntos con niveles de agua subterránea observados. Ambos son trabajo de nuestro grupo con colaboradores,
ambos están publicados y ambos son de una sola región.

### El Valle Central de California { #californias-central-valley }

Stevens et al. (2025) construyeron un registro de almacenamiento a partir de pozos de las bases de datos del USGS y del Departamento de Recursos
Hídricos de California, rellenado con un esquema de aprendizaje automático y convertido a almacenamiento con el mapa de rendimiento específico
del Central Valley Hydrologic Model del USGS. Con un umbral de 75 meses de registro (572 pozos) la curva basada en pozos se ajustó estrechamente
a ese modelo calibrado, con r² = 0,87 y RMSE 9,04 km³.

Frente a ese registro, el agua subterránea de GRACE en la aplicación seguía bien el calendario — r² = 0,725 en 2002–2021 — y resultaba varias
veces demasiado pequeña. El estudio calibró un factor de escala de unos 5 (± 1,0) para alinearla. GLDAS 2.2, que pierde 6 cm a lo largo del
registro donde la ruta de GRACE pierde 32, es el más alejado de los tres de lo que muestran los pozos.

Véase [Valle Central](../case-studies/central-valley.md) para el método y las figuras.

### La cuenca del Volta { #the-volta-basin }

Barbosa et al. (2025) estimaron la recarga con el método de fluctuación del nivel freático a partir de ambos conjuntos y compararon el resultado
con pozos:

| Fuente | Recarga |
|:---|:---:|
| Ruta de GRACE, método WTF 1 | 5,8 cm/año |
| Ruta de GRACE, método WTF 2 | 10,7 cm/año |
| Pozos de la subcuenca de Nasia, rendimiento específico 0,05 | 10,4 cm/año |
| Obuobie et al. (2012), una estimación independiente anterior | 8,6 cm/año |
| GLDAS 2.2, método WTF 1 | 17,4 cm/año |
| GLDAS 2.2, método WTF 2 | 36,1 cm/año |

La ruta de GRACE deja la cifra basada en pozos entre sus dos métodos. GLDAS 2.2 queda muy por encima de todas las demás estimaciones. Ese estudio
es la base para recomendar GRACE para recarga.

Véase [Cuenca del Volta](../case-studies/volta.md), que además muestra que el lago Volta explica cerca de la mitad de la señal de almacenamiento
de la cuenca.

## La evidencia tras cada recomendación { #the-evidence-behind-each-recommendation }

### 2.2 aplana las tendencias { #22-flattens-trends }

El apoyo más fuerte viene del equipo que construyó GLDAS 2.2. Li et al. (2019) validaron la asimilación con datos in situ de unos 4000 pozos y
encontraron que mejoraba sobre el modelo solo: errores un 36 % menores y correlación un 16 % mayor a escala regional, y un 10 % y un 22 % en
puntos individuales. También enuncian su límite con claridad — la asimilación **no puede compensar la ausencia de un esquema de extracción de
agua subterránea en el modelo Catchment en zonas de bombeo intenso.** Ese es el mecanismo detrás de cada fila de la tabla de tendencias, dicho
por los propios autores del producto.

Scanlon et al. (2018) encontraron el mismo déficit en los modelos en general: siete modelos globales de superficie terrestre y de recursos
hídricos frente a GRACE en 186 cuencas fluviales, 2002–2014, con las medianas de los modelos subestimando con mucho tanto las grandes tendencias
descendentes que ve GRACE (≤ −0,5 km³/año) como las ascendentes (≥ 0,5 km³/año). Sumados sobre las cuencas, los modelos daban una tendencia
negativa del almacenamiento terrestre donde GRACE daba una positiva.

Lo que esto no establece es el tamaño de la tendencia correcta. Apoya preferir GRACE sobre 2.2 para un ritmo de cambio; no dice que la cifra de
GRACE sea la buena. El Valle Central es el único lugar donde se ha consultado a los pozos, y allí GRACE mismo resultó varias veces demasiado
pequeño.

### El método residual es estructuralmente frágil { #the-residual-method-is-structurally-shaky }

Getirana, Kumar y Rodell (2025) examinan el supuesto que hay tras la ruta de GRACE: que los almacenes de humedad del suelo, nieve y dosel de un
modelo de superficie terrestre son compartimentos distintos y físicamente significativos que contienen exactamente el agua que sus etiquetas
implican. Sostienen que las simplificaciones y las convenciones de nomenclatura de los modelos rompen ese supuesto, y recomiendan modelos que
representen el subsuelo de forma más completa con asimilación de datos — lo que describe a GLDAS 2.2.

Es un argumento sobre cómo se construyen los modelos, no una medición contra pozos. El patrón de la proporción de humedad del suelo en 299
acuíferos de [Cómo se ven las diferencias](examples.md) es coherente con él, pero coherencia no es confirmación: ningún registro de pozos
establece que el calendario estacional de 2.2 sea el correcto en ninguno de esos acuíferos.

### Las dos soluciones GRACE coinciden a escala de cuenca y divergen en tendencias { #the-two-grace-solutions-agree-at-basin-scale-and-diverge-on-trends }

Scanlon et al. (2016) compararon los productos mascon de CSR y JPL en 176 cuencas fluviales y encontraron que sus registros de agua total se
seguían de cerca, con las tendencias a largo plazo como la parte que aún diverge. Por eso la diferencia de construcción importa más para
tendencias y menos para el calendario, y los dos conjuntos de esta aplicación se comportan igual.

### Comparar cualquiera de estas cosas con pozos es más difícil de lo que parece { #comparing-any-of-this-against-wells-is-harder-than-it-sounds }

Chen, Famiglietti, Scanlon y Rodell (2016) señalan que convertir niveles de pozo en almacenamiento exige un rendimiento específico para cada
pozo, que es a su vez incierto incluso donde la red de monitoreo es densa. Bhanja et al. (2016) llevaron a cabo una comparación así en la India.
Tanto el estudio del Valle Central como el del Volta dependen de un rendimiento específico, así que su coincidencia arrastra esa incertidumbre.

## Cuánto peso soporta cada recomendación { #how-much-weight-each-recommendation-carries }

| Recomendación | Se apoya en | Fuerza |
|:---|:---|:---|
| Usar GRACE para el tamaño de una tendencia | Li et al. (2019) sobre el esquema de extracción ausente, Scanlon et al. (2018) en 186 cuencas, y las proporciones medidas aquí | fuerte en dirección, débil en magnitud |
| Usar GRACE para recarga | Barbosa et al. (2025) frente a pozos en una cuenca | una región, un método |
| Preferir 2.2 para la forma estacional donde la humedad del suelo oscila tanto como el agua total | Getirana et al. (2025) sobre la construcción, y el patrón en 299 acuíferos | el mecanismo está bien argumentado, ningún registro de pozos confirma qué calendario es el correcto |
| Usar 2.2 para regiones pequeñas y series sin interrupciones | las mallas publicadas y los periodos de registro | un hecho de los productos, no un hallazgo |
| Informar ambos cuando importe | — | una práctica, no un resultado |

## Qué sigue sin validar { #what-is-still-unvalidated }

Ninguno de los estudios anteriores evaluó estos dos conjuntos de la aplicación entre sí, y ninguno usó esta aplicación. La validación directa con
pozos llega al Valle Central y a la cuenca del Volta y ahí se detiene — dos regiones de los cientos que cubre la aplicación, ambas en el trabajo
de un solo grupo.

En particular, nada de lo aquí expuesto establece:

- cuál conjunto acierta el calendario estacional en un acuífero con nivel freático somero
- si el problema de escala de la ruta de GRACE en el Valle Central se generaliza a otros acuíferos estrechos
- cómo se comporta cualquiera de los dos en el trópico húmedo, en permafrost o allí donde el agua superficial es gran parte de la señal
- una incertidumbre para GLDAS 2.2, ya que la NASA no publica ninguna y es una única corrida de modelo, no un conjunto

Trate las recomendaciones como razonamiento a partir de cómo se construye cada conjunto y del comportamiento medido, respaldado por la literatura
sobre cada mecanismo, y no como una clasificación validada. Donde tenga pozos, úselos: esa comparación supera a todo lo de esta página.

## Referencias { #references }

- Barbosa, S. A., Jones, N. L., Williams, G. P., Teklu, H., Yidana, S. M., Pulla, S. T., et al. (2025). A Multi-Source Approach to Groundwater
  Storage and Recharge Assessment in the Volta Basin. *Science of the Total Environment*.
  [doi:10.1016/j.scitotenv.2025.180421](https://doi.org/10.1016/j.scitotenv.2025.180421){:target="_blank"}
- Bhanja, S. N., Mukherjee, A., Saha, D., Velicogna, I., y Famiglietti, J. S. (2016). Validation of GRACE based groundwater storage anomaly
  using in-situ groundwater level measurements in India. *Journal of Hydrology*, 543, 729–738.
  [doi:10.1016/j.jhydrol.2016.10.042](https://doi.org/10.1016/j.jhydrol.2016.10.042){:target="_blank"}
- Chen, J., Famiglietti, J. S., Scanlon, B. R., y Rodell, M. (2016). Groundwater Storage Changes: Present Status from GRACE Observations.
  *Surveys in Geophysics*, 37, 397–417. [doi:10.1007/s10712-015-9332-4](https://doi.org/10.1007/s10712-015-9332-4){:target="_blank"}
- Getirana, A., Kumar, S., y Rodell, M. (2025). Inconsistencies in GRACE-Based Groundwater Storage Estimation — A Call for a Proper Use of
  Land Surface Models. *Geophysical Research Letters*, 52, e2025GL119197.
  [doi:10.1029/2025GL119197](https://doi.org/10.1029/2025GL119197){:target="_blank"}
- Li, B., Rodell, M., Kumar, S., Beaudoing, H. K., Getirana, A., Zaitchik, B. F., et al. (2019). Global GRACE Data Assimilation for Groundwater
  and Drought Monitoring: Advances and Challenges. *Water Resources Research*, 55, 7564–7586.
  [doi:10.1029/2018WR024618](https://doi.org/10.1029/2018WR024618){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Wiese, D. N., Landerer, F. W., Long, D., Longuevergne, L., y Chen, J. (2016). Global evaluation of new
  GRACE mascon products for hydrologic applications. *Water Resources Research*, 52, 9412–9429.
  [doi:10.1002/2016WR019494](https://doi.org/10.1002/2016WR019494){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Sun, A. Y., Müller Schmied, H., van Beek, L. P. H., et al. (2018). Global models underestimate large
  decadal declining and rising water storage trends relative to GRACE satellite data. *Proceedings of the National Academy of Sciences*, 115(6),
  E1080–E1089. [doi:10.1073/pnas.1704665115](https://doi.org/10.1073/pnas.1704665115){:target="_blank"}
- Stevens, M. D., Ramirez, S. G., Martin, E.-M. H., Jones, N. L., Williams, G. P., Adams, K. H., Ames, D. P., y Pulla, S. T. (2025).
  Groundwater storage loss in the Central Valley analysis using a novel method based on in situ data compared to GRACE-derived data.
  *Environmental Modelling & Software*, 186, 106368.
  [doi:10.1016/j.envsoft.2025.106368](https://doi.org/10.1016/j.envsoft.2025.106368){:target="_blank"}
