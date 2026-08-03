# ==========================================
# Institutional Trade Engine
# File : volume_profile.py
# Version : 1.0
# ==========================================

import yfinance as yf


def get_volume_profile(
    symbol,
    period="5d",
    interval="15m",
    bins=20
):

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


        price = df["Close"]

        volume = df["Volume"]


        min_price = float(price.min())

        max_price = float(price.max())


        levels = []


        step = (
            max_price - min_price
        ) / bins


        for i in range(bins):

            low = min_price + (step * i)

            high = low + step


            mask = (
                (price >= low)
                &
                (price < high)
            )


            vol = volume[mask].sum()


            levels.append({

                "low": round(low,2),

                "high": round(high,2),

                "volume": int(vol)

            })


        levels.sort(

            key=lambda x: x["volume"],

            reverse=True

        )


        high_volume_node = levels[0]


        current_price = float(
            price.iloc[-1]
        )


        if current_price > high_volume_node["high"]:

            signal = "BUY"


        elif current_price < high_volume_node["low"]:

            signal = "SELL"


        else:

            signal = "NEUTRAL"


        return {

            "signal": signal,

            "current_price": round(current_price,2),

            "high_volume_node": high_volume_node,

            "levels": levels

        }


    except Exception as e:

        print(
            "Volume Profile Error:",
            e
        )

        return None
