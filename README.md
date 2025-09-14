
# Data Explorer

**Data Explorer** is a Streamlit app that lets anyone explore a CSV dataset using plain English. You can ask questions like “top 5 products this quarter” or “show seasonality by region” and get tables, charts, and explanations without needing any BI tools.

The app automatically suggests possible interpretations for unclear queries and keeps the workflow simple and transparent.

---

## Features

- **CSV Upload & Preview:** See your data instantly.
- **Natural Language Queries:** Ask questions in everyday language.
- **Suggestions for Vague Queries:** Choose from 2–3 possible interpretations.
- **Operations:** Filter, sort, group, aggregate, pivot, top N.
- **Charts:** Bar and line charts to visualize results.
- **Explanations:** Short description of what each operation does.
- **Quick Insights:** Detect missing values, duplicates, and basic stats.
- **Export & Save:** Export results and save workflow state in JSON.

---

## How It Works

1. **Upload a CSV file.**
2. **Enter a query in plain language.**
3. **If multiple interpretations exist, select one.**
4. **See the transformed table and chart.**
5. **Read the explanation of the operation.**
6. **Refine the view with new queries.**
7. **Export the final view or save the workflow.**

---

## Installation

Clone the repo:

```bash
git clone <your-repo-url>
cd data_explorer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Running the App

```bash
streamlit run app.py
```

---

## Folder Structure

```
data_explorer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── modules/
│   ├── data_loader.py
│   ├── query_parser.py
│   ├── operations.py
│   ├── suggestions.py
│   ├── explanations.py
│   ├── charts.py
│   ├── export_utils.py
│   └── persistence.py
│
└── tests/
    ├── test_parser.py
    ├── test_operations.py
    ├── test_suggestions.py
    ├── test_explanations.py
    ├── test_persistence.py
    └── test_validation.py
```

---

## Testing

Run all tests with:

```bash
pytest tests/
```

Tests cover parsing, operations, suggestions, explanations, persistence, and validation.
````
