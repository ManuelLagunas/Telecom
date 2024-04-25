# Libraries ----------------------------------------

import re
import pandas as pd
import os
import sys

sys.path.append(os.getcwd())  
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

contract_raw = pd.read_csv("datasets/input/contract.csv")
internet_raw = pd.read_csv("datasets/input/internet.csv")
personal_raw = pd.read_csv("datasets/input/personal.csv")
phone_raw = pd.read_csv("datasets/input/phone.csv")

# Correct name columns ----------------------------------------

def snake_case_columns(df):
    df.columns = df.columns.map(lambda x: re.sub(r'(?<=[a-z])(?=[A-Z])', '_', x).lower())
    return df

contract_df = snake_case_columns(contract_raw)
internet_df = snake_case_columns(internet_raw)
personal_df = snake_case_columns(personal_raw)
phone_df = snake_case_columns(phone_raw)

# Save data ----------------------------------------

contract_df.to_csv("files/datasets/intermediate/a02_contract_columns_name.csv", index=False)
internet_df.to_csv("files/datasets/intermediate/a02_internet_columns_name.csv", index=False)
personal_df.to_csv("files/datasets/intermediate/a02_personal_columns_name.csv", index=False)
phone_df.to_csv("files/datasets/intermediate/a02_phone_columns_name.csv", index=False)