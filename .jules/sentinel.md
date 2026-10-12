## 2026-06-27 - Path Sanitization for Dynamic and Environment-Based Dataset Loading

**Vulnerability:** Unsanitized file paths loaded via environment variables or dataset paths in Jupyter notebook workflows can lead to Path Traversal vulnerabilities if relative/untrusted path strings are supplied.
**Learning:** Hardcoded dataset paths in data science notebooks should be wrapped in safe path canonicalization (`os.path.realpath`) and file extension validation (`.csv`) before passing to `pd.read_csv`, supporting optional environment variable overrides (`DATASET_PATH`).
**Prevention:** Always validate file extensions and canonicalize paths using `os.path.realpath` prior to file I/O operations in data processing notebooks.
