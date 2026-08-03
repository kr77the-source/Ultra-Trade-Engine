# ==========================================
# Institutional Trade Engine
# File : indicators.py
# Version : 2.0
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

    except Exception:

        return None


def get_ema(symbol):

    try:

        df = yf.download(
            symbol,
            period="5d",
            interval="5m",
            progress=False,
            auto_adjust=False
        )

        if len(df) < 60:
            return None

        ema20 = df["Close"].ewm(span=20).mean()

        ema50 = df["Close"].ewm(span=50).mean()

        return {

            "ema20": round(float(ema20.iloc[-1]),2),

            "ema50": round(float(ema50.iloc[-1]),2)

        }

    except:

        return None
