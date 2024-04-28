# Pipeline Bienvenido

## Información

+ En esta carpeta se guardan los script para ejecutar en secuencia todos los scripts para entrenar el modelo o para predecir.


## Descripción

# Proyecto Telecom

## Fuente de Informacion

* **"preprocessing/"**
* **"models/"**


## Paso 01

**Archivo**
```
./preprocessing/a02_nombre_de_las_columnas.py
```

**Descripcion:**
* Se arreglan los nombres de las columnas a la convención snake_case.

## Paso 02

**Archivo**
```
./preprocessing/a03_tipos_de_datos.py
```

**Descripcion:**
* Se arreglan los problemas con los tipos de datos, se convierten a codificación one-hot encoding y por ultimo se determina como manejar las fechas

## Paso 03

**Archivo**
```
./preprocessing/a04_fusion_de_dataframes.py
```

**Descripcion:**
* Fusiona los cuatro dataframes en uno solo

## Paso 04

**Archivo**
```
./preprocessing/a05_creacion_de_caracteristicas_y_objetivo.py
```

**Descripcion:**
* Se determina cuales serán las caracteristicas y el objetivo del modelo

## Paso 05

**Archivo**
```
./preprocessing/a06_creacion_de_conjunto_de_datos.py
```

**Descripcion:**
* Se divide el dataframe fusionado en el conjunto de entrenamiento y prueba

## Paso 06

**Archivo**
```
./preprocessing/a07_sobremuestreo.py
```

**Descripcion:**
* Utiliza la tecnica de upsampling para manejar el desbalanceo de clases

## Paso 07

**Archivo**
```
./models/b03_modelos_con_sobremuestreo.py
```

**Parametros**
param_grid = {
    'n_estimators': [10, 20, 30],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [None, 10, 20, 30],
    'num_leaves': [31, 62, 93],
    'min_child_samples': [20, 30, 40]
}

**Descripcion:**
* Se utiliza una grilla para determinar los mejores hiperparametros  de los modelos LogisticRegression, RandomForest y LigthGBM utilizando los datos sobremuestreados ver: **"preprocessing/a07_sobremuestreo.py"**

## Paso 08

**Archivo**
```
./models/b05_evaluacion_del_modelo.py
```

**Parametros**
Best Hyperparameters: {'learning_rate': 0.2, 'max_depth': 20, 'min_child_samples': 20, 'n_estimators': 30, 'num_leaves': 93}

**Descripcion:**
* Se evalua el modelo de LightGBM con sobremuestreo, con el conjunto de prueba

# Gracias