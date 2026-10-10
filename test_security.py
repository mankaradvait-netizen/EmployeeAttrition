import pytest
from pathlib import Path

def get_safe_path(target_path, base_dir=None):
    """
    Validates that target_path is within base_dir or allowed Kaggle directory
    to prevent path traversal vulnerabilities.
    """
    if base_dir is None:
        base_dir = Path.cwd()
    resolved_path = Path(target_path).resolve()
    resolved_base = Path(base_dir).resolve()
    if str(resolved_path).startswith('/kaggle/input'):
        return resolved_path
    try:
        resolved_path.relative_to(resolved_base)
        return resolved_path
    except ValueError:
        raise ValueError(f"Security Alert: Path traversal attempt blocked for path: {target_path}")


def test_get_safe_path_valid_local(tmp_path):
    valid_file = tmp_path / "data.csv"
    valid_file.touch()

    result = get_safe_path(valid_file, base_dir=tmp_path)
    assert result == valid_file.resolve()


def test_get_safe_path_path_traversal_blocked(tmp_path):
    sub_dir = tmp_path / "subdir"
    sub_dir.mkdir()
    outside_file = tmp_path / "outside.csv"
    outside_file.touch()

    # Attempt to access outside_file from sub_dir base
    with pytest.raises(ValueError, match="Path traversal attempt blocked"):
        get_safe_path("../outside.csv", base_dir=sub_dir)


def test_get_safe_path_kaggle_path_allowed():
    kaggle_path = "/kaggle/input/datasets/sample.csv"
    result = get_safe_path(kaggle_path)
    assert str(result) == kaggle_path
