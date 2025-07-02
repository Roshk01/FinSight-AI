import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import yfinance as yf

# Load the model
model = joblib.load("model_XGB.pkl")

# Page Config
st.set_page_config(page_title="Money Mind AI", page_icon="💸", layout="centered")

# Title and Intro
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💸 Money Mind AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #cdcfab;'> Real Time Market Price</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>A Smart Stock Price Predictor on 7th Days</h4>", unsafe_allow_html=True)
st.markdown("---")

# Ticker Input Section
st.markdown("### 🔍 Choose a Stock Ticker")
col1, col2 = st.columns([2, 3])

with col1:
    popular_tickers = ['NONE','AAPL', 'MSFT', 'AMZN', 'GOOG', 'META', 'TSLA', 'NFLX', 'NVDA', 'INTC', 'JPM', 'V', 'MA', 'ADBE', 'BRK-B', 'PYPL']
    select_ticker = st.selectbox("Popular Tickers", popular_tickers)

with col2:
    custom_ticker = st.text_input("Or enter manually (e.g., AAPL, TSLA)")

ticker = custom_ticker.strip().upper() if custom_ticker else select_ticker

# Processing the Ticker
if ticker and ticker != "NONE":
    try:
        stock = yf.Ticker(ticker)
        data = stock.history(period="2y", interval="1d")
        
        if data.empty:
            st.error("❌ No data found for the given ticker.")
        else:
            data.reset_index(inplace=True)
            data['days'] = np.arange(len(data))

            # Price Trend Plot
            st.markdown("### 📈 Historical Close Price")
            fig, ax = plt.subplots(figsize=(10, 4))
            ax.plot(data['days'], data['Close'], label='Close Price', color='#1f77b4')
            ax.set_xlabel("Days")
            ax.set_ylabel("Price ($)")
            ax.set_title(f"{ticker} Closing Price Over Time")
            ax.grid(True)
            ax.legend()
            st.pyplot(fig)

            # Prediction
            x = data.drop(columns=['Close', 'Date'])
            last_row = x.iloc[-1]
            future_rows = [last_row.copy() for _ in range(7)]
            future_x = pd.DataFrame(future_rows)

            predict_data = model.predict(future_x)
            day_7_price = predict_data[-1]

            # Prediction Display
            st.markdown("### 🧠 Predicted Close Price")
            st.success(f"📅 Predicted Price for Day 7: **${day_7_price:.2f}**")

    except Exception as e:
        st.error(f"⚠️ Error occurred while fetching data: {e}")
else:
    st.info("👆 Select a ticker or enter one manually to begin prediction.")
