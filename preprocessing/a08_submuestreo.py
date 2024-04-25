# Libraries ----------------------------------------

import pandas as pd
import os
import sys
from sklearn.utils import resample, shuffle

sys.path.append(os.getcwd())  
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

features_train=pd.read_csv("files/datasets/intermediate/a06_features_train.csv")
target_train=pd.read_csv("files/datasets/intermediate/a06_target_train.csv")

# Downsampler creation ----------------------------------------

def downsample(features, target):
    # Convert target to a pandas Series if it's a one-column DataFrame
    if isinstance(target, pd.DataFrame):
        target = target.squeeze()

    # Combine features and target
    df = pd.concat([features, target], axis=1)

    # Class separation
    df_majority = df[target==0]
    df_minority = df[target==1]

    # Calculate the fraction of majority samples to keep
    fraction = len(df_minority) / len(df_majority)

    # Downsample the majority class
    df_majority_downsampled = df_majority.sample(frac=fraction, random_state=123)

    # Combine the minority class with the downsampled majority class
    df_downsampled = pd.concat([df_majority_downsampled, df_minority])

    # Shuffle the data
    df_downsampled = df_downsampled.sample(frac=1, random_state=123)

    # Separate features and target
    features_downsampled = df_downsampled.drop(target.name, axis=1)
    target_downsampled = df_downsampled[target.name]

    return features_downsampled, target_downsampled

# Downsampling ----------------------------------------

features_train_downsampled, target_train_downsampled = downsample(features_train, target_train)

# Save data ----------------------------------------

target_train_downsampled.to_csv("files/datasets/intermediate/a08_target_train_downsampled.csv", index=False)
features_train_downsampled.to_csv("files/datasets/intermediate/a08_features_train_downsampled.csv", index=False)