# Cuenca del Volta: separar un gran embalse del agua subterránea

!!! cite "Artículo"
    Barbosa, S. A., Jones, N. L., Williams, G. P., Teklu, H., Yidana, S. M., Pulla, S. T., Sanchez, J. L., Nelson, E. J., Ames, D. P., and
    Miller, A. W. (2025). **A multi-source approach to groundwater storage and recharge assessment in the Volta Basin.** *Science of The Total
    Environment*, 1001, 180421. [doi:10.1016/j.scitotenv.2025.180421](https://doi.org/10.1016/j.scitotenv.2025.180421){:target="_blank"}

## Contexto y datos { #setting-and-data }

La cuenca del Volta abarca unos 400,000 km² en Ghana, Burkina Faso, Togo, Malí, Costa de Marfil y Benín. El lago Volta, detrás de la presa de Akosombo,
cubre solo cerca del 2% de la cuenca, pero almacena un volumen de agua grande y variable.

![Ubicación de la cuenca del Volta](../../static/images/grace/papers/volta-fig1-study-area.webp)

*Ubicación de la cuenca del Volta. Barbosa et al. (2025), Fig. 1, CC BY 4.0.*

El estudio usó la TWSa de los mascons de JPL y el ensamble de GLDAS 2.1 de abril de 2002 a diciembre de 2022, el mismo balance hídrico que la aplicación, y agregó un
término de agua superficial, SWSa, calculado a partir de la altimetría Copernicus del lago Volta:

```text
GWSa = TWSa − (SMa + SWEa + CANa + SWSa)
```

Los vacíos se rellenaron por descomposición estacional con una tendencia lineal por tramos, el enfoque que usa la aplicación (consulta
[El Modelo Estacional](../gap-filling/seasonal-model.md)). El estudio también comparó los resultados con el almacenamiento de agua subterránea calculado directamente por el modelo
Catchment de GLDAS 2.2, con la lluvia de CHIRPS y con 10 pozos de monitoreo en la subcuenca del Nasia.

## Por qué importa el lago { #why-the-lake-matters }

El lago Volta representa cerca de la mitad del cambio total de almacenamiento de agua de la cuenca. Sin el término del lago, la GWSa calculada sigue al lago: de
2002 a 2012 es casi por completo agua del lago. Al quitar el lago, el almacenamiento de agua subterránea cambió poco hasta cerca de 2012 y luego subió, con una
ganancia total de unos 30 km³, o unos 10 cm de agua, en 2002–2022.

![SWSa a partir de la altimetría del lago Volta, y GWSa con y sin el lago](../../static/images/grace/papers/volta-fig6-swsa-gwsa.webp)

*Anomalía de almacenamiento de agua superficial (SWSa) calculada a partir de datos de altimetría del lago Volta y anomalía de almacenamiento de agua subterránea (GWSa) obtenida con y sin
considerar la SWSa. Barbosa et al. (2025), Fig. 6, CC BY 4.0.*

La GWSa de la aplicación para esta cuenca corresponde a la curva verde, porque la aplicación no resta el agua superficial (consulta
[Cálculo del Almacenamiento de Agua Subterránea](../background/deriving-groundwater.md#the-water-balance)).

GLDAS 2.2, que asimila GRACE, mostró la misma tendencia pero oscilaciones estacionales mucho mayores, así que los autores lo recomiendan para tendencias pero no para
estimar la recarga.

![GWSa de la cuenca del Volta según el modelo CLSM de GLDAS 2.2](../../static/images/grace/papers/volta-fig7-gldas22-vs-grace.webp)

*Anomalía de almacenamiento de agua subterránea (GWSa) de la cuenca del Volta obtenida con el modelo CLSM de GLDAS 2.2. Barbosa et al. (2025), Fig. 7, CC BY 4.0.*

## Recarga { #recharge }

Aplicado a la GWSa de GRACE para 2010–2020 (los años anteriores a 2010 no tenían un ciclo estacional claro), el método de fluctuación del nivel freático dio una recarga
promedio de 5.8 cm/año (Método 1) y 10.7 cm/año (Método 2). Los pozos de la subcuenca del Nasia dieron una mediana de 10.4 cm/año, suponiendo un rendimiento
específico de 0.05, y un estudio anterior de Obuobie et al. (2012) dio 8.6 cm/año. GLDAS 2.2 dio 17.4 y 36.1 cm/año, muy por encima de las demás estimaciones.

![Diagrama de caja de la recarga en la cuenca del Volta](../../static/images/grace/papers/volta-fig8-recharge-boxplot.webp)

*Diagrama de caja de la recarga en la cuenca del Volta estimada con los Métodos 1 y 2 de WTF usando datos de GRACE, usando el nuevo conjunto de datos de GLDAS V2.2, con WTF
usando datos de pozos de observación, y según un estudio previo de Obuobie et al. (2012). Barbosa et al. (2025), Fig. 8, CC BY 4.0.*

## Conclusiones { #conclusions }

- El almacenamiento de agua subterránea en la cuenca subió unos 30 km³ en 2002–2022, sobre todo después de principios de la década de 2010.
- En una cuenca con un gran embalse, dejar el agua superficial fuera del balance atribuye al agua subterránea los cambios del embalse.
- La recarga basada en GRACE concuerda con las estimaciones basadas en pozos y con estudios anteriores, así que GRACE puede respaldar estimaciones de recarga donde el monitoreo es
  escaso.

**Para usuarios de la aplicación:** antes de interpretar la GWSa como agua subterránea en una cuenca con un gran lago, embalse o humedal, revisa qué parte de la señal de almacenamiento
corresponde al agua superficial, y quítala si es grande.

Para repetir este análisis en cualquier región, pon **Gap filling** en **Seasonal model** y abre el
[Análisis de Recarga](../recharge/opening.md).
