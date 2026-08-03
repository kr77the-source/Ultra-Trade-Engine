# ==========================================
# Institutional Trade Engine
# File : indicators.py
# Version : 1.0
# ==========================================

import yfinance as yf


def get_vwap(symbol):

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

        tp = (df["High"] + df["Low"] + df["Close"]) / 3

        volume = df["Volume"]

        vwap = (tp * volume).cumsum() / volume.cumsum()

        return round(float(vwap.iloc[-1]), 2)

    except Exception as e:

        print("VWAP Error :", e)

        return None
