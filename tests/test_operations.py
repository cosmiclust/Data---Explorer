import pandas as pd
from modules.operations import apply_operation

def test_top_operation():
    df = pd.DataFrame({"Category": ["X", "X", "Y", "Z", "Z", "Z"]})
    parsed = {"intent": "top", "columns": ["Category"], "filters": []}
    result, chart, explanation = apply_operation(df, parsed)
    assert "Category" in result.columns
    assert explanation.startswith("Top")

def test_sum_operation():
    df = pd.DataFrame({"Sales": [100, 200, 300]})
    parsed = {"intent": "sum", "columns": ["Sales"], "filters": []}
    result, chart, explanation = apply_operation(df, parsed)
    assert result.iloc[0]["Sales"] == 600
    assert "Total" in explanation
