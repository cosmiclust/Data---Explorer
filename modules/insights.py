def generate_insights(df):
    insights = []
    if df.shape[0] > 1000:
        insights.append("Large dataset detected")
    if df.isnull().any().any():
        insights.append("Contains missing values")
    if df.select_dtypes(include="number").shape[1] > 0:
        numeric_cols = df.select_dtypes(include="number").columns
        for col in numeric_cols:
            insights.append(f"Average {col}: {df[col].mean():.2f}")
    return insights
