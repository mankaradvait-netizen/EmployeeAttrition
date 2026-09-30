import os
import pytest
import importlib.util

spec = importlib.util.spec_from_file_location("secure_data", "EmployeeAttrition_[AdvaitMankar]/secure_data.py")
secure_data = importlib.util.module_from_spec(spec)
spec.loader.exec_module(secure_data)

def test_safe_load_csv_valid():
    df = secure_data.safe_load_csv("EmployeeAttrition_[AdvaitMankar]/WA_Fn-UseC_-HR-Employee-Attrition.csv")
    assert not df.empty
    assert "Attrition" in df.columns

def test_safe_load_csv_invalid_extension():
    with pytest.raises(ValueError, match="Invalid file extension"):
        secure_data.safe_load_csv("EmployeeAttrition_[AdvaitMankar]/summary.pdf")

def test_safe_load_csv_nonexistent():
    with pytest.raises(FileNotFoundError):
        secure_data.safe_load_csv("EmployeeAttrition_[AdvaitMankar]/nonexistent.csv")

def test_safe_load_csv_path_traversal():
    with pytest.raises(ValueError, match="outside allowed directories"):
        secure_data.safe_load_csv("/tmp/unauthorized.csv")
