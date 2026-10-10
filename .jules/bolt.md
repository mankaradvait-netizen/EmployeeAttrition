## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-10-10 - Preventing Joblib Thread Thrashing in Parallel GridSearchCV

**Learning:** When using parallel `GridSearchCV(..., n_jobs=-1)` with tree ensemble estimators like `RandomForestClassifier`, setting `n_jobs=-1` on the base estimator creates nested worker pools ($N \times N$ worker processes/threads). This causes CPU core oversubscription, lock contention, and thread thrashing, adding over 30% execution overhead (~10.8s vs ~7.4s). Setting `n_jobs=1` on the base estimator allows `GridSearchCV` to parallelize cross-validation fits efficiently without thread oversubscription.

**Action:** Always set `n_jobs=1` on base estimators when wrapped inside an outer parallel search cross-validator (`GridSearchCV` or `RandomizedSearchCV`) configured with `n_jobs=-1`.
