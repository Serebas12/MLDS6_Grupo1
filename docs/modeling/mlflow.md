# Implementación modelos MlFlow

## Registro MlFlow

Con el fin de poder tener una trazabilidad clara de todos los experimentos realizados en el entrenamiento de modelos, ser realiza uso de MlFlow, en donde se dispondrá el modelo entrenado con las métricas de *accuracy*, *precision*, *recall*, y *f1_score*,  *loss* para cada uno de los casos. Par alo cual se generá el experimento *proyecto_mdls6_v1* y se realiza el registro de los siguientes modelos entrenados:

- model_128N: Modelo convolucional con una capa de salida de 128 neuronas.
- model_256N: Modelo convolucional con una capa de salida de 256 neuronas.
- model_512N: Modelo convolucional con una capa de salida de 512 neuronas.

![Registro](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/Registro.png)

El detalle del código utilizado para el registro de cada uno de los experimentos se puede encontrar el notebook MlFlow

## Selección modelo

Para la selección del modelo ganador, se realizará una comparación de las métricas alojadas en MlFlow para los 3 modelos entrenados, encontrando que en todos los casos el modelo con la capa densa de 512 neuronas tiene un mejor desempeño, obteniendo valor mayor para las métricas de *accuracy*, *precision*, *recall*, y *f1_score* y valor menor para la métrica *loss*. 

![Comparacion](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/Comparacion.png)

## Publicación modelo

Una vez seleccionado el modelo ganador, se procede a la publicación del mismo, con el fin de posteriormente poderlo utilizar, así mismo, generar la versión 1 del modelo *Clasifiacion_flores*, el cual será utilizado para el despliegue y consumo del mismo en la clasificación de nuevas imágenes.

![Modelo](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/Modelo.png)
