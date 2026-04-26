import numpy as np
import scipy.stats as stats
import pandas as pd

def total_spending(df):
    return np.sum(df["amount"])

def category_spending(df):
    return df.groupby("category")["amount"].sum()

def monthly_trend(df):
    return df.groupby(df["date"].dt.to_period("M"))["amount"].sum()

def average_spending(df):
    return np.mean(df["amount"])

def predict_next_month(df):
    monthly = monthly_trend(df)
    return monthly.mean()

def correlation_statistics(df):
    monthly =  df.groupby(df["date"].dt.to_period("M")).agg({
        "amount": ["sum","mean","max","count"]
    })

    monthly.columns = [
        'Total Spending',
        'Average Spending',
        'Max Spending',
        'TransactionCount'
    ]

    monthly = monthly.reset_index()
    return monthly

def outlier_detection(df):
    df_copy = df.copy()
    df_copy["zscore"] = stats.zscore(df_copy["amount"])

    outliers = df_copy[abs(df_copy["zscore"]) > 3]
    clean = df_copy[abs(df_copy["zscore"]) <= 3]

    return clean, outliers

def monthly_growth(df):
    df = df.copy()

    df["date"] = pd.to_datetime(df["date"])

    numeric_cols = df.select_dtypes(include="number").columns
    monthly = (
            df.groupby(df["date"].dt.to_period("M"))[numeric_cols]
            .sum()
    )
    growth = monthly.pct_change() * 100
    return growth

def moving_average_growth(df):
    df = df.copy()
    df["date"] = pd.to_datetime(df["date"])
    monthly = df.groupby(df["date"].dt.to_period("M"))['amount'].sum()
    growth = monthly.rolling(2).mean()
    return growth, monthly
