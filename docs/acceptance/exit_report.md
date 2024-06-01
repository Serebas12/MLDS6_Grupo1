# Informe de salida

## Resumen Ejecutivo

En el presente proyecto se desarrolló e implementó un sistema de clasificación de especies de flores utilizando técnicas de aprendizaje profundo, con el fin de proporcionar una herramienta eficiente y accesible para la identificación precisa de plantas silvestres. 

Para esto, se entrenó una red neuronal convolucional con un total de 14 capas , usando una base de datos de flores con 2,252 imágenes, clasificadas en 18 categorías o etiquetas distintas, para las cuales contábamos con un catálogo de etiquetas en inglés que proporciona los nombres de las flores representadas en cada imagen.

Finalmente, se despliega el modelo en una interfaz de línea de comandos, donde el usuario debe cargar los archivos del modelo final, para luego predecir la categoría de cualquier imagen de una flor.


## Resultados del proyecto

El proyecto se llevó a cabo a través de varias etapas, resultando así mismo en los siguientes entregables

- [Entendimiento del negocio](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/business_understanding/project_charter.md): Se define la pertinencia de un modelo clasificador de flores, teniendo en cuenta los datos con los que contamos. Se define también el alcance del proyecto y su metodología. Vemos en esta etapa final que el objetivo principal del proyecto ha sido alcanzados exitosamente, ya que contamos con un modelo de clasificación que clasifica imágenes de flores en su categoría.
-	Carga de los datos: Los datos se obtuvieron de Kaggle, y presentamos la [definición de los datos](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/data_definition.md), su respectivo [reporte](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/data_summary.md) y [diccionario](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/data/data_dictionary.md).
-	Modelamiento: Previo a desarrollar este proyecto, se hizo un trabajo exploratorio de una red neuronal convolucional inicial la cual se presenta como el [modelo base](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/baseline_models.md), en el cual tomamos la base completa de Kaggle (8,189 imágenes con 102 categorías). Con el objetivo de mejorar los resultados obtenidos en este primer intento, se [entrenan](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/trained%20models.md) otras tres redes convolucionales, con un conjunto de datos reducido, el cual está mejor representado por categorías. Para comparar las métricas entre los diferentes modelos entrenados, cargamos estos y sus métricas sobre el conjunto de prueba a [MLflow](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/mlflow.md). Finalmente, mostramos el modelo con las mejores métricas como el [modelo final](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/model_report.md).
-	Despliegue: Al contar con nuestro modelo escogido, lo ponemos en producción usando una interfaz de línea de comando [(CLI)](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/deployment/deploymentdoc.md).


## Lecciones aprendidas

- Entre los principales desafíos que encontramos están la disponibilidad de imágenes en cada categoría de flor con la contábamos. En nuestro modelo base, a pesar de obtener buen accuracy en el modelo en general, por categrías era difícil que el modelo identificara las categorías con muy poca representación. Es por esto que procedemos a trabajar únicamente con las categorías con representación adecuada. En segunda medida, los tiempos de entrenamiento de este tipo de redes neuronales son dispendiosos, además de las restricciones en los tiempos de uso de GPU de Google Colab. Este inconveniente lo sorteamos usando varias cuentas de Google y esperando los tiempos de entrenamiento debidos.
- En un futuro, se podría enriquecer la base con imágenes en las categorías poco representadas, para poder fortalecer el modelo y que sea capaz de identificar más especies de flores. Este es un trabajo que debe hacerse cuidadosamente, para lograr cumplir con la calidad de imagen que se espera para que la red neuronal logre captar las características de las flores. Adicionalmente, se podría incrementar la capacidad de procesamiento adquiriendo una cuenta premium de Google Colab, o procediendo a entrenar en una máquina local más potente que la que nos ofrece la cuenta gratuita de Google.

## Impacto del proyecto

- El uso de redes neuronales convolucionales en problemas de clasificación tiene un impacto muy importante en cuanto a la automatización de procesos. En nuestro caso particular, la identificación de tipos de flor puede ser de utilidad para aficionados a la botánica que, sin un conocimiento experto, quieren clasificar flores usando una foto de la misma facilitando así el análisis de campo y contribuyendo a la comprensión y conservación de la biodiversidad vegetal. El proyecto también establece una base inicial para la clasificación de flores que pueda expandirse en el futuro, incluyendo la detección de nuevas especies y la capacidad de comparación entre especies para fines educativos, profesionales e investigativos.
- Para continuar contribuyendo a esta área de investigación, expertos en el tema podrían sumarse a este proyecto, incluyendo imágenes de diferentes tipos de flores y apoyándonos en la interpretación más específica de las características captadas por la red neuronal, logrando así enriquecer este modelo de automatización con estos conocimientos.

## Conclusiones

- En conclusión, las redes neuronales convolucionales son una herramiento muy poderosa en la automatización de procesos de clasificación que puede permitir a una persona, que puede ser o no experta en botánica, identificar el tipo de flor usando una foto de la misma. Este es, sin embargo, un primer paso para lograr un modelo que clasifique de manera precisa, debido a la falta de representación de muchas de las categorías de flores con las que contábamos inicialmente. Es así que queda un campo de investigación abierto donde se puedan incluir más imágenes al entrenamiento, además de conocimiento de expertos en el tema.

