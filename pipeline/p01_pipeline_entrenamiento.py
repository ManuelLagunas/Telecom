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

print(f"---------------------------------- \nAreglando el nombre de las columnas \n----------------------------------")
os.system(f"python{extension_binarios} preprocessing/a02_nombres_de_las_columnas.py") # Se ejecuta el script que renombra las columnas

print(f"---------------------------------- \nCodificando a one-hot \n----------------------------------")
os.system(f"python{extension_binarios} preprocessing/a03_tipos_de_datos.py") # Se ejecuta el script que cambia los tipos de datos

print(f"---------------------------------- \nFusionando dataframes \n----------------------------------")
os.system(f"python{extension_binarios} preprocessing/a04_fusion_de_dataframes.py") # Se ejecuta el script que fusiona los dataframes

print(f"---------------------------------- \nCreando características y objetivo \n----------------------------------")
os.system(f"python{extension_binarios} preprocessing/a05_creacion_de_caracteristicas_y_objetivo.py") # Se ejecuta el script que crea las características y el objetivo

print(f"---------------------------------- \nCreando conjunto de datos \n----------------------------------")
os.system(f"python{extension_binarios} preprocessing/a06_creacion_de_conjunto_de_datos.py") # Se ejecuta el script que separa los datos en entrenamiento y testeo

print(f"---------------------------------- \nSobremuestreando datos \n----------------------------------")
os.system(f"python{extension_binarios} preprocessing/a07_sobremuestreo.py") # Se ejecuta el script que sobremuestrea los datos

# Modelo ---------------------------------------- 

print(f"---------------------------------- \nCreando modelos \n----------------------------------")
os.system(f"python{extension_binarios} models/b03_modelos_con_sobremuestreo.py")

print(f"---------------------------------- \nMostrando resultados \n----------------------------------")
os.system(f"python{extension_binarios} models/b05_evaluacion_del_modelo.py")