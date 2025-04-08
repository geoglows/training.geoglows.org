!!! danger "La descarga masiva generalmente no es necesaria"
    La mayoría de los usuarios no necesitan este tutorial. Todos los productos de pronóstico y simulación retrospectiva están disponibles para consultas, descargas masivas y a través del servicio de datos. Sin embargo, las instrucciones para consultar datos son la forma más rápida, conveniente (y económica para GEOGLOWS) para la mayoría de los usos.  
    Por favor, sigue el tutorial sobre [cómo consultar datos de ríos](query-data.es.md) antes de continuar con esta sección.


## Referencias

La mayoría de los usuarios no necesitan descargar el resultado completo de la simulación para todo el mundo. A menudo, puede ser suficiente con una consulta/descarga más grande. Si decide continuar, debe estar familiarizado con awscli o algún equivalente similar. Una regla general útil para estimar el espacio en disco necesario es:

- 1 día de pronósticos son aproximadamente 150 GB
- La simulación retrospectiva por hora en formato zarr son aproximadamente 6 TB
- La simulación retrospectiva diaria en formato zarr son aproximadamente 500 GB
- La simulación retrospectiva mensual en formato zarr son aproximadamente 20 GB
- La simulación retrospectiva anual en formato zarr son aproximadamente 2 GB

## awscli

La mejor manera de descargar grandes cantidades de datos de los buckets de S3 es utilizando una herramienta de línea de comandos diseñada para este propósito. Estas herramientas permiten descargar múltiples conjuntos de datos simultáneamente y a velocidades más altas que las posibles mediante el navegador web. La herramienta básica para esto es awscli.
Use los [tutoriales de AWS S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/download-objects.html){:target="_blank"} para comenzar.

!!! tip "Usa `--no-sign-request`"
    Usa la bandera `--no-sign-request` para evitar errores, especialmente si no tienes credenciales de AWS en tu computadora.

Al descargar datos de los buckets de S3, las URIs raíz para el bucket de pronósticos es `s3://geoglows-v2-forecast/` y para el bucket retrospectivo es `s3://rfs-v2/`.

El patrón general del comando CLI para los conjuntos de datos de pronósticos es:

```shell
aws s3 cp s3://geoglows-v2-forecast/<fecha>.zarr </ruta/local/de/guardado> --recursive --no-sign-request
```
El patrón general del comando CLI para los conjuntos de datos retrospectivos es:

```shell
aws s3 cp s3://rfs-v2/daily.zarr </ruta/local/de/guardado>  --recursive --no-sign-request
```

## s5cmd
`s5cmd` es una alternativa de alto rendimiento a `awscli`. Consulte [la documentación de s5cmd](https://github.com/peak/s5cmd){:target="_blank"}. El patrón general del comando CLI para los conjuntos de datos de pronósticos es:

```shell
s5cmd --no-sign-request cp "s3://geoglows-v2-forecast/<fecha>.zarr/*" </ruta/local/de/guardado.zarr/>

```
