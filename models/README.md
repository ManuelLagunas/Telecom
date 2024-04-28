# Models

## Información

### b01_modelos_de_control.py
Se utiliza una grilla para determinar los mejores hiperparametros  de los modelos LogisticRegression, RandomForest y LigthGBM sin ninguna tecnica que tome en cuenta los desbalanceos de clase

### b02_modelos_con_balanceo.py
Se utiliza una grilla para determinar los mejores hiperparametros  de los modelos LogisticRegression, RandomForest y LigthGBM con el hiperparametro Class:Balanced

### b03_modelos_con_sobremuestreo.py
Se utiliza una grilla para determinar los mejores hiperparametros  de los modelos LogisticRegression, RandomForest y LigthGBM utilizando los datos sobremuestreados ver: **"preprocessing/a07_sobremuestreo.py"**
**Es parte del pipeline**

### b04_modelos_con_submuestreo.py
Se utiliza una grilla para determinar los mejores hiperparametros  de los modelos LogisticRegression, RandomForest y LigthGBM utilizando los datos submuestreados ver: **"preprocessing/a08_submuestreo.py"**

### b05_evaluacion_del_modelo.py
Se evalua el modelo de LightGBM con sobremuestreo, con el conjunto de prueba
**Es parte del pipeline**

# Gracias