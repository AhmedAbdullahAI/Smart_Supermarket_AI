import pandas as pd


def get_product_sales(df):
    """
    Calculate total sales for each product line.
    """
    sales = (
        df.groupby("Product line")["Total"]
        .sum()
        .sort_values(ascending=False)
    )

    return sales


def recommend_products(df, top_n=3):
    """
    Recommend the top-selling products.
    """
    sales = get_product_sales(df)

    return sales.head(top_n)