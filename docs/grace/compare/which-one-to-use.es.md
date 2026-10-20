# Cuál usar

Ninguno de los dos conjuntos gana en todas partes. [Cómo se ven las diferencias](examples.md) muestra los casos de los que sale este consejo, y
[Hasta dónde está validado](validation.md) dice cuánto peso puede soportar.

## La respuesta corta { #the-short-answer }

| Lo que busca | Use | Porque |
|:---|:---|:---|
| Una tasa de agotamiento o recuperación, en cm/año o km³/año | GRACE | 2.2 aplana las tendencias a aproximadamente un cuarto |
| La forma y el momento del ciclo estacional | 2.2 donde la humedad del suelo oscila tanto como el agua total; en otro caso, cualquiera | la resta puede invertir el calendario |
| Una región de pocas celdas | 2.2 | promediado a 0,25° donde el otro está a 1° |
| Una serie mensual sin interrupciones | 2.2 | el modelo corre a través de los vacíos de GRACE |
| Recarga por el método WTF | GRACE | Barbosa et al. (2025), y el riesgo de una estación invertida |
| Una cifra de incertidumbre por celda | GRACE | 2.2 no publica ninguna |
| Cualquier cosa anterior a febrero de 2003 | GRACE | el registro de 2.2 empieza ahí |
| Un resultado que vaya a publicar | ambos | y diga dónde coinciden y dónde no |

Dos respuestas independientes que coinciden son difíciles de descartar. Donde discrepen, dibuje las piezas: una diferencia que vive en la humedad
del suelo es un problema distinto de una que vive en el agua total.

## La comprobación antes de fiarse de un ciclo estacional { #the-check-to-run-before-trusting-a-seasonal-cycle }

Una sola comparación dice si puede fiarse del calendario estacional de la ruta de GRACE en su región, y lleva un minuto en la aplicación.

1. Abra su región y dibuje **SMa** y **TWSa** del conjunto GRACE.
2. Compare la altura de sus ciclos estacionales, del mes más bajo al más alto.
3. Si la humedad del suelo oscila la mitad que el agua total o menos, el ciclo subterráneo de GRACE tiene forma propia. Cualquiera de los dos
   conjuntos sirve para preguntas estacionales.
4. Si la humedad del suelo oscila tanto como el agua total o más, la resta está cancelando casi toda la señal. Prefiera 2.2 para la forma y el
   momento del ciclo, y no lea el mes del máximo de GRACE como el mes en que el nivel freático está más alto.

En 299 acuíferos esa proporción predice la concordancia entre los dos ciclos estacionales con una correlación de −0,75. Por debajo de 0,7 la
concordancia mediana es 0,93; por encima de 1,0 es −0,39.

## Antes de tratar una gran diferencia como un resultado { #before-treating-a-large-difference-as-a-result }

1. Dibuje la nieve (**SWEa**). El hielo y la nieve explican la mayoría de los extremos, y un ciclo subterráneo con la forma del ciclo de nieve
   invertido es el término de nieve.
2. Dibuje el agua total (**TWSa**) de ambos conjuntos. Donde los totales coinciden y solo discrepa el agua subterránea, los dos están dividiendo
   la columna de forma distinta y la medición del satélite no está en cuestión.
3. Compare la amplitud estacional de la humedad del suelo (**SMa**) frente al agua total, como arriba.
4. Compruebe cuánta agua se mueve en realidad. Por debajo de unos 5 cm de variación los dos conjuntos correlacionan a una mediana de 0,19, y ese
   número no dice nada sobre ninguno de ellos.
5. Pregúntese si un río, una llanura de inundación, un lago o un embalse podrían explicar el agua.

## Para qué sirve la GWSa, en cualquiera de los dos conjuntos { #what-gwsa-is-good-for-in-either-dataset }

Ambos conjuntos responden preguntas regionales de dirección y ritmo: ¿está bajando el almacenamiento de este acuífero, a qué velocidad, y se
frenó el descenso tras un cambio de política o una racha de años húmedos? Ninguno sirve para decisiones a escala de un campo de pozos o de un
solo distrito de riego, y ninguno dice nada sobre niveles ni sobre calidad del agua. Ambos promedian el cambio de almacenamiento sobre un área
mucho mayor que un campo de pozos, y ambos meten el agua superficial en el término subterráneo.

Donde existan pozos de monitoreo, compare la tendencia con el cambio de almacenamiento estimado a partir de los pozos. Esa comparación es la
comprobación más fuerte disponible para cualquiera de los dos conjuntos, y la coincidencia entre ambos refuerza a los dos.

## Referencias { #references }

- Barbosa, S. A., Jones, N. L., Williams, G. P., Teklu, H., Yidana, S. M., Pulla, S. T., et al. (2025). A Multi-Source Approach to Groundwater
  Storage and Recharge Assessment in the Volta Basin. *Science of the Total Environment*.
  [doi:10.1016/j.scitotenv.2025.180421](https://doi.org/10.1016/j.scitotenv.2025.180421){:target="_blank"}
