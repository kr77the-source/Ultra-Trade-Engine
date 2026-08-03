# ==========================================
# Institutional Trade Engine
# File : strategy_ema.py
# Version : 1.0
# ==========================================

def ema_strategy(current_price, ema20, ema50):

    signal = "NO TRADE"
    confidence = 0

    try:

        # Strong Up Trend
        if current_price > ema20 and ema20 > ema50:

            signal = "BUY"
            confidence = 90

        # Strong Down Trend
        elif current_price < ema20 and ema20 < ema50:

            signal = "SELL"
            confidence = 90

    except Exception as e:

        print("EMA Strategy Error :", e)

    return {

        "signal": signal,

        "confidence": confidence

    }
