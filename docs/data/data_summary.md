# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

El conjunto de datos contiene un total de 8,189 imágenes, clasificadas en 102 categorías o etiquetas distintas, y almacenadas en formato .jpg. El peso total del conjunto de datos es de 330.74 MB. Además, incluye un catálogo de etiquetas en inglés que proporciona los nombres de las flores representadas en cada imagen.

## Resumen de calidad de los datos

Nuestro conjunto de datos presenta un desbalanceo significativo, ya que cada una de las 102 categorías abarca un rango de imágenes que oscila entre 40 y 258. Esta diversidad refleja más fielmente la complejidad y variabilidad que encontramos en escenarios del mundo real, aunque pueda presentar desafíos en el entrenamiento de modelos de aprendizaje profundo debido a la insuficiencia de muestras por categoría. Es indispensable considerar estrategias de desarrollo adicionales para lograr resultados óptimos en este contexto.

Al revisar nuestra base de entrenamiento, vemos que todas las imágenes del conjunto de datos son legibles y pueden cargarse fácilmente, lo que elimina cualquier obstáculo en la lectura de datos para nuestro proyecto. Además, el hecho de que todas las imágenes estén en formato .jpg simplifica aún más su manejo e integración en nuestro flujo de trabajo, garantizando una implementación fácil y eficiente durante el desarrollo del proyecto.

Adicionalmente, al examinar los tamaños de las imágenes con las que contamos en cada categoría, se concluye que si bien sus resoluciones están en un rango de alrededor de 500 a 800 pixeles en ancho y altura, estas no tienen, en general, el mismo tamaño por lo que vemos la necesidad de reescalarlas para tener consistencia en el proceso de entrenamiento.

## Variable objetivo

El conjunto de datos está etiquetado con un total de 102 categorías, esto define la variable objetivo, y enfoca el desarrollo del proyecto en un modelo de clasificación, además, cada una de las categorías tiene entre 40 y 258 imágenes, lo que implica que es un conjunto de datos desbalanceado.

## Variables individuales

El conjunto de datos está dado sólo por la imagen y la etiqueta de la flor que representa la imagen, por lo tanto, el conjunto de datos carece de mayor información o variables que pueda ayudar con el entrenamiento del modelo, por lo que el modelo se enfoca solamente en la correcta clasificación de las imágenes que se le pueda dar en representación de una flor.

## Ranking de variables

Al contar con imágenes de flores y su respectiva etiqueta, no contamos en este punto con un ranking de variables. Por lo tanto, será necesario establecer una metodología de representación para cada una de las imágenes, la cual incluya componentes como la forma y el color de la flor, lo cual nos ayude a su correcta clasificación por categorías.

## Relación entre variables explicativas y variable objetivo

Como vimos anteriormente, las flores en cada categoría cuentan con características comunes que nos van a permitir realizar un proceso adecuado de clasificación. Además de esto, por no contar con variables diferentes a las imágenes y su etiqueta, no contamos con variables redundantes ni es posible realizar análisis de correlación de variables.
