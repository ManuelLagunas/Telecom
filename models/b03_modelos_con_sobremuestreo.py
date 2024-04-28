# Libraries ----------------------------------------

import os
import sys
import pandas as pd
import joblib
from sklearn.metrics import make_scorer, roc_auc_score
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
import lightgbm as lgb
from lightgbm import LGBMClassifier

sys.path.append(os.getcwd())
# Esto es para agregar al path la ruta de ejecución actual y poder importar respecto a la ruta del proyecto, desde donde se debe ejecutar el código

# Loading data ----------------------------------------

features_train = pd.read_csv("files/datasets/intermediate/a07_features_train_upsampled.csv")
target_train = pd.read_csv("files/datasets/intermediate/a07_target_train_upsampled.csv")

# Tuning models ----------------------------------------

# ---------------- Logistic Regression ----------------
# Define the hyperparameters grid
# param_grid = {
#     'penalty': ['l1', 'l2'],
#     'C': [0.001, 0.01, 0.1, 1, 10, 100],
#     'solver': ['liblinear', 'saga']
# }

# # Create the logistic regression model
# logreg = LogisticRegression()

# # Create the GridSearchCV object
# grid_search = GridSearchCV(
#     estimator=logreg, param_grid=param_grid, scoring='roc_auc', cv=5)

# # Fit the model to the training data
# grid_search.fit(features_train, target_train)

# # Get the best hyperparameters and the corresponding AUC-ROC score
# best_params_lr = grid_search.best_params_
# best_score_lr = grid_search.best_score_

# # Print the best hyperparameters and the corresponding AUC-ROC score
# print("Best Hyperparameters:", best_params)
# print("Best AUC-ROC Score:", best_score)

# ---------------- Random Forest ----------------
# Define the hyperparameters grid
# param_grid = {
#     'n_estimators': [10, 20, 30],
#     'max_depth': [None, 10, 20, 30],
#     'min_samples_split': [2, 5, 10],
#     'min_samples_leaf': [1, 2, 4],
# }

# # Create the random forest model
# rf = RandomForestClassifier()

# # Create scorer
# auc_roc_scorer = make_scorer(roc_auc_score)

# # Create the GridSearchCV object
# grid_search = GridSearchCV(
#     estimator=rf, param_grid=param_grid, scoring=auc_roc_scorer, cv=5, n_jobs=-1)

# # Fit the model to the training data
# grid_search.fit(features_train, target_train)

# # Get the best hyperparameters and the corresponding AUC-ROC score
# best_params_rf = grid_search.best_params_
# best_score_rf = grid_search.best_score_

# # Print the best hyperparameters and the corresponding AUC-ROC score
# print("Best Hyperparameters:", best_params)
# print("Best AUC-ROC Score:", best_score)

# ---------------- LightGBM ----------------
# Define the hyperparameters grid
param_grid = {
    'n_estimators': [10, 20, 30],
    'learning_rate': [0.01, 0.1, 0.2],
    'max_depth': [None, 10, 20, 30],
    'num_leaves': [31, 62, 93],
    'min_child_samples': [20, 30, 40]
}

# Create the LightGBM model
lgbm = LGBMClassifier()

# Create scorer
auc_roc_scorer = make_scorer(roc_auc_score)

# Create the GridSearchCV object
grid_search = GridSearchCV(estimator=lgbm, param_grid=param_grid, scoring=auc_roc_scorer, cv=5, n_jobs=-1)

# Fit the model to the training data
grid_search.fit(features_train, target_train)

# Get the best hyperparameters and the corresponding AUC-ROC score
best_params_lgbm = grid_search.best_params_
best_score_lgbm = grid_search.best_score_

# Print the best hyperparameters and the corresponding AUC-ROC score
print("Best Hyperparameters:", best_params_lgbm)
print("Best AUC-ROC Score:", best_score_lgbm)

# Create the best model ----------------------------------------

lgbm_upsampled = LGBMClassifier(**best_params_lgbm)
lgbm_upsampled.fit(features_train, target_train)

# Save the best model ----------------------------------------

joblib.dump(lgbm_upsampled,
        f"files/modeling_output/model_fit/b03_lgbm_upsampled.joblib"
        )