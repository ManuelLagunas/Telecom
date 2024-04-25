# Libraries ----------------------------------------

import pandas as pd
import os
import sys

sys.path.append(os.getcwd())  
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

contract_df = pd.read_csv("files/datasets/intermediate/a02_contract_columns_name.csv")
internet_df = pd.read_csv("files/datasets/intermediate/a02_internet_columns_name.csv")
personal_df = pd.read_csv("files/datasets/intermediate/a02_personal_columns_name.csv")
phone_df = pd.read_csv("files/datasets/intermediate/a02_phone_columns_name.csv")

# Correct columns dtype ----------------------------------------

#-------- contract_df --------
contract_df['begin_date'] = pd.to_datetime(contract_df['begin_date'])
#contract_df['end_date'] = pd.to_datetime(contract_df['end_date'])
contract_df = pd.get_dummies(contract_df, columns=['type'], prefix='type', drop_first=True)
contract_df = pd.get_dummies(contract_df, columns=['paperless_billing'], prefix='paperless_billing', drop_first=True)
contract_df = pd.get_dummies(contract_df, columns=['payment_method'], prefix='payment_method', drop_first=True)
contract_df['total_charges'] = pd.to_numeric(contract_df['total_charges'], errors='coerce')
# contract_df.info()

#-------- internet_df --------
cols_to_encode = [col for col in internet_df.columns if col not in ['customer_id']]
internet_df = pd.get_dummies(internet_df, columns=cols_to_encode, drop_first=True)
# internet_df.info()

#-------- personal_df --------
cols_to_encode = [col for col in personal_df.columns if col not in ['customer_id', 'senior_citizen']]
personal_df = pd.get_dummies(personal_df, columns=cols_to_encode, drop_first=True)
personal_df['senior_citizen'] = personal_df['senior_citizen'].astype('bool')
# personal_df.info()

#-------- phone_df --------
phone_df = pd.get_dummies(phone_df, columns=['multiple_lines'], prefix='multiple_lines', drop_first=True)
phone_df.info()

# Save data ----------------------------------------

contract_df.to_csv("files/datasets/intermediate/a03_contract_dtype.csv", index=False)
internet_df.to_csv("files/datasets/intermediate/a03_internet_dtype.csv", index=False)
personal_df.to_csv("files/datasets/intermediate/a03_personal_dtype.csv", index=False)
phone_df.to_csv("files/datasets/intermediate/a03_phone_dtype.csv", index=False)