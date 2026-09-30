"""Dataset Security & Validation Utility for HR Analytics."""

from pathlib import Path
import pandas as pd


def resolve_safe_path(target_path: str, base_dir: str = ".") -> str:
    """Resolve path safely, ensuring it remains within base_dir to prevent path traversal."""
    base, target = Path(base_dir).resolve(), Path(target_path).resolve()
    try:
        target.relative_to(base)
    except ValueError:
        raise ValueError(
            f"Security Error: Path traversal attempt blocked for '{target_path}'"
        )
    return str(target)


def validate_hr_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Validate HR dataset schema and ensure required fields are present."""
    req_cols = ["Attrition", "Age", "Department", "JobRole", "MonthlyIncome"]
    if df is None or df.empty:
        raise ValueError("Security Validation Error: Dataset is empty.")
    missing = [c for c in req_cols if c not in df.columns]
    if missing:
        raise ValueError(f"Security Validation Error: Missing columns {missing}")
    return df


def load_validated_dataset(file_path: str, base_dir: str = ".") -> pd.DataFrame:
    """Safely resolve file path, load dataset, and enforce schema validation."""
    safe_path = resolve_safe_path(file_path, base_dir=base_dir)
    df = pd.read_csv(safe_path)
    return validate_hr_dataset(df)
