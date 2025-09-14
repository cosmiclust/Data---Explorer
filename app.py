# app.py
import streamlit as st
import pandas as pd
from core.messy_data_fix import tidy_dataset
from core.auto_insights import generate_auto_insights
from core.story_export import export_story_bytes
from ui.chat_ui import chat_interface
from ui.insights_cards import render_insights

st.set_page_config(page_title="Data Explorer NL", layout="wide", initial_sidebar_state="expanded")
st.title("Data Explorer — Natural Commands")

st.sidebar.header("Quick demo")
st.sidebar.markdown("- Upload CSV\n- Try: `Top 5 products this quarter`")

uploaded = st.file_uploader("Upload CSV (CSV only)", type=["csv"])
if st.sidebar.button("Load sample dataset"):
    uploaded = "sample_data/sales.csv"

if not uploaded:
    st.info("Upload a CSV to begin, or click 'Load sample dataset' in the sidebar.")
    st.stop()

# Load dataframe
if isinstance(uploaded, str):
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv(uploaded)

# Tidy automatically
df = tidy_dataset(df)
st.session_state.setdefault("df_original", df)

st.markdown("### Dataset preview")
st.dataframe(df.head(8))

# Auto insights
insights = generate_auto_insights(df)
render_insights(insights)

# Chat interface
chat_interface(df, insights)

# Export whole story / data
if st.button("Export Full Data Story (PDF)"):
    pdf_bytes = export_story_bytes(df, insights, title="Full Data Story")
    st.download_button("⬇ Download story.pdf", pdf_bytes, file_name="data_story.pdf")
