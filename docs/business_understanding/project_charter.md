# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

**Clasificación de Flores para Entusiastas**

## Objetivo del Proyecto

Desarrollar e implementar un sistema de clasificación de especies de flores utilizando técnicas de aprendizaje profundo, con el fin de proporcionar una herramienta eficiente y accesible para la identificación precisa de plantas silvestres. Este sistema permitirá a usuarios sin experiencia botánica especializada identificar especies de flores simplemente tomando una fotografía, facilitando así el análisis de campo y contribuyendo a la comprensión y conservación de la biodiversidad vegetal. El proyecto también aspira a establecer una base inicial para la clasificación de flores que pueda expandirse en el futuro, incluyendo la detección de nuevas especies y la capacidad de comparación entre especies para fines educativos, profesionales e investigativos.

## Alcance del Proyecto

### Incluye:

- Tenemos un conjunto de datos que consta de imágenes de disponibilidad pública desde Kaggle, el cual cuenta con 102 tipos de flores en total y es desbalanceado ya que cada tipo de flor tiene entre 40 y 258 imágenes como representación. Esto supone un riesgo para el modelo que vamos a aplicar en este proceso.

- Se espera con este proyecto poder crear un modelo de clasificación de imágenes desde cero, sin depender de arquitecturas de deep learning públicas y ampliamente conocidas. El modelo busca predecir con precisión la mayoría de los tipos de flores en nuestro conjunto de datos. Esto se debe a que algunos tipos de flores están subrepresentados, limitando la información disponible y reduciendo la precisión de la clasificación para esos casos específicos.

- Podemos considerar que el modelo planteado para este proyecto es bueno si logramos un accuracy por encima del 50%. Adicionalmente, debe ser capaz de predecir correctamente una buena cantidad de tipos de flores. Esto lo verificaremos mediante el f1-score aplicado para cada una de las categorías.

### Excluye:

- Por las limitantes de tiempo, nos condicionamos al conjunto de datos disponible, por lo tanto, no agregaremos más información para mejorar el balance que tenemos dentro del conjunto de datos. Esto limita poder afinar el modelo para la correcta detección de las categorías con bajo nivel de información en comparación con las que tienen mayor cantidad de imágenes disponibles.

## Metodología

- Transformación de imágenes a tensores que permitan el uso de algoritmos de Aprendizaje Profundo (Deep Learning).

- Mediante técnicas de Deep Learning, se busca implementar un clasificador de flores para las 102 especies disponibles en el conjunto de datos.

- Evaluación y comparación de múltiples algoritmos para determinar el más optimo sobre los datos objetivo.

- Poder aplicar con fotos nuevas la capacidad de predicción de la flor en cuestión.
  
- Implementar el modelo para que pueda ser utilizado por usuarios que no tienen conocimientos de programación.

## Cronograma

Para alcanzar nuestros objetivos, es esencial diseñar un plan de trabajo eficiente que nos permita cumplir con el alcance previamente definido, incorporando las metodologías de deep learning y despliegue de modelos esperadas. Para ello, tenemos en cuenta que ya hemos trabajado anterioremente con estos datos y, por lo tanto, el tiempo empleado para el análisis exploratorio y el modelamiento será reducido. Esto nos permitirá enfocarnos en el despliegue y evaluación del modelo. Siendo así, tendremos en cuenta los siguientes momentos clave: 

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 1 semana | del 2 de mayo al 9 de mayo |
| Preprocesamiento, análisis exploratorio | 3 días | del 10 de mayo al 12 de mayo |
| Modelamiento y extracción de características | 4 días | del 13 de mayo al 16 de mayo |
| Despliegue | 1 semana | del 17 de mayo al 23 de mayo |
| Evaluación y entrega final | 1 semana | del 24 de mayo al 2 de junio |


## Equipo del Proyecto

- Diana Carolina Diaz Ortigoza (dicdiazor@unal.edu.co)
- Julio Cesar Roa Davila (jucroada@unal.edu.co)
- Jair Sebastian Saavedra Alvarado (jssaavedraa@unal.edu.co)
