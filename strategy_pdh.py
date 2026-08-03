# ==========================================
# Institutional Trade Engine
# File : strategy_pdh.py
# Version : 1.0
# ==========================================

def pdh_strategy(current, previous, prev_day):

    """
    current  = Current Candle
    previous = Mother Candle
    prev_day = Previous Day High/Low

    Return:
        BUY
        SELL
        NO TRADE
    """

    signal = "NO TRADE"
    confidence = 0

    # -----------------------------
    # BUY SETUP
    # -----------------------------
    if (

        current["close"] > prev_day["high"]

        and previous["close"] > previous["open"]

        and current["close"] < current["open"]

        and current["high"] <= previous["high"]

        and current["low"] >= previous["low"]

        and current["volume"] < previous["volume"]

    ):

        signal = "BUY"

        confidence = 95

    # -----------------------------
    # SELL SETUP
    # -----------------------------
    elif (

        current["close"] < prev_day["low"]

        and previous["close"] < previous["open"]

        and current["close"] > current["open"]

        and current["high"] <= previous["high"]

        and current["low"] >= previous["low"]

        and current["volume"] < previous["volume"]

    ):

        signal = "SELL"

        confidence = 95

    return {

        "signal": signal,

        "confidence": confidence

    }
