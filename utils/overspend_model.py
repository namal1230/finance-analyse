import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def prepare_dataset(df):
    df["day"] = pd.to_datetime(df["day"])

    monthly = df.groupby(df["day"].dt.to_period('M'))["amount"].sum()
    monthly = monthly.reset_index()
    monthly.columns = ["month", "amount"]

    monthly["prev"] = monthly["amount"].shift(1)
    monthly = monthly.dropna()

    monthly["overspend"] = (monthly["amount"] > monthly["prev"]).astype(int)

    return monthly

def train_model(monthly):
    x = monthly[["amount", "prev"]]
    y= monthly["overspend"]

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100)
    model.fit(x_train, y_train)

    return model

def predict_overspend(model, monthly):
    last = monthly.iloc[-1]

    input_data = np.array([last["amount"], last["prev"]])
    prediction = model.predict(input_data)[0]

    return prediction