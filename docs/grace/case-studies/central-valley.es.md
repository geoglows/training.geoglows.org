# Valle Central de California: corrección de GRACE con datos de pozos

!!! cite "Artículo"
    Stevens, M. D., Ramirez, S. G., Martin, E.-M. H., Jones, N. L., Williams, G. P., Adams, K. H., Ames, D. P., and Pulla, S. T. (2025).
    **Groundwater storage loss in the Central Valley analysis using a novel method based on in situ data compared to GRACE-derived data.**
    *Environmental Modelling & Software*, 186, 106368.
    [doi:10.1016/j.envsoft.2025.106368](https://doi.org/10.1016/j.envsoft.2025.106368){:target="_blank"}

## Contexto { #setting }

!!! tip "Qué región elegir en la aplicación"
    **Central Valley aquifer system**, del conjunto **Principal Aquifers, USA (USGS)**: 52,500 km², el contorno de la aplicación más próximo a
    los ~52,000 km² sobre los que trabajó el estudio. El conjunto **Global Aquifers** también ofrece **California Central Valley**, pero ese
    contorno tiene 71,000 km², un tercio más grande, y promedia GRACE sobre terreno que el estudio no incluyó.

El Valle Central de California mide unos 700 km de largo y 80 km de ancho, unos 52,000 km², y es uno de los sistemas acuíferos con más bombeo del
mundo. Es más angosto que un solo mascon de GRACE de 3° (unos 333 × 264 km a esa latitud), y el descenso por bombeo se concentra en el valle
mientras las montañas circundantes se comportan de otra manera. Eso lo convierte en un caso típico de [fuga de señal](../mission/resolution-and-leakage.md#leakage):
promediado sobre el valle, GRACE subestima la pérdida de almacenamiento.

## Una estimación independiente a partir de pozos { #an-independent-estimate-from-wells }

El estudio construyó un registro de almacenamiento a partir de datos de pozos para 1960–2020:

![Análisis del almacenamiento de agua subterránea con datos in situ](../../static/images/grace/papers/cv-fig3-workflow.webp)

*Análisis del almacenamiento de agua subterránea con datos in situ. (a) se identifican los pozos con vacíos en los datos, (b) los vacíos se imputan con un algoritmo de aprendizaje
automático de varios pasos que incorpora observaciones de la Tierra, (c) se usa interpolación temporal y luego espacial para generar rásteres de nivel de agua
variables en el tiempo, (d) los rásteres de nivel de agua se combinan con coeficientes de almacenamiento para estimar el cambio de almacenamiento de agua subterránea en cada intervalo de tiempo.
Reproducido de Stevens et al. (2025), Fig. 3, © 2025 Elsevier, reutilizado bajo los derechos de los autores.*

1. Los pozos de las bases de datos del USGS y del California Department of Water Resources se filtraron por longitud de registro; el estudio comparó umbrales de
   150, 75 y 50 meses con observaciones (181, 572 y 921 pozos).
2. Los vacíos del registro de cada pozo se rellenaron en tres etapas: interpolación PCHIP en los vacíos de menos de 120 días, luego un modelo
   de aprendizaje automático entrenado para cada pozo con el Índice de Severidad de Sequía de Palmer y GLDAS (Noah a 0.25°, versión 2.0 antes
   de 2000 y 2.1 después), y luego un refinamiento iterativo que se reentrenaba con los tres pozos mejor correlacionados.
3. Los registros rellenados se interpolaron por kriging en superficies mensuales de nivel de agua sobre una cuadrícula de 0.1°, recortada al valle.
4. Los cambios de nivel de agua se convirtieron en cambios de almacenamiento con el mapa de rendimiento específico del USGS Central Valley Hydrologic Model (CVHM).

Con el umbral de 75 meses, la curva de almacenamiento basada en pozos coincidió estrechamente con el CVHM (r² = 0.87, RMSE 9.04 km³).

## Calibración de GRACE { #calibrating-grace }

La GWSa de GRACE para el valle, convertida a volumen, siguió la curva basada en pozos en su temporalidad pero fue mucho menor. El estudio la
tomó de GGST, la predecesora de esta aplicación, leyendo los mascones de JPL ya remuestreados a 0.5° con los factores de ganancia de la NASA:
el mismo producto y el mismo escalado que la aplicación ofrece hoy, en una versión anterior (RL06.1 v03 frente a la RL06.3 v04 de la
aplicación; ver [Factores de ganancia](../gldas/deriving-groundwater.md#gain-factors)). La corrección de la fuga de señal que sigue se aplica
encima de ese escalado.

En 2002–2021 las dos series correlacionan con r² = 0.725, y esa cifra se mantiene con cualquier factor de escala, porque un multiplicador
constante deja la correlación intacta. Son los errores los que fijan el factor. Una prueba de sensibilidad de 3.5 a 6 situó el RMSE más bajo en
5.5 con las series alineadas en la fecha de inicio de GRACE, y en 4.5 con los pozos retrasados seis meses; los autores se decidieron por 5
(± 1.0) como el valor que sirve con cualquiera de las dos alineaciones. Con 5, el error medio es de −14.4 km³ y el RMSE de 21.2 km³.

![Comparación de la curva de almacenamiento basada en pozos con GRACE escalado por 5](../../static/images/grace/papers/cv-fig11-grace-75obs.webp)

*Comparación de la imputación iterativa de pozos con GRACE usando el conjunto de datos con umbral de 75 meses de observación. Reproducido de Stevens et al. (2025), Fig. 11,
© 2025 Elsevier, reutilizado bajo los derechos de los autores.*

Con el factor aplicado, las pérdidas de almacenamiento de GRACE concuerdan con la mayoría de las estimaciones publicadas para los mismos periodos:

| Estudio publicado | Periodo | Pérdida publicada | GRACE × 5 en este estudio |
|---|---|---|---|
| Famiglietti et al. (2011) | oct 2003 – mar 2010 | 20.3 km³ | 26.7 km³ |
| Scanlon et al. (2012) | oct 2006 – mar 2010 | 31 km³ | 31.1 km³ |
| Xiao et al. (2017) | abr 2002 – sep 2016 | 64.6 km³ | 70.7 km³ |
| Ojha et al. (2018) | dic 2006 – ene 2010 | 21.3 km³ | 53.2 km³ |

El ± 1.0 muestra aquí su efecto: un factor de 4 deja el periodo de Famiglietti en 21.4 km³ frente a sus 20.3 km³, más cerca que los 26.7 km³ que
da un factor de 5. Ojha et al. (2018) sigue siendo más del doble, y los autores lo señalan sin explicarlo. La cifra de GRACE para Xiao et al.
llega hasta agosto de 2016, porque septiembre aún no estaba disponible.

## Conclusiones { #conclusions }

- Los registros de pozos con vacíos rellenados pueden producir una historia de almacenamiento que concuerda con un modelo regional calibrado de agua subterránea.
- Esa historia da una forma directa de calibrar un factor de escala de fuga de señal para GRACE, de alrededor de 5 para el Valle Central.
- Una vez calibrado, GRACE puede seguir el cambio de almacenamiento en el valle en adelante, y el mismo enfoque podría usarse en regiones con pocos datos que tengan
  algunos registros de pozos.

**Para usuarios de la aplicación:** en un acuífero pequeño o angosto, el promedio de GRACE de la aplicación capta la temporalidad y la dirección del cambio de almacenamiento, pero puede
subestimar su magnitud varias veces. Un factor de escala calibrado con pozos corrige eso, solo para ese acuífero.
