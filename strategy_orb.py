# ==========================================
# Institutional Trade Engine
# File : strategy_orb.py
# Version : 1.0
# ==========================================

def orb_strategy(current, opening_high, opening_low):

    signal = "NO TRADE"
    confidence = 0

    try:

        # BUY
        if current["close"] > opening_high:

            signal = "BUY"
            confidence = 90

        # SELL
        elif current["close"] < opening_low:

            signal = "SELL"
            confidence = 90

    except Exception as e:

        print("ORB Strategy Error :", e)

    return {
        "signal": signal,
        "confidence": confidence
    }
