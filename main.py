from fastapi import FastAPI, Query, HTTPException
from fastapi.responses import JSONResponse
from data_loader import get_data
from backtester import Backtester
from visualizer import plot_equity_curve

app = FastAPI(title="Backtesting Framework for Indian Stock Market")

@app.get("/backtest/json")
def backtest_json(
    ticker: str = Query(..., description="Stock ticker, e.g., RELIANCE.NS, INFY.NS, TCS.NS"),
    start: str = Query("2015-01-01"),
    end: str = Query("2025-01-01")
):
    try:
        df = get_data(ticker, start=start, end=end)

        if df is None or df.empty:
            raise HTTPException(status_code=404, detail=f"No data available for {ticker}")

        # Run backtester
        bt = Backtester(df)
        results = bt.run()

        return JSONResponse(content={
            "ticker": ticker,
            "metrics": results
        })

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/backtest/graph")
def backtest_graph(
    ticker: str = Query(..., description="Stock ticker, e.g., RELIANCE, INFY, TCS"),
    start: str = Query("2015-01-01"),
    end: str = Query("2025-01-01")
):
    try:
        df = get_data(ticker, start=start, end=end)

        if df is None or df.empty:
            raise HTTPException(status_code=404, detail=f"No data available for {ticker}")

        # Run backtester
        bt = Backtester(df)
        results = bt.run()
        equity_curve_b64 = plot_equity_curve(bt.equity_curve)

        return JSONResponse(content={
            "ticker": ticker,
            "metrics": results,
            "equity_curve_base64": equity_curve_b64
        })

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
