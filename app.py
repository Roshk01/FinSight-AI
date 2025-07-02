import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import yfinance as yf


model = joblib.load("model_XGB.pkl")

st.title("Stock Price Predictor AI")
st.markdown("predict the next 7 days stock price of a company")

popular_tickers = [
    'NONE','AAPL', 'MSFT', 'AMZN', 'GOOG', 'META', 'TSLA', 'NFLX', 'NVDA',
    'INTC', 'JPM', 'V', 'MA', 'ADBE', 'BRK-B', 'PYPL'
]

select_ticker = st.selectbox("Select a popular stock ticker:", popular_tickers)
custom_ticker = st.text_input("Enter the stock ticker Manually (e.g., AAPL, MSFT):")

# final ticker selection
ticker = custom_ticker.strip().upper() if custom_ticker else select_ticker

if ticker:
    # data fetching
    ticker = yf.Ticker(ticker)
    data = ticker.history(period="2y", interval="1d")
    if data.empty:
        st.error(" ❌ No data found for the given ticker.")
    else:
        data.reset_index(inplace=True)
        data['days'] = np.arange(len(data))

        st.subheader(f"Stock Price Data for {ticker}")
        fig ,ax = plt.subplots(figsize=(10, 4))
        ax.plot(data['days'],data['Close'], label='Close Price')
        ax.set_title(f"{ticker} closing Price")
        ax.set_xlabel("Days")
        ax.set_ylabel("Price")
        st.pyplot(fig)

        #  predict next 7 days prince data
        x = data.drop(columns=['Close', 'Date'])
        last_row = x.iloc[-1]
        future_rows = []
        for i in range(7):
            row = last_row.copy()
            future_rows.append(row)
        future_x = pd.DataFrame(future_rows)
        predict_data = model.predict(future_rows)
        # Only get the prediction for the 7th day
        seventh_day_prediction = predict_data[-1]

        st.header("Predicted Stock Price for the 7th Day")
        st.write(f"Predicted Close Price (Day 7): {seventh_day_prediction:.2f}")

