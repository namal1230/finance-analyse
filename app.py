import pandas as pd
import streamlit as st
from utils.preprocess import load_daa

st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("💰 Finance Analyzer Dashboard")
st.markdown("Analyze your spending patterns with insights & predictions")

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file:

    df = load_daa(uploaded_file)

    st.sidebar.header("🔍 Filters")

    categories = df["category"].unique()
    selected_category = st.sidebar.selectbox(
        "Select Category",
        ["All"] + list(categories)
    )

    if selected_category != "All":
        df = df[df["category"] == selected_category]

    df["date"] = pd.to_datetime(df["date"])
    min_date = df["date"].min()
    max_date = df["date"].max()

    date_range = st.sidebar.date_input(
        "📅 Date Range",
        [min_date, max_date]
    )

    if len(date_range) == 2:
        start_date, end_date = date_range
        df = df[
            (df["date"] >= pd.to_datetime(start_date)) &
            (df["date"] <= pd.to_datetime(end_date))
            ]

    st.markdown("### 📊 Key Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💸 Total Spending", f"{total_spending(df)}")

    with col2:
        st.metric("📉 Average Spending", f"{average_spending(df)}")

    with col3:
        st.metric("📅 Predicted Next Month", f"{predict_next_month(df)}")


else:
    st.info("👆 Upload a CSV file to get started")