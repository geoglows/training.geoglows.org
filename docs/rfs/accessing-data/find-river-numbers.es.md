## Visión general

Existen 6.25 millones de segmentos de río modelados en los conjuntos de datos RFS V2. Estos números son únicos para el conjunto de datos TDX-Hydro y son diferentes de los números en cualquier otro conjunto de datos de arroyos y versiones anteriores del modelo. Todos los números de identificación tienen 9 dígitos. Como referencia, esta tabla proporciona los ID de algunos ríos principales y sus ubicaciones generales.

| Número de ID | Ríos seleccionados y ubicaciones generales |
|--------------|---------------------------------------------|
| 760021611    | Mississippi, EE. UU.                        |
| 160064246    | Nilo, África Oriental                      |
| 710462910    | Colorado, EE. UU. y México                  |
| 441057380    | Ganges, India                               |
| 430157411    | Mekong, Vietnam                             |
| 210406913    | Tíber, Italia                              |
| 621010293    | Amazonas, Brasil                            |
| 130747391    | Congo, República Democrática del Congo     |
| 640255644    | Paraná, Argentina                           |

Los números de ID de RFS son de 9 dígitos. Aunque los números grandes a menudo se delimitan, comúnmente con una coma o punto en varios idiomas, cualquier código que escribas para recuperar datos ***no debe*** incluir delimitadores. Estos ID son enteros. La mayoría de los lenguajes de programación interpretarán las comillas, puntos, comas u otros caracteres como algo distinto a un entero, lo que hará que el proceso de recuperación falle. Por ejemplo, el número `123456789` ***no debe*** escribirse como `123,456,789` o `123.456.789` o `"123456789"` o `"123,456,789"` o cualquier otra variación. Solo la representación entera `123456789` funcionará.

!!! warning "Usuarios migrando desde V1"
    RFS v2 se deriva de un Modelo de Elevación Digital (DEM) diferente al de v1 y tiene significativamente más ríos modelados. Debido a la mayor resolución y los cambios en la ubicación de los canales de ríos, no es posible proporcionar un mapeo de todos los números de la versión 1 a los números de la versión 2. Hemos detallado algunos pasos a continuación para mapear un ID antiguo a un ID RFS 2.

## Uso de la aplicación web

La forma más fácil de encontrar el ID de un río es utilizar la [aplicación web RFS](https://hydroviewer.geoglows.org/es/){:target="_blank"}. Haz clic en un río en el mapa. Para asegurarte de hacer clic en el río exacto que deseas, el mapa hará un zoom a un nivel de detalle mayor si estás demasiado alejado. Después de hacer clic en un río, el mapa identificará el segmento de río en el que hiciste clic y el ID se presentará en la ventana emergente con gráficos y otra información.

## Uso de los datos de hidrografía

Los datos de hidrografía están disponibles en el [catálogo de datos](../datasets/catalog.es.md){:target="_blank"}. Puedes descargar y ver los ríos o cuencas en un software GIS como ArcGIS o QGIS. Puedes hacer clic en las características o usar herramientas de análisis espacial para seleccionar muchos ríos. Los números de ID de esos ríos están almacenados en el atributo LINKNO.

## Encontrar ríos con Lat/Lon

Existen muchos métodos para intentar encontrar un ID de río dado una latitud y longitud. Ninguno es perfecto para todos los casos. Existen varios errores potenciales de métodos automatizados debido a la precisión y exactitud de tus puntos lat/lon, la precisión de las líneas de los arroyos en esa ubicación específica, si deseas ajustarte al punto de salida más cercano o al arco de arroyo más cercano, si tu lat/lon está cerca de una confluencia donde el GIS podría confundirse debido a tener múltiples opciones cercanas, etc. Los métodos automatizados deben considerarse imperfectos y verificados por precisión contra otras fuentes como una cuenca conocida aguas arriba en el lat/lon de un punto de medición, el nombre del río, comparaciones con mapas base de imágenes u otros medios.

Un método para comenzar es cargar los archivos GIS de los arroyos para tu área de interés en un software GIS. Puedes ajustarlos al arco de arroyo más cercano. En QGIS, la herramienta se llama "Snap geometries to layer”. Usa el algoritmo para encontrar el punto más cercano e insertar vértices adicionales si es necesario.

Otro método es descargar los polígonos de las cuencas y cruzarlos con una capa que contenga tus puntos lat/lon. El trabajo GIS es sencillo, pero ocasionalmente menos preciso y requiere descargas de archivos más grandes.
