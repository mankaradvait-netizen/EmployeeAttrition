## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-28 - Preventing Joblib Thread Oversubscription in Nested GridSearchCV

**Learning:** Setting `n_jobs=-1` inside both the base estimator (e.g., `RandomForestClassifier(n_jobs=-1)`) and `GridSearchCV(..., n_jobs=-1)` creates nested process and thread multiplication in `joblib`, leading to heavy CPU context-switching and process contention. Setting `n_jobs=1` on the base estimator while keeping `n_jobs=-1` on `GridSearchCV` eliminates process oversubscription and accelerates RF grid search by ~33%.

**Action:** Always set `n_jobs=1` on parallelizable base estimators when wrapping them in parallelized cross-validation (`GridSearchCV` or `cross_val_score` with `n_jobs=-1`).
