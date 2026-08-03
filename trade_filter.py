# ==========================================
# Institutional Trade Engine
# File : trade_filter.py
# Version : 1.0
# ==========================================


def validate_trade(
    strategy_signal,
    strategy_confidence,
    global_signal,
    sector_signal,
    breadth_signal,
    option_signal,
    news_allowed
):

    reasons = []

    score = strategy_confidence

    # -----------------------------
    # News Filter
    # -----------------------------
    if not news_allowed:

        return {

            "allow": False,

            "signal": "NO TRADE",

            "confidence": 0,

            "reasons": ["High Impact News"]

        }

    # -----------------------------
    # Global Market
    # -----------------------------
    if global_signal == strategy_signal:

        score += 10
        reasons.append("Global Market Confirmed")

    else:

        score -= 10

    # -----------------------------
    # Sector Strength
    # -----------------------------
    if sector_signal == strategy_signal:

        score += 10
        reasons.append("Sector Strong")

    else:

        score -= 10

    # -----------------------------
    # Market Breadth
    # -----------------------------
    if breadth_signal == strategy_signal:

        score += 10
        reasons.append("Market Breadth Positive")

    else:

        score -= 10

    # -----------------------------
    # Option Chain
    # -----------------------------
    if option_signal == strategy_signal:

        score += 15
        reasons.append("Option Chain Confirmed")

    else:

        score -= 15

    # -----------------------------
    # Final Decision
    # -----------------------------
    if score >= 95:

        allow = True

    else:

        allow = False

        strategy_signal = "NO TRADE"

    return {

        "allow": allow,

        "signal": strategy_signal,

        "confidence": max(0, min(score, 100)),

        "reasons": reasons

    }
