from modules.explanations import generate_explanation

def test_top_explanation():
    exp = generate_explanation("top", ["Sales"])
    assert "top values of Sales" in exp

def test_sum_explanation():
    exp = generate_explanation("sum", ["Revenue"])
    assert "total of Revenue" in exp

def test_seasonality_explanation():
    exp = generate_explanation("seasonality", ["Date"])
    assert "Grouped Date over time" in exp
