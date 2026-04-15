import numpy as np

def total_spending(df):
    return np.sum(df["amount"])

def category_spending(df):
    return df.groupby("category")["amount"].sum()

def monthly_trend(df):
    return df.groupby("month")["amount"].sum()

def average_spending(df):
    return np.mean(df["amount"])

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

def predict_next_month(df):
    monthly = df.groupby("month")["amount"].sum()
    return monthly.mean()