# Diccionario de datos

## Variables

El conjunto de datos está etiquetado con un total de 102 categorías, esto define la variable objetivo, y enfoca el desarrollo del proyecto en un modelo de clasificación, además, cada una de las categorías tiene entre 40 y 258 imágenes, lo que implica que es un conjunto de datos desbalanceado.

Adicional, el conjunto de datos está dado sólo por la imagen y la etiqueta de la flor que representa la imagen, por lo tanto, el conjunto de datos carece de mayor información o variables que pueda ayudar con el entrenamiento del modelo, por lo que el modelo se enfoca solamente en la correcta clasificación de las imágenes que se le pueda dar en representación de una flor.

## Variable objetivo

Las imágenes se encuentran en 3 diferentes carpetas (), la división de estas carpetas se encuentra desde el repositorio original en Kaggle, razón por la cual se decide para objetivos del proyecto mantener las mismas. Sin embargo, es de gran importancia poder generar las etiquetas (103) correspondientes a cada una de las imágenes, la cual se puede extraer de la estructura de la información que se tiene, a continuación, se muestra un ejemplo de dicha estructura: 

![Imagen1](MLDS6_Grupo1/docs/data/Prueba.png)

Para realizar la extracción de las etiquetas se realiza el uso de la librería os, en donde se genera una iteración para cada conjunto de imanes, cada caregoria y finalmente para cada una de imágenes, posteriormente, dichas etiquetas son guardadas en un array, el cual será utilizado más adelante en la etapa de modelamiento.
