import pandas as pd

def export_view(df):
    df.to_csv("exported_view.csv", index=False)
