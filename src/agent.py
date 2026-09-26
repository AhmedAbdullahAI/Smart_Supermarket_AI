from src.data_loader import load_data, clean_data
from src.recommender import recommend_products


def run_agent():
    # Load and clean the supermarket data
    df = load_data()
    df = clean_data(df)

    # Generate product recommendations
    recommendations = recommend_products(df, top_n=3)

    print("=== SMART SUPERMARKET AI ===")
    print("\nTop 3 Recommended Products:")
    print(recommendations)


if __name__ == "__main__":
    run_agent()