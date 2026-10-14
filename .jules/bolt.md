## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-28 - Eliminating Nested Thread Oversubscription in Parallel GridSearchCV

**Learning:** Initializing base estimators like `RandomForestClassifier(n_jobs=-1)` inside `GridSearchCV(n_jobs=-1)` creates nested parallel oversubscription ($N \times N$ worker processes/threads), leading to CPU context switching and joblib thread pool lock contention. Removing `n_jobs=-1` from the base estimator while retaining `GridSearchCV(n_jobs=-1)` speeds up Random Forest grid execution by ~33% (from ~11.2s to ~7.5s) without altering search grids or model outputs.

**Action:** Ensure base estimators inside parallel `GridSearchCV` or `cross_val_score` leave `n_jobs=None` (or 1) so outer parallelization operates cleanly across CPU cores.
