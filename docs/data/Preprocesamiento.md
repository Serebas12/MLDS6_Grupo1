# Preprocesamiento de los datos

Como vimos en [data_summary](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/data_summary.md), tenemos categorías con imágenes de validación y testeo por debajo de las 10 unidades, por lo tanto se puede llegar a generar un sesgo en el proceso de calificación de validación y testeo, por lo tanto, cogeremos aquellas categorías que cuente con más de 10 imágenes en sus respectivas muestras de validación y testeo.

Obteniendo así las siguientes categorías, con el respectivo número de imágenes en el conjunto de entrenamiento:
![Total Train por categoría](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/Total%20TRAIN%20por%20categor%C3%ADa.png)

Así mismo, para el conjunto de validación:

![Total Valid por categoría](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/Total%20VALID%20por%20categor%C3%ADa.png)

Finalmente, para el conjunto de prueba tenemos:

![Total Test por categoría](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/Total%20TEST%20por%20categor%C3%ADa.png)

Una vez decididas las categorías con las que vamos a trabajar, se decide aplicar la técnica de aumentación de datos (data augmentation), la cual considera diversas transformaciones de las imágenes actuales y nos permite enriquecer las características que el modelo captura de nuestra base de datos. A continuación, algunos ejemplos del resultado de esta metodología.

![Data augmentation](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/Data%20Augmentation%20Examples.png)
