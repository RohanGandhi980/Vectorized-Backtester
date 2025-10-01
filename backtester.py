import pandas as pd
import numpy as np
import math

class Backtester:
    def __init__(self, df: pd.DataFrame, initial_capital: float = 10000):
        self.df = df.copy()
        self.initial_capital = initial_capital
        self.equity_curve = None
        self.results = {}

    def run(self):
        # Ensure sorted by date
        self.df.sort_index(inplace=True)

        # Calculate daily returns
        self.df["Returns"] = self.df["Close"].pct_change().fillna(0)

        # Equity curve
        self.df["Equity_Curve"] = (1 + self.df["Returns"]).cumprod() * self.initial_capital
        self.equity_curve = self.df["Equity_Curve"]

        # Metrics
        sharpe = self._sharpe_ratio()
        max_dd = self._max_drawdown()
        final_equity = float(self.df["Equity_Curve"].iloc[-1]) if not self.df.empty else None

        #keeping nan values json safe
        def safe(val):
            if val is None:
                return None
            if isinstance(val, float) and (math.isnan(val) or math.isinf(val)):
                return None
            return val

        self.results = {
            "Final Equity": safe(final_equity),
            "Sharpe Ratio": safe(sharpe),
            "Max Drawdown": safe(max_dd)
        }
        return self.results

    def _sharpe_ratio(self, risk_free_rate=0.0):
        daily_ret = self.df["Returns"].mean()
        daily_vol = self.df["Returns"].std()
        if daily_vol == 0:
            return 0.0
        sharpe = (daily_ret - risk_free_rate/252) / daily_vol
        return round(sharpe * np.sqrt(252), 4)

    def _max_drawdown(self):
        cummax = self.df["Equity_Curve"].cummax()
        drawdown = self.df["Equity_Curve"] / cummax - 1
        return round(float(drawdown.min()), 4)
