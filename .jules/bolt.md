## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-07-15 - Avoiding Nested Parallelism in Scikit-Learn GridSearchCV

**Learning:** Initializing base estimators like `RandomForestClassifier(n_jobs=-1)` inside parallel `GridSearchCV(n_jobs=-1)` creates severe CPU thread contention and process over-subscription. Removing `n_jobs=-1` from the inner estimator while keeping `n_jobs=-1` on outer `GridSearchCV` speeds up fitting by ~60%+ (22.6s down to 8.2s) with zero impact on outputs or metrics.

**Action:** Always verify that estimators wrapped in parallel `GridSearchCV` or `cross_val_score` have `n_jobs=None` to allow Joblib to manage worker thread allocation cleanly without thread over-subscription.
