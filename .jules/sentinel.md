## 2026-06-29 - Secure CSV Data Loading in Data Science Notebook Projects
**Vulnerability:** Direct `pd.read_csv` on arbitrary user/input paths can risk path traversal and loading corrupted or improperly formatted datasets without schema verification.
**Learning:** In static Jupyter Notebook repository structures, modifying single-line JSON notebook files produces large unreviewable diffs. Decoupling file loading validation into a dedicated module allows robust security testing and clean diffs.
**Prevention:** Validate canonical path extensions, file existence, and mandatory schema columns before reading data.
