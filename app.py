# app.py
import streamlit as st
import pandas as pd
from core.tidy import tidy_dataset
from core.insights import generate_auto_insights
from core.nlp import parse_command, find_best_column
from core.ops import apply_operations
from core.explain import explain_ops
from core.export_story import export_story_bytes
from core.history import History

st.set_page_config(page_title="Data Explorer — Natural Commands", layout="wide")
st.title(" Data Explorer — Natural Commands")

# initialize history in session
if "history" not in st.session_state:
    st.session_state["history"] = History()

# sidebar quick actions
st.sidebar.header("Quick demo & controls")
st.sidebar.markdown("Try commands like:\n- `Top 5 products this quarter`\n- `Show seasonality by region`\n- `Filter Year >= 2023 and Region = Asia`")
if st.sidebar.button("Load sample dataset"):
    st.session_state["uploaded_sample"] = True

uploaded = st.file_uploader("Upload CSV file", type=["csv"], accept_multiple_files=False)
if st.session_state.get("uploaded_sample"):
    uploaded = "sample_data/sales.csv"

if not uploaded:
    st.info("Upload a CSV to begin or click 'Load sample dataset' in the sidebar.")
    st.stop()

# load dataframe
if isinstance(uploaded, str):
    df = pd.read_csv(uploaded)
else:
    df = pd.read_csv(uploaded)

# tidy and coerce
df = tidy_dataset(df)
st.session_state.setdefault("df_original", df)

# top bar: KPIs
st.markdown("### 🔍 Quick KPIs")
col1, col2, col3 = st.columns(3)
nums = df.select_dtypes(include=["number"]).columns.tolist()
if nums:
    col1.metric("Numeric columns", len(nums))
else:
    col1.metric("Numeric columns", 0)
col2.metric("Rows", len(df))
cats = df.select_dtypes(include=["object","category"]).columns.tolist()
col3.metric("Categorical cols", len(cats))

# Data health checks
st.markdown("### 🩺 Data Health Check")
missing = df.isna().mean().round(3) * 100
dup_count = df.duplicated().sum()
st.write(f"- Duplicate rows: **{dup_count}**")
st.write("- Missing values (% per column):")
st.dataframe(missing.to_frame("missing_pct").sort_values("missing_pct", ascending=False))

# Auto-insights
insights = generate_auto_insights(df)
st.markdown("### Auto Insights")
cols = st.columns(3)
for i, ins in enumerate(insights):
    c = cols[i % 3]
    c.info(ins)

# Chat input UI
st.markdown("###  Ask your data (chat)")
user_input = st.text_input("Type a natural-language command (e.g. 'Top 5 products this quarter')")

# suggestions panel: we will show parsed suggestions
if user_input:
    parsed = parse_command(user_input, df)
    st.markdown("**Parsed intent:**")
    st.json(parsed)

    # produce candidate suggestions (simple heuristics)
    suggestions = []
    intent = parsed.get("intent")
    if intent == "top_n":
        n =
