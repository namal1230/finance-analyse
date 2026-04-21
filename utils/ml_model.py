from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans

from app import month_data


def predict_spending(df):
    df = df.copy()
    df['MonthIndex'] = range(len(df))

    x= np.array(df['MonthIndex']).reshape(-1,1)
    y=df["Amount"].values

    model = LinearRegression()
    model.fit(x,y)

    next_month=np.array([[len(df)]])
    prediction = model.predict(next_month)

    return prediction[0]

def detect_anomalies(df):
    model = IsolationForest(contamination=0.1)
    df['anomaly'] = model.fit_predict(df[['Amount']])
    anomalies = df[df["anomaly"] == -1]
    return anomalies

def cluster_spending(df):
    model = KMeans(n_clusters=3)
    df['cluster'] = model.fit_predict(df[['Amount']])
    return df