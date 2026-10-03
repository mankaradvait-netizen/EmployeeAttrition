## 2026-10-03 - Path Traversal Prevention in Data Pipelines via Base Directory Relative Check

**Vulnerability:** Loading CSV datasets using raw string paths in `pd.read_csv()` allows potential directory traversal if path strings are modified or sourced from external user inputs.
**Learning:** Checking `Path(path).is_file()` alone is insufficient because resolved absolute paths (e.g., `/etc/passwd`) still return `True` for `is_file()`. Confinement within an allowed base directory using `path.relative_to(allowed_base_dir)` (or `is_relative_to`) is required to strictly enforce path boundary limits.
**Prevention:** Always validate resolved paths against an allowed root directory before file read operations in data ingestion pipelines.
