# Por qué difieren los dos conjuntos

La aplicación ofrece dos registros de agua subterránea para el mismo mes y la misma celda, y no coinciden. Esta página trata del origen del
desacuerdo. [Cómo se ven las diferencias](examples.md) muestra los casos, [Cuál usar](which-one-to-use.md) indica qué serie citar para cada
pregunta, y [Hasta dónde está validado](validation.md) dice cuánto peso puede soportar ese consejo.

[Cálculo del almacenamiento de agua subterránea](../gldas/deriving-groundwater.md) da ambas construcciones completas. En resumen:

- **La ruta de GRACE.** JPL mide el almacenamiento total de agua. La aplicación resta la humedad del suelo, la nieve y el agua del dosel de
  GLDAS 2.1, y lee el resto como agua subterránea.
- **La ruta de GLDAS 2.2.** La NASA ejecuta el modelo de superficie terrestre Catchment con GRACE asimilado, y el modelo informa directamente un
  estado de agua subterránea. No se resta nada.

Estas páginas usan los nombres de capa de la aplicación. **TWSa** es el almacenamiento total de agua: toda forma de agua retenida en la columna
en ese lugar — humedad del suelo, nieve, agua sobre las hojas, agua superficial y agua subterránea juntas. **GWSa** es la parte subterránea,
**SMa** la humedad del suelo, **SWEa** la nieve y **CANa** el agua retenida en la vegetación. La *a* de cada una significa anomalía: cada valor
es una desviación respecto al promedio 2004–2009 de esa misma celda, en centímetros de agua repartidos uniformemente sobre ella. Cero significa
condiciones promedio para ese lugar, nunca un acuífero vacío.

## Lo que ya difiere antes de contar una sola gota { #what-already-differs-before-any-water-is-counted }

| | Ruta de GRACE | GLDAS 2.2 |
|:---|:---|:---|
| Solución GRACE | mascons de JPL, RL06.3 v04 CRI | mascons de CSR, RL06 |
| Huella nativa de GRACE | casquetes de área igual de 3° | 1° de área igual en el ecuador |
| Malla servida | 1° | 0,25°, promediada a 1° para la malla global |
| Inicio del registro | abril de 2002 | febrero de 2003 |
| Meses faltantes | los vacíos de GRACE, rellenados o marcados | ninguno; el modelo corre sin corregir |
| Factores de ganancia | los de JPL, aplicados | ninguno |
| Capas de incertidumbre | publicadas por celda | ninguna |
| Celdas de tierra en la malla de 1° | 15 159 | 17 346 |

El inicio del registro y la máscara de tierra son contabilidad, y aparecen como datos faltantes más que como desacuerdo. Todas las demás filas
cambian las cifras.

## Dos grupos, un par de satélites { #two-groups-one-pair-of-satellites }

GRACE nunca midió agua. Dos satélites volaban en formación, uno delante del otro, y el instrumento entre ellos medía su separación con precisión
de unas pocas micras. La masa adicional en el terreno de abajo — agua, sobre todo — tira primero del satélite delantero y un momento después del
trasero, alterando esa separación en una cantidad diminuta. Meses de esas mediciones pueden convertirse en un mapa de dónde se ganó y se perdió
masa.

Esa conversión no tiene una única respuesta correcta. Muchas disposiciones distintas del agua sobre el terreno encajan igual de bien con el mismo
registro orbital, así que cada centro de procesamiento añade supuestos propios para quedarse con una. JPL y CSR añaden supuestos distintos. Ambos
publican el resultado como **mascons**: bloques de la superficie terrestre, cada uno con un valor de agua por mes.

| | JPL | CSR |
|:---|:---|:---|
| Bloques sobre los que se resuelve | casquetes de área igual de 3°, unos 300 km | teselas de área igual de 1° en el ecuador, unos 110 km |
| Malla en que se distribuyen los archivos | 0,5° | 0,25° |
| Qué guía la respuesta donde GRACE sola es ambigua | un modelo de superficie terrestre | solo los datos de GRACE |
| Bloques que cruzan una costa | un filtro separa la parte terrestre de la oceánica | el bloque se divide en dos a lo largo de la costa |
| Factores de corrección | JPL publica factores de ganancia y recomienda aplicarlos | CSR afirma que sus mascons no los necesitan |

Ambas mallas son más finas que lo que GRACE puede ver realmente. Los satélites resuelven rasgos de unos pocos cientos de kilómetros, sea cual sea
el centro que los procese, de modo que la malla es cómo se empaqueta una respuesta más que cuánto detalle contiene.

Scanlon et al. (2016) compararon los productos de ambos centros en 176 cuencas fluviales y encontraron que sus registros de agua total se seguían
de cerca, con las tendencias a largo plazo como la parte que aún diverge. Los dos conjuntos de esta aplicación se comportan igual.

## Cómo se mide la concordancia en estas páginas { #how-agreement-is-measured-on-these-pages }

La concordancia se mide como una **correlación**: un número entre −1 y 1 que dice con qué fidelidad dos registros mensuales suben y bajan juntos.
En 1 se mueven al unísono, en 0 no hay relación, en −1 uno sube cada vez que el otro baja. Una correlación no dice nada sobre si ambos coinciden
en cuánta agua hay — solo sobre el momento y la forma de las subidas y bajadas.

Cada correlación aquí cubre los 281 meses que ambos conjuntos proporcionan, de febrero de 2003 a junio de 2026. Para una cuenca, cada conjunto se
promedia primero sobre la cuenca, que es la serie que dibuja la vista regional de la aplicación, y se comparan esos dos promedios. Las tendencias
se dejan dentro, así que un descenso que ambos ven cuenta a favor de su concordancia.

En las 37 cuencas WHYMAP los dos registros de agua total correlacionan a una mediana de 0,87, y 15 de las 37 superan 0,9. La concordancia se
debilita al reducirse el área: comparando celda de 1° por celda, la mediana baja a 0,75, porque promediar sobre una cuenca cancela el ruido
mensual que una sola celda arrastra por su cuenta.

## De dónde viene la diferencia { #where-the-difference-comes-from }

Ninguno de los dos conjuntos mide el agua subterránea. Ambos llegan a ella por resta: se parte del agua total almacenada en la columna y se quita
el agua retenida como humedad del suelo, nieve y dosel. Lo que queda se llama agua subterránea.

Por tanto las dos series pueden separarse de dos maneras, y de ninguna otra.

1. **Parten de un total distinto.** Las capas GRACE de la aplicación llevan la solución de JPL y GLDAS 2.2 lleva la de CSR incorporada. Allí donde
   esas dos discrepan sobre el agua total, el agua subterránea que implican hereda esa discrepancia íntegra.
2. **Quitan una cantidad distinta.** Los tres modelos GLDAS 2.1 que promedia la ruta de GRACE, y el modelo Catchment dentro de 2.2, guardan
   cantidades distintas de humedad del suelo y de nieve para el mismo lugar en el mismo mes. Quitar más deja menos agua subterránea.

No entra nada más, así que las tres diferencias quedan ligadas exactamente: la diferencia en agua subterránea es igual a la diferencia en agua
total menos la diferencia en la resta. Escribiendo d para «la diferencia entre los dos conjuntos», TWS para el agua total y REST para todo lo de
la columna que no es agua subterránea,

$$ d_{GW} = d_{TWS} - d_{REST} $$

Las tres pueden medirse, lo que resuelve qué causa domina y dónde.

**RMS** es el tamaño típico de una diferencia, en centímetros de agua: se toma la diferencia entre los dos conjuntos en cada mes, se eleva al
cuadrado, se promedia sobre el registro y se saca la raíz cuadrada. El desfase fijo de cada celda se retira antes, así que el RMS mide el
desacuerdo que varía en el tiempo y no una distancia constante entre ambos.

**Proporción** dice cuánto de la diferencia en agua subterránea podría explicar una causa por sí sola. Cada diferencia oscila alrededor de su
propio promedio en cierta medida, y la proporción compara el tamaño de esa oscilación con la del agua subterránea.

Ambas son medianas sobre las celdas de tierra que comparten los dos conjuntos, de febrero de 2003 a junio de 2026, contando cada celda en
proporción a su área, de modo que una celda ancha en el ecuador pesa más que una estrecha cerca de un polo.

| La diferencia entre los dos conjuntos en | RMS | Proporción de la diferencia subterránea |
|:---|:---:|:---:|
| agua subterránea, que es lo que se ve en pantalla | 6,42 cm | — |
| agua total, JPL frente a CSR | 5,73 cm | 0,85 |
| la resta: suelo, nieve y dosel | 3,38 cm | 0,32 |

Las dos proporciones suman más de 1 porque las diferencias se mueven en parte juntas, así que no reparten la culpa en porcentajes limpios. Léanse
como un orden: en una celda típica de 1°, el desacuerdo entre JPL y CSR explica la mayor parte de la diferencia subterránea, y la resta alrededor
de un tercio.

Promediar sobre una cuenca cambia ese equilibrio. El promedio cancela buena parte del ruido a escala de celda de las soluciones GRACE y deja
intacta la diferencia sistemática en cómo se divide la columna, así que cuanto mayor es la región, más desacuerdo procede de la resta. Las
proporciones por cuenca llegan a una mediana de 0,72 para el agua total y 0,32 para la resta, y en 11 de las 37 cuencas la resta es la causa
mayor.

El agua subterránea discrepa más que el agua total en todas partes. Celda a celda las series subterráneas de los dos conjuntos correlacionan a una
mediana de 0,42, frente a 0,75 del agua total; por cuenca, 0,61 frente a 0,87. Cada paso que se aleja de la medición cruda añade una decisión de
modelado que los dos conjuntos toman de forma distinta.

## Qué aspecto tiene eso sobre el terreno { #what-that-looks-like-on-the-ground }

Las dos causas anteriores producen cuatro patrones reconocibles, y uno más que no es un desacuerdo en absoluto:

| Patrón | Lo que se ve | Qué causa |
|:---|:---|:---|
| Los dos coinciden | ambos registros suben y bajan juntos, con uno o dos centímetros de diferencia | ninguna domina |
| La tendencia difiere | los mismos años húmedos y secos, sobre rectas que se separan | sobre todo la resta, por lo que 2.2 hace con la corrección |
| La amplitud difiere | el mismo momento, un ciclo varias veces más alto | la resta |
| Los ciclos van opuestos | máximos con meses de diferencia, correlación por debajo de cero | la resta, donde la humedad del suelo casi iguala al agua total |
| Un registro no es agua subterránea | metros de cambio, o un ciclo que pertenece a un río | hielo, agua superficial o suelo congelado, que ningún modelo lleva |

[Cómo se ven las diferencias](examples.md) recorre cada uno con acuíferos concretos en cinco continentes.

## Referencias { #references }

- Save, H., Bettadpur, S., y Tapley, B. D. (2016). High-resolution CSR GRACE RL05 mascons. *Journal of Geophysical Research: Solid Earth*,
  121, 7547–7569. [doi:10.1002/2016JB013007](https://doi.org/10.1002/2016JB013007){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Wiese, D. N., Landerer, F. W., Long, D., Longuevergne, L., y Chen, J. (2016). Global evaluation of new
  GRACE mascon products for hydrologic applications. *Water Resources Research*, 52, 9412–9429.
  [doi:10.1002/2016WR019494](https://doi.org/10.1002/2016WR019494){:target="_blank"}
