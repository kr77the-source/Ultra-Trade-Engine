# ==========================================
# Institutional Trade Engine
# File : smart_money.py
# Version : 1.0
# ==========================================

import yfinance as yf


def detect_smart_money(
    symbol,
    period="10d",
    interval="15m"
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


        avg_volume = (
            df["Volume"]
            .rolling(20)
            .mean()
        )


        latest = df.iloc[-1]


        current_volume = float(
            latest["Volume"]
        )


        average = float(
            avg_volume.iloc[-1]
        )


        volume_ratio = round(
            current_volume / average,
            2
        )


        candle_change = (

            float(latest["Close"])
            -
            float(latest["Open"])

        )


        signal = "NEUTRAL"

        confidence = 0


        # Institutional Buying

        if (
            volume_ratio >= 2
            and candle_change > 0
        ):

            signal = "BUY"

            confidence = 90


        # Institutional Selling

        elif (
            volume_ratio >= 2
            and candle_change < 0
        ):

            signal = "SELL"

            confidence = 90



        # Normal Activity

        else:

            confidence = 50



        return {

            "signal": signal,

            "confidence": confidence,

            "volume_ratio": volume_ratio,

            "current_volume": current_volume,

            "average_volume": average

        }


    except Exception as e:

        print(
            "Smart Money Error:",
            e
        )

        return None
