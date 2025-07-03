import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib
import yfinance as yf

# Load the model
model = joblib.load("model_LR.pkl")

# Page Config
st.set_page_config(page_title="Money Mind AI", page_icon="💸", layout="centered")

# Title and Intro
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>💸 Money Mind AI</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #cdcfab;'> Real Time Market Price</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: gray;'>A Smart Stock Price Predictor on 30-Day Intervals</h4>", unsafe_allow_html=True)
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
            future_rows = []
            predicted_prices = []
            day_counter = last_row['days']
            for i in range(365):
                last_row['days'] += 1
                if i % 30 == 0:
                    future_rows.append(last_row.copy())
            
            future_x = pd.DataFrame(future_rows)
            predict_data = model.predict(future_x)
            future_df = pd.DataFrame({
                'Day': [f"Month {i+1}" for i in range(len(predict_data))],
                'Predicted Close Price': predict_data.round(2)
            })

            # 🎯 Prediction Display
            st.markdown("## 📊 Monthly Stock Price Prediction")
            st.markdown("---")

            # Create columns for icon/label and text
            col1, col2 = st.columns([1, 6])

            with col1:
                st.markdown("### ✨ Result")

            with col2:
                st.markdown("""
                    <div style='
                        background-color:#f0f2f6;
                        padding: 15px;
                        border-radius: 10px;
                        font-size: 16px;
                        color: #333;
                        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                    '>
                        📅 <b>Forecasted stock prices with ~30-Day intervals.</b>
                    </div>
                """, unsafe_allow_html=True)

            # Display styled dataframe below
            st.dataframe(future_df.round(2), use_container_width=True)

    except Exception as e:
        st.error(f"⚠️ Error occurred while fetching data: {e}")
    else:
        st.info("👆 Select a ticker or enter one manually to begin prediction.")
