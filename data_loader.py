import pandas as pd

# yahooquery
try:
    from yahooquery import Ticker as YQTicker
except ImportError:
    YQTicker = None

# yfinance fallback
try:
    import yfinance as yf
except ImportError:
    yf = None


def get_data(ticker: str, start="2015-01-01", end="2025-01-01"):
    # yahooquery
    if YQTicker:
        try:
            print(f"Trying yahooquery for {ticker}...")
            yq_symbol = ticker if ticker.endswith(".NS") or ticker.endswith(".BO") else f"{ticker}.NS"
            yq = YQTicker(yq_symbol)
            df = yq.history(start=start, end=end)

            if not df.empty:
                if isinstance(df.index, pd.MultiIndex):
                    df.reset_index(inplace=True)
                    df.set_index("date", inplace=True)

                df.rename(columns={
                    "open": "Open",
                    "high": "High",
                    "low": "Low",
                    "close": "Close",
                    "adjclose": "Adj Close",
                    "volume": "Volume"
                }, inplace=True)

                df = df[["Open", "High", "Low", "Close", "Adj Close", "Volume"]]
                df.dropna(inplace=True)
                print(f"Data loaded from yahooquery for {yq_symbol}")
                return df
        except Exception as e:
            print(f"yahooquery failed for {ticker}: {e}")

    #yfinance
    if yf:
        try:
            print(f"Trying yfinance for {ticker}...")
            yf_symbol = ticker if (ticker.endswith(".NS") or ticker.endswith(".BO")) else f"{ticker}.NS"
            df = yf.download(yf_symbol, start=start, end=end, progress=False, timeout=30)

            if df is not None and not df.empty:
                df = df[['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']]
                df.dropna(inplace=True)
                print(f"✅ Data loaded from yfinance for {yf_symbol}")
                return df
        except Exception as e:
            print(f"yfinance failed for {ticker}: {e}")

    raise ValueError(f"No data available for {ticker} from yahooquery or yfinance.")
