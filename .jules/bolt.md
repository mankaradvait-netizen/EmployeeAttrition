## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-28 - Preventing CPU Thread Oversubscription in Nested GridSearchCV

**Learning:** Specifying `n_jobs=-1` on both an inner estimator (e.g. `RandomForestClassifier(n_jobs=-1)`) and an outer `GridSearchCV(n_jobs=-1)` creates nested parallelism. Joblib worker processes and estimator threads contend for CPU cores, causing severe context switching and lock overhead. Removing `n_jobs=-1` from the inner estimator while retaining `GridSearchCV(n_jobs=-1)` yields a ~33% fit speedup (~11.1s down to ~7.4s) with zero metric change.

**Action:** When using `GridSearchCV(..., n_jobs=-1)`, leave the inner estimator's `n_jobs` at default (`None`/1) to let joblib handle process-level parallelism cleanly without thread oversubscription.
