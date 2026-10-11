import os
import sys
import pytest

# Add package directory to sys.path
pkg_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'EmployeeAttrition_[AdvaitMankar]'))
if pkg_dir not in sys.path:
    sys.path.insert(0, pkg_dir)

from utils import load_dataset_safely


def test_safe_dataset_loading():
    base_dir = pkg_dir
    valid_path = os.path.join(base_dir, 'WA_Fn-UseC_-HR-Employee-Attrition.csv')
    df = load_dataset_safely([valid_path], allowed_base_dir=base_dir)
    assert df is not None
    assert len(df) > 0


def test_path_traversal_rejection():
    base_dir = pkg_dir
    traversal_path = os.path.join(base_dir, '..', 'README.md')

    with pytest.raises(FileNotFoundError):
        load_dataset_safely([traversal_path], allowed_base_dir=base_dir)


def test_directory_path_rejection(tmp_path):
    directory_path = str(tmp_path)

    with pytest.raises(FileNotFoundError):
        load_dataset_safely([directory_path], allowed_base_dir=directory_path)


def test_notebook_imports_utils():
    notebook_path = os.path.join(pkg_dir, 'analysis-ipynb.ipynb')
    with open(notebook_path, 'r', encoding='utf-8') as f:
        import json
        nb = json.load(f)

    cell_2_source = ''.join(nb['cells'][2]['source'])
    assert 'from utils import load_dataset_safely' in cell_2_source
