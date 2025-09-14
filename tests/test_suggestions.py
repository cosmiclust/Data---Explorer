from modules.suggestions import suggest_interpretations

def test_top_suggestion():
    parsed = {"intent": "top", "columns": ["Product"], "filters": []}
    df_mock = None
    options = suggest_interpretations(parsed, df_mock)
    assert "Top values of Product" in options

def test_seasonality_suggestion():
    parsed = {"intent": "seasonality", "columns": ["Date"], "filters": []}
    df_mock = None
    options = suggest_interpretations(parsed, df_mock)
    assert "Trend over time" in options

def test_default_suggestion():
    parsed = {"intent": None, "columns": [], "filters": []}
    df_mock = None
    options = suggest_interpretations(parsed, df_mock)
    assert "Show raw data" in options
