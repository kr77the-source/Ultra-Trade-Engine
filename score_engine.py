# ==========================================
# Institutional Trade Engine
# File : score_engine.py
# Version : 1.0
# ==========================================

def calculate_score(
    pdh,
    orb,
    vwap,
    ema,
    cpr
):

    buy_score = 0
    sell_score = 0

    # -------------------------
    # PDH Strategy
    # -------------------------

    if pdh["signal"] == "BUY":
        buy_score += 25

    elif pdh["signal"] == "SELL":
        sell_score += 25

    # -------------------------
    # ORB Strategy
    # -------------------------

    if orb["signal"] == "BUY":
        buy_score += 20

    elif orb["signal"] == "SELL":
        sell_score += 20

    # -------------------------
    # VWAP Strategy
    # -------------------------

    if vwap["signal"] == "BUY":
        buy_score += 20

    elif vwap["signal"] == "SELL":
        sell_score += 20

    # -------------------------
    # EMA Strategy
    # -------------------------

    if ema["signal"] == "BUY":
        buy_score += 20

    elif ema["signal"] == "SELL":
        sell_score += 20

    # -------------------------
    # CPR Strategy
    # -------------------------

    if cpr["signal"] == "BUY":
        buy_score += 15

    elif cpr["signal"] == "SELL":
        sell_score += 15

    # -------------------------
    # Final Decision
    # -------------------------

    signal = "NO TRADE"
    confidence = 0

    if buy_score >= 80:

        signal = "BUY"
        confidence = buy_score

    elif sell_score >= 80:

        signal = "SELL"
        confidence = sell_score

    return {

        "signal": signal,

        "confidence": confidence,

        "buy_score": buy_score,

        "sell_score": sell_score

    }
