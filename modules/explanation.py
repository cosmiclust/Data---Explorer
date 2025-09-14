def generate_explanation(intent, columns, details=None):
    if intent == "top":
        return f"Selected top values of {columns[0]}"
    elif intent == "sum":
        return f"Calculated total of {columns[0]}"
    elif intent == "average":
        return f"Calculated average of {columns[0]}"
    elif intent == "seasonality":
        return f"Grouped {columns[0]} over time to show seasonality"
    elif intent == "pivot":
        return f"Created pivot table with {columns[0]}"
    else:
        return "Displayed data as is"
