import matplotlib.pyplot as plt
import pandas as pd

def generate_chart(intent, df, columns):
    fig, ax = plt.subplots()
    if intent == "top":
        df.plot.bar(x=columns[0], y="count", ax=ax)
    elif intent == "seasonality":
        df.plot(x=columns[0], y="count", kind="line", ax=ax)
    elif intent in ["sum", "average"]:
        df.plot.bar(x=columns[0], y=columns[0], ax=ax)
    elif intent == "pivot":
        df.plot(kind="bar", ax=ax)
    else:
        return None
    return fig
