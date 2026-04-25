import numpy as np
from pandas.core._numba.kernels import mean_
import scipy.stats as st

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
    df["zscore"]=st.zscore(df["amount"])

    outliers = df[abs(df["zscore"])>3]

    return outliers

def generate_insights(df):
    insights = []

    total = df["amount"].sum()
    food = df[df['category']=="food"]["amount"].sum()

    if food/total > 0.3:
        insights.append("High spending on Food (>30%)")

    weekend = df[df['day'].isin(['saturday','sunday'])]["amount"].sum()

    weeekday = df[~df['day'].isin(['saturday','sunday'])]["amount"].sum()

    if weekend>weeekday:
        insights.append("You spend more on weekends")

    return insights
