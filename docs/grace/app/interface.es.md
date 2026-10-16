# La Interfaz de la Aplicación

## Abrir la aplicación { #opening-the-app }

Abre [apps.geoglows.org/grace-anomalies](https://apps.geoglows.org/grace-anomalies){:target="_blank"} en una versión actual de Chrome, Edge,
Firefox o Safari. No hay que instalar nada ni iniciar sesión. La primera visita descarga los datos de las capas predeterminadas, lo que puede
tardar unos segundos con una conexión lenta; después, la aplicación guarda una copia en el navegador y abre rápidamente.

![GRACE Regional Analyst al abrirse](../../static/images/grace/app-home.webp)

La ventana tiene tres partes: el **panel de control** a la izquierda, el **mapa** arriba a la derecha y el **panel del gráfico** debajo del mapa.
Arrastra los tres puntos entre el mapa y el gráfico para darle más espacio a cualquiera de los dos; haz doble clic en ellos para restablecer la
división predeterminada.

## Panel de control { #control-panel }

![El panel de control](../../static/images/grace/app-panel.webp){ align=right width="260" }

De arriba hacia abajo:

- **Regions / Global.** Cambia entre la vista regional, que muestra los contornos de las regiones y analiza una región a la vez, y la
  [vista global](global-view.md), que anima el mundo entero. Hacer clic en **Regions** con una región abierta regresa a la vista general.
- **Upload.** Carga el límite de tu propia región desde un archivo GeoJSON (ver [Vista Regional](regional-view.md#uploading-a-region)).
- **Settings.** Ajustes de visualización, descritos más abajo.
- **Dataset** (conjunto de datos). Sobre cuál de los dos conjuntos de datos de agua subterránea tratan el panel, el mapa y el gráfico:
  **GRACE + GLDAS 2.1**, con el agua subterránea obtenida restando tres modelos de superficie terrestre de la medición de GRACE, y
  **GLDAS 2.2**, con el agua subterránea leída de un modelo que asimila GRACE (ver
  [Cálculo del Almacenamiento de Agua Subterránea](../gldas/deriving-groundwater.md)). Una línea bajo el control dice cómo obtiene ese conjunto
  el agua subterránea y con qué resolución. Cambiar de conjunto mantiene seleccionada la misma magnitud y abierta la misma región, así que la
  comparación está a un clic.
- **Displayed layer** (capa mostrada). El componente del almacenamiento que se muestra en el mapa y se grafica en el gráfico: Groundwater
  Storage Anomaly (GWSa, la predeterminada), Total Water Storage Anomaly (TWSa), Soil Moisture Anomaly (SMa), Snow Water Equivalent Anomaly
  (SWEa) y Canopy Water Storage Anomaly (CANa). El desplegable da los nombres completos; las abreviaturas son las que usan la leyenda del
  gráfico y el CSV.
- **Time series** (series temporales). Marca otros componentes para añadirlos al gráfico y compararlos. La capa mostrada siempre se grafica (ver
  [Vista Regional](regional-view.md#the-time-series-chart)).
- **Also show …** (mostrar también). Dibuja en el gráfico las mismas magnitudes del otro conjunto de datos, para poder leer uno frente al otro.
  Refleja lo que esté marcado arriba en lugar de ofrecer un segundo juego de casillas, y no cambia nada en el mapa.
- **Gap filling** (relleno de vacíos). Lo que hace el gráfico en los meses sin datos de GRACE. **None** corta la línea en cada vacío,
  **Straight line** une los meses a ambos lados, y **Seasonal model** rellena los vacíos con valores estimados a partir del resto del registro,
  dibujados como una línea discontinua con marcadores huecos (ver [Vacíos y Relleno de Vacíos](../mission/gap-filling.md)). Este ajuste solo cambia el
  gráfico, nunca el CSV descargado. GLDAS 2.2 no tiene meses faltantes, así que este control queda oculto mientras ese conjunto está
  seleccionado.
- **Color ramp.** Seis paletas. Viridis, Cividis, Brown-Teal y Purple-Green son seguras para personas con deficiencia en la visión de los colores.
- **Layer opacity.** Atenúa las celdas de anomalía para ver el mapa base debajo.
- **Cell boundaries / Mascon boundaries.** Dibuja el contorno de las celdas de la malla, o de los mascones de GRACE de 3° que fijan la
  resolución real de los datos. Los mascones pertenecen a la medición de GRACE, así que ese control queda oculto con GLDAS 2.2.
- **Region names.** Etiqueta los contornos de las regiones al acercarte.
- **Light mode.** Cambia entre el tema claro y el oscuro.
- **Regions.** Elige un conjunto de regiones, fíltralo por nombre y haz clic en un nombre para analizar esa región.

<div style="clear: both;"></div>

Tres de estos controles quedan ocultos en lugar de atenuados mientras está seleccionado **GLDAS 2.2**, porque describen cosas que ese conjunto
de datos no tiene: **Gap filling** (su registro no tiene vacíos), **Mascon boundaries** (es un modelo y no una solución de mascones) y la banda
de incertidumbre del gráfico (es una sola ejecución de un modelo, sin conjunto del que tomar una dispersión). Un control atenuado invita a
preguntarse cómo activarlo, así que se retira.

## Mapa { #map }

El mapa tiene botones de zoom y un menú de mapas base (el icono de capas debajo de los botones de zoom) con los mapas base OpenStreetMap,
topográfico, imágenes, calles, gris claro, gris oscuro y relieve. Hay una barra de escala en la esquina inferior derecha. La barra de colores en la
esquina superior derecha da la escala de las celdas de anomalía, siempre centrada en cero; la leyenda de tendencias aparece encima de ella
mientras se muestran las tendencias.

El **control de tiempo** en la parte inferior del mapa recorre los meses:

![El control de tiempo](../../static/images/grace/app-time-control.webp){ width="410" }

Pulsa reproducir para animar, o arrastra el deslizador. En el conjunto de datos de GRACE el deslizador solo se detiene en meses con datos de
GRACE; GLDAS 2.2 tiene un valor en todos los meses desde febrero de 2003, así que los recorre todos. El mes actual también se marca en el
gráfico con una línea roja discontinua.

## Barra de encabezado { #header-bar }

![La barra de encabezado: ruta de navegación a la izquierda, controles de tendencia a la derecha](../../static/images/grace/app-header.webp){ width="800" }

La ruta de navegación a la izquierda muestra dónde estás: **Home** (la vista general), el nombre de una región, **Global map** o las coordenadas
de una celda seleccionada. Haz clic en **Home** para volver a la vista general. A la derecha, **Analyze trends / Hide trends** activa y desactiva
la clasificación de tendencias, y el selector **Window** fija el periodo sobre el que se calcula la tendencia. Ver
[Análisis de Tendencias](trends.md).

## Ajustes { #settings }

![El cuadro de diálogo Display Settings](../../static/images/grace/app-settings.webp){ width="510" }

- **GRACE Mascon Footprints** y **Anomaly Cell Boundaries:** un deslizador **Boundary width** para cada una de las dos capas de contornos. La
  sección de los mascones lleva además una nota sobre por qué una malla más fina no es una medición más fina.
- **Show color bar on map:** oculta o muestra la barra de colores.
- **Dynamic scale (fit to data):** con esta opción activada, la escala de colores se ajusta a los datos que estás viendo, de modo que las
  anomalías pequeñas siguen siendo visibles. Llega al percentil 95 de los valores absolutos sobre las celdas a la vista y todos los meses, tanto
  en una región como en la vista global, así que unas pocas celdas extremas se saturan en lugar de aplanar todo lo demás. Desactívala para usar
  una escala fija de −30 a +30 cm, que es mejor para comparar capturas de pantalla de distintas regiones.
- **Clear cached data:** borra la copia de los datos que la aplicación guarda en tu navegador. La siguiente visita vuelve a descargarlo todo.
  Úsalo si la aplicación se comporta de forma extraña después de una actualización de datos.

Los ajustes duran hasta que cierras la página. El tema claro u oscuro y el tamaño del panel del gráfico se recuerdan entre visitas.
