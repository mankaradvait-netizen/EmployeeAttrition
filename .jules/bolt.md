## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-28 - Avoiding Nested `n_jobs=-1` Parallelism in GridSearchCV Estimators

**Learning:** Setting `n_jobs=-1` on an estimator (e.g. `RandomForestClassifier`) while simultaneously passing it into `GridSearchCV(..., n_jobs=-1)` creates nested parallel worker pools. Every joblib process spawned by `GridSearchCV` attempts to spin up threads across all available CPU cores, causing severe thread contention, context switching overhead, and lock contention.

**Action:** When using `GridSearchCV(n_jobs=-1)`, ensure the base estimator has default thread settings (`n_jobs=None` or `1`) so `GridSearchCV` handles process parallelism cleanly.
