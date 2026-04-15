import pandas as pd

def load_daa(file):
    df = pd.read_csv(file)

    # Clean column names
    df.columns = df.columns.str.strip().str.lower()

    # Debug (shows in terminal)
    print("Columns:", df.columns.tolist())

    # Flexible date handling
    if "data" in df.columns:
        df.rename(columns={"data": "date"}, inplace=True)

    if "date" not in df.columns:
        raise ValueError(f"No 'date' column found. Columns: {df.columns.tolist()}")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    df = df.dropna()
    df = df.drop_duplicates()

    df["month"] = df["date"].dt.to_period("M")
    df["day"] = df["date"].dt.day_name()

    return df