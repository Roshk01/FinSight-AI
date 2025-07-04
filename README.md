<h1 align="center">📈 Money Mind AI</h1>
<p align="center"><em>Empowering Smarter Investments with AI-Driven Insights</em></p>

<p align="center">
  <a href="https://github.com/Roshk01/Money_mind_AI">
    <img src="https://img.shields.io/badge/last%20commit-today-blue" alt="last commit">
  </a>
  <img src="https://img.shields.io/github/languages/count/Roshk01/FinSight-AI" alt="language count">
  <img src="https://img.shields.io/badge/jupyter%20notebook-98.2%25-blue" alt="notebook">
  <img src="https://img.shields.io/badge/Python-1.8%25-blue" alt="Python">
</p>


---

## 💡 Overview

**Money Mind AI** is an AI-powered stock price prediction tool that forecasts the **stock's closing price on every 30-day interval** using real-time financial data. Built with XGBoost, Linear Regression, and deployed via Streamlit, this tool helps users make informed investment decisions.

---

## 🔍 Key Features

- 📊 Real-time data using `yfinance`
- 📈 Predicts the **stock price on every 30-day interval**
- ✅ Interactive UI with Streamlit
- 📦 Clean and modular code
- 📉 Model evaluation metrics for performance validation

---

## 📊 Model Evaluation

| Metric               | XGBOOST   | Linear Regression  |
|----------------------|---------|------------|
| 🧮 Mean Squared Error (MSE)  | **10.02**  | **2.95**  |
| 📉 Mean Absolute Error (MAE) | **2.27**   | **1.25**  |
| 🎯 R² Score                  | **0.96**   | **0.99**  |

> ⚠️ Note: The model predicts **only** the stock’s closing price for the 30th future day interval based on past trends, not all days individually.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/Numpy-013243?logo=numpy&logoColor=white)
![scikit-learn](https://img.shields.io/badge/Scikit--Learn-F7931E?logo=scikit-learn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-EC6C00?logo=xgboost&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![yfinance](https://img.shields.io/badge/yfinance-0A66C2?logo=chart&logoColor=white)
![yfinance](https://img.shields.io/badge/Linear--Regression-632d91?logo=chart&logoColor=white)

---

## 🚀 Run Locally

```bash
git clone https://github.com/Roshk01/Money_mind_AI.git
cd Money_mind_AI
pip install -r requirements.txt
streamlit run app.py
```


📝 License
Licensed under MIT.

🔮 Future Improvements
Add sentiment analysis using financial news

Include LSTM-based deep learning models

Email alerts for price thresholds
