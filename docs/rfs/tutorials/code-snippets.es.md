## Descargar datos de pronóstico de RFS para mi río

Si solo necesitas descargar datos para algunos ríos o no deseas escribir código, ¡usa la aplicación web! Nuestras aplicaciones te permiten explorar gráficamente un mapa de ríos, ver y descargar datos de pronóstico o retrospectivos, comparar pronósticos con la última imagen satelital y encontrar enlaces a más información. Visita [hydroviewer.geoglows.org](https://hydroviewer.geoglows.org/es/){:target="_blank"} para comenzar.

## Obtener una lista de IDs en mi cuenca hidrográfica

Cada río en el modelo RFS tiene un atributo llamado "TerminalLink". El TerminalLink es el número de ID del río en la salida de la cuenca hidrográfica en la que se encuentra el río de interés. Todos los ríos en la cuenca tienen la misma salida. Puedes filtrar la tabla de ríos para seleccionar solo aquellos que drenan hacia el mismo río. Puedes usar los conjuntos de datos GIS y realizar esta operación en ArcGIS o QGIS. Puedes encontrar enlaces para obtener los archivos GIS de los ríos en la página de Datos Disponibles y el tutorial sobre Cómo Encontrar Números de Ríos. Alternativamente, puedes hacerlo mediante código utilizando las tablas de metadatos de RFS y la tabla de metadatos del modelo. Necesitarás descargar esa tabla (aproximadamente 250 MB) para resolver este problema mediante código.

<script src="https://gist.github.com/rileyhales/e94f0c51090f26bc396e2289d41edefd.js"></script>

## Recuperar pronóstico para muchos ríos

El paquete de Python de GEOGLOWS te permite solicitar datos para muchos ríos simultáneamente. No es necesario usar bucles `for` en tu código para hacer solicitudes secuenciales de datos para un solo río. Prepara una lista con todos los números de ID de los ríos para los cuales deseas obtener datos. Como ejemplo, podrías obtener una lista de todos los ríos en una cuenca hidrográfica (consulta el tutorial en esta página). Al usar el paquete de Python de GEOGLOWS, puedes pasar esa lista completa de ríos a las funciones para recuperar los datos.

<script src="https://gist.github.com/rileyhales/963be8a9cbbc179d99ed82fd5c61bf46.js"></script>

## Guardar el conjunto de datos de registros de pronóstico

Se generan nuevos pronósticos diariamente. Los flujos promedio del conjunto de modelos que se predice que ocurrirán en las 24 horas entre nuevos pronósticos se archivan cada día al inicio de una nueva simulación de pronóstico. Este conjunto de datos se conoce como el registro de pronóstico. Se actualiza continuamente cada día. Este conjunto de datos no está archivado en un bucket de AWS. Solo está disponible a través del servicio REST para facilitar la creación de gráficos sobre la marcha. Sin embargo, la predicción completa del flujo de los ríos del conjunto de modelos se guarda todos los días.

Por favor, no escribas código que recorra una lista de ríos y descargue los registros de pronóstico cada día. Esto es una carga para el servicio REST y no es tan rápido ni eficiente si el número de ríos es grande. Si deseas descargar una copia de estos, puedes recuperarlos desde AWS, donde se guarda el pronóstico completo del conjunto de modelos cada día, y calcularlos utilizando las herramientas disponibles en el paquete de Python de GEOGLOWS.

<script src="https://gist.github.com/rileyhales/11ac6df64593dabb641ad9f044b23e37.js"></script>

## Guardar una copia local de los datos de pronóstico o retrospectivos

Muchos usuarios desean mantener copias de los nuevos pronósticos en sus propios dispositivos. En particular, algunos usuarios necesitan descargar los datos para poder moverlos a un entorno de cómputo seguro o a un centro de cómputo de alto rendimiento. Puedes usar el paquete de Python de GEOGLOWS para recuperar datos de pronóstico o retrospectivos y guardar una copia.

<script src="https://gist.github.com/rileyhales/ec78fa1c1d6453c407faee8d9c72acea.js"></script>

De forma predeterminada, los datos se descargan como un DataFrame (datos tabulares). Tienes varias opciones para guardar los DataFrames en disco, como Parquet, CSV o Excel. Si estás almacenando tablas grandes de datos, como flujos de río retrospectivos o de pronóstico del conjunto de modelos para muchos ríos, recomendamos el formato Parquet. Será más rápido para leer y escribir, además de más comprimido que muchos otros formatos.

Para usuarios más avanzados, también puedes recuperar datos como un conjunto de datos Xarray, adecuado para datos de mayor dimensión y formatos de archivo como netCDF o Zarr. También puedes guardar conjuntos de datos Xarray en disco en varios formatos. El formato adecuado depende del caso de uso anticipado. Para especificar el formato de los datos a descargar, usa `format='df'` para recuperar tablas de datos (DataFrames) o `format='xarray'` para recuperar como un conjunto de datos multidimensional. La mayoría de los usuarios debería usar el formato predeterminado, DataFrame.
