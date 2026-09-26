import streamlit as st

from src.data_loader import load_data, clean_data
from src.recommender import recommend_products


# Load and clean data
df = clean_data(load_data())


# App title
st.title("🛒 Smart Supermarket AI")

st.write("Welcome to the Smart Supermarket AI Recommendation System.")


# Show recommendations
st.subheader("🔥 Top Recommended Products")

recommendations = recommend_products(df, top_n=3)

st.dataframe(recommendations)