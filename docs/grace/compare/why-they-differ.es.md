# Por qué difieren los dos conjuntos

La aplicación sirve dos registros de agua subterránea para el mismo mes y la misma celda, y no concuerdan. Esta página trata de dónde viene el
desacuerdo. [Cuándo fiarse de cada uno](trusting-each-one.md) trata de a cuál creer, y [Artefactos conocidos](known-artifacts.md) recoge los
lugares donde uno de los dos sencillamente se equivoca.

[Cálculo del almacenamiento de agua subterránea](../gldas/deriving-groundwater.md) da las dos construcciones completas. En resumen:

- **La ruta de GRACE.** El JPL mide el almacenamiento total de agua. La aplicación resta la humedad del suelo, la nieve y el agua del dosel de
  GLDAS 2.1, y lee el resto como agua subterránea.
- **La ruta de GLDAS 2.2.** La NASA corre el modelo de superficie terrestre Catchment con GRACE asimilado dentro, y el modelo informa un estado
  de agua subterránea directamente. No se resta nada.

Estas páginas usan los nombres de las capas de la aplicación. **TWSa** es el agua total almacenada: todas las formas de agua retenidas en la
columna en ese lugar —humedad del suelo, nieve, agua sobre las hojas, agua superficial y agua subterránea—. **GWSa** es la parte subterránea,
**SMa** la humedad del suelo, **SWEa** la nieve y **CANa** el agua retenida en la vegetación. La *a* de cada una significa anomalía: cada valor
es una desviación respecto al promedio de 2004–2009 de esa misma celda, en centímetros de agua repartidos por igual sobre la celda. Cero
significa condiciones promedio para ese lugar, nunca un acuífero vacío.

## Lo que ya difiere antes de contar una sola gota { #what-already-differs-before-any-water-is-counted }

| | Ruta de GRACE | GLDAS 2.2 |
|:---|:---|:---|
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

GRACE nunca midió agua. Dos satélites volaban en formación, uno delante del otro, y el instrumento entre ellos medía su separación con precisión
de unas pocas micras. La masa adicional del terreno de abajo —sobre todo agua— tira primero del satélite delantero y un instante después del
trasero, lo que cambia esa separación en una cantidad diminuta. Meses de esas mediciones se pueden convertir de nuevo en un mapa de dónde se
ganó y se perdió masa.

Esa conversión no tiene una única respuesta correcta. Muchas disposiciones distintas del agua sobre el terreno encajan igual de bien con el mismo
registro orbital, así que cada centro de procesamiento añade supuestos propios para quedarse con una. El JPL y el CSR añaden supuestos
distintos. Ambos publican el resultado en forma de **mascones**: bloques de la superficie terrestre, cada uno con un valor de agua por mes.

| | JPL | CSR |
|:---|:---|:---|
| Bloques sobre los que se resuelve | casquetes de igual área de 3°, unos 300 km | teselas de igual área de 1° en el ecuador, unos 110 km |
| Malla en la que se distribuyen los archivos | 0.5° | 0.25° |
| Qué orienta la respuesta donde GRACE por sí solo es ambiguo | un modelo de superficie terrestre | los propios datos de GRACE |
| Bloques que cruzan una costa | un filtro separa la parte terrestre de la oceánica | el bloque se parte en dos a lo largo de la costa |
| Factores de corrección | el JPL publica factores de ganancia y recomienda aplicarlos | el CSR afirma que sus mascones no los necesitan |

Las dos mallas son más finas que lo que GRACE puede ver realmente. Los satélites resuelven rasgos de unos pocos cientos de kilómetros, los
procese quien los procese, así que la malla es la forma de empaquetar una respuesta más que la cantidad de detalle que contiene.

Scanlon et al. (2016) compararon los productos de los dos centros en 176 cuencas fluviales y encontraron que sus registros de agua total se
siguen de cerca, y que las tendencias a largo plazo son la parte que sigue divergiendo. Los dos conjuntos de esta aplicación se comportan igual.

La concordancia en estas páginas se mide como una **correlación**: un solo número entre −1 y 1 que dice con qué fidelidad dos registros mensuales
suben y bajan juntos. En 1 se mueven al unísono, en 0 no hay relación, en −1 uno sube cada vez que el otro baja. Una correlación no dice nada
sobre si los dos coinciden en cuánta agua hay, solo sobre el momento y la forma de las subidas y bajadas.

Cada correlación de aquí cubre los 281 meses que ambos conjuntos ofrecen, de febrero de 2003 a junio de 2026. Para una cuenca, cada conjunto se
promedia primero sobre la cuenca, que es la serie que dibuja la vista regional de la aplicación, y se comparan esos dos promedios. Las tendencias
se dejan dentro, así que un descenso que ambos conjuntos ven cuenta a favor de su concordancia.

En las 37 cuencas de WHYMAP los dos registros de agua total correlacionan a una mediana de 0.87, y 15 de las 37 superan 0.9. La concordancia se
debilita a medida que el área se reduce: comparando una celda de 1° cada vez, la mediana baja a 0.75, porque promediar sobre una cuenca cancela
el ruido de mes a mes que una sola celda arrastra por su cuenta.
## De dónde viene la diferencia { #where-the-difference-comes-from }

Ninguno de los dos conjuntos mide el agua subterránea. Los dos llegan a ella por resta: se parte del agua total almacenada en la columna y se
descuenta el agua retenida como humedad del suelo, nieve y agua del dosel. Lo que queda se llama agua subterránea.

Las dos series de agua subterránea pueden separarse por dos vías, y por ninguna otra.

1. **Parten de un total distinto.** Las capas de GRACE de la aplicación llevan la solución del JPL y GLDAS 2.2 tiene incorporada la del CSR. Allí
   donde esas dos discrepan sobre el agua total, el agua subterránea que implican hereda esa discrepancia por completo.
2. **Descuentan una cantidad distinta.** Los tres modelos de GLDAS 2.1 que promedia la ruta de GRACE, y el modelo Catchment dentro de 2.2,
   guardan cantidades distintas de humedad del suelo y de nieve para el mismo lugar en el mismo mes. Descontar más deja menos agua subterránea.

No entra nada más, así que las tres diferencias quedan ligadas de forma exacta: la diferencia de agua subterránea es igual a la diferencia de agua
total menos la diferencia de la resta. Escribiendo d para «la diferencia entre los dos conjuntos», TWS para el agua total y REST para todo lo que
en la columna no es agua subterránea,

$$ d_{GW} = d_{TWS} - d_{REST} $$

Las tres se pueden medir, lo que resuelve qué causa domina en cada sitio.

El **RMS** es el tamaño típico de una diferencia, en centímetros de agua: se toma la diferencia entre los dos conjuntos en cada mes, se eleva al
cuadrado, se promedia sobre el registro y se toma la raíz cuadrada. A cada celda se le quita primero su desfase fijo, de modo que el RMS mide la
discrepancia que se mueve con el tiempo y no una distancia constante entre los dos.

La **participación** dice cuánto de la diferencia de agua subterránea podría explicar una causa por sí sola. Cada diferencia oscila alrededor de
su propio promedio en cierta medida, y la participación compara el tamaño de esa oscilación con la de la diferencia de agua subterránea.

Ambas son medianas sobre las celdas terrestres que comparten los dos conjuntos, de febrero de 2003 a junio de 2026, contando cada celda en
proporción a su área, de modo que una celda ancha en el ecuador pesa más que una estrecha cerca de un polo.

| La diferencia entre los dos conjuntos en | RMS | Participación en la diferencia de agua subterránea |
|:---|:---:|:---:|
| el agua subterránea, que es lo que se ve en pantalla | 6.42 cm | — |
| el agua total, JPL frente a CSR | 5.73 cm | 0.85 |
| la resta: suelo, nieve y dosel | 3.38 cm | 0.32 |

Las dos participaciones suman más de 1 porque las diferencias se mueven en parte juntas, así que no reparten la culpa en porcentajes limpios.
Léanse como un orden: en una celda típica de 1°, el desacuerdo entre JPL y CSR explica la mayor parte de la diferencia de agua subterránea, y la
resta alrededor de un tercio.

Promediar sobre una cuenca cambia ese equilibrio. El promedio cancela buena parte del ruido a escala de celda de las soluciones de GRACE y deja en
pie la diferencia sistemática en cómo se divide la columna, así que cuanto mayor es la región, más parte del desacuerdo procede de la resta. Las
participaciones por cuenca llegan a una mediana de 0.72 para el agua total y de 0.32 para la resta, y en 11 de las 37 cuencas la resta es la causa
mayor.

El agua subterránea discrepa más que el agua total en todo el recorrido. Celda a celda las series de agua subterránea de los dos conjuntos
correlacionan a una mediana de 0.42, frente a 0.75 del agua total; por cuenca, 0.61 frente a 0.87. Cada paso que se aleja de la medición cruda
añade una decisión de modelado que los dos conjuntos toman de forma distinta.

## Qué dice la literatura sobre la resta { #what-the-literature-says-about-the-subtraction }

Getirana, Kumar y Rodell (2025) cuestionan el método que hay detrás de la ruta de GRACE. Restar la humedad del suelo y la nieve de un modelo a un
total de GRACE da agua subterránea solo si los compartimentos de suelo y nieve del modelo contienen exactamente el agua que esas etiquetas
sugieren, y en muchos modelos no es así. Las capas de suelo terminan a una profundidad fija, lo que queda por debajo se trata por convenio, y
donde el nivel freático es somero el agua que un modelo archiva como humedad del suelo es la misma que un hidrólogo llamaría agua subterránea.
Al restarla se va con ella la señal que se buscaba. Recomiendan modelos que lleven un subsuelo más completo y que asimilen GRACE, que es lo que
describe a GLDAS 2.2.

La crítica se aplica a la ruta de GRACE de esta aplicación. Las secciones sobre ciclos estacionales de [Dónde confiar en cada
uno](trusting-each-one.md) ponen cifras a un caso concreto: en la llanura costera atlántica, donde el nivel freático es somero, la ruta de GRACE
sitúa su máximo de agua subterránea en la estación equivocada.

Eso no deja inservible a la ruta de GRACE. Scanlon et al. (2018) contrastaron siete modelos globales de superficie terrestre con tres soluciones
de GRACE en 186 cuencas fluviales y encontraron que los modelos salen sistemáticamente demasiado planos: donde GRACE ve una ganancia o una
pérdida grande de varios años, los modelos muestran una menor, en ambos sentidos. Un modelo es la mejor guía para saber cómo se reparte la
columna entre suelo, nieve y agua subterránea; los satélites son la mejor guía para saber cuánto ha cambiado el total.

Los dos artículos respaldan el reparto que recomiendan estas páginas: tomar de 2.2 la forma del ciclo y el reparto de la columna, y de GRACE el
tamaño de una ganancia o una pérdida a largo plazo.
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
