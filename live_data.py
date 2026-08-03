# ==========================================
# Institutional Trade Engine
# File : live_data.py
# ==========================================

import yfinance as yf


def get_live_price(symbol):

    try:

        ticker = yf.Ticker(symbol)

        df = ticker.history(
            period="1d",
            interval="1m"
        )

        if df.empty:
            return None

        last = df.iloc[-1]

        return {

            "open": round(float(last["Open"]), 2),

            "high": round(float(last["High"]), 2),

            "low": round(float(last["Low"]), 2),

            "close": round(float(last["Close"]), 2),

            "volume": int(last["Volume"])

        }

    except Exception as e:

        print("Live Data Error :", e)

        return None


def get_previous_day(symbol):

    try:

        ticker = yf.Ticker(symbol)

        df = ticker.history(period="5d")

        if len(df) < 2:
            return None

        prev = df.iloc[-2]

        return {

            "high": round(float(prev["High"]), 2),

            "low": round(float(prev["Low"]), 2),

            "close": round(float(prev["Close"]), 2)

        }

    except Exception as e:

        print("Previous Day Error :", e)

        return None
