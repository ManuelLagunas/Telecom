# Libraries ----------------------------------------

import os, sys
import argparse
sys.path.append(os.getcwd()) # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código
import params as params
    
# Defining executable file extensions ---------------------------------------- 

if params.sistema_operativo == 'Windows':
        extension_binarios = ".exe"
else:
        extension_binarios = ""

# Info ---------------------------------------- 

print(f"---------------------------------- \nComenzando proceso \n----------------------------------")

# Preproceso ---------------------------------------- 

os.system(f"python{extension_binarios} preprocessing/a02_nombres_de_las_columnas.py") # Se ejecuta el script que renombra las columnas

os.system(f"python{extension_binarios} preprocessing/a03_tipos_de_datos.py") # Se ejecuta el script que cambia los tipos de datos

os.system(f"python{extension_binarios} preprocessing/a04_fusion_de_dataframes.py") # Se ejecuta el script que fusiona los dataframes

os.system(f"python{extension_binarios} preprocessing/a05_creacion_de_caracteristicas_y_objetivo.py") # Se ejecuta el script que crea las características y el objetivo

os.system(f"python{extension_binarios} preprocessing/a06_creacion_de_conjunto_de_datos.py") # Se ejecuta el script que separa los datos en entrenamiento y testeo

os.system(f"python{extension_binarios} preprocessing/a07_sobremuestreo.py") # Se ejecuta el script que sobremuestrea los datos

# Modelo ---------------------------------------- 

# os.system(f"python{extension_binarios} models/b01_creacion_de_modelos.py")
