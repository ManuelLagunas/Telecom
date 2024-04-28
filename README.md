# Bienvenido

## Instrucciones

Correr el archivo: "pipeline/p01_pipeline_entrenamiento.py"

## Introducción

El presente trabajo, surge de la necesidad de la compañia Telecom de detectar a los clientes que podrian abandonar su plan tarifario causando perdidas a la compañia. Por lo que se ha encargado realizar un modelo de machine learning para poder resolver este problema, al detectar los clientes con mas probabilidades de irse, se podran generar acciones de mercadotecnia enfocadas a retenerlos.

## Plan de trabajo

- 1. Hacer análisis exploratorio de datos
- 2. Solucionar los problemas encontrados en el análisis exploratorio
- 3. Decidir cuales seran las caracteristicas y cual será el objetivo
- 4. Verificar posible desbalanceo de los datos
- 5. Crear un conjunto de entrenamiento y otro de prueba
- 6. Entrenar multiples modelos para seleccionar el mejor, utilizando multiples tecnicas que permitan solucionar el problema del desbalanceo (Si es que existiera)
- 7. Entrenar el modelo final
- 7. Probarlo con el conjunto de datos de prueba
- 8. Presentar los resultados y conclusiones

## Proceso de trabajo

- 1 Se realizó el analis exploratorio de los datos ver: **"preprocessing/a01_analisis.py"**
- 2 Se solucionaron los problemas encontrados ver: **"preprocessing/a02_nombres_de_las_columnas.py"**, **"preprocessing/a03_tipos_de_datos.py"**, **"preprocessing/a04_fusion_de_dataframes.py"**
- 3 Se fusionaron los dataframes en unos solo para poder entrenarlos ver: **"preprocessing/a04_fusion_de_dataframes.py"**
- 4 Se seleccionaron las caracteristicas y se determino el objetivo ver: **"preprocessing/a05_creacion_de_caracteristicas_y_objetivo.py"**
- 5 Se estudio un posible desbalanceo de los datos y se encontró que existia. Los usuarios inactivos representan el 26.53% de los datos del target. presentando un desbalanceo de casi 3 veces mas datos de usuarios activos (2.76) ver: **"test/t01_desvalanceo_de_clases.py"**
- 6 Se definieron los conjunto de entrenamiento y prueba ver: **"preprocessing/a06_creacion_de_conjunto_de_datos.py**
- 7 Se creo un conjunto de entrenamiento con la tecnica de sobremuestreo con el fin de estudiar si esto servia a crear un mejor modelo ver: **"preprocessing/a07_sobremuestreo.py"**
- 8 Se creo un conjunto de entrenamiento con la tecnica de submuestreo con el fin de estudiar si esto serviria a crear un mejor modelo ver: **"preprocessing/a08_submuestreo.py**
- 9 Se decidio buscar los mejores parametros para tres modelos de machine learning. LogisticRegression, RandomForest y LightGBM como modelos de prueba, Es decir Sin utilizar ninguna tecnica que buscara solucionar el desbalanceo de datos ver: **"models/b01_modelos_de_control.py"**
- 10 Los modelos enlistados en el punto anterior se trabajaron pasando el parametro class:Balanced ver: **"models/b02_modelos_con_balanceo.py"**
- 11 Se utilizó el conjunto con sobremuestreo para utilizar la tecnica de upsampled en los modelos mencionados en el punto 9 ver: **"models/b03_modelos_con_sobremuestreo.py"**
- 12 Se utilizó el conjunto con submuestreo para utilizar la tecnica de downsampling en los modelos mencionados en el punto 9 ver **"models/b04_modelos_con_submuestreo.py"**
- 13 Se evaluó el mejor modelo de los 12 siendo el modelo de lightGBM con la tecnica de upsampling Dando un resultado en la metrica AUC-ROC de 0.937050994782712. Segun la evaluación con el conjunto de prueba dio: 0.8439392064200313 ver: **"models/b05_evaluación_del_modelo.py"**
- 14 Por ultimo se armo el pipeline para poder reproduciir los pasos que nos llevan al resultado obtenido en el punto 13 ver: **"pipeline/p01_pipeline_entrenamiento.py"**

## Archivos de interes

"preprocessing/README.md"
"test/README.md"
"models/README.md"
"datasets/input/README.md"
"files/datasets/intermediate/README.md"
"files/modeling_output/figures/AUC-ROC_curve.png"
"files/modeling_output/model_fit/README.md"
"sandbox/README.md"
"pipeline/README.md"

## Conclusión


