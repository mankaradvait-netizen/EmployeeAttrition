import pandas as pd
import pytest

REQUIRED_COLUMNS = {
    'Attrition', 'Age', 'Department', 'JobRole', 'MonthlyIncome',
    'OverTime', 'WorkLifeBalance', 'JobSatisfaction', 'YearsAtCompany'
}


def validate_dataset_schema(df: pd.DataFrame) -> bool:
    """
    Security & Integrity Enhancement: Ensures dataset meets expected schema rules,
    failing securely if untrusted, empty, or corrupt input data is loaded.
    """
    if df is None or df.empty:
        raise ValueError("Security Alert: Input dataset is empty or None.")

    missing_cols = REQUIRED_COLUMNS - set(df.columns)
    if missing_cols:
        raise ValueError(f"Security Alert: Dataset schema validation failed. Missing required columns: {sorted(list(missing_cols))}")

    return True


def test_validate_dataset_schema_success():
    valid_df = pd.DataFrame(columns=list(REQUIRED_COLUMNS))
    valid_df.loc[0] = ['Yes', 30, 'Sales', 'Sales Executive', 5000, 'Yes', 3, 4, 2]
    assert validate_dataset_schema(valid_df) is True


def test_validate_dataset_schema_missing_columns():
    invalid_df = pd.DataFrame(columns=['Age', 'Department'])
    invalid_df.loc[0] = [30, 'Sales']
    with pytest.raises(ValueError, match="Security Alert: Dataset schema validation failed"):
        validate_dataset_schema(invalid_df)


def test_validate_dataset_schema_empty():
    with pytest.raises(ValueError, match="Security Alert: Input dataset is empty"):
        validate_dataset_schema(pd.DataFrame())
