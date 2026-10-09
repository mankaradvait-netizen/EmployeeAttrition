## 2026-06-27 - Preventing Path Traversal in Jupyter Notebook Data Loaders
**Vulnerability:** Naive `os.path.abspath` or `os.path.isfile` checks without boundary checks fail to prevent path traversal when loading external datasets.
**Learning:** Checking `os.path.isfile(os.path.abspath(filepath))` resolves relative traversal sequences (e.g. `../../etc/passwd`) but does not restrict access to intended base directories.
**Prevention:** Always verify that `os.path.commonpath([abs_target, abs_base]) == abs_base` against explicitly allowed base directory roots before reading files.
