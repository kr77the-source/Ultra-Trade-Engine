# ==========================================
# Institutional Trade Engine
# File : supertrend.py
# Version : 1.0
# ==========================================

import pandas as pd


def calculate_supertrend(df, period=10, multiplier=3):

    data = df.copy()

    data["H-L"] = data["High"] - data["Low"]

    data["H-PC"] = abs(data["High"] - data["Close"].shift())

    data["L-PC"] = abs(data["Low"] - data["Close"].shift())

    data["TR"] = data[["H-L", "H-PC", "L-PC"]].max(axis=1)

    data["ATR"] = data["TR"].rolling(period).mean()

    hl2 = (data["High"] + data["Low"]) / 2

    upperband = hl2 + (multiplier * data["ATR"])

    lowerband = hl2 - (multiplier * data["ATR"])

    supertrend = []

    direction = []

    for i in range(len(data)):

        if i == 0:

            supertrend.append(lowerband.iloc[i])

            direction.append("BUY")

            continue

        if data["Close"].iloc[i] > upperband.iloc[i-1]:

            direction.append("BUY")

            supertrend.append(lowerband.iloc[i])

        elif data["Close"].iloc[i] < lowerband.iloc[i-1]:

            direction.append("SELL")

            supertrend.append(upperband.iloc[i])

        else:

            direction.append(direction[-1])

            supertrend.append(supertrend[-1])

    data["SuperTrend"] = supertrend

    data["Direction"] = direction

    return {

        "signal": direction[-1],

        "value": round(float(supertrend[-1]),2)

    }
