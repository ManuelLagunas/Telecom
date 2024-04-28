# Libreries ---------------------------------------- 

import pandas as pd
import joblib
import numpy as np
import os, sys
from sklearn.metrics import roc_auc_score
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve

sys.path.append(os.getcwd()) # Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ---------------------------------------- 

target_test = pd.read_csv("files/datasets/intermediate/a06_target_test.csv")
features_test = pd.read_csv("files/datasets/intermediate/a06_features_test.csv")

model_lgbm_up = joblib.load(f"files/modeling_output/model_fit/b03_lgbm_upsampled.joblib")

# Model application ----------------------------------------

predictions = model_lgbm_up.predict(features_test)
auc_roc = roc_auc_score(target_test, predictions)
print("AUC-ROC:", auc_roc)

# AUC-ROC graph ----------------------------------------

fpr, tpr, thresholds = roc_curve(target_test, predictions)
plt.plot(fpr, tpr)
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.show()

# Save data ----------------------------------------

np.savetxt("files/datasets/output/b05_predictions.csv", predictions, delimiter=',')
