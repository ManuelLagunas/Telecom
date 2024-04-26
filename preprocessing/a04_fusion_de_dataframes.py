# Libraries ----------------------------------------

import pandas as pd
import os
import sys

sys.path.append(os.getcwd())  
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

contract_df = pd.read_csv("files/datasets/intermediate/a03_contract_dtype.csv")
internet_df = pd.read_csv("files/datasets/intermediate/a03_internet_dtype.csv")
personal_df = pd.read_csv("files/datasets/intermediate/a03_personal_dtype.csv")
phone_df = pd.read_csv("files/datasets/intermediate/a03_phone_dtype.csv")

# Dataframes fusion ----------------------------------------

merged_df = pd.merge(contract_df, internet_df, on='customer_id', how='outer')
merged_df = pd.merge(merged_df, personal_df, on='customer_id', how='outer')
merged_df = pd.merge(merged_df, phone_df, on='customer_id', how='outer')

# Check data ----------------------------------------

# print(merged_df.info())
# print(merged_df.isnull().sum())
# print(merged_df.isnull().sum() / len(merged_df) * 100)

# Fill missing values ----------------------------------------

merged_df['total_charges'].dropna(inplace=True)
merged_df.fillna(False, inplace=True)

# Check data ----------------------------------------

# print(merged_df.info())
# print(merged_df.isnull().sum())
# print(merged_df.isnull().sum() / len(merged_df) * 100)

# Correct columns dtype ----------------------------------------

# merged_df['begin_date'] = pd.to_datetime(merged_df['begin_date'])
merged_df['end_date'] = pd.to_numeric(merged_df['end_date'], errors='coerce')
merged_df['total_charges'] = pd.to_numeric(merged_df['total_charges'], errors='coerce')

# Check data ----------------------------------------

# print(merged_df.info())

# Save data ----------------------------------------

merged_df.to_csv("files/datasets/intermediate/a04_merged_df.csv", index=False)