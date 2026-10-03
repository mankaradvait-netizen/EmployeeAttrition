## 2026-06-27 - Preventing Path Traversal in Jupyter Data Ingestion Notebooks
**Vulnerability:** Unsanitized file paths used directly in `pd.read_csv()` calls in Jupyter Notebooks allow arbitrary file reading or path traversal if paths or parameters are supplied dynamically or modified.
**Learning:** Hardcoded dataset loading fallbacks in data science notebooks can attempt to access out-of-bounds files if file paths contain `../` sequences or untrusted input.
**Prevention:** Wrap `pd.read_csv` and file load calls in a validator function that compares `os.path.abspath(filepath)` against `os.path.abspath(allowed_dir)` using string prefix checks (`abs_path == allowed_base or abs_path.startswith(allowed_base + os.sep)`) before accessing disk.
