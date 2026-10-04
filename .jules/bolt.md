## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-28 - Avoiding Parallel Process Thread Oversubscription in GridSearchCV

**Learning:** Combining `GridSearchCV(n_jobs=-1)` with tree estimators configured for internal parallelism (`RandomForestClassifier(n_jobs=-1)`) creates severe CPU thread oversubscription. Each parallel cross-validation worker process attempts to spawn threads across all available CPU cores, causing heavy context switching and thread lock contention. Leaving `n_jobs=None` (single-thread tree fitting) on the estimator while setting `n_jobs=-1` on `GridSearchCV` improved RF search performance by ~33% (~11.3s down to ~7.5s) with 0 metric changes.

**Action:** When using `GridSearchCV(..., n_jobs=-1)`, ensure underlying estimators (e.g. `RandomForestClassifier`, `ExtraTreesClassifier`) do not also set `n_jobs=-1`.
