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

Para la evaluación del modelo obtenemos un accuracy con el conjunto de testeo del 62% y el f1-score evaluado para cada categoría de manera inestable, como se puede observar a continuación:



Descripción de las métricas utilizadas para evaluar el rendimiento del modelo.

### Resultados de evaluación

Tabla que muestra los resultados de evaluación del modelo baseline, incluyendo las métricas de evaluación.

## Análisis de los resultados

Descripción de los resultados del modelo baseline, incluyendo fortalezas y debilidades del modelo.

## Conclusiones

Conclusiones generales sobre el rendimiento del modelo baseline y posibles áreas de mejora.

## Referencias

Lista de referencias utilizadas para construir el modelo baseline y evaluar su rendimiento.

Espero que te sea útil esta plantilla. Recuerda que puedes adaptarla a las necesidades específicas de tu proyecto.
