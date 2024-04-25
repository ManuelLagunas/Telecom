# Libraries ----------------------------------------

import os
import sys
import pandas as pd
from sklearn.utils import resample, shuffle

sys.path.append(os.getcwd())  
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

features_train=pd.read_csv("files/datasets/intermediate/a06_features_train.csv")
target_train=pd.read_csv("files/datasets/intermediate/a06_target_train.csv")

# Upsampler creation ---------------------------------------- 

def upsample(features, target):
    # Convert target to a pandas Series if it's a one-column DataFrame
    if isinstance(target, pd.DataFrame):
        target = target.squeeze()

    # Combine features and target
    df = pd.concat([features, target], axis=1)

    # Class separation
    df_majority = df[target==0]
    df_minority = df[target==1]

    # Upsampling the minority class
    df_minority_upsampled = resample(df_minority, 
                                     replace=True,     
                                     n_samples=len(df_majority),    
                                     random_state=123) 

    # Combine the majority class with the minority upsampled class
    df_upsampled = pd.concat([df_majority, df_minority_upsampled])

    # Shuffle the data
    df_upsampled = df_upsampled.sample(frac=1, random_state=123)

    # Separate features and target
    features_upsampled = df_upsampled.drop(target.name, axis=1)
    target_upsampled = df_upsampled[target.name]

    return features_upsampled, target_upsampled

# Upsampling ----------------------------------------

features_train_upsampled, target_train_upsampled = upsample(features_train, target_train)

# Save data ---------------------------------------- 

target_train_upsampled.to_csv("files/datasets/intermediate/a07_target_train_upsampled.csv", index=False)
features_train_upsampled.to_csv("files/datasets/intermediate/a07_features_train_upsampled.csv", index=False)
