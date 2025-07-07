!!! note
    Los métodos descritos aquí son los medios preferidos para recuperar datos del River Forecast System (RFS).

## Estructuras de Datos

La mayoría de los datos de RFS se almacenan en formato Zarr y están fragmentados de manera que pueden ser consultados de manera eficiente para series temporales. Puedes leer esos archivos Zarr directamente desde AWS S3 utilizando cualquier lenguaje de programación con una biblioteca cliente Zarr. La forma más fácil de hacerlo es en Python utilizando el paquete `geoglows`.

Para recuperar datos, necesitarás conocer el número de ID de los ríos que te interesan. Por favor, revisa el [tutorial sobre cómo encontrar los números de río](find-river-numbers.es.md) antes de continuar.

## Paquete Python geoglows

La forma más sencilla de descargar datos del servicio de datos es utilizando el paquete cliente oficial de Python titulado "geoglows". Para tutoriales completos, por favor consulta la [documentación del paquete Python geoglows](https://geoglows.readthedocs.io){:target="_blank"}.

Para fragmentos de código para tareas comúnmente necesarias, consulta el [Recetario](../tutorials/code-snippets.md).

## Ejemplo en Python

Para escribir tu propio código en Python que lea directorios Zarr, necesitarás los siguientes paquetes:

- [zarr](https://zarr.readthedocs.io/en/stable/){:target="_blank"} >= 3
- [s3fs](https://s3fs.readthedocs.io/en/latest/){:target="_blank"} >= 2025
- [xarray](http://xarray.pydata.org/en/stable/){:target="_blank"} >= 2025

!!! warning
    Las versiones anteriores de estas dependencias también funcionan, pero no están probadas para este sitio de capacitación.

Para encontrar las rutas a los directorios Zarr, deberías consultar el [catálogo de datos](../datasets/catalog.md){:target="_blank"}. Puedes pasar el URI comenzando con `s3://` directamente a la función `xr.open_dataset()`. No necesitas una cuenta de AWS para acceder a los datos, pero debes asegurarte de configurarlo para realizar la consulta de forma anónima, estableciendo storage_options={'anon': True}.

```python
import xarray as xr

retro_hourly_zarr_uri = 's3://rfs-v2/retrospective/hourly.zarr'
ds = xr.open_dataset(retro_hourly_zarr_uri, engine='zarr', storage_options={'anon': True})

# now select the 1 or more rivers you want to get data for
rivers = [621054340, ]

df = ds.sel(river_id=rivers)["Q"].to_dataframe()

# save the dataframe as csv, do some analysis, make a plot, etc
df.to_csv('./my_river_data.csv')
```

## JavaScript Example

To write your own JavaScript code, you will need a dependency which reads from Zarr directories. Some options include:

- [zarrita.js](https://zarrita.dev/){:target="_blank"}
- [zarr.js](https://guido.io/zarr.js/){:target="_blank"}

```javascript
import * as zarr from "https://cdn.jsdelivr.net/npm/zarrita/+esm";

const baseZarrUrl = "http://geoglows-v2.s3-us-west-2.amazonaws.com/retrospective/daily.zarr"

// open the river_id variable
const idStore = new zarr.FetchStore(`${baseZarrUrl}/river_id`);
const idNode = await zarr.open(idStore, {mode: "r", format: 2});
// open the discharge variable
const qStore = new zarr.FetchStore(`${baseZarrUrl}/Q`);
const qNode = await zarr.open(qStore, {mode: "r", format: 2});
// open the time variable
const tStore = new zarr.FetchStore(`${baseZarrUrl}/time`);
const tNode = await zarr.open(tStore, {mode: "r", format: 2});

// get the time values and convert from "time since origin" values to ISO strings
const tUnits = tNode.attrs.units
const tArray = await zarr.get(tNode, [null])
const originTime = tUnits.split("since")[1].trim()
const conversionFactor = {
  seconds: 1,
  minutes: 60,
  hours: 60 * 60,
  days: 60 * 60 * 24,
}[tUnits.split("since")[0].trim()]
const times = [...tArray.data].map(t => {
  let origin = new Date(originTime)
  origin.setSeconds(origin.getSeconds() + (t * conversionFactor))
  return origin.toISOString()
})

// determine the index of the river with your ID of interest
const idArray = await zarr.get(idNode, [null])
const idx = idArray.data.indexOf(760127992)

// get the discharge values for the river with your ID of interest
const qArray = await zarr.get(qNode, [null, idx])

// do something with your arrays of data
console.log("preview of data retrieved:")
console.log("times:", times.slice(0, 50))
console.log("discharge:", qArray.data.slice(0, 50))
```
