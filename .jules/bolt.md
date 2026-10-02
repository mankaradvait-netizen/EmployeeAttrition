## 2026-06-27 - Optimizing GridSearchCV Search Spaces for Small Tabular Notebooks

**Learning:** Oversized hyperparameter grids in `GridSearchCV` (e.g. 200–300 trees and redundant parameter combinations) account for over 85% of execution time in tabular ML notebooks (~81s out of 95s). Pruning unnecessary hyperparameter combinations (reducing fits from 280 to 120) speeds up total notebook execution by ~58% (from 95s to 39s) with zero loss in model evaluation metrics or best model selection.

**Action:** When profiling Jupyter notebooks containing `GridSearchCV`, inspect candidate grid combinations (`n_estimators`, `max_depth`, `max_features`) relative to dataset size. Streamline grids to high-yield subspaces before running full cross-validation.

## 2026-06-28 - Preventing Thread Oversubscription in GridSearchCV with Parallel Estimators

**Learning:** Setting `n_jobs=-1` on both `GridSearchCV` and an estimator like `RandomForestClassifier` creates $N \times N$ worker processes/threads via joblib/loky, causing severe CPU core oversubscription and context switching overhead. Setting `n_jobs=1` on the base estimator while leaving `n_jobs=-1` on `GridSearchCV` speeds up cross-validation searches by ~33% (~12.7s down to ~8.4s) while maintaining 100% identical search results.

**Action:** When using `GridSearchCV(n_jobs=-1)` with multi-threaded estimators (`RandomForestClassifier`, `XGBClassifier`, etc.), ensure the base estimator has `n_jobs=1` to let `GridSearchCV` handle parallel fold evaluation cleanly.
