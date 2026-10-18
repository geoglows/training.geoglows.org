# Cuándo fiarse de cada uno

Ninguno de los dos conjuntos gana en todas partes. [Por qué difieren los dos conjuntos](why-they-differ.md) explica el desacuerdo; esta página
dice qué serie citar para cada pregunta, y da el diagnóstico que hay que correr cuando quieras decidir por tu cuenta en una región que las tablas
de abajo no cubren.

## La concordancia sigue al tamaño de la señal { #agreement-follows-the-size-of-the-signal }

Ordenando las celdas de tierra de 1° según cuánto se mueve de verdad el agua subterránea de GRACE, medido por su desviación típica —la distancia
habitual entre un mes y el promedio a largo plazo de esa misma celda—:

| Cuánto se mueve el agua subterránea de GRACE | Correlación mediana | Diferencia mediana entre los dos | Celdas |
|:---|:---:|:---:|:---:|
| menos de 5 cm | 0.19 | 4.58 cm | 5,854 |
| 5–15 cm | 0.51 | 8.32 cm | 7,110 |
| más de 15 cm | 0.77 | 27.32 cm | 2,171 |

Una celda tranquila que correlaciona a 0.2 son dos señales pequeñas que no llegan a alinearse, y no dice nada sobre si alguno de los dos
conjuntos es sólido. Los acuíferos que alguien analizaría están en la fila de abajo. Lee una correlación junto a la cantidad de agua en juego,
nunca sola.

## Para el tamaño de una tendencia, usa GRACE { #for-the-size-of-a-trend-use-grace }

Promediada sobre las 37 grandes cuencas de agua subterránea de WHYMAP, la tendencia de GWSa de 2.2 ronda la cuarta parte de la de GRACE: una razón
mediana de 0.26 en las cuencas que pierden almacenamiento y de 0.33 en las que lo ganan, así que el aplanamiento va en los dos sentidos:

| Cuenca | GRACE | GLDAS 2.2 | 2.2 / GRACE |
|:---|:---:|:---:|:---:|
| Ganges-Brahmaputra | −1.53 | −0.44 | 0.29 |
| Indo | −1.45 | −0.21 | 0.14 |
| Valle Central de California | −1.37 | −0.24 | 0.18 |
| Cáucaso Norte | −1.03 | −0.68 | 0.66 |
| Llanura del Norte de China | −0.67 | −0.25 | 0.38 |
| Arábigo | −0.65 | −0.10 | 0.16 |
| Tarim | −0.55 | −0.06 | 0.11 |
| Ogallala (High Plains) | −0.45 | −0.22 | 0.49 |
| Sahara Septentrional | −0.44 | −0.10 | 0.23 |

Tendencias en cm/año, promediadas por área en cada cuenca, de febrero de 2003 a junio de 2026.

La razón está en cómo se construye 2.2. El modelo Catchment no tiene bombeo: en el mundo del modelo nadie riega, así que el modelo por sí solo
nunca agotará un acuífero. El agotamiento llega al agua subterránea de 2.2 únicamente a través de la corrección mensual que GRACE aplica al
modelo, y esa corrección se reparte entre los almacenes de superficie, zona radicular y profundo en lugar de caer solo en el agua subterránea.
Entre correcciones, el modelo vuelve a derivar hacia su propio balance hídrico.

Scanlon et al. (2018) encontraron el mismo aplanamiento en modelos corridos sin ninguna corrección de GRACE. Comparando siete de ellos con tres
soluciones de GRACE en 186 cuencas fluviales entre 2002 y 2014, hallaron que los modelos subestiman gravemente las grandes tendencias a escala de
década que ve GRACE, en ambos sentidos, lo que atribuyen a que el riego y otros usos humanos del agua quedan fuera de la física del modelo. 2.2
sí recibe una corrección de GRACE, así que se le devuelve parte del camino; las razones de arriba son lo que queda.

Tres cuencas discrepan en el signo —el Amazonas, el Congo y el Pechora—, todas ellas lugares donde la tendencia es pequeña frente al ciclo
estacional.

## Para la forma del ciclo estacional, compara la humedad del suelo con el agua total { #for-the-shape-of-the-seasonal-cycle-compare-soil-moisture-against-total-water }

Los dos conjuntos pueden diferir en cuán grande es el vaivén estacional y en cuándo alcanza su máximo. En las 37 cuencas de WHYMAP el vaivén
estacional de 2.2 es una mediana de 1.23 veces el de GRACE; en los 31 acuíferos principales del USGS, 1.52. En algunos sitios es varias veces
mayor:

| Acuífero | GRACE | GLDAS 2.2 | 2.2 / GRACE |
|:---|:---:|:---:|:---:|
| Willamette Lowland | 4.8 | 33.3 | 7.0 |
| Cuenca de París | 3.0 | 17.3 | 5.7 |
| Denver Basin | 1.2 | 4.7 | 4.0 |
| Northern Atlantic Coastal Plain | 2.9 | 9.9 | 3.4 |
| Bassin Sénégalo-Mauritanien | 5.8 | 18.7 | 3.2 |

Altura entre el mes bajo y el mes alto del ciclo estacional promedio, en cm, sin la tendencia a largo plazo, de febrero de 2003 a junio de 2026.

El momento también puede separarse. En el Northern Atlantic Coastal Plain el agua subterránea de GRACE alcanza su máximo en junio y la de 2.2 en
febrero, cuatro meses de diferencia, y los dos ciclos estacionales correlacionan a −0.54: van casi opuestos. El Sahara Septentrional está medio
año desfasado; el Indo enfrenta marzo contra septiembre.

Una sola comparación dice qué regiones harán esto: cuán grande es el ciclo de humedad del suelo al lado del ciclo de agua total. En las cuencas
de WHYMAP esa razón correlaciona a −0.65 con lo bien que concuerdan los dos ciclos de agua subterránea, y a −0.83 en los acuíferos del USGS:
cuanto más oscila la humedad del suelo frente al agua total, peor concuerdan los dos conjuntos. Toda región cuyos ciclos estacionales corren al
revés tiene la humedad del suelo oscilando tanto como el agua total, o más:

| Acuífero | Vaivén del agua total | Vaivén de la humedad del suelo | Razón | Correlación estacional |
|:---|:---:|:---:|:---:|:---:|
| Ogaden-Juba | 2.0 | 3.3 | 1.70 | −0.74 |
| Upper carbonate | 7.2 | 9.9 | 1.37 | −0.60 |
| Sahara Septentrional | 0.5 | 0.7 | 1.35 | −0.83 |
| Cambrian-Ordovician | 9.9 | 11.4 | 1.15 | −0.38 |
| Indo | 5.7 | 6.3 | 1.11 | −0.39 |
| Northern Atlantic Coastal Plain | 7.9 | 8.4 | 1.06 | −0.54 |

Las regiones donde los dos conjuntos concuerdan tienen razones entre 0.4 y 0.6: la humedad del suelo explica cerca de la mitad del vaivén total,
y al agua subterránea que queda le sobra ciclo propio.

La aritmética lo explica. En la ruta de GRACE, el agua subterránea es lo que queda tras sacar del total medido la humedad del suelo, la nieve y
el agua del dosel. Donde la humedad del suelo del modelo sube y baja tanto como el total medido, y en la misma época del año, ambas casi se
cancelan, y lo que queda alcanza su máximo cuando el suelo está más seco. El ciclo de agua subterránea resultante es la pequeña diferencia entre
dos números grandes y parecidos, así que es sensible a cualquier error en cualquiera de los dos.

En el Northern Atlantic Coastal Plain eso coloca el máximo de agua subterránea de GRACE cuatro meses después de que el nivel freático esté
realmente más alto, mientras que el máximo de febrero de 2.2 cae donde lo pondría la recarga de fin de invierno. La causa probable son los
niveles freáticos someros: parte de lo que los modelos de GLDAS 2.1 cuentan como humedad del suelo es agua subterránea, de modo que la resta
elimina la señal subterránea dos veces. Getirana, Kumar y Rodell (2025) formulan la versión general de este argumento: los compartimentos de un
modelo no son los almacenes físicamente separados que la resta supone.

**Prefiere 2.2 para la forma estacional donde la humedad del suelo oscila tanto como el agua total.** La comprobación lleva un minuto en la
aplicación: dibuja las capas SMa y TWSa de tu región y compara la altura de sus ciclos estacionales.

## Para la recarga, usa GRACE { #for-recharge-use-grace }

Barbosa et al. (2025) aplicaron el método de fluctuación del nivel freático a ambos conjuntos en la Cuenca del Volta y obtuvieron 17.4 y
36.1 cm/año con 2.2 frente a 5.8 y 10.7 cm/año con GRACE, mientras que los pozos daban una mediana de 10.4. Recomiendan 2.2 para tendencias y no
para recarga (ver [Cuenca del Volta](../case-studies/volta.md)). Un ciclo estacional desfasado es una segunda razón para la misma conclusión: el
método lee un valle y un pico de la serie, y si sus meses están mal, la estimación de recarga lo está con ellos.

## Resumen { #summary }

| Lo que buscas | Usa | Porque |
|:---|:---|:---|
| Una tasa de agotamiento o recuperación, en cm/año o km³/año | GRACE | 2.2 aplana las tendencias a cerca de una cuarta parte |
| La forma y el momento del ciclo estacional | 2.2 donde la humedad del suelo oscila tanto como el agua total; si no, cualquiera | la resta puede invertir el calendario |
| Una región de unas pocas celdas | 2.2 | promediada en 0.25° donde la otra está en 1° |
| Una serie mensual sin interrupciones | 2.2 | el modelo atraviesa los vacíos de GRACE |
| Recarga por el método WTF | GRACE | Barbosa et al. (2025), más el riesgo de fase |
| Una cifra de incertidumbre por celda | GRACE | 2.2 no publica ninguna |
| Cualquier cosa anterior a febrero de 2003 | GRACE | el registro de 2.2 empieza ahí |
| Un resultado que pienses publicar | ambos | y di dónde concuerdan y dónde no |

Dos respuestas independientes que coinciden son difíciles de descartar. Donde discrepen, dibuja las piezas: una diferencia que vive en la
humedad del suelo es un problema distinto de una que vive en el agua total.

## Hasta dónde está validado todo esto { #how-far-any-of-this-is-validated }

Los números de esta página salen de comparar entre sí los dos conjuntos publicados, lo que establece cómo difieren y por qué, y no resuelve nada
sobre cuál está más cerca del nivel freático. El respaldo independiente de las recomendaciones es indirecto:

- **Los modelos subestiman las tendencias.** Scanlon et al. (2018), siete modelos globales frente a tres soluciones de GRACE en 186 cuencas.
- **El método del residuo es estructuralmente frágil.** Getirana, Kumar y Rodell (2025), sobre que los almacenes de los modelos no son los
  compartimentos separables que la resta necesita.
- **Las dos soluciones mascon concuerdan a escala de cuenca y divergen en tendencias.** Scanlon et al. (2016), CSR y JPL en 176 cuencas.
- **La comparación in situ es más difícil de lo que parece.** Chen, Famiglietti, Scanlon y Rodell (2016) señalan que convertir niveles de pozo en
  almacenamiento exige un rendimiento específico por pozo, que es incierto incluso donde la red de monitoreo es densa. Bhanja et al. (2016)
  llevaron a cabo una comparación así en toda la India.

Ninguno de esos estudios evaluó estos dos conjuntos uno contra otro, y ninguno usó esta aplicación. La validación directa con pozos aquí llega
solo al [Valle Central](../case-studies/central-valley.md) y a los pozos del Volta de Barbosa et al. Toma las recomendaciones de arriba como un
razonamiento a partir de la construcción y del comportamiento medido, apoyado en la literatura sobre cada mecanismo, y no como una clasificación
validada.

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
- Scanlon, B. R., Zhang, Z., Save, H., Wiese, D. N., Landerer, F. W., Long, D., Longuevergne, L., y Chen, J. (2016). Global evaluation of new
  GRACE mascon products for hydrologic applications. *Water Resources Research*, 52, 9412–9429.
  [doi:10.1002/2016WR019494](https://doi.org/10.1002/2016WR019494){:target="_blank"}
- Scanlon, B. R., Zhang, Z., Save, H., Sun, A. Y., Müller Schmied, H., van Beek, L. P. H., et al. (2018). Global models underestimate large
  decadal declining and rising water storage trends relative to GRACE satellite data. *Proceedings of the National Academy of Sciences*, 115(6),
  E1080–E1089. [doi:10.1073/pnas.1704665115](https://doi.org/10.1073/pnas.1704665115){:target="_blank"}
