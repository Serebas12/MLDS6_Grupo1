# Reporte de los modelos entrenados

Teniendo en cuenta el trabajo previo explicado en [baseline_models](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/baseline_models.md), se entrenaron tres redes neuronales convolucionales, cada una con una arquitectura diferente. Se tuvo en cuenta que los datos en nuestro conjunto de entrenamiento presentan un desequilibrio entre las distintas clases, por lo cual, se tomaron aquellas categorías que están mayor representadas en la base, como se explica en el [preprocesamiento](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/Preprocesamiento.md). Adicionalmente, se implementaron técnicas de aumento de datos (data augmentation). 

## Variables de entrada

Optamos para el análisis general de las flores, delimitar la cantidad de categorías para modelar, seleccionando nada más las categorías que cuente con al menos 10 imágenes en el conjunto de validación y testeo (10 para cada muestra). Obtenemos con este resultado una gran reducción de tipos de flores a incluir, siendo un total de 18 categorías en total.

## Variable objetivo

Como variable objetivo tenemos la categoría de cada tipo de flor. Para identificar cada flor se usan números ordenados y el diccionario adjunto del conjunto de datos que nos permite la asociación de cada flor con su categoría para el modelo base.

Para los modelos entrenados con la redefinición del alcance para clasificar sólo 18 tipos de flores, necesitamos reasignar las etiquetas númericas sin perder la información de la correspondncia de la etiqueta inicial. Es decir, si un tipo de flor tiene la categoría 50, y al reasignar la etiqueta es numero 2, tenemos anotado que la etiqueta antigüa de la categoría dos era el número 50. 

### Descripción del modelo 1

El primer modelo desarrollado cuenta con un total de 18 capas, donde tenemos 6 capas convolucionales, 6 capas de pooling correspondiente a cada capa convolucional, una capa (flatten) que vectoriza los datos trabajados por la sección de extracción de características (capas convolucionales y de pooling), dos capas densas con 128 neuronas y activación relu, que organizan y trabajan los datos del vector obtenido con la capa flatten. Finalmente, una capa de dropout y una capa final con 128 neuronas y activación softmax que clasifica las 18 categorías o tipos de flores que tenemos para el desarrollo del proyecto. 
![Arquitectura 128](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/Arquitectura%20128.png)

### Descripción del modelo 2

El segundo modelo desarrollado cuenta con un total de 16 capas, donde tenemos 5 capas convolucionales, 5 capas de pooling correspondiente a cada capa convolucional, una capa (flatten) que vectoriza los datos trabajados por la sección de extracción de características (capas convolucionales y de pooling), dos capas densas con 256 neuronas y activación relu, que organizan y trabajan los datos del vector obtenido con la capa flatten. Finalmente, una capa de dropout y una capa final con 256 neuronas y activación softmax que clasifica las 18 categorías o tipos de flores que tenemos para el desarrollo del proyecto.
![Arquitectura 256](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/Arquitectura%20256.png)

### Descripción del modelo 3

El tercer modelo desarrollado cuenta con un total de 14 capas, donde tenemos 4 capas convolucionales, 4 capas de pooling correspondiente a cada capa convolucional, una capa (flatten) que vectoriza los datos trabajados por la sección de extracción de características (capas convolucionales y de pooling), dos capas densas con 512 neuronas y activación relu, que organizan y trabajan los datos del vector obtenido con la capa flatten. Finalmente, una capa de dropout y una capa final con 512 neuronas y activación softmax que clasifica las 18 categorías o tipos de flores que tenemos para el desarrollo del proyecto.
![Arquitectura 512](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/Arquitectura%20512.png)

## Análisis de los resultados

Con los tres modelos entrenados, el objetivo era analizar cómo el cambio del número de bloques de capas de convolución y pooling podía afectar el desempeño general del modelo. Así mismo, revisar cómo el número de neuronas en las capas de clasificación afectaba el resultado general. Para realizar la comparativa de los modelos, podemos usar métricas de ajuste en la clasificación tales como accuracy, precision, recall, y f1_score y loss.

## Conclusiones

Como se puede ver en el [reporte de MLflow](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/mlflow.md), al hacer la evaluación de las métricas accuracy, precision, recall, y f1_score y loss, concluímos que el mejor modelo es el modelo 3, el cual tiene 512 neuronas en las capas finales de su arquitectura, además de contar con únicamente 4 bloques de capas de convolución y pooling. Con esto se ve que agregar más de 4 bloques de extracción de características, no ayuda a mejorar el modelo, mientras que el uso de más neurones en las capas finales sí mejora la clasificación de las imágenes. 
