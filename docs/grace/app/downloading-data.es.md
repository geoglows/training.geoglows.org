# Descarga de Datos

## Descargar un CSV { #downloading-a-csv }

Con una región o una celda seleccionada, haz clic en **Download CSV** en la esquina superior derecha del panel del gráfico. El archivo contiene los
valores mensuales de las cinco capas para esa región o celda, independientemente de cuáles estén graficadas. Se llama `grace_gwsa_data.csv` para
una región (la parte central corresponde a la capa mostrada) o `grace_cell_<lat>_<lon>_data.csv` para una sola celda.

| Columna | Contenido |
|---|---|
| `Date` | Primer día del mes, `YYYY-MM-DD` |
| `GWSa`, `TWSa`, `SMa`, `SWEa`, `CANa` | Anomalía media del mes ponderada por área, en cm de equivalente de agua líquida |
| `<layer>_upper`, `<layer>_lower` | La media más y menos 1σ |
| `GWSa_filled`, `TWSa_filled` | La misma serie con sus vacíos rellenados por el modelo estacional; igual al valor observado en todos los demás meses |
| `GWSa_is_filled`, `TWSa_is_filled` | 1 en los meses que rellenó el modelo estacional, 0 en los demás |

Por ejemplo, el inicio del vacío entre misiones para el Sistema Acuífero Northern Midwest:

```text
Date,GWSa,GWSa_upper,GWSa_lower,GWSa_filled,GWSa_is_filled,TWSa,...
2017-06-01,9.529,14.913,4.146,9.529,0,12.536,...
2017-07-01,,,,11.146,1,,...
2017-08-01,,,,12.694,1,,...
```

El archivo tiene una fila por cada mes desde abril de 2002 hasta la publicación más reciente. En los meses sin datos de GRACE, las celdas de
`GWSa` y `TWSa` están vacías, mientras que las capas de GLDAS (`SMa`, `SWEa`, `CANa`) sí tienen valores, porque los modelos de superficie terrestre
se ejecutan todos los meses. Las columnas `_filled` aportan un valor para esos meses (ver [Vacíos en el Registro](../gap-filling/gaps.md)). Se
escriben con cualquier ajuste de **Gap filling**, así que el archivo es el mismo sin importar cómo se dibuje el gráfico.

Excel, Google Sheets, Python y R leen el archivo directamente, y las fechas ISO no necesitan conversión (en pandas, usa
`pd.read_csv(path, parse_dates=["Date"])`). Para obtener la incertidumbre σ a partir de los límites, calcula `(upper − lower) / 2`.

## Convertir a volumen { #converting-to-volume }

Las anomalías son láminas de agua promediadas sobre la región. Multiplica por el área de la región para obtener un volumen:

```text
ΔV (km³) = GWSa (cm) × Area (km²) / 100,000
```

Por ejemplo, una GWSa de −12 cm sobre un acuífero de 400,000 km² equivale a 12 × 400,000 / 100,000 = 4.8 km³ (4,800 millones de m³) de agua menos
que el promedio de 2004–2009. El cambio entre dos fechas es la diferencia de sus anomalías multiplicada por el área, y una tendencia en cm/año
multiplicada por el área da una tasa de pérdida o ganancia en km³/año.

Usa el área de la región tal como la definiste. Para una región subida, un SIG puede calcular el área del polígono; calcúlala en una proyección de
igual área, no en grados.

## Qué hacer después { #what-to-do-next }

El CSV es el punto de partida para análisis fuera de la aplicación. Para estimar la recarga, usa el [análisis de recarga](../recharge/opening.md) de
la aplicación, que aplica el método de fluctuación del nivel freático a la serie rellenada y tiene su propia descarga en CSV.
[El Modelo Estacional](../gap-filling/seasonal-model.md#filling-the-gaps) describe cómo se estiman las columnas `GWSa_filled` y `TWSa_filled`.
