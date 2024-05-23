# Implementación modelos MlFlow

## Registro MlFlow

![Registro](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/Registro.png)

## Selección modelo

Para la selección del modelo ganador, se realizará una comparación de las métricas alojadas en MlFlow para los 3 modelos entrenados, encontrando que en todos los casos el modelo con la capa densa de 512 neuronas tiene un mejor desempeño, obteniendo valor mayor para las métricas de *accuracy*, *precision*, *recall*, y *f1_score* y valor menor para la métrica *loss*. 

![Comparacion](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/Comparacion.png)

## Publicación modelo

Una vez seleccionado el modelo ganador, se procede a la publicación del mismo, con el fin de posteriormente poderlo utilizar, así mismo, generar la versión 1 del modelo *Clasifiacion_flores*, el cual será utilizado para el despliegue y consumo del mismo en la clasificación de nuevas imágenes.

![Modelo](https://github.com/Serebas12/MLDS6_Grupo1/blob/master/docs/modeling/Modelo.png)
