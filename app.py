import pandas as pd
import streamlit as st

from utils.analysis import category_spending, monthly_trend, total_spending, average_spending, predict_next_month, \
    generate_insights
from utils.preprocess import load_daa
from utils.visualization import plot_category_spending, plot_monthly_trend, plot_heatmap

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


    st.markdown("---")
    st.markdown("### 📈 Visual Analysis")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("#### 🧾 Category Spending")
        cat_data = category_spending(df)
        st.pyplot(plot_category_spending(cat_data))

    with col2:
        st.markdown("#### 📆 Monthly Trend")
        month_data = monthly_trend(df)
        st.pyplot(plot_monthly_trend(month_data))

    st.markdown("### 🔥 Spending Heatmap")
    st.pyplot(plot_heatmap(df))

    st.markdown("---")
    st.markdown("### 📋 Data Preview")

    st.dataframe(df, use_container_width=True)

    st.markdown("---")
    st.markdown("### 🧠 Insights")

    insights = generate_insights(df)
    for insight in insights:
        st.info(insight)


else:
    st.info("👆 Upload a CSV file to get started")