import pandas as pd


def load_data():
    df = pd.read_csv("data/supermarket_sales.csv")
    return df


def clean_data(df):
    df = df.copy()

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"])

    return df