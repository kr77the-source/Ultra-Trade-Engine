# ==========================================
# Institutional Trade Engine
# File : live_data.py
# Version : 2.0
# ==========================================

import yfinance as yf


def get_live_price(symbol):

    try:

        df = yf.download(
            symbol,
            period="1d",
            interval="5m",
            progress=False,
            auto_adjust=False
        )

        if df.empty:
            return None


        last = df.iloc[-1]


        return {

            "open": float(last["Open"]),

            "high": float(last["High"]),

            "low": float(last["Low"]),

            "close": float(last["Close"]),

            "volume": float(last["Volume"])

        }


    except Exception as e:

        print("Live Price Error:", e)

        return None



def get_candles(symbol):

    try:

        df = yf.download(

            symbol,

            period="30d",

            interval="15m",

            progress=False,

            auto_adjust=False

        )


        if df.empty:

            return None


        return df



    except Exception as e:

        print("Candle Error:", e)

        return None



def get_previous_day(symbol):

    try:

        df = yf.download(

            symbol,

            period="5d",

            interval="1d",

            progress=False,

            auto_adjust=False

        )


        if len(df) < 2:

            return None


        prev = df.iloc[-2]


        return {

            "high": float(prev["High"]),

            "low": float(prev["Low"]),

            "close": float(prev["Close"])

        }


    except Exception as e:

        print("Previous Day Error:", e)

        return None
