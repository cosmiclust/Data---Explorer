import pandas as pd
from modules.query_parser import parse_query

def test_parse_top_query():
    df = pd.DataFrame({"Product": ["A", "B", "C"]})
    result = parse_query("top products", df)
    assert result["intent"] == "top"
    assert "Product" in result["columns"]

def test_parse_sum_query():
    df = pd.DataFrame({"Sales": [10, 20, 30]})
    result = parse_query("total sales", df)
    assert result["intent"] == "sum"
    assert "Sales" in result["columns"]
