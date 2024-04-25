# Libraries ----------------------------------------

import pandas as pd
import os
import sys
from sklearn.utils import shuffle

sys.path.append(os.getcwd())  
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

features_train=pd.read_csv("files/datasets/intermediate/a06_features_train.csv")
target_train=pd.read_csv("files/datasets/intermediate/a06_target_train.csv")

# Downsampler creation ----------------------------------------

def downsample(features, target, fraction):
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]

    features_downsampled = pd.concat(
        [features_zeros.sample(frac=fraction, random_state=12345)]
        + [features_ones]
    )
    target_downsampled = pd.concat(
        [target_zeros.sample(frac=fraction, random_state=12345)]
        + [target_ones]
    )

    features_downsampled, target_downsampled = shuffle(
        features_downsampled, target_downsampled, random_state=12345
    )

    return features_downsampled, target_downsampled

# Downsampling ----------------------------------------

features_train_downsampled, target_train_downsampled = downsample(features_train, target_train, 0.3)

# Save data ----------------------------------------

target_train_downsampled.to_csv("files/datasets/intermediate/a08_target_train_downsampled.csv", index=False)
features_train_downsampled.to_csv("files/datasets/intermediate/a08_features_train_downsampled.csv", index=False)