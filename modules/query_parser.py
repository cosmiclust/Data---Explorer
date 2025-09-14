import re

def parse_query(query, df):
    query = query.lower()
    result = {"intent": None, "columns": [], "filters": []}

    if "top" in query:
        result["intent"] = "top"
    elif "seasonality" in query or "trend" in query:
        result["intent"] = "seasonality"
    elif "average" in query:
        result["intent"] = "average"
    elif "sum" in query or "total" in query:
        result["intent"] = "sum"

    for col in df.columns:
        if col.lower() in query:
            result["columns"].append(col)

    numbers = re.findall(r"\d+", query)
    if numbers:
        result["filters"].append(numbers[0])

    return result
