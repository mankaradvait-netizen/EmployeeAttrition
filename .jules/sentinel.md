## 2026-06-27 - Path Traversal Prevention in Data Loading
**Vulnerability:** Loading CSV datasets using raw file paths without directory confinement checks allows arbitrary file read if path parameters are manipulated (CWE-22).
**Learning:** Checking `os.path.realpath` alone is insufficient for path traversal defense; `os.path.commonpath` must be used to verify that the resolved target path remains within the allowed base directory (`base_dir`).
**Prevention:** Always validate file paths with `os.path.commonpath([base_dir, target_path]) == base_dir` prior to opening or parsing files.
