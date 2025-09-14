import streamlit as st
import pandas as pd

from modules.data_loader import load_csv
from modules.query_parser import parse_query
from modules.operations import apply_operation
from modules.suggestions import suggest_interpretations
from modules.explanations import generate_explanation
from modules.charts import generate_chart
from modules.export_utils import export_view
from modules.validation import validate_dataset
from modules.persistence import save_state, load_state

st.set_page_config(page_title="Data Explorer", layout="wide")
st.title("Data Explorer")

uploaded = st.file_uploader("Upload CSV", type="csv")

if uploaded:
    df = load_csv(uploaded)
    st.subheader("Preview")
    st.dataframe(df.head())

    issues = validate_dataset(df)
    if issues:
        st.warning("Data quality issues found:")
        for i in issues:
            st.write("-", i)

    st.subheader("Enter Query")
    query = st.text_input("Ask in plain English")

    if query:
        parsed = parse_query(query, df)
        options = suggest_interpretations(parsed, df)

        if len(options) > 1:
            choice = st.radio("Interpretations:", options)
        else:
            choice = options[0]

        result, chart, explanation = apply_operation(df, parsed)
        st.subheader("Result")
        st.dataframe(result)

        if chart:
            st.subheader("Chart")
            st.pyplot(chart)

        st.subheader("Explanation")
        st.write(explanation)

        st.subheader("Export")
        if st.button("Export current view"):
            export_view(result)
            save_state("current_state.json", {"query": query, "result": result.to_dict()})
            st.success("View and state exported")
