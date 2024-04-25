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

# Upsampler creation ---------------------------------------- 

def upsample(features, target, repeat):
    features_zeros = features[target == 0]
    features_ones = features[target == 1]
    target_zeros = target[target == 0]
    target_ones = target[target == 1]

    features_upsampled = pd.concat([features_zeros] + [features_ones] * repeat)
    target_upsampled = pd.concat([target_zeros] + [target_ones] * repeat)

    features_upsampled, target_upsampled = shuffle(
        features_upsampled, target_upsampled, random_state=12345
    )

    return features_upsampled, target_upsampled

# Upsampling ----------------------------------------

features_train_upsampled, target_train_upsampled = upsample(features_train, target_train, 3)

# Save data ---------------------------------------- 

target_train_upsampled.to_csv("files/datasets/intermediate/a07_target_train_upsampled.csv", index=False)
features_train_upsampled.to_csv("files/datasets/intermediate/a07_features_train_upsampled.csv", index=False)
