# ==========================================
# Institutional Trade Engine
# File : strategy_vwap.py
# Version : 1.0
# ==========================================

def vwap_strategy(current, vwap):

    signal = "NO TRADE"
    confidence = 0

    try:

        # BUY
        if current["close"] > vwap:

            signal = "BUY"
            confidence = 85

        # SELL
        elif current["close"] < vwap:

            signal = "SELL"
            confidence = 85

    except Exception as e:

        print("VWAP Strategy Error :", e)

    return {

        "signal": signal,

        "confidence": confidence

    }
