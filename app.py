import numpy as np
import pandas as pd
import streamlit as st

from utils.analysis import category_spending, monthly_trend, total_spending, average_spending, predict_next_month, \
    generate_insights, correlation_statistics, outlier_detection
from utils.preprocess import load_daa
from utils.visualization import plot_category_spending, plot_monthly_trend, plot_heatmap, plot_distribution, plot_outliers, correlation_heatmap
from utils.ml_model import predict_spending, detect_anomalies, cluster_spending
from utils.overspend_model import prepare_dataset, train_model, predict_overspend
st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("💰 Finance Analyzer Dashboard")
st.markdown("Analyze your spending patterns with insights & predictions")

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file:
    try:
        df = load_daa(uploaded_file)
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error("Please provide a valid structure [date, category, amount, description]")
        exit()

#     st.sidebar.header("🔍 Filters")
# # ==========================================================================================================
#     categories = df["category"].unique()
#     selected_category = st.sidebar.selectbox(
#         "Select Category",
#         ["All"] + list(categories)
#     )
#
#     if selected_category != "All":
#         df = df[df["category"] == selected_category]
#
#     df["date"] = pd.to_datetime(df["date"])
#     min_date = df["date"].min()
#     max_date = df["date"].max()
#
#     date_range = st.sidebar.date_input(
#         "📅 Date Range",
#         [min_date, max_date]
#     )
#
#     if len(date_range) == 2:
#         start_date, end_date = date_range
#         df = df[
#             (df["date"] >= pd.to_datetime(start_date)) &
#             (df["date"] <= pd.to_datetime(end_date))
#             ]

    st.markdown("### 📊 Key Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💸 Total Spending", f"{total_spending(df)}")

    with col2:
        st.metric("📉 Average Spending", f"{average_spending(df)}")

    with col3:
        st.metric("📅 Predicted Next Month", f"{predict_next_month(df)}")

# ================================================================================================
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

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### 🔥 Spending Heatmap")
        st.pyplot(plot_heatmap(df))
    with col2:
        st.markdown("### Distribution of Amount")
        st.pyplot(plot_distribution(df))

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### Outliers")
        st.pyplot(plot_outliers(df))

# ===============================================================================
    st.markdown("---")
    st.markdown("### 📈 Statistical Analysis")

    st.write(f"Mean Spending: {df["amount"].mean(): .2f}")
    st.write(f"Median Spending: {df["amount"].median(): .2f}")
    st.write(f"Standard Deviation: {df["amount"].std(): .2f}")
    st.write(f"Variance: {df["amount"].var(): .2f}")

    st.write("Correlation")
    df_co = correlation_statistics(df)
    st.dataframe(df_co, use_container_width=True)

    corr = df_co.corr(numeric_only=True)
    
    st.write("Correlation Matrix")
    st.dataframe(corr)

    st.pyplot(correlation_heatmap(corr))

    st.write(f"Outliers: {outlier_detection(df)}")
    insights = generate_insights(df)
    for insight in insights:
        st.info(insight)

    # st.subheader("AI Prediction")
    #
    # prediction = predict_spending(df)
    # st.write(f"Next Spending Prediction: {prediction: .2f}")
    #
    # st.subheader("Anomaly Detected")
    # anomaly = detect_anomalies(df)
    #
    # if not anomaly.empty:
    #     st.write(anomaly)
    # else:
    #     st.success("No usual spending detected")
    #
    # st.subheader("Spending clusters")
    # df_clustered = cluster_spending(df)
    # st.write(df_clustered[['amount','cluster']])
    #
    # st.subheader("Overspending Prediction")
    # monthly = prepare_dataset(df)
    # model = train_model(monthly)
    #
    # if model is None:
    #     st.warning("Not enough data to train model")
    # else:
    #     pred = predict_overspend(model, monthly)
else:
    st.info("👆 Upload a CSV file to get started")