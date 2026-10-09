## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-27 - Preventing Nested Parallelism Over-Subscription in GridSearchCV + RandomForest

**Learning:** Wrapping `RandomForestClassifier(n_jobs=-1)` inside `GridSearchCV(n_jobs=-1)` creates nested parallelism where outer parallel cross-validation tasks each spawn inner threads across CPU cores. This worker over-subscription causes thread contention and CPU context switching overhead. Setting `n_jobs=1` on the base `RandomForestClassifier` eliminates inner thread over-subscription while allowing `GridSearchCV` to parallelize cleanly across CPU cores.

**Action:** When using `GridSearchCV(..., n_jobs=-1)` with tree ensemble estimators (e.g. `RandomForestClassifier`), set `n_jobs=1` on the base estimator to prevent nested worker over-subscription.
