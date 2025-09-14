import pandas as pd
from modules.charts import generate_chart
from modules.explanations import generate_explanation

def apply_operation(df, parsed):
    intent = parsed["intent"]
    cols = parsed["columns"]

    if intent == "top" and cols:
        target = cols[0]
        result = df[target].value_counts().head(5).reset_index()
        result.columns = [target, "count"]
        chart = generate_chart(intent, result, [target])
        explanation = generate_explanation(intent, cols)
        return result, chart, explanation

    elif intent == "seasonality" and "date" in [c.lower() for c in df.columns]:
        date_col = [c for c in df.columns if "date" in c.lower()][0]
        result = df.groupby(pd.to_datetime(df[date_col]).dt.to_period("M")).size().reset_index(name="count")
        result.rename(columns={"index": date_col}, inplace=True)
        chart = generate_chart(intent, result, [date_col])
        explanation = generate_explanation(intent, [date_col])
        return result, chart, explanation

    elif intent == "sum" and cols:
        target = cols[0]
        result = pd.DataFrame({target: [df[target].sum()]})
        chart = generate_chart(intent, result, [target])
        explanation = generate_explanation(intent, cols)
        return result, chart, explanation

    elif intent == "average" and cols:
        target = cols[0]
        result = pd.DataFrame({target: [df[target].mean()]})
        chart = generate_chart(intent, result, [target])
        explanation = generate_explanation(intent, cols)
        return result, chart, explanation

    elif intent == "pivot":
        if len(cols) >= 2:
            result = pd.pivot_table(df, index=cols[0], columns=cols[1], aggfunc='sum', fill_value=0)
            chart = generate_chart(intent, result, cols)
            explanation = generate_explanation(intent, cols)
            return result, chart, explanation

    return df, None, "Showing data as is"
