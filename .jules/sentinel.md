## 2026-06-27 - Avoiding Security Theater in Static Jupyter Data Science Notebooks
**Vulnerability:** Attempted path sanitization (`os.path.normpath`, `os.path.basename`) on hardcoded static strings and local file listings (`os.listdir`) within a static analysis notebook.
**Learning:** Static analysis notebooks without web servers, APIs, or untrusted user inputs do not suffer from path traversal risks. Adding path manipulation helpers on hardcoded path strings constitutes security theater without providing real security benefits.
**Prevention:** Verify the threat model and confirm untrusted input boundaries before applying path sanitization or security controls. If no security vulnerabilities exist in a purely static dataset repository, do not introduce artificial security wrappers.
