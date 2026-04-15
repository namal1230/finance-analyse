import pandas as pd
import streamlit as st
from utils.preprocess import load_daa

st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("💰 Finance Analyzer Dashboard")
st.markdown("Analyze your spending patterns with insights & predictions")

uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])

if uploaded_file:

    df = load_daa(uploaded_file)

else:
    st.info("👆 Upload a CSV file to get started")