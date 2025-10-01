import pandas as pd

def sma_crossover(df: pd.DataFrame, short_window=20, long_window=50):
    if len(df) < long_window:
        df["Signal"] = 0
        df["Position"] = 0
        df["Note"] = "Not enough data for SMA strategy"
        return df

    df["SMA_Short"] = df["Close"].rolling(window=short_window, min_periods=1).mean()
    df["SMA_Long"] = df["Close"].rolling(window=long_window, min_periods=1).mean()
    df["Signal"] = 0
    df.loc[df["SMA_Short"] > df["SMA_Long"], "Signal"] = 1
    df.loc[df["SMA_Short"] < df["SMA_Long"], "Signal"] = -1
    df["Position"] = df["Signal"].shift(1).fillna(0)

    return df
