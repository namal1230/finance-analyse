import pandas as pd

def load_daa(file):
    df = pd.read_csv(file)

    if len(df.columns) != 2:
        raise Exception("Please provide 4 columns")

    if len(df.columns) == 2:
        df = df.iloc[:, 0].str.split(",", expand=True)
        df.columns = ["date", "category", "amount", "description"]

    df.columns = df.columns.str.lower().str.strip()

    if "date" not in df.columns:
        date_cols = df.filter(regex="date|day|time", axis=1).columns

        if len(date_cols) > 0:
            df = df.rename(columns={date_cols[0]: "date"})
        else:
            print("No date column found")

    if "category" not in df.columns:
        cat_cols = df.filter(regex="category|type", axis=1).columns

        if len(cat_cols) > 0:
            df = df.rename(columns={cat_cols[0]: "category"})
        else:
            print("No category column found")

    if "amount" not in df.columns:
        amount_cols = df.filter(regex="amount", axis=1).columns

        if len(amount_cols) > 0:
            df = df.rename(columns={amount_cols[0]: "amount"})
            df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
        else:
            print("No amount column found")

    if "description" not in df.columns:
        description_cols = df.filter(regex="description|info", axis=1).columns

        if len(description_cols) > 0:
            df = df.rename(columns={description_cols[0]: "description"})
        else:
            print("No description column found")

    if "amount" in df.columns:
        df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    print(df.head())

    df = df.dropna()
    df = df.drop_duplicates()

    return df