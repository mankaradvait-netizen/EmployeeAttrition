import os
import pandas as pd

ALLOWED_BASE_DIRS = [
    os.path.abspath("."),
    os.path.abspath("/kaggle/input")
]

def safe_load_csv(path: str, required_column: str = "Attrition") -> pd.DataFrame:
    """
    Safely loads a CSV file after validating path containment and extension
    to prevent path traversal vulnerabilities and unsafe dataset execution.
    """
    abs_path = os.path.abspath(path)

    # Path traversal check: verify abs_path is within allowed base directories
    is_allowed = any(
        os.path.commonpath([abs_path, base_dir]) == base_dir
        for base_dir in ALLOWED_BASE_DIRS
        if os.path.exists(base_dir)
    )
    if not is_allowed:
        raise ValueError(f"Security error: Path '{path}' outside allowed directories")

    if not abs_path.endswith(".csv"):
        raise ValueError(f"Security error: Invalid file extension for '{path}'")
    if not os.path.exists(abs_path):
        raise FileNotFoundError(f"File not found: {abs_path}")

    df = pd.read_csv(abs_path)
    if df.empty or required_column not in df.columns:
        raise ValueError("Security error: Invalid or empty dataset schema")

    return df
