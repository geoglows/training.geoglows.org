# Por qué difieren los dos conjuntos

La aplicación sirve dos registros de agua subterránea para el mismo mes y la misma celda, y no concuerdan. Esta página trata de dónde viene el
desacuerdo. [Cuándo fiarse de cada uno](trusting-each-one.md) trata de a cuál creer, y [Artefactos conocidos](known-artifacts.md) recoge los
lugares donde uno de los dos sencillamente se equivoca.

[Cálculo del almacenamiento de agua subterránea](../gldas/deriving-groundwater.md) da las dos construcciones completas. En resumen:

- **La ruta de GRACE.** El JPL mide el almacenamiento total de agua. La aplicación resta la humedad del suelo, la nieve y el agua del dosel de
  GLDAS 2.1, y lee el resto como agua subterránea.
- **La ruta de GLDAS 2.2.** La NASA corre el modelo de superficie terrestre Catchment con GRACE asimilado dentro, y el modelo informa un estado
  de agua subterránea directamente. No se resta nada.

## Lo que ya difiere antes de contar una sola gota { #what-already-differs-before-any-water-is-counted }

| | Ruta de GRACE | GLDAS 2.2 |
|---|---|---|
| Solución de GRACE | mascones del JPL, RL06.3 v04 CRI | mascones del CSR, RL06 |
| Huella nativa de GRACE | calotas de 3° de área igual | 1° de área igual en el ecuador |
| Malla servida | 1° | 0.25°, promediada a 1° para la malla global |
| El registro empieza | abril de 2002 | febrero de 2003 |
| Meses faltantes | los vacíos de GRACE, rellenos o marcados | ninguno; el modelo los atraviesa sin corregir |
| Factores de ganancia | los del JPL, aplicados | ninguno |
| Capas de incertidumbre | publicadas por celda | ninguna |
| Celdas de tierra en la malla de 1° | 15,159 | 17,346 |

El inicio del registro y la máscara de tierra son contabilidad, y aparecen como datos faltantes y no como desacuerdo. Todas las demás filas
cambian los números.

## Dos grupos, un par de satélites { #two-groups-one-pair-of-satellites }

GRACE nunca midió agua. Midió la distancia entre dos satélites, con precisión de unas micras, mientras caían alrededor de la Tierra y la masa de
abajo tiraba de ellos. Recuperar un mapa de masa a partir de ese registro está indeterminado —muchas distribuciones de masa distintas encajan con
las mismas órbitas—, así que cada centro de procesamiento impone supuestos adicionales para llegar a una respuesta única. El JPL y el CSR imponen
supuestos distintos.

| | JPL | CSR |
|---|---|---|
| Resuelto sobre | calotas esféricas de 3° de área igual | malla geodésica de área igual, 1° en el ecuador |
| Entregado en | 0.5° | 0.25° |
| Regularización | restricción informada por un modelo de superficie terrestre | restricción derivada solo de los datos de GRACE, con el parámetro elegido por una L-ribbon |
| Costas | un filtro CRI separa tierra y océano dentro de un mascon a caballo | las teselas costeras se parten en dos a lo largo de la costa |
| Factores de escala | publicados, y el JPL recomienda aplicarlos | el CSR afirma que sus mascones no los necesitan |

Scanlon et al. (2016) compararon los mascones del CSR y del JPL entre sí y con los armónicos esféricos reescalados en 176 cuencas fluviales, y
encontraron series de agua total que correlacionan en su mayoría por encima de 0.9, con las tendencias como la parte que sigue divergiendo. Eso
coincide con lo que hacen aquí los dos conjuntos: en las 37 cuencas de WHYMAP las series de TWSa correlacionan a una mediana de 0.87, y 15 de las
37 superan 0.9. La concordancia cae a medida que la región se hace más pequeña, y celda a celda en todo el globo la correlación mediana de TWSa
es 0.75.

## Repartir la diferencia entre sus dos causas { #splitting-the-difference-into-its-two-causes }

Los dos conjuntos satisfacen el mismo balance hídrico, TWSa = GWSa + SMa + SWEa + CANa. Escribiendo REST para todo lo que no es agua subterránea,
la diferencia entre las dos series de agua subterránea queda fijada por otras dos diferencias:

$$ d_{GW} = d_{TWS} - d_{REST} $$

Cada término se puede medir. Celda a celda, medianas ponderadas por área entre 2003-02 y 2026-06:

| | RMS | participación mediana en la varianza de d<sub>GW</sub> |
|---|---:|---:|
| d<sub>GW</sub>, la diferencia de agua subterránea que se ve | 6.42 cm | — |
| d<sub>TWS</sub>, las dos soluciones de GRACE discrepando | 5.73 cm | 0.85 |
| d<sub>REST</sub>, la columna repartida de otra forma | 3.38 cm | 0.32 |

Las participaciones suman más de 1 porque las dos diferencias están parcialmente correlacionadas.

Promediando sobre una cuenca el equilibrio cambia. Las medianas por cuenca son 0.72 para d<sub>TWS</sub> y 0.32 para d<sub>REST</sub>, y en 11 de
las 37 cuencas el reparto es el mayor de los dos. Promediar cancela buena parte del ruido por celda de las soluciones de GRACE y deja en pie la
diferencia sistemática en cómo se divide la columna, así que cuanto mayor es la región, más trata el desacuerdo sobre el reparto y menos sobre
JPL contra CSR.

El agua subterránea discrepa más que el agua total en todos los casos. Celda a celda las medianas son 0.42 para GWSa frente a 0.75 para TWSa; por
cuenca, 0.61 frente a 0.87. Cuanto más lejos queda una magnitud de la medición cruda, más se separan las dos construcciones.

## Qué dice la literatura sobre la resta { #what-the-literature-says-about-the-subtraction }

Getirana, Kumar y Rodell (2025) argumentan que el método del residuo —restar de la TWS de GRACE la humedad del suelo, la nieve y el agua del
dosel modeladas y leer el resto como agua subterránea— se apoya en un supuesto que no se sostiene: que los modelos representan cada almacén que
no es agua subterránea en compartimentos separados y con sentido físico. Piden a los usuarios que sopesen qué hacen al resultado las
simplificaciones y convenciones de los modelos, y recomiendan la asimilación de datos y modelos con una representación más completa del subsuelo.

Esa crítica se aplica a la ruta de GRACE de esta aplicación, y las secciones sobre ciclos estacionales de
[Cuándo fiarse de cada uno](trusting-each-one.md) ponen números a un caso concreto. No deja inservible la ruta de GRACE. Scanlon et al. (2018)
compararon siete modelos globales con tres soluciones de GRACE en 186 cuencas fluviales y encontraron que los modelos subestiman gravemente las
grandes tendencias decenales que ve GRACE, en ambos sentidos, lo que es una razón para mantener la medición en el cuadro en lugar de entregar la
pregunta a un modelo. Los dos artículos apuntan en la misma dirección: tomar el reparto del modelo mejor planteado y la magnitud del cambio de la
medición.

## Referencias { #references }

- Getirana, A., Kumar, S., y Rodell, M. (2025). Inconsistencies in GRACE-Based Groundwater Storage Estimation — A Call for a Proper Use of
  Land Surface Models. *Geophysical Research Letters*, 52, e2025GL119197.
  [doi:10.1029/2025GL119197](https://doi.org/10.1029/2025GL119197){:target="_blank"}
- Li, B., Rodell, M., Kumar, S., Beaudoing, H. K., Getirana, A., Zaitchik, B. F., et al. (2019). Global GRACE Data Assimilation for Groundwater
  and Drought Monitoring: Advances and Challenges. *Water Resources Research*, 55, 7564–7586.
  [doi:10.1029/2018WR024618](https://doi.org/10.1029/2018WR024618){:target="_blank"}
- Save, H., Bettadpur, S., y Tapley, B. D. (2016). High-resolution CSR GRACE RL05 mascons. *Journal of Geophysical Research: Solid Earth*,
  121, 7547–7569. [doi:10.1002/2016JB013007](https://doi.org/10.1002/2016JB013007){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Wiese, D. N., Landerer, F. W., Long, D., Longuevergne, L., y Chen, J. (2016). Global evaluation of new
  GRACE mascon products for hydrologic applications. *Water Resources Research*, 52, 9412–9429.
  [doi:10.1002/2016WR019494](https://doi.org/10.1002/2016WR019494){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Sun, A. Y., Müller Schmied, H., van Beek, L. P. H., et al. (2018). Global models underestimate large
  decadal declining and rising water storage trends relative to GRACE satellite data. *Proceedings of the National Academy of Sciences*, 115(6),
  E1080–E1089. [doi:10.1073/pnas.1704665115](https://doi.org/10.1073/pnas.1704665115){:target="_blank"}
