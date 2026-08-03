# ==========================================
# Institutional Trade Engine
# File : atr.py
# Version : 1.0
# ==========================================

import yfinance as yf


def calculate_atr(
    symbol,
    period=14
):

    try:

        df = yf.download(
            symbol,
            period="10d",
            interval="15m",
            progress=False,
            auto_adjust=False
        )

        if len(df) < period:

            return None


        high = df["High"]

        low = df["Low"]

        close = df["Close"]


        previous_close = close.shift(1)


        tr1 = high - low

        tr2 = abs(high - previous_close)

        tr3 = abs(low - previous_close)


        true_range = tr1.combine(
            tr2,
            max
        ).combine(
            tr3,
            max
        )


        atr = true_range.rolling(
            period
        ).mean()


        return round(
            float(atr.iloc[-1]),
            2
        )


    except Exception as e:

        print(
            "ATR Error:",
            e
        )

        return None



def create_levels(
    entry,
    atr,
    risk_multiplier=1.5,
    reward_multiplier=3
):

    if atr is None:

        return None


    stop_loss = round(
        entry - (atr * risk_multiplier),
        2
    )


    target = round(
        entry + (atr * reward_multiplier),
        2
    )


    return {

        "entry": entry,

        "stop_loss": stop_loss,

        "target": target,

        "risk_reward": "1:2"

    }
