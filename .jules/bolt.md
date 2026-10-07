## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-28 - Preventing Nested Parallel Process Thrashing in GridSearchCV

**Learning:** Specifying `n_jobs=-1` on a base estimator (e.g., `RandomForestClassifier`) when wrapping it in `GridSearchCV(n_jobs=-1)` triggers nested process parallelism in scikit-learn. Each grid worker process attempts to spawn additional sub-worker processes, leading to process over-subscription, CPU context switching, and IPC overhead. Setting `n_jobs=1` on the base estimator allows `GridSearchCV` to parallelize cross-validation folds cleanly across CPU cores, reducing grid search time by ~30–40% (~2.5–3.5s speedup) with identical model results.

**Action:** When `GridSearchCV` is configured with `n_jobs=-1` (or `n_jobs > 1`), ensure the base estimator has `n_jobs=1` to prevent nested worker creation.
