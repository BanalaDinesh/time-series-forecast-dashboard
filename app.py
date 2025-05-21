
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(layout="wide")
st.title("📈 Time Series Forecast Dashboard")

st.markdown("### Upload your forecast data")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Data Preview:")
    st.dataframe(df.head())

    model_col = st.selectbox("Select Forecasting Model", df.columns[1:], index=0)
    date_col = df.columns[0]

    fig, ax = plt.subplots(figsize=(12, 5))
    sns.lineplot(x=df[date_col], y=df[model_col], label=model_col)
    plt.xticks(rotation=45)
    plt.title(f"Forecast using {model_col}")
    plt.xlabel("Date")
    plt.ylabel("Value")
    st.pyplot(fig)
else:
    st.info("Upload a CSV file with at least 2 columns: Date and Forecast Values")
