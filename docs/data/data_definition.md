# Definición de los datos

## Origen de los datos

El conjunto de datos para el desarrollo del proyecto se obtuvo desde la página Kaggle. Teniendo en cuenta que en esta página se encuentra un repositorio de conjuntos de datos abiertos para todo tipo de análisis, aprovechamos para obtener un conjunto de datos para iniciar este propósito de análisis y que nos ofrezca la información suficiente para el desarrollo de este proyecto. Dejamos como referencia la ruta donde se puede encontrar el conjunto de datos: https://www.kaggle.com/datasets/yousefmohamed20/oxford-102-flower-dataset/data.

## Especificación de los scripts para la carga de datos

Para la carga y preprocesamiento de las imágenes, el código se encuentra en el siguiente [enlace](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/scripts/preprocessing/Preprocesamiento.ipynb), donde incluimos de manera progresiva la lectura de los datos y el preprocesamiento de los mismos, además de una visualización de los datos que contiene nuestro conjunto de datos.

El conjunto de datos se lee desde el origen y se trabaja directamente en memoria desde Colab, aprovechando la ventaja de que es un conjunto de datos ligero que nos permite no tener que realizar un almacenamiento de la preparación del mismo, donde los tiempos de ejecución del preprocesamiento de las imágenes son bajos.

La dirección para la lectura del conjunto de datos es yousefmohamed20/oxford-102-flower-dataset, donde, usando la API de Kaggle para Unix, se puede hacer la descarga directamente del conjunto de datos.

Rutas de origen de datos
La fuente del conjunto de datos es https://www.kaggle.com/datasets/yousefmohamed20/oxford-102-flower-dataset/data.
La ruta de descarga del conjunto de datos por medio de la API de Kaggle en Unix es yousefmohamed20/oxford-102-flower-dataset.
El conjunto de datos viene ordenado en carpetas, donde la carpeta principal está comprimida en formato .zip con el nombre 102 flower, y de aquí se desprenden las demás carpetas de la siguiente manera:

```
**102 flowers/**
├── flowers/
│   ├── test/
|   |   └── (Carpetas indexadas con números del 1 al 102)
│   |── train
|   |   └── (Carpetas indexadas con números del 1 al 102)
│   |── valid
|   |   └── (Carpetas indexadas con números del 1 al 102)
|   └── cat_to_name.json
└── README.md
```

Donde la marca de las carpetas indexadas son 102 carpetas enumeradas del 1 al 102, cada una de estas contiene imágenes de un tipo de flor. Estas imágenes se indexan en el archivo .json que se encuentra en la carpeta **flowers**. El archivo **cat_to_name.json** es un archivo con indexación del número 1 al 102, donde cada número provee el nombre del tipo de flor que se clasifica en las imágenes distribuidas en las carpetas indexadas.

El archivo **README.md** es un archivo plano que contiene una breve descripción del conjunto de datos.

### Base de datos de destino

Como todos los datos se van a manejar en caliente, es decir, después de realizar la recolección de datos desde la fuente, se realiza el preprocesamiento y no se almacena en ningún lado. Con la memoria que nos ofrece Colab, los almacenamos para el proceso de entrenamiento y las diferentes pruebas y validaciones del modelo.
