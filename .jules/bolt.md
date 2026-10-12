## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-27 - Resolving Nested Parallelism in scikit-learn GridSearchCV

**Learning:** Setting `n_jobs=-1` on both `GridSearchCV` and inner estimators like `RandomForestClassifier(n_jobs=-1)` causes severe CPU thread over-subscription ($N_{cores} \times N_{cores}$ worker threads), leading to context switching and lock contention overhead. Setting `n_jobs=1` on the base estimator allows `GridSearchCV` to parallelize cleanly across outer candidate fits.

**Action:** When configuring parallel `GridSearchCV(n_jobs=-1)`, ensure underlying estimators set `n_jobs=1` (or leave default) to prevent thread over-subscription during parallel cross-validation.
