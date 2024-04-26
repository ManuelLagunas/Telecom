# Libraries ----------------------------------------

import os
import sys
import pandas as pd
import joblib
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import lightgbm as lgb

sys.path.append(os.getcwd())  
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

features_train = pd.read_csv("files/datasets/intermediate/a06_features_train.csv")
target_train = pd.read_csv("files/datasets/intermediate/a06_target_train.csv")

# Tuning models ----------------------------------------

#---------------- Logistic Regression ----------------
# Define the hyperparameters grid
param_grid = {
    'penalty': ['l1', 'l2'],
    'C': [0.001, 0.01, 0.1, 1, 10, 100],
    'solver': ['liblinear', 'saga']
}

# Create the logistic regression model
logreg = LogisticRegression()

# Create the GridSearchCV object
grid_search = GridSearchCV(estimator=logreg, param_grid=param_grid, scoring='roc_auc', cv=5)

# Fit the model to the training data
grid_search.fit(features_train, target_train)

# Get the best hyperparameters and the corresponding AUC-ROC score
best_params = grid_search.best_params_
best_score = grid_search.best_score_

# Print the best hyperparameters and the corresponding AUC-ROC score
print("Best Hyperparameters:", best_params)
print("Best AUC-ROC Score:", best_score)
