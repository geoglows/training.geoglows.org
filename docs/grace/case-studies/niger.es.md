# Níger: cambio de almacenamiento y recarga en las cuencas de Iullemeden y del Chad

!!! cite "Artículo"
    Barbosa, S. A., Pulla, S. T., Williams, G. P., Jones, N. L., Mamane, B., and Sanchez, J. L. (2022). **Evaluating groundwater storage change
    and recharge using GRACE data: A case study of aquifers in Niger, West Africa.** *Remote Sensing*, 14(7), 1532.
    [doi:10.3390/rs14071532](https://doi.org/10.3390/rs14071532){:target="_blank"}

El estudio se realizó en el marco del proyecto NASA SERVIR West Africa con el Centro Regional AGRHYMET en Niamey. Sigue el mismo flujo de trabajo que
la aplicación: calcular GWSa para cada acuífero, rellenar los vacíos del registro y estimar la recarga anual con el método de fluctuación del nivel freático (WTF).

## Contexto y datos { #setting-and-data }

El sur de Níger se encuentra sobre dos grandes cuencas sedimentarias. La cuenca de Iullemeden, al oeste, abarca unos 620,000 km² y recibe 550–650 mm de lluvia al
año; el estudio analizó sus acuíferos Continental Intercalaire y Continental Terminal. La cuenca del lago Chad, al este, abarca unos
2.5 millones de km² y recibe 200–400 mm al año; el estudio analizó sus acuíferos Manga y Korama. Casi toda la lluvia cae entre junio y
septiembre, y hay pocos pozos de monitoreo.

![Acuíferos seleccionados de las cuencas de Iullemeden y del Chad](../../static/images/grace/papers/niger-fig4-study-aquifers.webp)

*Acuíferos seleccionados de las cuencas de Iullemeden y del Chad. Barbosa et al. (2022), Fig. 4, CC BY 4.0.*

GWSa se calculó en GGST a partir de la TWSa de los mascons de JPL y la media de los modelos Noah, VIC y CLSM de GLDAS, respecto a la media de 2004–2009, de abril
de 2002 a septiembre de 2021. Los meses faltantes se rellenaron por descomposición estacional: cada valor faltante es la tendencia en ese mes más los valores
estacional y residual promedio de ese mes calendario.

![GWSa medida e imputada](../../static/images/grace/papers/niger-fig7-gwsa-imputed.webp)

*Datos de GWSa medidos (negro) e imputados (rojo), que muestran visualmente que los datos imputados respetan la tendencia de largo plazo y la variación estacional presentes
en los datos. Barbosa et al. (2022), Fig. 7, CC BY 4.0.*

## Cambio de almacenamiento { #storage-change }

En la cuenca de Iullemeden, el almacenamiento subió ligeramente de 2002 a 2011 y mucho más rápido de 2011 a 2021, hasta un aumento total de más de 10 cm
de agua. En la cuenca del Chad, el almacenamiento bajó ligeramente hasta 2011 y subió de 2011 a 2020. La lluvia aumentó en el mismo periodo, pero la
correlación entre almacenamiento y lluvia fue baja (0.2 para Iullemeden y 0.35 para el Chad, con un desfase de 7 meses), por lo que los autores sugieren que el cambio
de uso del suelo también contribuyó.

![Anomalías de almacenamiento de agua subterránea en la región de la cuenca de Iullemeden](../../static/images/grace/papers/niger-fig10-gwsa-iullemeden.webp)

*Anomalías de almacenamiento de agua subterránea en la región de la cuenca de Iullemeden. Barbosa et al. (2022), Fig. 10, CC BY 4.0.*

## Recarga { #recharge }

Los autores aplicaron el método de fluctuación del nivel freático a cada año del registro de GWSa rellenado. El Método 1 cuenta solo el ascenso estacional visible
y da una estimación inferior; el Método 2 suma el drenaje que el ascenso compensó y da una estimación superior.

![Valores estimados de recarga en las cuencas de Iullemeden](../../static/images/grace/papers/niger-fig17-recharge-iullemeden.webp)

*Valores estimados de recarga en las cuencas de Iullemeden. Barbosa et al. (2022), Fig. 17, CC BY 4.0.*

El artículo comparó sus promedios con estudios anteriores en Níger (su Tabla 1):

| Fuente | Región | Método | Periodo | Recarga (cm/año) |
|---|---|---|---|---|
| Barbosa et al. (2022) | Cuenca de Iullemeden | WTF, GRACE | 2002–2011 | 4.0–7.3 |
| Barbosa et al. (2022) | Cuenca de Iullemeden | WTF, GRACE | 2012–2021 | 4.5–9.2 |
| Barbosa et al. (2022) | Cuenca del Chad | WTF, GRACE | 2002–2011 | 2.9–5.4 |
| Barbosa et al. (2022) | Cuenca del Chad | WTF, GRACE | 2012–2021 | 4.1–7.6 |
| Bromley et al. (1997) | Suroeste de Níger | Balance de masa de cloruros | 1992 | 1.3 |
| Leduc et al. (1997) | Sur de Níger | WTF, pozos | 1991 | 5–6 |
| Leduc et al. (2001); Favreau et al. (2002) | Suroeste de Níger | Radioisótopos (¹⁴C y ³H) | décadas de 1950–2000 | 0.1–0.5 |
| Leduc et al. (2001) | Suroeste de Níger | WTF, pozos | décadas de 1990–2000 | 2–5 |
| Vouillamoz et al. (2008) | Suroeste de Níger | WTF, pozos | décadas de 1990–2000 | 2–5 |

Los rangos de este estudio van del Método 1 al Método 2. El Método 1 cae dentro del rango de los estudios anteriores de fluctuación del nivel freático; el Método 2 es
más alto, lo que los autores consideran razonable para un periodo en que el almacenamiento se estaba acumulando. Los métodos de cloruros e isótopos, que integran periodos
mucho más largos, dan valores más bajos.

## Conclusiones { #conclusions }

- El almacenamiento de agua subterránea en ambas cuencas ha ido en aumento durante la última década, así que los acuíferos no están sobreexplotados y hay margen para un mayor
  aprovechamiento, siempre que se siga monitoreando el almacenamiento.
- Los datos satelitales hicieron posible este análisis donde los registros de pozos son demasiado escasos para hacerlo desde tierra.
- Reportar ambos métodos WTF acota la recarga probable.

Para repetir este análisis en cualquier región, pon **Gap filling** en **Seasonal model** y abre el
[Análisis de Recarga](../recharge/opening.md).
