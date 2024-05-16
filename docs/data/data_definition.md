# Definición de los datos

## Origen de los datos

El conjunto de datos para el desarrollo del proyecto se obtuvo desde la página Kaggle, teniendo en cuenta que en está página se encuentra un repositorio de conjuntos de datos abiertos para todo tipo de análisis, aprovechamos para obtener un conjunto de datos para iniciar este propósito de análisis, y nos ofrezca la información suficiente para el desarrollo de este proyecto. Dejamos como apartado, la ruta donde se puede encontrar la referencia del conjunto de datos se encuentra en https://www.kaggle.com/datasets/yousefmohamed20/oxford-102-flower-dataset/data.

## Especificación de los scripts para la carga de datos

- [ ] Especificar los scripts utilizados para la carga de los datos. 

## Referencias a rutas o bases de datos origen y destino

El conjunto de datos se lee desde el origen y se trabaja directamente en memoría desde colab, aprovechando la ventaja que es un conjunto de datos lígero que nos permite no tener que realizar un almacenamiento de la preparación del mismo, donde los tiempos de ejecución del preprocesamiento de las imágenes son bajos son bajos.

La dirección para la lectura del conjunto de datos es yousefmohamed20/oxford-102-flower-dataset, donde usando la api de kaggle para unix se puede hacer la descarga directamente del conjunto de datos.

### Rutas de origen de datos

-  La fuente del conjunto de datos es https://www.kaggle.com/datasets/yousefmohamed20/oxford-102-flower-dataset/data
-  La ruta de descarga del conjunto de datos por medio de la api de Kaggle en Unix es yousefmohamed20/oxford-102-flower-dataset
-  El conjunto de datos viene ordenado en carpetas, donde la carpeta principal viene comprimido en formato .zip con el nombre **102 flower**, y de aquí se desprende las demás carpetas d ela siguiente manera:

**102 flower**

+  flowers

++     test

+++       ...

++     train

+++       ...

++     valid

+++       ...

++     cat_to_name.json

+   README.md

Donde los puntos suspensivos (...) señala conjuntos de carpetas las cuales se encuentran enumeradas del 1 al 102 y cada una almacena las imagenes de un tipo de flor. Esta selección viene dada por el catálogo almacenado en el archivo **cat_to_name.json** donde viene el nombre de la flor, identado por un número del 1 a 102, haciendo la relación con el nombre las carpetas que almacenan las respectivas imágenes.

El archivo **README.md** es un archivo plano, el cual trae una breve descripción del conjunto de datos.


### Base de datos de destino

- [ ] Especificar la base de datos de destino para los datos.
- [ ] Especificar la estructura de la base de datos de destino.
- [ ] Describir los procedimientos de carga y transformación de los datos en la base de datos de destino.
