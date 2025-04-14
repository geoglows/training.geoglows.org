## Términos y Vocabulario

- **ERA5**: La quinta generación del reanálisis atmosférico del clima global del ECMWF. Es el conjunto de datos de reanálisis más reciente producido por el Centro Europeo de Pronósticos Meteorológicos a Medio Plazo (ECMWF). Está disponible desde 1940 hasta el presente y se actualiza diariamente con un desfase de 5 días.
- **Reanálisis**: Un producto modelado que incorpora datos in situ y/o de teledetección para proporcionar la mejor estimación posible de las condiciones hidrometeorológicas históricas. Los datos de reanálisis se utilizan como insumos para el modelo RFS.

---

## Descripción General

La simulación retrospectiva de RFS es una simulación determinista con una duración de más de 85 años, a resolución horaria, que comienza el 1 de enero de 1940. La simulación retrospectiva y muchos productos derivados se actualizan semanalmente. Está basada en el conjunto de datos ERA5. Los nuevos datos de ERA5 se producen cada día con un desfase de 5 días respecto al tiempo real, por lo tanto, el mínimo desfase posible es de 5 días. Una vez a la semana, todos los nuevos datos de ERA5 desde la última simulación se utilizan para extender la simulación retrospectiva, devolviendo el desfase a 5 días.

![image](../../static/images/retrospective_graph.png)

El conjunto de datos es determinista y está basado en modelado de superficie terrestre mediante reanálisis, lo que significa que hay solo 1 valor por intervalo de tiempo, a diferencia de los pronósticos. La simulación retrospectiva proporciona caudales promedio horarios que se remuestrean a promedios diarios, mensuales y anuales. Los caudales se reportan como el promedio que ocurrió durante el siguiente intervalo (hora, día, mes o año). Las fechas se reportan al inicio del intervalo en la zona horaria UTC +00:00 (por ejemplo, fechas "alineadas a la izquierda"). El valor dado representa el caudal promedio desde ese momento hasta el siguiente intervalo. Todos los valores están en metros cúbicos por segundo.

Los datos de promedios mensuales están disponibles en dos formatos diferentes. Uno está optimizado para leer toda la serie temporal de un solo río o grupo de ríos, lo cual se anticipa como el caso de uso más común. El otro está optimizado para leer múltiples ríos en un momento específico.

| Propiedad del Modelo              | Simulación Retrospectiva      |
|-----------------------------------|-------------------------------|
| Fecha más antigua                 | 01 de enero de 1940           |
| Tipo de simulación                | Determinista                  |
| Miembros del conjunto             | 1                             |
| Tiempo de desfase                 | 5-12 días desde el presente   |
| Paso de tiempo                    | Promedio horario              |
| Frecuencia de actualización       | Semanal, domingo 00:00 UTC    |
| Descarga masiva disponible        | Sí                            |
| Consulta y subconjunto disponible | Sí                            |

---

## Productos Derivados

### Periodos de Retorno

Un periodo de retorno es una estimación de cuán infrecuentemente ocurre un flujo alto extremo (inundación) o un periodo prolongado de bajo caudal (sequía). Los periodos de retorno han sido precalculados utilizando la Distribución de Gumbel y la Distribución Log-Pearson Tipo 3, y los caudales máximos horarios promedio de cada año completo. Los periodos de retorno precalculados se usan para definir niveles de alerta para cada segmento de río en el modelo. Los valores precalculados son para intervalos de recurrencia de 2, 5, 10, 25, 50 y 100 años. Puedes calcular un periodo de retorno usando tu método preferido accediendo al mismo conjunto de datos de máximos anuales.

### Curvas de Duración de Caudal

**Las Curvas de Duración de Caudal (FDCs)** son una representación de los patrones de flujo en un río. Relacionan cada caudal con una probabilidad de excedencia. La probabilidad de excedencia es la posibilidad de que cualquier valor de caudal muestreado al azar sea mayor o igual al caudal correspondiente a esa probabilidad. Las grandes inundaciones tienen una baja probabilidad de excedencia, mientras que los bajos caudales tienen una alta probabilidad de excedencia. Las FDCs son herramientas útiles para entender la variabilidad del caudal y la probabilidad de diferentes tasas de flujo. Las FDCs están precalculadas para cada mes (es decir, 12 curvas en total que representan cada mes) y para todo el periodo de registro del río. Estas ayudan a comprender el caudal a lo largo del año y los cambios estacionales, lo cual es aplicable a la gestión efectiva de recursos hídricos, la previsión de inundaciones y la comprensión de los patrones hidrológicos.
