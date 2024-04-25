# Libraries ----------------------------------------

import pandas as pd
import os
import sys
from sklearn.model_selection import train_test_split

sys.path.append(os.getcwd())  
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

target=pd.read_csv("files/datasets/intermediate/a05_target.csv")
features=pd.read_csv("files/datasets/intermediate/a05_features.csv")

# Split data ----------------------------------------

features_train, features_test, target_train, target_test = train_test_split(features, target, test_size=0.25, random_state=42)

# Save data ----------------------------------------

target_train.to_csv("files/datasets/intermediate/a06_target_train.csv", index=False)
target_test.to_csv("files/datasets/intermediate/a06_target_test.csv", index=False)
features_train.to_csv("files/datasets/intermediate/a06_features_train.csv", index=False)
features_test.to_csv("files/datasets/intermediate/a06_features_test.csv", index=False)