import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import markers


def plot_monthly_trend(data):
    fig, ax = plt.subplots()
    data.plot(kind='line',marker="x",ax=ax)
    plt.title('Monthly Spending Trend')
    ax.set_xlabel("Month")
    ax.set_ylabel("Amount")
    return fig

def plot_category_spending(data):
    fig, ax = plt.subplots()
    sns.barplot(x=data.index,y=data.values,ax=ax)
    plt.title('Category Spending')
    return fig

def plot_heatmap(df):
    df["month"] = df["date"].dt.to_period("M")

    pivot = df.pivot_table(values="amount",index="category",columns="month",aggfunc="sum",fill_value=0)
    fig, ax = plt.subplots()
    sns.heatmap(pivot, cmap="coolwarm", ax=ax)
    return fig

def plot_distribution(df):
    fig, ax = plt.subplots()

    sns.histplot(
        df["amount"],
        bins=15,
        kde=True,
        ax=ax
    )

    ax.set_title("Distribution of Amount")
    return fig

def plot_outliers(df):
    fig, ax = plt.subplots()
    sns.boxplot(x=df["amount"],ax=ax)
    ax.set_title("Outliers")
    return fig

def correlation_heatmap(corr):
    fig, ax = plt.subplots(figsize=(8,5))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Matrix")
    return fig

def moving_avg(monthly,moving):
    fig, ax = plt.subplots()
    monthly.plot(ax=ax, label="Actual")
    moving.plot(ax=ax, label="Moving Average")
    ax.legend()
    return fig