def validate_dataset(df):
    issues = []
    if df.isnull().any().any():
        issues.append("Missing values found")
    if df.duplicated().any():
        issues.append("Duplicate rows detected")
    return issues
