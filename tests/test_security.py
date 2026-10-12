import json
import os
import pytest
import pandas as pd


def get_load_dataset_safely_fn():
    nb_path = os.path.join(
        os.path.dirname(__file__),
        "..",
        "EmployeeAttrition_[AdvaitMankar]",
        "analysis-ipynb.ipynb"
    )
    with open(nb_path, "r") as f:
        nb = json.load(f)

    target_code = None
    for cell in nb["cells"]:
        source = "".join(cell["source"])
        if "def load_dataset_safely" in source:
            target_code = source
            break

    if not target_code:
        raise ValueError("Could not find load_dataset_safely definition in notebook.")

    func_lines = []
    for line in target_code.splitlines(keepends=True):
        if line.startswith("ENV_PATH") or line.startswith("KAGGLE_PATH"):
            break
        func_lines.append(line)

    scope = {"os": os, "pd": pd}
    exec("".join(func_lines), scope)
    return scope["load_dataset_safely"]


def test_load_dataset_safely_valid(tmp_path):
    load_fn = get_load_dataset_safely_fn()
    csv_file = tmp_path / "test_data.csv"
    df = pd.DataFrame({"col1": [1, 2], "col2": ["A", "B"]})
    df.to_csv(csv_file, index=False)

    loaded_df = load_fn(str(csv_file))
    assert len(loaded_df) == 2
    assert list(loaded_df.columns) == ["col1", "col2"]


def test_load_dataset_safely_invalid_extension(tmp_path):
    load_fn = get_load_dataset_safely_fn()
    txt_file = tmp_path / "test_data.txt"
    txt_file.write_text("dummy data")

    with pytest.raises(ValueError, match="Invalid dataset format"):
        load_fn(str(txt_file))


def test_load_dataset_safely_nonexistent_file():
    load_fn = get_load_dataset_safely_fn()
    with pytest.raises(FileNotFoundError):
        load_fn("non_existent_dataset_12345.csv")


def test_load_dataset_safely_path_traversal_attempt(tmp_path):
    load_fn = get_load_dataset_safely_fn()
    # Create non-csv target file
    sensitive_file = tmp_path / "sensitive.txt"
    sensitive_file.write_text("secret_data")

    traversal_path = os.path.join(tmp_path, "sub", "..", "sensitive.txt")
    with pytest.raises(ValueError, match="Invalid dataset format"):
        load_fn(traversal_path)
