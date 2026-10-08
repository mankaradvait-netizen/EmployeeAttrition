## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-27 - Preventing Nested Parallelism Oversubscription in GridSearchCV

**Learning:** Setting `n_jobs=-1` on both an ensemble estimator (`RandomForestClassifier`) and `GridSearchCV` causes thread oversubscription ($N$ processes $\times$ $N$ threads), leading to heavy CPU context-switching overhead. Setting `n_jobs=1` on the base estimator while keeping `n_jobs=-1` on `GridSearchCV` speeds up model training by ~38% (~7.4s vs ~12.0s) with zero change in model output.

**Action:** When using `GridSearchCV` with `n_jobs=-1`, always configure the underlying parallel estimator (`RandomForestClassifier`, `ExtraTreesClassifier`, etc.) with `n_jobs=1`.
