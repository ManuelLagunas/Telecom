### Modelos de control

#### LogisticRegression
>>> print("Best Hyperparameters:", best_params)
Best Hyperparameters: {'C': 1, 'penalty': 'l1', 'solver': 'liblinear'}
>>> print("Best AUC-ROC Score:", best_score)
Best AUC-ROC Score: 0.8299176848943608

#### Random Forest
GridSearchCV(cv=5, estimator=RandomForestClassifier(), n_jobs=-1,
             param_grid={'max_depth': [None, 10, 20, 30],
                         'min_samples_leaf': [1, 2, 4],
                         'min_samples_split': [2, 5, 10],
                         'n_estimators': [10, 20, 30]},
             scoring=make_scorer(roc_auc_score))
>>> best_params = grid_search.best_params_
>>> best_score = grid_search.best_score_
>>> print("Best Hyperparameters:", best_params)
Best Hyperparameters: {'max_depth': 30, 'min_samples_leaf': 1, 'min_samples_split': 5, 'n_estimators': 20}
>>> print("Best AUC-ROC Score:", best_score)
Best AUC-ROC Score: 0.7518240435025418

#### Light
GridSearchCV(cv=5, estimator=LGBMClassifier(), n_jobs=-1,
             param_grid={'learning_rate': [0.01, 0.1, 0.2],
                         'max_depth': [None, 10, 20, 30],
                         'min_child_samples': [20, 30, 40],
                         'n_estimators': [10, 20, 30],
                         'num_leaves': [31, 62, 93]},
             scoring=make_scorer(roc_auc_score))
>>> best_params = grid_search.best_params_
>>> best_score = grid_search.best_score_
>>> print("Best Hyperparameters:", best_params)
Best Hyperparameters: {'learning_rate': 0.2, 'max_depth': None, 'min_child_samples': 20, 'n_estimators': 30, 'num_leaves': 93}
>>> print("Best AUC-ROC Score:", best_score)
Best AUC-ROC Score: 0.8152084352364263


### Modelos con balanceo

#### LogisticRegression
GridSearchCV(cv=5, estimator=LogisticRegression(),
             param_grid={'C': [0.001, 0.01, 0.1, 1, 10, 100],
                         'class_weight': ['balanced'], 'penalty': ['l1', 'l2'],
                         'solver': ['liblinear', 'saga']},
             scoring='roc_auc')
>>> best_params = grid_search.best_params_
>>> best_score = grid_search.best_score_
>>> print("Best Hyperparameters:", best_params)
Best Hyperparameters: {'C': 0.1, 'class_weight': 'balanced', 'penalty': 'l1', 'solver': 'liblinear'}
>>> print("Best AUC-ROC Score:", best_score)
Best AUC-ROC Score: 0.8300068725309557

### Random Forest

GridSearchCV(cv=5, estimator=RandomForestClassifier(), n_jobs=-1,
             param_grid={'class_weight': ['balanced', 'balanced_subsample'],
                         'max_depth': [None, 10, 20, 30],
                         'min_samples_leaf': [1, 2, 4],
                         'min_samples_split': [2, 5, 10],
                         'n_estimators': [10, 20, 30]},
             scoring=make_scorer(roc_auc_score))
>>> best_params = grid_search.best_params_
>>> best_score = grid_search.best_score_
>>> print("Best Hyperparameters:", best_params)
Best Hyperparameters: {'class_weight': 'balanced_subsample', 'max_depth': 10, 'min_samples_leaf': 2, 'min_samples_split': 5, 'n_estimators': 30}
>>> print("Best AUC-ROC Score:", best_score)
Best AUC-ROC Score: 0.785688920541382
>>> 

### Light

GridSearchCV(cv=5, estimator=LGBMClassifier(), n_jobs=-1,
             param_grid={'class_weight': ['balanced'],
                         'learning_rate': [0.01, 0.1, 0.2],
                         'max_depth': [None, 10, 20, 30],
                         'min_child_samples': [20, 30, 40],
                         'n_estimators': [10, 20, 30],
                         'num_leaves': [31, 62, 93]},
             scoring=make_scorer(roc_auc_score))
>>> best_params = grid_search.best_params_
>>> best_score = grid_search.best_score_
>>> print("Best Hyperparameters:", best_params)
Best Hyperparameters: {'class_weight': 'balanced', 'learning_rate': 0.2, 'max_depth': None, 'min_child_samples': 30, 'n_estimators': 30, 'num_leaves': 93}
>>> print("Best AUC-ROC Score:", best_score)
Best AUC-ROC Score: 0.8369454199535916
>>> 

### Modelos con sobremuestreo

#### LogisticRegression

GridSearchCV(cv=5, estimator=LogisticRegression(),
             param_grid={'C': [0.001, 0.01, 0.1, 1, 10, 100],
                         'penalty': ['l1', 'l2'],
                         'solver': ['liblinear', 'saga']},
             scoring='roc_auc')
>>> best_params = grid_search.best_params_
>>> best_score = grid_search.best_score_
>>> print("Best Hyperparameters:", best_params)
Best Hyperparameters: {'C': 0.1, 'penalty': 'l1', 'solver': 'liblinear'}
>>> print("Best AUC-ROC Score:", best_score)
Best AUC-ROC Score: 0.836800111375168

#### Randomforest

GridSearchCV(cv=5, estimator=RandomForestClassifier(), n_jobs=-1,
             param_grid={'max_depth': [None, 10, 20, 30],
                         'min_samples_leaf': [1, 2, 4],
                         'min_samples_split': [2, 5, 10],
                         'n_estimators': [10, 20, 30]},
             scoring=make_scorer(roc_auc_score))
>>> best_params = grid_search.best_params_
>>> best_score = grid_search.best_score_
>>> print("Best Hyperparameters:", best_params)
Best Hyperparameters: {'max_depth': 30, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 30}
>>> print("Best AUC-ROC Score:", best_score)
Best AUC-ROC Score: 0.9254860063821854

#### Light

GridSearchCV(cv=5, estimator=LGBMClassifier(), n_jobs=-1,
             param_grid={'learning_rate': [0.01, 0.1, 0.2],
                         'max_depth': [None, 10, 20, 30],
                         'min_child_samples': [20, 30, 40],
                         'n_estimators': [10, 20, 30],
                         'num_leaves': [31, 62, 93]},
             scoring=make_scorer(roc_auc_score))
>>> best_params_lgbm = grid_search.best_params_
>>> best_score_lgbm = grid_search.best_score_
>>> print("Best Hyperparameters:", best_params)
Best Hyperparameters: {'max_depth': 30, 'min_samples_leaf': 1, 'min_samples_split': 2, 'n_estimators': 30}
>>> print("Best AUC-ROC Score:", best_score)
Best AUC-ROC Score: 0.9254860063821854
>>> print("Best Hyperparameters:", best_params_lgbm)
Best Hyperparameters: {'learning_rate': 0.2, 'max_depth': 20, 'min_child_samples': 20, 'n_estimators': 30, 'num_leaves': 93}
>>> print("Best AUC-ROC Score:", best_score_lgbm)
Best AUC-ROC Score: 0.937050994782712


### Modelos con submuestreo

#### LogisticRegression

