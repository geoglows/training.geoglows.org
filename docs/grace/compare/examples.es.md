# Cómo se ven las diferencias

[Por qué difieren los dos conjuntos](why-they-differ.md) expone las dos causas. Esta página muestra lo que producen, en acuíferos concretos de
cinco continentes, con ambos conjuntos dibujados sobre los mismos ejes en todos los casos.

Cada serie aquí es el promedio ponderado por área sobre la región, que es lo que dibuja la vista regional de la aplicación, sobre los 281 meses
que ambos conjuntos proporcionan. Un **ciclo estacional** es la forma media de un año una vez retirada la tendencia a largo plazo, y una
**amplitud** es la altura desde su mes más bajo hasta el más alto. La primera mitad de la página trata de desacuerdos reales sobre el agua
subterránea. La segunda, de lugares donde uno de los dos no está informando agua subterránea en absoluto.

## Donde los dos coinciden { #where-the-two-agree }

Cuatro acuíferos, cuatro continentes, nada en disputa:

![Registros mensuales de agua subterránea de ambos conjuntos sobre la cuenca de Parecis, el Tauro-Zagros, la meseta del Decán y la meseta de Khorat, siguiéndose de cerca](../../static/images/grace/compare-agreement.png)

| Acuífero | r mensual | r estacional | Amplitud, GRACE | Amplitud, 2.2 |
|:---|:---:|:---:|:---:|:---:|
| Cuenca de Parecis, Brasil | 0,94 | 0,97 | 35,3 cm | 37,7 cm |
| Tauro-Zagros, Irak e Irán | 0,92 | 0,96 | 13,7 cm | 10,7 cm |
| Meseta del Decán, India | 0,91 | 0,94 | 26,5 cm | 22,5 cm |
| Meseta de Khorat, Tailandia y Laos | 0,89 | 0,95 | 27,7 cm | 31,1 cm |

Nada de lo que un gestor del agua concluiría en estos cuatro cambia con la elección del conjunto. Cubren una cuenca tropical húmeda, un frente
montañoso semiárido, una meseta monzónica y una llanura monzónica, y los cuatro bajan o suben en ambos registros a la vez — el Decán gana en
ambos (+0,64 y +0,37 cm/año), el Tauro-Zagros pierde en ambos (−0,73 y −0,43).

Lo que tienen en común es la proporción que recorre el resto de esta página: en cada uno, el ciclo de humedad del suelo de los modelos es
alrededor de 0,4 del ciclo de agua total. La resta retira menos de la mitad de lo que midió GRACE y deja una señal subterránea con forma propia.

## Donde difiere la tendencia { #where-the-trend-differs }

Los dos conjuntos pueden ver los mismos años húmedos y secos y aun así situarse sobre rectas que se separan sin pausa:

![Ambos conjuntos sobre el Valle Central, el acuífero de Disi, la llanura costera de Veracruz y la cuenca del Tarim, con rectas de tendencia que divergen en cada caso](../../static/images/grace/compare-trend.png)

| Acuífero | GRACE | GLDAS 2.2 | 2.2 / GRACE |
|:---|:---:|:---:|:---:|
| Valle Central, California | −1,37 | −0,24 | 0,18 |
| Saq-Ram (Disi), Jordania y Arabia Saudí | −1,08 | −0,11 | 0,10 |
| Llanura costera de Veracruz, México | −1,21 | −0,06 | 0,05 |
| Cuenca del Tarim, China | −0,55 | −0,06 | 0,11 |
| Ganges-Brahmaputra | −1,53 | −0,44 | 0,29 |
| Indo | −1,45 | −0,21 | 0,14 |
| Llanura del Norte de China | −0,67 | −0,25 | 0,38 |
| Ogallala (Altas Llanuras) | −0,45 | −0,22 | 0,49 |

Tendencias en cm/año, ponderadas por área, de febrero de 2003 a junio de 2026. En las 37 cuencas WHYMAP la tendencia de 2.2 queda en una mediana
de 0,26 de la de GRACE donde el almacenamiento cae y 0,33 donde sube, de modo que el aplanamiento va en ambos sentidos.

El Valle Central es el caso más claro porque los pozos pueden zanjarlo. A lo largo del registro la ruta de GRACE pierde 32 cm y 2.2 pierde 6 cm:
una cuenca en agotamiento serio frente a otra que baja con suavidad. El estudio del Valle Central encontró que el registro de GRACE seguía en el
tiempo a una historia de almacenamiento basada en pozos pero resultaba varias veces demasiado pequeño, y calibró un factor de escala de unos 5
para ajustarlo (véase [Valle Central](../case-studies/central-valley.md)). Frente a los pozos, 2.2 es el más alejado de los tres.

La causa está en cómo se construye 2.2. El modelo Catchment no tiene bombeo: nadie riega en el mundo del modelo, así que el modelo por sí solo
nunca agotará un acuífero. El agotamiento llega al agua subterránea de 2.2 solo mediante la corrección mensual que GRACE aplica al modelo, y esa
corrección se reparte entre los almacenes superficial, de zona radicular y profundo en lugar de recaer solo sobre el agua subterránea. Entre
correcciones el modelo deriva de vuelta hacia su propio balance hídrico.

Disi deja clara la misma idea sin distritos de riego de por medio. Es un acuífero fósil bajo el desierto jordano y saudí, bombeado para ciudades
y para granjas que casi no recargan. GRACE lo tiene cayendo 25 cm a lo largo del registro y 2.2 lo tiene cayendo 3 cm.

## Donde difiere la amplitud { #where-the-swing-differs }

El momento puede coincidir casi a la perfección mientras el tamaño del ciclo estacional no lo hace:

![La cuenca senegalo-mauritana y el valle del río Nu, cada uno con los dos ciclos de agua subterránea junto a los ciclos de agua total y humedad del suelo que resta la ruta de GRACE](../../static/images/grace/compare-amplitude.png)

En la cuenca senegalo-mauritana ambos conjuntos suben con las lluvias de verano, ambos alcanzan su máximo con un mes de diferencia como mucho, y
sus ciclos correlacionan a 0,94 — pero 2.2 oscila 3,2 veces más. El panel derecho muestra de dónde viene la menor amplitud de la ruta de GRACE.
El agua total sube y baja 15,8 cm a lo largo del año y la humedad del suelo de los modelos 11,7 cm, así que restar una de otra deja un resto de
5,8 cm. El valle del río Nu, en la frontera entre China y Myanmar, hace lo mismo: ciclos que correlacionan a 0,94 y amplitudes de 11,8 cm frente
a 31,5 cm.

El modelo Catchment dentro de 2.2 divide la misma columna de otra forma y conserva una porción mucho mayor del ciclo en su almacén subterráneo.
En las 37 cuencas WHYMAP la amplitud de 2.2 es una mediana de 1,23 veces la de GRACE; en los 31 acuíferos principales del USGS, 1,52.

Ninguna de las dos amplitudes puede contrastarse con un pozo en estas cuencas, así que la lectura honesta es que los dos conjuntos discrepan sobre
cómo se reparte una estación húmeda entre el suelo y el acuífero que hay debajo.

## Donde los ciclos van opuestos { #where-the-cycles-run-opposite }

En algunas regiones los dos no solo difieren en tamaño. Alcanzan su máximo en estaciones distintas:

![Ciclos estacionales de ambos conjuntos en seis acuíferos de cinco continentes, cada par corriendo casi en oposición](../../static/images/grace/compare-phase.png)

| Acuífero | GRACE culmina | 2.2 culmina | r estacional | Humedad del suelo ÷ agua total |
|:---|:---|:---|:---:|:---:|
| Devónico báltico, Letonia y Estonia | agosto | marzo | −0,99 | 2,24 |
| Montaña Occidental, Israel y Palestina | agosto | marzo | −0,93 | 3,22 |
| Macizo Armoricano, Francia | agosto | febrero | −0,90 | 1,56 |
| Shabelle, Etiopía y Somalia | septiembre | diciembre | −0,84 | 2,83 |
| Cratón de Pilbara, Australia | septiembre | abril | −0,65 | 1,40 |
| Llanura Costera Atlántica Norte, EE. UU. | junio | febrero | −0,54 | 1,06 |

La última columna es el diagnóstico, y es la misma cantidad que hacía coincidir a los acuíferos concordantes. Donde el ciclo de humedad del suelo
de los modelos es pequeño frente al ciclo medido de agua total, la resta deja una señal subterránea con forma propia. Donde la humedad del suelo
oscila tanto como el agua total o más, las dos casi se cancelan:

![Los ciclos de agua total y humedad del suelo de la llanura costera atlántica casi superpuestos, y un diagrama de dispersión de la proporción de humedad del suelo frente a la concordancia estacional en 299 acuíferos](../../static/images/grace/compare-phase-mechanism.png)

El panel izquierdo es el mecanismo en una sola imagen. En la Llanura Costera Atlántica Norte el agua total oscila 7,9 cm a lo largo del año, la
humedad del suelo de los modelos oscila 8,4 cm, y las dos curvas quedan casi superpuestas. Restar una de la otra deja el resto discontinuo:
pequeño, y desplazado para culminar cuando el suelo está más seco, que es pleno verano. El ciclo subterráneo que informa la ruta de GRACE es la
pequeña diferencia entre dos números grandes y parecidos, así que cualquier error en cualquiera de ellos recae entero sobre él.

El panel derecho es el patrón en 299 acuíferos de los conjuntos de regiones de la aplicación. La humedad del suelo dividida por el agua total
predice lo bien que concuerdan los dos ciclos estacionales, con una correlación de −0,75. Por debajo de una proporción de 0,7 la concordancia
estacional mediana es 0,93; por encima de 1,0 es −0,39. De los 59 acuíferos cuyos ciclos van opuestos, 42 tienen la humedad del suelo oscilando
más que el agua total.

Los niveles freáticos someros son la razón probable de que la proporción suba tanto. Parte de lo que los modelos GLDAS 2.1 cuentan como humedad
del suelo es agua que un hidrólogo llamaría subterránea, así que la resta retira la señal subterránea dos veces. Getirana, Kumar y Rodell (2025)
formulan la versión general de este argumento: que los compartimentos de un modelo no son los almacenes físicamente separados que la resta supone.

## Donde una concordancia baja no significa nada { #where-a-low-agreement-score-means-nothing }

El mapa de **agreement** (concordancia) pregunta si los dos registros suben y bajan juntos. En una celda donde el almacenamiento apenas se mueve
—unos pocos centímetros por encima y por debajo de lo normal, año tras año— los dos registros casi no tienen con qué subir y bajar. Cada uno
sigue sus propias pequeñas oscilaciones, esas oscilaciones no se alinean, y la puntuación sale baja haya o no algo mal en alguno de los dos
conjuntos:

![Todas las celdas terrestres ordenadas en las clases de concordancia de la aplicación según cuánta agua subterránea se mueve: donde apenas se mueve, el 60% sale Weak u Opposite; donde se mueve mucho, el 75% sale Close o Very close](../../static/images/grace/compare-signal-size.png)

Casi el 40% de las celdas terrestres apenas se mueve, y el 60% de ellas cae en las clases **Weak** (débil) u **Opposite** (opuesta) de la
aplicación. Por encima de 15 cm las clases se invierten: tres cuartas partes de las celdas salen **Close** (estrecha) o **Very close** (muy
estrecha), y el 4% va opuesto.

| Cuánto se aleja de lo normal el agua subterránea de GRACE | Celdas | Opposite o Weak | Close o Very close | Puntuación mediana |
|:---|:---:|:---:|:---:|:---:|
| menos de 5 cm | 5854 | 60% | 11% | 0,19 |
| 5 a 15 cm | 7110 | 32% | 40% | 0,51 |
| más de 15 cm | 2171 | 11% | 75% | 0,77 |

*El alejamiento de lo normal es la desviación estándar de los valores mensuales de la celda a lo largo de todo el registro.*

Los acuíferos que cualquiera gestiona están en la última fila, donde una puntuación baja sí significa algo. Antes de leerla como un desacuerdo,
abra la región y mire la gráfica. Dos líneas planas con algo de ruido encima no son dos conjuntos de datos contradiciéndose; allí no hay nada
sobre lo que concordar.

## Diferencias que no son agua subterránea { #differences-that-are-not-groundwater }

En los casos siguientes uno de los dos registros informa algo real que no es agua subterránea. La aplicación dibuja esas celdas como cualquier
otra.

### Capas de hielo y glaciares { #ice-sheets-and-glaciers }

![Una sola celda en el este de Groenlandia donde la ruta de GRACE cae 22 metros, y la cuenca del Pascua en la Patagonia donde cae 3 metros](../../static/images/grace/compare-artifact-ice.png)

GRACE mide capas de hielo y glaciares perdiendo masa, año tras año. Ningún modelo GLDAS lleva unos ni otros, así que ninguno informa esa pérdida
como nieve, y la resta no tiene dónde ponerla salvo en el agua subterránea.

Una celda de 1° en el este de Groenlandia, a 66,5°N 36,5°O, informa agua subterránea cayendo **22 metros** a lo largo del registro — una línea
recta interrumpida solo por el vacío de la misión, en un lugar sin acuífero y sin agua subterránea que perder. Esa línea es la capa de hielo de
Groenlandia. La nieve de esa misma celda corre 303 cm por encima de su línea base, porque la nieve del modelo se acumula sin límite donde debería
haber hielo. La cuenca del Pascua, que drena el Campo de Hielo Patagónico Sur, hace lo mismo con 3 metros.

2.2 esquiva la aritmética sin escapar del problema: su modelo Catchment tampoco tiene hielo, y la corrección de GRACE que recibe se reparte entre
todos los almacenes del modelo, así que informa una cifra mucho menor por la misma razón por la que aplana tendencias en otros sitios. Ninguna de
las dos series significa nada como agua subterránea aquí. Dos cuencas fluviales de los conjuntos de la aplicación, Alsek y Santa Cruz, llevan una
GWSa muy grande por este motivo.

**Cómo reconocerlo.** Cambie la capa mostrada a nieve (SWEa). Donde llegue a cientos de centímetros, o la región se asiente sobre un casquete de
hielo a cualquier latitud, la capa de agua subterránea está informando hielo.

### Agua superficial que los modelos no llevan { #surface-water-the-models-do-not-carry }

![Los ciclos estacionales del Amazonas, el de GRACE más del doble de grande, y el Amu Daria donde GRACE cae cuatro veces más rápido que 2.2](../../static/images/grace/compare-artifact-water.png)

Ningún modelo GLDAS representa ríos, lagos, llanuras de inundación ni embalses. En la ruta de GRACE esa agua no tiene dónde ir en la resta, así
que acaba en el agua subterránea.

En el Amazonas el momento no está en disputa — los dos ciclos correlacionan a 0,99, ambos con máximo en mayo con la crecida. El tamaño sí: la
ruta de GRACE oscila 40,8 cm frente a 18,1 cm, y el agua de más es el propio río subiendo y bajando sobre la llanura de inundación. Las
tendencias entonces apuntan en direcciones opuestas, +0,31 frente a −0,40 cm/año, así que quien pregunte si el agua subterránea del Amazonas gana
o pierde obtiene una respuesta distinta de cada conjunto. El Congo se comporta igual.

El Amu Daria muestra el mismo mecanismo como tendencia y no como ciclo. La ruta de GRACE tiene el almacenamiento cayendo 58 cm a lo largo del
registro frente a los 14 cm de 2.2, y buena parte de eso es el mar de Aral y los canales de riego que se llevan el agua — agua superficial
saliendo de la cuenca, contada como subterránea.

**Cómo reconocerlo.** Un ciclo subterráneo de GRACE mucho mayor que el de 2.2, en una cuenca con un río importante, un lago grande o un embalse
grande, suele ser agua superficial.

### Nieve y suelo congelado en latitudes altas { #snow-and-frozen-ground-at-high-latitude }

![Las cuencas del Indigirka y del George, donde el ciclo subterráneo de GRACE es la imagen invertida del ciclo de nieve](../../static/images/grace/compare-artifact-frozen.png)

| Banda | Diferencia típica | Nieve media | Celdas |
|:---|:---:|:---:|:---:|
| 60°S–30°S | 5,92 cm | 0,33 cm | 540 |
| 30°S–0° | 8,48 cm | 0,01 cm | 2428 |
| 0°–30°N | 7,41 cm | 0,02 cm | 3094 |
| 30°N–60°N | 6,49 cm | 2,12 cm | 5397 |
| 60°N–90°N | 7,75 cm | 18,91 cm | 3700 |

La banda más septentrional es la que lleva la nieve. En la cuenca del Indigirka, en Siberia, el agua subterránea de GRACE oscila 7,0 cm a lo largo
del año frente a los 1,6 de 2.2, y en la cuenca del río George, en el norte de Quebec, 6,9 frente a 1,9. La curva punteada de cada panel es el
ciclo de nieve, y el agua subterránea de GRACE es casi su imagen especular: donde el modelo guarda demasiada o demasiado poca nieve, el error pasa
directo a la resta. El agua retenida en suelo estacionalmente congelado se suma, ya que ningún modelo GLDAS la mantiene como almacén propio.

**Cómo reconocerlo.** Dibuje la nieve (SWEa) junto al agua subterránea. Un ciclo subterráneo que es el ciclo de nieve del revés es el término de
nieve, no un acuífero.

### Niveles freáticos someros { #shallow-water-tables }

Donde el nivel freático está cerca de la superficie, parte de lo que los modelos cuentan como humedad del suelo es agua subterránea, y restarla
retira la señal subterránea dos veces. Este es el mecanismo tras los ciclos opuestos de más arriba, y la proporción de esa sección es cómo
detectarlo.
