# Diccionario de datos

## Variables explicativas

El conjunto de datos está etiquetado con un total de 102 categorías, esto define la variable objetivo, y enfoca el desarrollo del proyecto en un modelo de clasificación, además, cada una de las categorías tiene entre 40 y 258 imágenes, lo que implica que es un conjunto de datos desbalanceado.

Adicional, el conjunto de datos está dado sólo por la imagen y la etiqueta de la flor que representa la imagen, por lo tanto, el conjunto de datos carece de mayor información o variables que pueda ayudar con el entrenamiento del modelo, por lo que el modelo se enfoca solamente en la correcta clasificación de las imágenes que se le pueda dar en representación de una flor.

## Variable objetivo

Las imágenes se encuentran en 3 diferentes carpetas (train, valid, test), la división de estas carpetas se encuentra desde el repositorio original en Kaggle, razón por la cual se decide para objetivos del proyecto mantener las mismas. Sin embargo, es de gran importancia poder generar las etiquetas (102) correspondientes a cada una de las imágenes, la cual se puede extraer de la estructura de la información que se tiene, a continuación, se muestra un ejemplo de dicha estructura sobre el conjunto test: 

![Carpetas](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/carpetas.png)

Para realizar la extracción de las etiquetas se realiza el uso de la librería os, en donde se genera una iteración para cada conjunto de imagenes, cada categoria y finalmente para cada una de imágenes, posteriormente, dichas etiquetas son guardadas en un array, el cual será utilizado más adelante en la etapa de modelamiento. el detalle de la función utilizada se puede encontrar en el notebook [Creación etiqueta](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/scripts/preprocessing/Creacion%20etiqueta.ipynb)


## Correspondencia etiquetas

Con la ejecución del procedimiento detallado anteriormente, se logra obtener la correspondencia de cada etiqueta a cada imagen, sin embargo, estas etiquetas corresponden a un número, y es requerido conocer el nombre de la especie a la cual pertenece dicha flor, esto lo podemos lograr con el archivo [cat_to_name.json](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/cat_to_name.json), el cual es un archivo .json que contiene todas las correspondencias de cada especie de flor como su etiqueta en número. Este archivo también se encuentra en el repositorio inicial de Kaggle.

