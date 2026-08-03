# ==========================================
# Institutional Trade Engine
# live_data.py
# ==========================================

import yfinance as yf


def get_live_price(symbol):

    try:

        ticker = yf.Ticker(symbol)

        df = ticker.history(period="1d", interval="1m")

        if df.empty:
            return None

        last = df.iloc[-1]

        return {
            "open": round(last["Open"], 2),
            "high": round(last["High"], 2),
            "low": round(last["Low"], 2),
            "close": round(last["Close"], 2),
            "volume": int(last["Volume"])
        }

    except Exception as e:

        print(e)

        return None
