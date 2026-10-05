# Sentinel Security Journal

## 2026-06-27 - Path Traversal & Safe Path Joining in Data Pipelines
**Vulnerability:** Raw string formatting/concatenation (`f'charts/{f}'`) used during file operations inside Jupyter notebooks and data scripts can introduce path traversal or invalid path errors across operating systems.
**Learning:** Hardcoded directory string interpolation lacks path normalization and proper separator handling.
**Prevention:** Always use `os.path.join()` or `pathlib.Path` for constructing file paths safely across environments.
