## 2026-10-01 - Path Traversal Prevention in Data Science Notebook File Loaders
**Vulnerability:** File paths in notebook data loaders (`pd.read_csv`) accepted arbitrary user/environment path inputs without validating against allowed base directories.
**Learning:** In shared or automated Jupyter environments (e.g., Kaggle/Colab or batch pipelines), arbitrary path variables can lead to path traversal vulnerabilities if user input controls file path locations.
**Prevention:** Resolve canonical file paths using `os.path.realpath()` and verify that resolved paths start with expected base directory paths before opening or passing to data processors.
