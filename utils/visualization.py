import matplotlib.pyplot as plt
import seaborn as sns

def plot_monthly_trend(data):
    fig, ax = plt.subplots()
    data.plot(kind='line',ax=ax)
    plt.title('Monthly Spending Trend')
    return fig

def plot_category_spending(data):
    fig, ax = plt.subplots()
    sns.barplot(x=data.index,y=data.values,ax=ax)
    plt.title('Category Spending')
    return fig

def plot_heatmap(df):
    pivot = df.pivot_table(values="amount",index="day",columns="month",aggfunc="sum")
    fig, ax = plt.subplots()
    sns.heatmap(pivot, cmap="coolwarm", ax=ax)
    return fig