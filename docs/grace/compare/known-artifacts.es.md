# Artefactos conocidos

Algunas de las mayores diferencias entre los dos conjuntos están en lugares donde uno de ellos, normalmente la ruta de GRACE, informa agua que no
es agua subterránea. La aplicación dibuja esas celdas como cualquier otra. Esta página las nombra para que puedas reconocer una a simple vista en
lugar de leerla como un hallazgo.

## Capas de hielo y glaciares { #ice-sheets-and-glaciers }

Las doce celdas de 1° donde más difieren los dos registros de agua subterránea son todas de hielo:

| Celda | Diferencia típica | Correlación | Nieve media |
|:---|:---:|:---:|:---:|
| 66.5°N, 36.5°O (Groenlandia oriental) | 1019 cm | −0.03 | 327 cm |
| 66.5°N, 35.5°O | 805 cm | 0.02 | 283 cm |
| 66.5°N, 37.5°O | 777 cm | 0.02 | 330 cm |
| 76.5°N, 67.5°O (Ellesmere y Baffin) | 739 cm | 0.13 | 9 cm |
| 78.5°N, 15.5°E (Svalbard) | 734 cm | 0.39 | 24 cm |
| 76.5°N, 68.5°O | 729 cm | 0.19 | 6 cm |

GRACE mide la capa de hielo perdiendo masa, año tras año. Ningún modelo de GLDAS lleva glaciares ni capas de hielo, así que ninguno informa esa
pérdida como nieve, y la resta no tiene dónde ponerla salvo en el agua subterránea. El resultado son cambios de agua subterránea de escala métrica
en celdas que no tienen acuífero alguno. 2.2 esquiva la aritmética sin escapar del problema: su modelo Catchment tampoco tiene hielo, y la
corrección de GRACE que recibe se reparte entre todos los almacenes del modelo, así que informa una cifra mucho menor por la misma razón por la
que aplana tendencias en otros sitios. Ninguna de las dos series significa nada como agua subterránea aquí.

Dos cuencas fluviales de los propios conjuntos de la aplicación, Alsek y Santa Cruz, cargan con una GWSa enorme por este motivo (ver
[Cálculo del almacenamiento de agua subterránea](../gldas/deriving-groundwater.md)).

**Cómo reconocerlo.** Cambia la capa mostrada a la nieve (SWEa). Donde llegue a centenares de centímetros, o la región esté sobre un casquete de
hielo a cualquier latitud, la capa de agua subterránea está informando hielo.

## Agua superficial que los modelos no llevan { #surface-water-the-models-do-not-carry }

En el Amazonas el agua subterránea de GRACE oscila 40.8 cm a lo largo del año frente a los 18.1 de 2.2, y su tendencia va a +0.31 cm/año frente a
los −0.40 de 2.2: los dos conjuntos ni siquiera coinciden en la dirección. La mayor parte del ciclo del agua del Amazonas ocurre en los cauces y
en la llanura de inundación, y ningún modelo de GLDAS representa ninguno de los dos. En la ruta de GRACE esa agua no tiene adónde ir en la resta,
así que acaba en el agua subterránea. El Congo se comporta igual.

Cualquier cuenca donde un río grande suba y baje estacionalmente sobre una llanura de inundación amplia hará alguna versión de esto.

**Cómo reconocerlo.** Un ciclo de agua subterránea de GRACE mucho mayor que el de 2.2, en una cuenca húmeda con un río importante, suele ser agua
superficial.

## Nieve y suelo helado en latitudes altas { #snow-and-frozen-ground-at-high-latitude }

Diferencia típica entre los dos registros de agua subterránea, por banda de latitud:

| Banda | Diferencia típica | Nieve media | Celdas |
|:---|:---:|:---:|:---:|
| 60°S–30°S | 5.92 cm | 0.33 cm | 540 |
| 30°S–0° | 8.48 cm | 0.01 cm | 2,428 |
| 0°–30°N | 7.41 cm | 0.02 cm | 3,094 |
| 30°N–60°N | 6.49 cm | 2.12 cm | 5,397 |
| 60°N–90°N | 7.75 cm | 18.91 cm | 3,700 |

La banda más septentrional es la que lleva la nieve, y las cuencas siberianas muestran la ruta de GRACE oscilando mucho más a lo largo del año:
el Pechora con 12.1 cm frente a los 3.3 de 2.2, Siberia Occidental con 14.0 frente a 4.6. Dos cosas acaban allí en el agua subterránea de GRACE:
la masa de nieve que la capa de nieve del modelo no iguala, y el agua atrapada en suelo estacionalmente helado, que ningún modelo de GLDAS guarda
como almacén propio.

La banda tropical es la peor de las bandas libres de hielo, y eso es el agua de las llanuras de inundación de más arriba y no algo helado.

## Niveles freáticos someros { #shallow-water-tables }

Donde el nivel freático está cerca de la superficie, parte de lo que los modelos de GLDAS 2.1 cuentan como humedad del suelo es en realidad agua
subterránea, de modo que restarla elimina la señal subterránea dos veces. El caso más claro es el Northern Atlantic Coastal Plain, donde el ciclo
de agua subterránea de GRACE acaba cuatro meses desacompasado respecto al de 2.2. [Cuándo fiarse de cada uno](trusting-each-one.md) da la
comprobación que conviene hacer y los acuíferos afectados.

## Regiones donde pasa poco { #regions-where-little-happens }

En las celdas de 1° donde el agua subterránea de GRACE apenas se mueve —menos de 5 cm de variación típica—, los dos conjuntos correlacionan a una
mediana de 0.19. Dos señales pequeñas que no llegan a alinearse producen ese número haya o no algo mal. Antes de leer una correlación baja como un
problema, mira cuánta agua se mueve de verdad: la misma comparación da 0.77 en celdas que varían más de 15 cm.

## Una lista breve { #a-short-checklist }

Antes de tratar una diferencia grande como un resultado:

1. Dibuja la nieve (SWEa). El hielo y la nieve explican la mayoría de los extremos.
2. Dibuja el agua total (TWSa) de los dos conjuntos. Donde los totales concuerdan y solo discrepa el agua subterránea, los dos conjuntos están
   repartiendo la columna de forma distinta; la medición del satélite no está en cuestión.
3. Compara el vaivén estacional de la humedad del suelo (SMa) con el del agua total (TWSa). Donde sean parecidos, desconfía del calendario del
   ciclo de agua subterránea de GRACE.
4. Mira cuánta agua se mueve antes de leer nada en una correlación.
5. Pregúntate si un río, una llanura de inundación o un embalse podrían dar cuenta del agua.
