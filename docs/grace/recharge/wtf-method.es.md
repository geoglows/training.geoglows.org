# El Método WTF

## Recarga a partir del ascenso del nivel freático { #recharge-from-a-rising-water-table }

El método de fluctuación del nivel freático (WTF) estima la recarga de agua subterránea a partir del ascenso de los niveles de agua subterránea que sigue a una temporada húmeda (Healy y
Cook, 2002). En un clima con una temporada seca y una temporada húmeda al año, el almacenamiento se vacía durante los meses secos a medida que el agua subterránea descarga hacia
ríos, manantiales, pozos y evapotranspiración. Cuando la lluvia o el deshielo llegan al nivel freático, el almacenamiento vuelve a subir. La magnitud de ese ascenso
mide cuánta agua entró al acuífero.

En el hidrograma de un pozo, el ascenso es un cambio de carga hidráulica, Δh, y la recarga es el rendimiento específico del acuífero multiplicado por ese ascenso:

$$
R = S_y \, \Delta h
$$

El rendimiento específico rara vez se conoce bien y varía dentro de un acuífero, así que suele ser la mayor fuente de error en una estimación basada en pozos.
GRACE elimina ese paso. GWSa ya es una lámina de agua, el cambio en el almacenamiento de agua subterránea promediado sobre la región, así que, aplicado a GWSa, el
método da la recarga directamente en centímetros por año, sin rendimiento específico:

$$
R = \Delta \text{GWSa}
$$

Barbosa et al. (2022) aplicaron el método de esta forma a las cuencas de Iullemeden y del Chad en Níger, usando el registro de agua subterránea de GRACE en lugar de
hidrogramas de pozos (consulta [Casos de Estudio](../case-studies/niger.md)).
La página Recharge Analysis de la aplicación sigue su enfoque.

## Un año hidrológico { #one-water-year }

El método trabaja un año hidrológico a la vez. Un año hidrológico contiene una temporada seca seguida de una temporada húmeda, así que comienza en el mes en que
el almacenamiento suele estar en su punto más bajo. Para cada año hidrológico, el método necesita cuatro valores de GWSa:

![El método de fluctuación del nivel freático aplicado a un año hidrológico](../../static/images/grace/wtf-concept.png)

- **S<sub>A</sub>**, el pico de la temporada húmeda anterior, donde comienza la recesión de la temporada seca
- **S<sub>B</sub>**, el valle, el almacenamiento más bajo antes del ascenso de este año
- **S<sub>P</sub>**, el pico que alcanza esta temporada húmeda
- **S<sub>L</sub>**, el almacenamiento que habría alcanzado el acuífero en el momento del pico si hubiera seguido vaciándose sin recarga

La línea de recesión da S<sub>L</sub>. Se ajusta una línea recta a GWSa desde S<sub>A</sub> hasta S<sub>B</sub>, lo que da la tasa a la
que el almacenamiento se vacía sin recarga. Esa pendiente se prolonga luego desde S<sub>B</sub> hasta el mes del pico:

$$
S_L = S_B + m \, (t_P - t_B)
$$

donde *m* es la pendiente de la línea ajustada (cm por mes), y *t*<sub>B</sub> y *t*<sub>P</sub> son los meses del valle y del pico.

## Dos estimaciones de la recarga { #two-estimates-of-recharge }

El ascenso visible del valle al pico es

$$
R_S = S_P - S_B
$$

El acuífero sigue vaciándose mientras se recarga, así que parte del agua que llegó durante la temporada húmeda volvió a salir antes del pico
y nunca aparece en el ascenso. La línea de recesión estima esa pérdida como el descenso adicional que habría mostrado el almacenamiento sin recarga:

$$
R_D = S_B - S_L
$$

Juntas dan dos estimaciones, que la aplicación reporta como R1 y R2:

$$
\begin{aligned}
R_1 &= R_S = S_P - S_B \\
R_2 &= R_S + R_D = S_P - S_L
\end{aligned}
$$

R1 cuenta solo el ascenso visible, así que es una estimación inferior. R2 suma el drenaje ocurrido durante el ascenso, pero depende de prolongar la
línea de recesión sobre meses a los que no se ajustó, y la tasa de drenaje suele disminuir a medida que baja el almacenamiento, así que R2 es una estimación superior.
Barbosa et al. (2022) los llaman Método 1 y Método 2 y reportan ambos. Lo más probable es que la recarga real esté entre los dos.

Cuando el almacenamiento estaba estable o subiendo antes del valle, no hay drenaje que corregir: la aplicación fija S<sub>L</sub> = S<sub>B</sub>, y R2
es igual a R1.

## Aplicación del método a datos de GRACE { #applying-the-method-to-grace-data }

Los datos de GRACE difieren del registro de un pozo en varios aspectos, y la aplicación maneja cada uno.

**Vacíos.** El método necesita un valor para cada mes: un mes faltante en un pico o un valle cambia el resultado de ese año. El Análisis de Recarga
solo está disponible con el relleno de vacíos **Seasonal model**, y se ejecuta sobre la serie rellenada (consulta [Vacíos en el Registro](../gap-filling/gaps.md)). Los años cuyos
puntos seleccionados o cuya línea de recesión caen en meses rellenados se marcan en los resultados.

**Tendencias de largo plazo.** Muchas regiones tienen un descenso o ascenso sostenido del almacenamiento a lo largo del registro. Si se seleccionaran sobre la serie original, un descenso pronunciado
empujaría el mes más alto de cada año al inicio del año hidrológico y su mes más bajo al final. La aplicación selecciona los meses de pico y de valle en
la serie sin la tendencia de largo plazo (la tendencia del modelo estacional), y luego lee S<sub>P</sub>, S<sub>B</sub> y la línea de recesión
en la propia serie rellenada.

**El año hidrológico.** La aplicación busca el mes con el valor más bajo en el ciclo estacional promedio y comienza cada año hidrológico en ese mes. Puedes
elegir otro mes de inicio (consulta [Años Hidrológicos y Selección de Puntos](picks.md)).

**Los puntos seleccionados.** En cada año hidrológico, S<sub>P</sub> es el mes más alto de la serie sin tendencia. S<sub>B</sub> es el mes más bajo sin tendencia
entre el pico del año anterior y el pico de este año. S<sub>A</sub> es el pico del año anterior. El primer año hidrológico del registro no tiene
pico anterior, así que su S<sub>A</sub> es el mes más alto sin tendencia antes de su valle.

**La línea de recesión.** La línea es un ajuste por mínimos cuadrados a la GWSa rellenada desde S<sub>A</sub> hasta S<sub>B</sub>. Cuando el valle llega menos
de cuatro meses después de S<sub>A</sub>, el ajuste usa en su lugar los cuatro meses que terminan en el valle, de modo que nunca se ajusta una pendiente a dos o tres
puntos.

**Unidades.** GWSa está en centímetros de agua, así que R1 y R2 están en cm por año, promediados sobre la región. Multiplicados por el área de la región
dan un volumen:

$$
V\,[\text{km}^3/\text{año}] = R\,[\text{cm/año}] \times 10^{-5} \times A\,[\text{km}^2]
$$

## Dónde se aplica el método { #where-the-method-applies }

El método interpreta el ascenso de cada año como la recarga de ese año, así que necesita un ciclo anual claro con una temporada de recarga al año. Funciona mejor
donde:

- el almacenamiento sube y baja una vez al año, aproximadamente en la misma época cada año
- la oscilación estacional es grande comparada con la incertidumbre ±1σ de un valor mensual de GRACE
- el descenso de la temporada seca es drenaje natural y no bombeo

No se aplica donde la recarga ocurre todo el año sin un ascenso claro, en regiones áridas con poca recarga estacional, ni donde los periodos húmedos
y secos plurianuales dominan el registro. La aplicación evalúa estas condiciones en cada serie antes de ejecutar el método (consulta
[Apertura del Análisis](opening.md)).

## Referencias { #references }

- Healy, R. W., and Cook, P. G. (2002). Using groundwater levels to estimate recharge. *Hydrogeology Journal*, 10, 91–109.
  [doi:10.1007/s10040-001-0178-0](https://doi.org/10.1007/s10040-001-0178-0){:target="_blank"}
- Barbosa, S. A., Pulla, S. T., Williams, G. P., Jones, N. L., Mamane, B., and Sanchez, J. L. (2022). Evaluating groundwater storage change and
  recharge using GRACE data: A case study of aquifers in Niger, West Africa. *Remote Sensing*, 14(7), 1532.
  [doi:10.3390/rs14071532](https://doi.org/10.3390/rs14071532){:target="_blank"}
