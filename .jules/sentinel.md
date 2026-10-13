## 2026-06-27 - Preventing Path Traversal in Data Pipeline Notebooks
**Vulnerability:** Unsanitized file paths used directly in file loading operations (`pd.read_csv`) in Jupyter notebooks can allow unauthorized directory traversal if path strings originate from untrusted/external inputs or parameters.
**Learning:** Hardcoded or user-configurable Kaggle/Local file paths in notebook scripts should be resolved and constrained to allowed directory roots (e.g., current workspace root or `/kaggle/input`).
**Prevention:** Use `os.path.realpath` to resolve canonical paths and verify that the path starts with an approved base directory before executing read or write file operations.
