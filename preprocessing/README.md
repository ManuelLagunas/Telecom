# Procesamiento de datos

## Información

### - a01_analisis.py

Este archivo, lee los dataframes originales y utiliza funciones de pandas para examinar y comprender los datos. Obteniendo las siguientes conclusiones:

- Las columnas no tienen la convencion snake_case
- Las columnas deben ser convertidas al tipo de datos adecuado
- Cambiar las columnas categoricas a one-hot encoding
- Determinar como se manejaran las columnas que tienen datos tipo fecha
- Fusionar los dataframes 
- Determinar los features y el target para el entrenamiento
- Dividir en conjunto de entrenamiento y prueba
- Manejar el desbalanceo de datos. Ver test/README.md
**No es parte del pipeline**

### - a02_nombres_de_las_columnas.py

Se arreglan los nombres de las columnas a la convención snake_case.
**Es parte del pipe line**

### - a03_tipos_de_datos.py

Se arreglan los problemas con los tipos de datos, se convierten a codificación one-hot encoding y por ultimo se determina como manejar las fechas
**Es parte del pipeline**

### - a04_fusion_de_dataframes.py

Fusiona los cuatro dataframes en uno solo
**Es parte del pipeline**

### - a05_creacion_de_caracteristicas_y_objetivos.py

Se determina cuales serán las caracteristicas y el objetivo del modelo
**Es parte del pipeline**

### - a06_creacion_del_conjunto_de_datos.py

Se divide el dataframe fusionado en el conjunto de entrenamiento y prueba
**Es parte del pipeline**

### - a07_sobremuestreo.py

Utiliza la tecnica de upsampling para manejar el desbalanceo de clases
**Es parte del pipeline**

### - a08_submuestreo.py

Utiliza la tecnica de downsampling para manejar el desbalanceo de clases
**No es parte del pipeline**

# Gracias