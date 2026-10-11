## 2026-06-27 - Rejecting Security Theater in Static Notebooks
**Vulnerability:** Attempted path traversal validation on hardcoded notebook file paths.
**Learning:** In static tabular data science repositories with hardcoded dataset paths, adding path sanitization is security theater without real security benefit.
**Prevention:** Avoid adding defensive validation on hardcoded constant strings when there is no untrusted input source.
