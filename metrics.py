import pandas as pd
import numpy as np

def sharpe_ratio(df: pd.DataFrame, risk_free_rate=0.0):
    if "Strategy_Returns" not in df.columns or df["Strategy_Returns"].empty:
        return None
    returns = df["Strategy_Returns"].dropna()
    if returns.std() == 0:
        return None
    return (returns.mean() - risk_free_rate) / returns.std()

def max_drawdown(df: pd.DataFrame):
    if "Equity_Curve" not in df.columns or df["Equity_Curve"].empty:
        return None
    cummax = df["Equity_Curve"].cummax()
    drawdown = (df["Equity_Curve"] - cummax) / cummax
    return float(drawdown.min()) if not drawdown.empty else None

#this file records the sharpe ratio and max drawdown functiomn
#performs a simple vetorized backtest

    

