# Resultados

La tercera sección de la página Recharge Analysis reporta la recarga de cada año hidrológico, usando los puntos seleccionados en la
[sección anterior](picks.md). Se actualiza en cuanto cambia un punto seleccionado o el inicio del año hidrológico.

## Recarga media { #mean-recharge }

Dos tarjetas dan la media de R1 y R2 sobre todos los años hidrológicos, en cm/año y, para una región o celda, como volumen en km³/año sobre su área:

![R1 y R2 medios del Northern Midwest Aquifer System](../../static/images/grace/app-recharge-summary.webp)

Para el Northern Midwest Aquifer System, la recarga media es de 9.81 cm/año (R1) a 17.88 cm/año (R2), o de 31.4 a 57.3 km³/año sobre 320,368 km².

## Recarga por año hidrológico { #recharge-by-water-year }

El gráfico muestra R1 y R2 de cada año hidrológico como pares de barras, con la media de cada uno como línea discontinua:

![R1 y R2 por año hidrológico del Northern Midwest Aquifer System](../../static/images/grace/app-recharge-chart.webp)

El gráfico muestra cuánto varía la recarga de un año a otro. Para el Northern Midwest Aquifer System, R1 va de 4.1 cm en 2024 a 18.1 cm
en 2023. La diferencia entre cada par de barras es R<sub>D</sub>, el drenaje que suma la línea de recesión, y es mayor en los años con una recesión
pronunciada, como 2013.

## La tabla { #the-table }

La tabla enumera todos los años hidrológicos:

![La tabla de resultados del Northern Midwest Aquifer System](../../static/images/grace/app-recharge-table.webp)

| Columna | Significado |
|---|---|
| Water year | se nombra por el año calendario en que comienza |
| Trough, Peak | los meses de S<sub>B</sub> y S<sub>P</sub> (valle y pico), con ✎ cuando se fijaron a mano |
| S_B, S_P, S_L | el valle, el pico y el final de la línea de recesión, en cm |
| R1, R2 | recarga del año, en cm |
| R1, R2 (km³) | recarga como volumen, para una región o celda |
| Notes | cualquier aspecto que revisar sobre el año |

La última fila da las medias. Haz clic en una fila para abrir ese año en el [editor del año](picks.md#the-year-editor).

La columna Notes señala tres cosas:

- **set by hand**: el valle, el pico o ambos se movieron en el editor.
- **uses filled months**: el pico, el valle o los meses a los que se ajustó la línea de recesión incluyen meses rellenados, así que el resultado depende
  del modelo de relleno de vacíos. Para el Northern Midwest Aquifer System esto aplica a todos los años de 2011 a 2019, cuando a GRACE le faltaron meses
  sueltos y luego los 11 meses entre GRACE y GRACE-FO.
- **long recession extrapolation**: la línea de recesión se prolongó por más del doble de meses de los que se usaron para ajustarla, así que R2 es menos
  confiable que de costumbre.

Un año cuyos puntos no se pueden seleccionar, por ejemplo con un pico fijado a mano que queda antes del pico anterior, muestra el motivo en la columna Notes y
queda fuera de las medias.

## Descarga de los resultados { #downloading-the-results }

**Download CSV** guarda la tabla como `recharge_<region>.csv`. Tiene una fila por año hidrológico y una última fila con las medias:

| Columna | Significado |
|---|---|
| `water_year` | se nombra por el año calendario en que comienza |
| `trough`, `peak` | meses de S<sub>B</sub> y S<sub>P</sub>, como YYYY-MM |
| `S_P_cm`, `S_B_cm`, `S_L_cm` | el pico, el valle y el final de la línea de recesión |
| `R_S_cm`, `R_D_cm` | el ascenso visible y el drenaje sumado |
| `R1_cm`, `R2_cm` | recarga del año |
| `R1_km3`, `R2_km3` | recarga como volumen (solo región o celda) |
| `long_extrapolation` | `true` cuando R2 depende de una extrapolación larga de la recesión |
| `uses_filled_months` | cuáles de `peak`, `trough` y `recession` usan meses rellenados |
| `set_by_hand` | cuáles de `peak` y `trough` se fijaron a mano |
| `note` | el motivo por el que un año no tiene resultado |

## Interpretación de los resultados { #interpreting-the-results }

- **Reporta R1 y R2 juntos.** Acotan la recarga: R1 deja fuera el drenaje durante el ascenso, y R2 prolonga la línea de recesión mucho
  más allá de los meses a los que se ajustó. Lo más probable es que el valor real esté entre ambos.
- **Usa promedios plurianuales.** La incertidumbre ±1σ de un valor mensual de GWSa suele ser tan grande como el ascenso de un solo año: ±4.4 cm frente a un
  R1 medio de 9.8 cm para el Northern Midwest Aquifer System. La estimación de un solo año es incierta, y una media de diez o más años es mucho más
  robusta.
- **Revisa los años que usan meses rellenados.** Los resultados de esos años dependen del modelo de relleno de vacíos, sobre todo alrededor del vacío de 2017–2018 entre
  las misiones.
- **El bombeo no es recarga.** En un acuífero con bombeo intenso, el descenso de la temporada seca incluye el bombeo además del drenaje natural. La línea de
  recesión prolonga ese descenso, así que R<sub>D</sub>, y con él R2, cuenta el bombeo como recarga. Ahí R1 es la estimación más segura.
- **Las regiones pequeñas subestiman el ascenso.** GRACE suaviza los cambios de almacenamiento sobre unos cuantos cientos de kilómetros, así que en una región pequeña o angosta el
  ascenso estacional, y con él la recarga, puede quedar subestimado (consulta
  [Resolución, Fuga de Señal y Regiones Pequeñas](../background/resolution-and-leakage.md)).
- **Compara con estimaciones independientes.** Los hidrogramas de pozos, el balance de masa de cloruros o los estudios publicados sobre el mismo acuífero sirven para verificar los
  valores de GRACE. Los casos de estudio de [Níger](../case-studies/niger.md) y del [Volta](../case-studies/volta.md) comparan la recarga de GRACE con estimaciones basadas en pozos.
