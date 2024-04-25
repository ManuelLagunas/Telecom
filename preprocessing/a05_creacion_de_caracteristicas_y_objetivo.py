# Libraries ----------------------------------------

import pandas as pd
import os
import sys

sys.path.append(os.getcwd())  
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

df=pd.read_csv("files/datasets/intermediate/a04_merged_df.csv")

# features creation ----------------------------------------

# df.columns
features = df.drop(columns=['customer_id', 'end_date'], axis=1)

# target creation ----------------------------------------

target = df['end_date']

# Save data ----------------------------------------

target.to_csv("files/datasets/intermediate/a05_target.csv", index=False)
features.to_csv("files/datasets/intermediate/a05_features.csv", index=False)