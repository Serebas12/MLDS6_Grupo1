# Despliegue de modelos

## Infraestructura

- **Nombre del modelo:** Clasificación de Flores

- **Plataforma de despliegue:** (plataforma donde se va a desplegar el modelo)
  
- **Requisitos técnicos:** Para los requisitos en la ejecución del proceso se deben tener en cuenta las siguientes consideraciones: 
1.	El código fue desarrollado con Python 3.10.12
2.	Las librerías utilizadas con sus respectivas versiones son:
   
![Dependencias](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/deployment/Dependencias.png)

4.	Referente a las especificaciones de máquina, en el alcance del proyecto se utilizó una máquina estándar de Google Colab con 12.7 GB de RAM y 107.7 GB de memoria, se recomienda como mínimo tener estas especificaciones en la infraestructura donde se desplegara la solución, ahora bien, si se requiere el análisis de múltiples imágenes (ejecución en batch) o la implementación del modelo en tiempo real como un endpoint, se recomienda realizar pruebas de carga y estrés para identificar la infraestructura necesaria para dar cumplimiento a las expectativas de los tiempos de ejecución y costos del proyecto a implementar.  

  
- **Requisitos de seguridad:** El proyecto fue desarrollado con el fin de que cualquier persona interesada en la clasificación de especies de flores pudiera realizar uso de los resultados obtenidos, razón por la cual no hay ninguna consideración de seguridad que se deba contemplar en este punto, adicionalmente, es importante menciona que la información con la cual se entrenó el modelo es publica, por lo cual tampoco tiene ninguna implicación referente a la seguridad de la información. La seguridad dependerá netamente de como el usuario requiera hacer uso del proceso desarrollado.
  
- **Diagrama de arquitectura:** El modelo será implementado mediante CLI, lo cual permite que la infraestructura sea decidida por el usuario que realice uso del modelo entrenado. Para el desarrollo y pruebas del mismo en el alcance del proyecto se utilizó una máquina de Google Colab con especificaciones de 12.7 GB de RAM y 107.7 GB de memoria. De manera de recomendación, se adjunta una arquitectura de referencia en GCP para la ejecución de casos en real time o en batch, lo cual dependerá del caso de uso y puede ser implementada por el usuario.

1. **Arquitectura Batch**

![Batch](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/deployment/Batch.png)

**Google Cloud Storage:** Tiene como objetivo alojar todas las imágenes las cuales serán sujetas al proceso de clasificación. 

**Compute Engine:** Es una máquina virtual que tiene como objetivo el despliegue y ejecución del CLI. Es posible la calendarización de las ejecuciones o ejecuciones a demanda. 

**BigQuery:** En este componentes se alojarán los resultados obtenidos de la clasificación, en formato estructurado.

2. **Arquitectura Real time**

![RealTime](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/deployment/RealTime.png)

**Cliente:** El cliente realiza una petición mediante el endpoint disponibilizado, en donde se debe adjuntar la imagen objetivo a clasificar. 

**Cloud Run:** En este componente se desplegará el CLI desarrollado, y será el encargado de la ejecución del mismo, para posteriormente regresar la respuesta al cliente.

**Google Cloud Storage:** Tiene como objetivo el guardar todas las imágenes que sean cargadas al proceso, con el fin de posteriormente utilizarlas en un reentrenamiento del modelo, o incluso, poder tener trazabilidad de las ejecuciones realizadas. 

**BigQuery:** En este componentes se alojarán los resultados obtenidos de la clasificación, en formato estructurado, con una traza de metadatos sobre cada llamada al API realizada.

Finalmente, se debe considerar la capada de seguridad y autenticación en cada uno de los casos, los cuales dependerán de los requerimientos que tiene el usuario para la implementación del mismo, ya sea por políticas de la empresa donde trabaja o por criterio propio.

## Código de despliegue

- **Archivo principal:** (nombre del archivo principal que contiene el código de despliegue)
- **Rutas de acceso a los archivos:** (lista de rutas de acceso a los archivos necesarios para el despliegue)
- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

## Documentación del despliegue

- **Instrucciones de instalación:** (instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
