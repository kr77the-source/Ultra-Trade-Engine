# ==========================================
# Institutional Trade Engine
# File : indicators.py
# Version : 3.0
# ==========================================

import yfinance as yf


def download_data(symbol, period="5d", interval="5m"):

    try:

        df = yf.download(
            symbol,
            period=period,
            interval=interval,
            progress=False,
            auto_adjust=False
        )

        if df.empty:
            return None

        return df

    except:
        return None


def get_vwap(symbol):

    df = download_data(symbol, "1d", "5m")

    if df is None:
        return None

    tp = (df["High"] + df["Low"] + df["Close"]) / 3

    volume = df["Volume"]

    vwap = (tp * volume).cumsum() / volume.cumsum()

    return round(float(vwap.iloc[-1]), 2)


def get_ema(symbol):

    df = download_data(symbol)

    if df is None:
        return None

    ema20 = df["Close"].ewm(span=20).mean()

    ema50 = df["Close"].ewm(span=50).mean()

    return {

        "ema20": round(float(ema20.iloc[-1]), 2),

        "ema50": round(float(ema50.iloc[-1]), 2)

    }


def get_cpr(symbol):

    df = download_data(symbol, "5d", "1d")

    if df is None:
        return None

    prev = df.iloc[-2]

    high = float(prev["High"])
    low = float(prev["Low"])
    close = float(prev["Close"])

    pivot = (high + low + close) / 3

    bc = (high + low) / 2

    tc = (pivot - bc) + pivot

    return {

        "pivot": round(pivot, 2),

        "tc": round(tc, 2),

        "bc": round(bc, 2)

    }
