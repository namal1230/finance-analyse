from sklearn.linear_model import LinearRegression
import numpy as np

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
