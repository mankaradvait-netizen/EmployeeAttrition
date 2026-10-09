## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-27 - Avoid Over-Pruning Machine Learning Hyperparameter Search Grids

**Learning:** Further pruning GridSearchCV hyperparameter spaces below reasonable exploration boundaries (e.g. dropping depth options like max_depth=8 or max_depth=4) to save execution seconds degrades model exploration quality and introduces notebook output inconsistencies.

**Action:** Do not arbitrarily cut hyperparameter search spaces in ML notebooks if the model tuning space is already streamlined; preserve valid model exploration bounds.
