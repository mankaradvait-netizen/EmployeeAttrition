## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-07-02 - Avoid Pruning Grid Search Parameters to Single Values

**Learning:** Reducing hyperparameter options in `GridSearchCV` to single fixed values (e.g. setting `min_samples_leaf` or `max_depth` to a single scalar array) turns off hyperparameter search along those dimensions. Rather than optimizing execution efficiency, this alters the intended model exploration scope of the notebook.

**Action:** Maintain multi-value parameter options for hyperparameter tuning. Focus optimizations on algorithmic choices or parallelization rather than flattening search grids.
