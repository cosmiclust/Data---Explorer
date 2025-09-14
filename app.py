import streamlit as st
import pandas as pd

from modules.data_loader import load_csv
from modules.query_parser import parse_query
from modules.operations import apply_operation
from modules.suggestions import suggest_interpretations
from modules.insights import generate_insights
from modules.export_utils import export_view
from modules.validation import validate_dataset

st.set_page_config(page_title="Data Explorer", layout="wide")

st.title("Data Explorer")

uploaded = st.file_uploader("Upload a CSV file", type="csv")

if uploaded:
    df = load_csv(uploaded)
    st.subheader("Preview")
    st.dataframe(df.head())

    issues = validate_dataset(df)
    if issues:
        st.warning("Data quality checks found issues:")
        for i in issues:
            st.write("-", i)

    st.subheader("Ask a question")
    query = st.text_input("Example: top 5 products this quarter")

    if query:
        parsed = parse_query(query, df)
        options = suggest_interpretations(parsed, df)

        if len(options) > 1:
            choice = st.radio("Possible interpretations:", options)
        else:
            choice = options[0]

        result, chart, explanation = apply_operation(df, choice)

        st.subheader("Result")
        st.dataframe(result)

        if chart:
            st.subheader("Chart")
            st.pyplot(chart)
