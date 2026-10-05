## 2026-06-27 - Validating File Paths in Data Science Notebooks
**Vulnerability:** Unsanitized file paths used directly in `pd.read_csv()` leave notebooks vulnerable to path traversal attacks if paths are constructed dynamically or sourced externally.
**Learning:** Checking `os.path.abspath` alone is insufficient to prevent path traversal. To securely validate paths, compare the normalized common path using `os.path.commonpath([abs_path, allowed_dir]) == allowed_dir` against white-listed base directories.
**Prevention:** Always enforce `os.path.commonpath` checks against allowed base directories before reading files from dynamic or configurable paths.
