# ==========================================
# Institutional Trade Engine
# File : strategy_cpr.py
# Version : 1.0
# ==========================================

def cpr_strategy(current_price, pivot, tc, bc):

    signal = "NO TRADE"
    confidence = 0

    try:

        # BUY
        if current_price > tc:

            signal = "BUY"
            confidence = 85

        # SELL
        elif current_price < bc:

            signal = "SELL"
            confidence = 85

    except Exception as e:

        print("CPR Strategy Error :", e)

    return {

        "signal": signal,

        "confidence": confidence

    }
