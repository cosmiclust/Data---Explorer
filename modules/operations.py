import pandas as pd
import matplotlib.pyplot as plt

def apply_operation(df, parsed):
    intent = parsed["intent"]
    cols = parsed["columns"]

    if intent == "top" and cols:
        target = cols[0]
        result = df[target].value_counts().head(5).reset_index()
        result.columns = [target, "count"]
        fig, ax = plt.subplots()
        result.plot.bar(x=target, y="count", ax=ax)
        explanation = f"Top 5 values in {target}"
        return result, fig, explanation

    elif intent == "seasonality" and "date" in [c.lower() for c in df.columns]:
        date_col = [c for c in df.columns if "date" in c.lower()][0]
        result = df.groupby(pd.to_datetime(df[date_col]).dt.to_period("M")).size().reset_index(name="count")
        fig, ax = plt.subplots()
        result.plot(x=date_col, y="count", kind="line", ax=ax)
        explanation = "Seasonality over time"
        return result, fig, explanation

    elif intent == "sum" and cols:
        target = cols[0]
        result = pd.DataFrame({target: [df[target].sum()]})
        explanation = f"Total of {target}"
        return result, None, explanation

    elif intent == "average" and cols:
        target = cols[0]
        result = pd.DataFrame({target: [df[target].mean()]})
        explanation = f"Average of {target}"
        return result, None, explanation

    return df, None, "Showing data as is"
