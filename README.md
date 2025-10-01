**Vectorized Backtester**
-

A backtesting framewwork powered by FastAPI for Indian stock market data
It fetches OHLCV data from **Yahoo Finance** (`yfinance` + `yahooquery`), runs a **vectorized buy and hold backtest**, and generates performance metrics like **Final Equity, Sharpe Ratio, and Max Drawdown**, along with optional equity curve plots.

**Features**
- Data fetching via Yahoofinance
- Vectorized Backtesting
- Supports NSE tickers like RELIANCE.NS, ONGC.NS, TCS.NS and many more
- Includes key metric components like Sharpe Ratio, Equity Curve and Max Drawdown

**Installation**
- 
- git clone https://github.com/RohanGandhi980/Vectorized-Backtester.git
- cd Vectorized-Backtester
- pip install -r requirements.txt
- uvicorn main:app --reload
- Repo will be live at: http://127.0.0.1:8000/docs


**Example Usage**
-

GET /backtest/json?ticker=ICICIBANK.NS&start=2015-01-01&end=2025-01-01

**Response**

{

  "ticker": "ICICIBANK.NS",
  
  "metrics": {
  
    "Final Equity": 40423.36,
    "Sharpe Ratio": 0.61,
    "Max Drawdown": -0.5235
  }
}
