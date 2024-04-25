# Libraries ----------------------------------------

import pandas as pd
import os
import sys

sys.path.append(
    os.getcwd()
)  # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

contract_raw = pd.read_csv("datasets/input/contract.csv")
internet_raw = pd.read_csv("datasets/input/internet.csv")
personal_raw = pd.read_csv("datasets/input/personal.csv")
phone_raw = pd.read_csv("datasets/input/phone.csv")

# Data exploration ----------------------------------------

#  --------- contract_raw ---------
# General information
contract_raw.shape
contract_raw.info()
contract_raw.describe()
# Null values
contract_raw.isnull().sum()
(contract_raw.isnull().sum() / len(contract_raw)) * 100
# duplicate values
contract_raw.duplicated().sum()

#  --------- internet_raw ---------
# General information
internet_raw.shape
internet_raw.info()
internet_raw.describe()
# Null values
internet_raw.isnull().sum()
(internet_raw.isnull().sum() / len(internet_raw)) * 100
# duplicate values
internet_raw.duplicated().sum()

#  --------- personal_raw ---------
# General information
personal_raw.shape
personal_raw.info()
personal_raw.describe()
# Null values
personal_raw.isnull().sum()
(personal_raw.isnull().sum() / len(personal_raw)) * 100
# duplicate values
personal_raw.duplicated().sum()

#  --------- phone_raw ---------
# General information
phone_raw.shape
phone_raw.info()
phone_raw.describe()
# Null values
phone_raw.isnull().sum()
(phone_raw.isnull().sum() / len(phone_raw)) * 100
# duplicate values
phone_raw.duplicated().sum()
(phone_raw.duplicated().sum() / len(phone_raw)) * 100
# duplicate values
phone_raw.duplicated().sum()



