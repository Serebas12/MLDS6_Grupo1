# Reporte de Datos

Este documento contiene los resultados del análisis exploratorio de datos.

## Resumen general de los datos

El conjunto de datos contiene un total de 8,189 imágenes, clasificadas en 102 categorías o etiquetas distintas, y almacenadas en formato .jpg. El peso total del conjunto de datos es de 330.74 MB. Además, incluye un catálogo de etiquetas en inglés que proporciona los nombres de las flores representadas en cada imagen.

## Resumen de calidad de los datos

Nuestro conjunto de datos presenta un desbalanceo significativo, ya que cada una de las 102 categorías abarca un rango de imágenes que oscila entre 40 y 258. Esta diversidad refleja más fielmente la complejidad y variabilidad que encontramos en escenarios del mundo real, aunque pueda presentar desafíos en el entrenamiento de modelos de aprendizaje profundo debido a la insuficiencia de muestras por categoría. Es indispensable considerar estrategias de desarrollo adicionales para lograr resultados óptimos en este contexto.

Al revisar nuestra base de entrenamiento, vemos que todas las imágenes del conjunto de datos son legibles y pueden cargarse fácilmente, lo que elimina cualquier obstáculo en la lectura de datos para nuestro proyecto. Además, el hecho de que todas las imágenes estén en formato .jpg simplifica aún más su manejo e integración en nuestro flujo de trabajo, garantizando una implementación fácil y eficiente durante el desarrollo del proyecto.

Adicionalmente, al examinar los tamaños de las imágenes con las que contamos en cada categoría, se concluye que si bien sus resoluciones están en un rango de alrededor de 500 a 800 pixeles en ancho y altura, estas no tienen, en general, el mismo tamaño por lo que vemos la necesidad de reescalarlas para tener consistencia en el proceso de entrenamiento.

## Limpieza de datos

Una vez cargado y analizado el contenido de nuestro conjunto de datos, se procederá a la transformación del mismo, de manera que permita la posterior ejecución de los modelos propuestos. Teniendo en cuenta que este proyecto busca realizar la clasificación de imágenes, se hará uso de redes convolucionales, las cuales tienen un mejor desempeño para este tipo de información insumo. En una fase posterior de análisis, se tomará la decisión de usar una red entrenada (Transfer Learning) o realizar un entrenamiento desde cero.

Adicionalmente, para lograr el mejor resultado del modelo y considerando que las imágenes tienen diferentes tamaños, se realizará un escalado de cada imagen para dejarlas en tensores de dimensión (224,224,3), donde se manejarán 3 canales, ya que todas las imágenes presentes en el conjunto de datos son a color.

Finalmente, para la etapa de modelado, requerimos que la información se encuentre separada por datos de entrenamiento, validación y prueba, requerimiento que ya se cumple, dado que la información en Kaggle se presenta de está forma. Por lo cual procederemos a hacer el procesamiento de información para cada conjunto de imágenes.

### Imágenes Conjunto Entrenamiento

La información del conjunto de entrenamiento se encuentra separada en carpetas, una para cada categoría, con un total de 102. Se realiza una iteración sobre cada categoría, para posteriormente realizar la transformación y re escalado de cada imagen, información que será alojada en la variable X_train, adicionalmente, se guardará la respectiva etiqueta en Y_train, la cual es extraída del nombre de la ruta de cada categoría.

Adicionalmente, se realiza un análisis en la distribución de la cantidad de imágenes en cada categoría para el conjunto de entrenamiento, encontrando que las categorías tienen de 27 a 206 imágenes, dato relevante, ya que será teniendo en cuenta posteriormente para la elección del modelo a usar.

![Entrenamiento](https://github.com/Serebas12/MLDS6_Grupo1/assets/169107851/bc48b8d3-6d52-48dc-96e7-9a7c9611a2b1)

### Imágenes Conjunto Validación

Semejante al conjunto de entrenamiento, las imágenes de validación se encuentran separadas en carpetas por cada categoría. Se realiza una iteración sobre cada carpeta, para posteriormente realizar la transformación y re escalado de cada imagen, información que será alojada en la variable X_valid, adicionalmente, se guardará la respectiva etiqueta en Y_valid, la cual es extraída del nombre de la ruta de cada categoría.

Referente a la distribución de la cantidad de imágenes en cada categoría para el conjunto de validación, se encuentra que las categorías tienen de 1 a 28 imágenes.

![Validación](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/Validaci%C3%B3n.png)

###  Imágenes Conjunto Test

Semejante al conjunto de entrenamiento, las imágenes de prueba se encuentran separadas en carpetas por cada categoría. Se realiza una iteración sobre cada carpeta, para posteriormente realizar la transformación y re escalado de cada imagen, información que será alojada en la variable X_test, adicionalmente, se guardará la respectiva etiqueta en Y_test, la cual es extraída del nombre de la ruta de cada categoría.

Referente a la distribución de la cantidad de imágenes en cada categoría para el conjunto de pruebas, se encuentra que las categorías tienen de 2 a 28 imágenes.

![Prueba](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/Prueba.png)


## Ranking de variables

Al contar con imágenes de flores y su respectiva etiqueta, no contamos en este punto con un ranking de variables. Por lo tanto, será necesario establecer una metodología de representación para cada una de las imágenes, la cual incluya componentes como la forma y el color de la flor, lo cual nos ayude a su correcta clasificación por categorías.

## Relación entre variables explicativas y variable objetivo

Como vimos anteriormente, las flores en cada categoría cuentan con características comunes que nos van a permitir realizar un proceso adecuado de clasificación. Además de esto, por no contar con variables diferentes a las imágenes y su etiqueta, no contamos con variables redundantes ni es posible realizar análisis de correlación de variables.
