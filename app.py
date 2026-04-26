import streamlit as st
import pandas as pd

from utils.preprocess import load_daa
from utils.analysis import category_spending, monthly_trend, total_spending, average_spending, predict_next_month, \
     correlation_statistics, outlier_detection, monthly_growth, moving_average_growth
from utils.visualization import plot_category_spending, plot_monthly_trend, plot_heatmap, plot_distribution, plot_outliers, correlation_heatmap, moving_avg
from utils.ml_model import arima_forecasting, clustering, classification_model, recommendation

st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("💰 Finance Analyzer Dashboard")
st.markdown("Analyze your spending patterns with insights & predictions")

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])
# ===================================================================================================
# Data Preprocessing
if uploaded_file:
    try:
        df = load_daa(uploaded_file)
        st.dataframe(df, use_container_width=True)
    except Exception as e:
        st.error("Please provide a valid structure [date, category, amount, description]")
        exit()

# # ==========================================================================================================
# Filters

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
# ================================================================================================
#     Basic Analysis

    st.markdown("### 📊 Key Metrics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("💸 Total Spending", f"{total_spending(df)}")

    with col2:
        st.metric("📉 Average Spending", f"{average_spending(df)}")

    with col3:
        st.metric("📅 Predicted Next Month", f"{predict_next_month(df)}")

# ================================================================================================
#     Visual Analysis

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
#     Statistical Analysis

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

    clean_df, df_outliers = outlier_detection(df)

    if df_outliers.empty:
        st.info("✅ No outliers detected")
    else:
        st.dataframe(df_outliers, use_container_width=True)

    st.markdown("---")
    st.markdown("### 📈 Trend Analysis")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Growth Percentage")

        growth_df = monthly_growth(df)
        growth_df = growth_df.reset_index()
        growth_df.rename(columns={"date": "month"}, inplace=True)
        st.dataframe(growth_df, use_container_width=True)

    with col2:
        st.markdown("### Moving Average")
        growth, monthly = moving_average_growth(df)
        st.write(growth)

        st.pyplot(moving_avg(monthly,growth))

# ===================================================================
#     Apply Machine Learning - ARIMA | CLUSTERING  | CLASSIFICATION  | RECOMMENDATIONS

    st.markdown("---")
    st.markdown("### 🤖 Advanced Insights")

    growth, monthly = moving_average_growth(df)
    clean_df, df_outliers = outlier_detection(df)

    forecast = arima_forecasting(monthly)

    if forecast is not None and not isinstance(forecast, str):
        st.metric("🔮 Next Month Prediction", f"{forecast:.2f}")
    else:
        st.warning("Not enough data for forecasting")

    clustered_df = clustering(df)
    st.subheader("🧠 Clustering Result")
    st.dataframe(clustered_df, use_container_width=True)

    accuracy = classification_model(df)
    if accuracy is not None:
        st.metric("🎯 Model Accuracy", f"{accuracy:.2f}")
    else:
        st.warning("Not enough variation for classification")

    messages = recommendation(df, df_outliers)
    st.subheader("💡 Smart Recommendations")
    if not messages:
        st.success("All spending looks balanced 👍")
    else:
        for msg in messages:
            st.warning(msg)

else:
    st.info("👆 Upload a CSV file to get started")