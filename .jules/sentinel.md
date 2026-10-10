## 2026-10-10 - Path Traversal Prevention in Notebook Data Loading
**Vulnerability:** Unvalidated relative file paths when loading dataset files in Jupyter notebooks can lead to path traversal vulnerabilities if file paths are manipulated or configured to access arbitrary system files.
**Learning:** Data science notebooks frequently hardcode or construct string paths for datasets without validating that resolved paths stay within the application's base directory.
**Prevention:** Always sanitize and resolve paths using `pathlib.Path` or `os.path.abspath` and verify that the target path is relative to the expected base directory (or allowed system input paths) before opening files.
