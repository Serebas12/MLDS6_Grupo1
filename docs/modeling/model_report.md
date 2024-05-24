# Reporte del Modelo Final

## Descripción del Problema

Desarrollar e implementar un sistema de clasificación de especies de flores utilizando técnicas de aprendizaje profundo, con el fin de proporcionar una herramienta eficiente y accesible para la identificación precisa de plantas silvestres. Este sistema permitirá a usuarios sin experiencia botánica especializada identificar especies de flores simplemente tomando una fotografía, facilitando así el análisis de campo y contribuyendo a la comprensión y conservación de la biodiversidad vegetal. El proyecto también aspira a establecer una base inicial para la clasificación de flores que pueda expandirse en el futuro, incluyendo la detección de nuevas especies y la capacidad de comparación entre especies para fines educativos, profesionales e investigativos.

## Descripción del Modelo

El modelo escogido cuenta con un total de 14 capas, donde tenemos 4 capas convolucionales, 4 capas de pooling correspondiente a cada capa convolucional, una capa (flatten) que vectoriza los datos trabajados por la sección de extracción de características (capas convolucionales y de pooling), dos capas densas con 512 neuronas y activación relu, que organizan y trabajan los datos del vector obtenido con la capa flatten. Finalmente, una capa de dropout y una capa final con 512 neuronas y activación softmax que clasifica las 18 categorías o tipos de flores que tenemos para el desarrollo del proyecto.

![Arquitectura 512](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/Arquitectura%20512.png)

## Evaluación del Modelo

Al revisar los modelos implementados, notamos que este modelo es el que presenta, para todas las métricas estudiadas, los mejores resultados. 

| Métrica  | Modelo con 512 Neuronas | Modelo con 216 Neuronas | Modelo con 128 Neuronas |
| ------------- | ------------- | ------------- | ------------- |
| Accuracy  | 0.49 | 0.46 | 0.42|
| F1-score  | 0.43  | 0.34 | 0.32 |
| Loss  | 8.06 | 8.67 | 9.26 |
| Precision  | 0.56 | 0.31 | 0.40 |
| Recall | 0.47  | 0.42 | 0.37 |

## Conclusiones y Recomendaciones

Como se puede ver, al hacer la evaluación de las métricas accuracy, precision, recall, y f1_score y loss, concluímos que el mejor modelo es el que tiene 512 neuronas en las capas finales de su arquitectura, además de contar con únicamente 4 bloques de capas de convolución y pooling. Con esto se ve que agregar más de 4 bloques de extracción de características, no ayuda a mejorar el modelo, mientras que el uso de más neurones en las capas finales sí mejora la clasificación de las imágenes.
