from statsmodels.tsa.arima.model import ARIMA
from sklearn.cluster import KMeans
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def arima_forecasting(monthly):
    try:
        if len(monthly) < 3:
            return None

        model = ARIMA(monthly, order=(1, 1, 1))
        model_fit = model.fit()

        forecast = model_fit.forecast(steps=1)

        return forecast.iloc[0]

    except Exception as e:
        return f"Error: {e}"

def clustering(filtered_df):
    if len(filtered_df) < 3:
        return filtered_df

    df_copy = filtered_df.copy()

    cluster_data = df_copy[['amount']]

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

    df_copy["Cluster"] = kmeans.fit_predict(cluster_data)

    return df_copy

def classification_model(filtered_df):
    df_copy = filtered_df.copy()

    df_copy["Overspend"] = np.where(
        df_copy["amount"] > 3000, 1, 0
    )

    if df_copy["Overspend"].nunique() < 2:
        return None

    X = df_copy[['amount']]
    y = df_copy['Overspend']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, pred)

    return accuracy

def recommendation(filtered_df, outliers):
    messages = []

    avg_spending = filtered_df["amount"].mean()

    food_spending = filtered_df[
        filtered_df["category"] == "Food"
        ]["amount"].sum()

    entertainment_spending = filtered_df[
        filtered_df["category"] == "Entertainment"
        ]["amount"].sum()

    if entertainment_spending > food_spending:
        messages.append("Reduce entertainment spending.")

    if avg_spending > 2500:
        messages.append("Average spending is high.")

    if not outliers.empty:
        messages.append("Unusual transactions detected.")

    return messages
