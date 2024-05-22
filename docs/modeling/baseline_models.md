# Reporte del Modelo Baseline

El modelo inicial fue desarrollado previamente con resultados que usamos para la redefinición del modelo y desarrollo del mismo, donde encontramos lo siguiente.

## Descripción del modelo

El modelo desarrollado previamente contaba con un total de 14 capas, donde tenemos 5 capas convolucionales, 5 capas de pooling correspondiente a cada capa convolucional, una capa (flatten) que vectoriza los datos trabajados por la sección de extracción de características (capas convolucionales y de pooling), dos capas densas que organizan y trabajan los datos del vector obtenido con la capa flatten, y una capa final que clasifica las 102 categorías o tipos de flores que tenemos dispocisión para el desarrollo del proyecto. 

Con esto decidimos replantear el análisis, debido que observamos varios problemas en el desarrollo, y que podemos corregir en este momento.

## Variables de entrada

Como entrada del modelo se tiene un total de 102 tipos de flores diferentes, donde tenemos casos donde el conjunto de validación o testeo puede ser de sólo una flor. 

Acá optamos para el análisis general de las flores, delimitar la cantidad de categorías para modelar, seleccionando nada más las categorías que cuente con al menos 10 imagenes en el conjunto de validación y testeo (10 para cada muestra). Obtenemos con este resultado una gran reducción de tipos de flores a incluir, siendo un total de 18 categorías en total.

## Variable objetivo

La correcta clasificación de cada tipo de flor, para esto se usa números ordenados para identificar cada flor, y el diccionario adjunto del conjunto de datos que nos permite la identificación de cada flor para el modelo base.

Para los modelos entrenados con la redefinición del alcance para clasificar sólo 18 tipos de flores necesitamos reasignar las etiquetas númericas, donde hacemos una reasignación sin perder la información de la correspondncia de la etiqueta inicial, es decir, si un tipo de flor tiene la categoría 50, y al reasignar la etiqueta es numero 2, tenemos anotado que la etiqueta antigüa de la categoría dos era el número 50. 

## Evaluación del modelo

Para la evaluación del modelo obtenemos un accuracy con el conjunto de testeo del 62% y el f1-score de ...

### Resultados de evaluación

Se puede observar a continuación la evaluación del f1-score individual de cada categoría, donde obtenemos varios tipos de flores con cero, y a modo de evidencia la necesidad de hacer un alcance del conjunto de datos.

![f1_score_modelo_base](https://github.com/Serebas12/MLDS6_Grupo1/assets/166343815/b8477ca1-c588-45dd-a096-eab65c727bae) 

Adicional hacemos una extención de los estadísticos recall y precition donde obtenemos de manera más clara la necesidad del acotamiento que mencionamos.

![tabla resultados iniciales](https://github.com/Serebas12/MLDS6_Grupo1/assets/166343815/c7e6f334-5796-4827-ac10-179405a264f5)

## Análisis de los resultados

Dentro del ejercicio inicial, observamos que un modelo con arquitectura sencilla es suficiente para este proyecto, pues previamente logramos hacer la comparativa con arquitecturas de modelos con reconocimiento público y mayor complejidad para el aprendizaje de imágenes, pero en este caso particular, esos modelos lograron tener una gran tendencia a sobreajustarse, pero el modelo a la medida logró obtener un ajuste más equilibrado.

## Conclusiones

El modelo tiene buenos resultados de clasificación para algunas categorías, pero no para todas, sobretodo para las categorías con baja información, por lo tanto es importante realizar un alcance basandonos en este tema, y profundizar sobre diferentes modelos para encontrar una arquitectura que nos pueda brindar mejores resultados para nuestro modelo.

## Referencias

Desarrollo del proyecto del modulo 5 de MLDS

Espero que te sea útil esta plantilla. Recuerda que puedes adaptarla a las necesidades específicas de tu proyecto.
