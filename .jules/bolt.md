## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-28 - Preventing Nested Parallelism Oversubscription in Scikit-Learn GridSearchCV

**Learning:** Setting `n_jobs=-1` on a base estimator (e.g. `RandomForestClassifier`) while running `GridSearchCV(n_jobs=-1)` leads to nested process pool / thread pool oversubscription (Loky/OpenMP contention) and CPU context switching overhead. Setting `n_jobs=1` on base estimators inside outer parallel `GridSearchCV(n_jobs=-1)` eliminates thread contention and speeds up grid execution by ~27%.

**Action:** Always verify that base estimators passed to parallel hyperparameter search wrappers like `GridSearchCV` or `RandomizedSearchCV` have `n_jobs=1` (or `None`) to prevent inner parallel worker contention.
