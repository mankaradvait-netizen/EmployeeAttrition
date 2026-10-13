## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-28 - Avoiding Joblib Thread Oversubscription in Nested GridSearchCV

**Learning:** Setting `n_jobs=-1` on both an estimator (such as `RandomForestClassifier`) and `GridSearchCV` causes nested `joblib` thread oversubscription and CPU thread contention. Disabling inner estimator parallelism (`n_jobs=None`) while allowing `GridSearchCV` to parallelize cross-validation folds (`n_jobs=-1`) yields a ~30–35% speedup in model search time without altering results.

**Action:** When profiling scikit-learn search pipelines, ensure inner estimators use `n_jobs=None` when wrapped in `GridSearchCV(..., n_jobs=-1)`.
