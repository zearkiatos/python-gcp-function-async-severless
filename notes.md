# GCP Cloud Storage: Activadores asíncronos para funciones como servicio

## Objetivos

- Orquestar la ejecución de funciones a partir de la ocurrencia de un evento.
- Crear y configurar funciones (Cloud Function) para que se ejecuten ante el evento de carga de los archivos en un bucket de Cloud Storage

> Este taller es una continuación del taller "GCP Funciones y storage". Por lo que si no lo ha realizado, por favor revisarlo antes de iniciar este.

## Estructura de carpetas

En el proyecto encontrará tres carpetas principales:

- La carpeta `procesar-creacion-heroe` en donde se encuentra la implementación de la función que se ejecutará cuando se cargue un archivo al Cloud Storage

## Publicación de la función

### Procesar Creación Heroe

Para poder publicar la función, debe abrir una consola de comandos en la ubicación donde descargamos el repositorio. Posteriormente, debe ejecutar los siguientes comandos:

> No olvide ajustar el valor de <nombre_bucket> con el nombre del bucket creado en el taller 5

```console
cd procesar-creacion-heroe
gcloud functions deploy funcion-bienvenida-heroe-crear --entry-point load --runtime python39 --trigger-resource <nombre_bucket> --trigger-event google.storage.object.finalize --memory 128M --region us-central1 --timeout 60 --min-instances 0 --max-instances 1
cd ..
```

En la consola deberá observar un mensaje de confirmación de creación de la función
