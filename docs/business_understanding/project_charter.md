# Project Charter - Entendimiento del Negocio

## Nombre del Proyecto

**Clasificación de Flores para Entusiastas**

## Objetivo del Proyecto

Desarrollar e implementar un sistema de clasificación de especies de flores utilizando técnicas de aprendizaje profundo, con el fin de proporcionar una herramienta eficiente y accesible para la identificación precisa de plantas silvestres. Este sistema permitirá a usuarios sin experiencia botánica especializada identificar especies de flores simplemente tomando una fotografía, facilitando así el análisis de campo y contribuyendo a la comprensión y conservación de la biodiversidad vegetal. El proyecto también aspira a establecer una base inicial para la clasificación de flores que pueda expandirse en el futuro, incluyendo la detección de nuevas especies y la capacidad de comparación entre especies para fines educativos, profesionales e investigativos.

## Alcance del Proyecto

### Incluye:

- Tenemos un conjunto de datos que consta de un conjunto de imágenes de disponibilidad pública desde Kaggle, este conjunto de datos constal de 102 tipos de flores en total, este conjunto de datos es desbalanceado, donde cada tipo de flor tiene entre 40 y 258 imágenes como representación, lo que supone un riesgo para el modelo que vamos a aplicar para este proceso.

- Se espera con este proyecto realizar un modelo de clasificación de imágenes planteado desde cero, que no depende de arquitecturas de modelos de deep learning públicos y reconocidos, y pueda generar una predicción acertada de la mayoría de los tipos de flores con el que dependemos dentro del conjunto de datos, donde nos encontramos limitados por la cantidad de información disponible.

- Podemos considerar que el modelo planteado para este proyecto es bueno, si logramos un accuracy por encima del 50%, adicional, que haga una correcta predicción de una buena cantidad de tipos de flores, donde lo podremos verificar con el f1-score aplicado para cada una de las categorías.

### Excluye:

- Por las limitantes de tiempo, nos condicionamos al conjunto de datos disponible, por lo tanto, no agregaremos más información para mejorar el balamce que tenemos dentro del clonjunto de datos, adicional, esto limita poder afinar el modelo para la correcta detección de las categorías con bajo nivel de información con respecto a las demás categorías donde se tiene mayor cantidad de información (mayor cantidad de imágenes disponible).

## Metodología

[Descripción breve de la metodología que se utilizará para llevar a cabo el proyecto]

## Cronograma

| Etapa | Duración Estimada | Fechas |
|------|---------|-------|
| Entendimiento del negocio y carga de datos | 2 semanas | del 1 de mayo al 15 de mayo |
| Preprocesamiento, análisis exploratorio | 4 semanas | del 16 de mayo al 15 de junio |
| Modelamiento y extracción de características | 4 semanas | del 16 de junio al 15 de julio |
| Despliegue | 2 semanas | del 16 de julio al 31 de julio |
| Evaluación y entrega final | 3 semanas | del 1 de agosto al 21 de agosto |

Hay que tener en cuenta que estas fechas son de ejemplo, estas deben ajustarse de acuerdo al proyecto.

## Equipo del Proyecto

- [Nombre y cargo del líder del proyecto]
- [Nombre y cargo de los miembros del equipo]
