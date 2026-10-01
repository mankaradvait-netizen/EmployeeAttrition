## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-27 - Eliminating Nested Parallelism in GridSearchCV

**Learning:** Setting `n_jobs=-1` on base estimators (e.g., `RandomForestClassifier`) while running `GridSearchCV` with `n_jobs=-1` causes severe CPU thread oversubscription and process contention. Disabling multi-threading on the base estimator (`n_jobs=None`) and letting `GridSearchCV` handle process-level cross-validation parallelism reduces cell execution time by ~35% (from ~12.9s to ~8.4s) with zero change in model output.

**Action:** When `GridSearchCV` uses `n_jobs=-1`, ensure base ensemble estimators use `n_jobs=None` (or 1) to avoid thread contention.
