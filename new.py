import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Time Series Forecasting Dashboard")

# ----- Replace these example datasets with your actual forecasts -----
# Example dates - adjust to your dataset dates
dates = pd.date_range(start='2020-01-01', periods=60)

# Example actual values - replace with your real test data
actual_values = pd.Series([100 + i*0.5 for i in range(50)], index=dates)

# Example forecasts - replace with your actual model forecast results (arrays or series)
arima_forecast = actual_values + 2  # replace with your ARIMA forecast values
prophet_forecast = actual_values + 1  # replace with your Prophet forecast values
lstm_forecast = actual_values + 3  # replace with your LSTM forecast values

# Plot the forecasts vs actual
st.subheader("Forecast Comparison")

fig, ax = plt.subplots(figsize=(10,5))
ax.plot(dates, actual_values, label='Actual', color='black', linewidth=2)
ax.plot(dates, arima_forecast, label='ARIMA Forecast', linestyle='--')
ax.plot(dates, prophet_forecast, label='Prophet Forecast', linestyle='--')
ax.plot(dates, lstm_forecast, label='LSTM Forecast', linestyle='--')
ax.set_xlabel("Date")
ax.set_ylabel("Value")
ax.legend()
st.pyplot(fig)

# Model selection dropdown
model_choice = st.selectbox("Select model for detailed metrics:", ["ARIMA", "Prophet", "LSTM"])

# Example metrics - replace with your actual performance numbers
metrics = {
    "ARIMA": {"MAE": 143.33064971751412, "RMSE": 175.60910936347028},
    "Prophet": {"MAE":  82.46, "RMSE": 135.29
},
    "LSTM": {"MAE": 18.663658920834067, "RMSE":  26.307071281734014}
}

st.write(f"### Performance metrics for {model_choice}")
st.write(f"MAE: {metrics[model_choice]['MAE']}")
st.write(f"RMSE: {metrics[model_choice]['RMSE']}")

# Add more sections or interactive widgets as you like!

