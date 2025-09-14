def suggest_interpretations(parsed, df):
    options = []

    if parsed["intent"] == "top":
        if parsed["columns"]:
            options.append(f"Top values of {parsed['columns'][0]}")
        else:
            options.append("Top values of most frequent column")

    elif parsed["intent"] == "seasonality":
        options.append("Trend over time")

    elif parsed["intent"] == "average":
        if parsed["columns"]:
            options.append(f"Average of {parsed['columns'][0]}")

    elif parsed["intent"] == "sum":
        if parsed["columns"]:
            options.append(f"Total of {parsed['columns'][0]}")

    if not options:
        options.append("Show raw data")

    return options
