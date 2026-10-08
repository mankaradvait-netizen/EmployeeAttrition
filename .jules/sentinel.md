## 2026-06-27 - Path Traversal Prevention in Data Loading Functions
**Vulnerability:** Loading dataset CSV files using unvalidated string path variables passed directly to `pd.read_csv()` creates path traversal risk.
**Learning:** In notebook environments and data pipelines, validating resolved paths against a strict list of allowed root directories (`os.path.realpath`) before file open operations enforces defense-in-depth against arbitrary file read or path traversal vulnerabilities.
**Prevention:** Always wrap path loading calls in a `safe_load_csv` helper that checks `realpath` against approved parent directories (`.` and `/kaggle/input`).
