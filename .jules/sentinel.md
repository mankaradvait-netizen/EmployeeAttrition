## 2026-10-10 - Avoiding Security Theater on Local Directory Listings
**Vulnerability:** Attempted path sanitization (`os.path.basename`) on `os.listdir` output in notebook file size calculation.
**Learning:** `os.listdir` returns file names directly from local directory inspection without user input; applying path sanitization functions here is redundant security theater.
**Prevention:** Only apply path sanitization on untrusted or external inputs. In static data science repositories, verify whether a threat vector actually exists before adding defensive logic.
