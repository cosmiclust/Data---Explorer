import pandas as pd
from modules.validation import validate_dataset

def test_missing_values():
    df = pd.DataFrame({"A": [1, None, 3]})
    issues = validate_dataset(df)
    assert "Missing values found" in issues

def test_duplicates():
    df = pd.DataFrame({"A": [1, 1, 2]})
    issues = validate_dataset(df)
    assert "Duplicate rows detected" in issues
