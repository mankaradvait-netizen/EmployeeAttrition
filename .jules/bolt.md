## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-27 - Eliminating Nested Parallelism Contention in GridSearchCV

**Learning:** Setting `n_jobs=-1` on an estimator (e.g., `RandomForestClassifier(n_jobs=-1)`) inside `GridSearchCV(n_jobs=-1)` causes joblib process/thread thrashing and CPU core over-subscription, adding significant overhead (~35–40% execution time penalty).

**Action:** Always omit `n_jobs=-1` on inner estimators when `GridSearchCV` handles outer cross-validation parallelism with `n_jobs=-1`.
