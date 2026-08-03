# ==========================================
# Institutional Trade Engine
# File : multi_timeframe.py
# Version : 1.0
# ==========================================

import yfinance as yf


def get_trend(symbol, period, interval):

    try:

        df = yf.download(

            symbol,

            period=period,

            interval=interval,

            progress=False,

            auto_adjust=False

        )


        if len(df) < 50:

            return "NEUTRAL"


        ema20 = (
            df["Close"]
            .ewm(span=20)
            .mean()
        )


        ema50 = (
            df["Close"]
            .ewm(span=50)
            .mean()
        )


        if ema20.iloc[-1] > ema50.iloc[-1]:

            return "BUY"


        elif ema20.iloc[-1] < ema50.iloc[-1]:

            return "SELL"


        else:

            return "NEUTRAL"



    except Exception as e:

        print(
            "Trend Error:",
            e
        )

        return "NEUTRAL"



def multi_timeframe_analysis(symbol):


    daily = get_trend(

        symbol,

        "6mo",

        "1d"

    )


    hourly = get_trend(

        symbol,

        "60d",

        "1h"

    )


    fifteen = get_trend(

        symbol,

        "30d",

        "15m"

    )


    five = get_trend(

        symbol,

        "10d",

        "5m"

    )


    trends = [

        daily,

        hourly,

        fifteen,

        five

    ]


    buy = trends.count("BUY")

    sell = trends.count("SELL")


    if buy >= 3:

        signal = "BUY"

        confidence = 90


    elif sell >= 3:

        signal = "SELL"

        confidence = 90


    else:

        signal = "NEUTRAL"

        confidence = 50



    return {


        "signal": signal,


        "confidence": confidence,


        "daily": daily,


        "hourly": hourly,


        "15min": fifteen,


        "5min": five


    }
