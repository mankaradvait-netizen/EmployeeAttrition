## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-28 - Eliminating Thread Oversubscription in Multi-threaded GridSearchCV

**Learning:** Setting `n_jobs=-1` on base estimators (such as `RandomForestClassifier`) when wrapped inside `GridSearchCV(n_jobs=-1)` causes nested thread oversubscription. Each worker process spawns $N$ threads, creating severe CPU context switching and lock contention that slows down fit times by over 35%. Setting `n_jobs=1` on the base estimator allows `GridSearchCV` to handle fold-level parallelism cleanly without thread contention.

**Action:** When `GridSearchCV` is executed with `n_jobs=-1` or `n_jobs > 1`, always set `n_jobs=1` on base estimators (like `RandomForestClassifier`) to avoid process/thread oversubscription.
