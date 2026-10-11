import os
import pandas as pd


def load_dataset_safely(paths, allowed_base_dir=None):
    """
    Loads dataset from a list of path candidates, validating that resolved file paths
    stay within allowed_base_dir to prevent path traversal vulnerabilities.
    """
    if allowed_base_dir is None:
        allowed_base_dir = os.path.abspath(os.getcwd())
    else:
        allowed_base_dir = os.path.abspath(allowed_base_dir)

    for path in paths:
        abs_path = os.path.abspath(path)
        # Check path traversal containment and file existence
        try:
            if (
                os.path.commonpath([allowed_base_dir, abs_path]) == allowed_base_dir
                and os.path.isfile(abs_path)
            ):
                return pd.read_csv(abs_path)
        except ValueError:
            # Different drive letters or invalid relative paths on Windows
            continue

    raise FileNotFoundError("No valid dataset file found within allowed base directory.")
