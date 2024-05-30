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
  
- **Diagrama de arquitectura:** (imagen que muestra la arquitectura del sistema que se utilizará para desplegar el modelo)

## Código de despliegue

- **Archivo principal:** (nombre del archivo principal que contiene el código de despliegue)
- **Rutas de acceso a los archivos:** (lista de rutas de acceso a los archivos necesarios para el despliegue)
- **Variables de entorno:** (lista de variables de entorno necesarias para el despliegue)

## Documentación del despliegue

- **Instrucciones de instalación:** (instrucciones detalladas para instalar el modelo en la plataforma de despliegue)
- **Instrucciones de configuración:** (instrucciones detalladas para configurar el modelo en la plataforma de despliegue)
- **Instrucciones de uso:** (instrucciones detalladas para utilizar el modelo en la plataforma de despliegue)
- **Instrucciones de mantenimiento:** (instrucciones detalladas para mantener el modelo en la plataforma de despliegue)
