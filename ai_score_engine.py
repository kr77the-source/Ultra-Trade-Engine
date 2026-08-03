# ==========================================
# Institutional Trade Engine
# File : ai_score_engine.py
# Version : 2.0
# ==========================================


def calculate_ai_score(data):

    buy_score = 0
    sell_score = 0

    reasons = []


    # -----------------------------
    # Price Action Strategies
    # -----------------------------

    for name, weight in [

        ("pdh",10),
        ("orb",8),
        ("vwap",8),
        ("ema",8),
        ("cpr",6),
        ("supertrend",8),
        ("smart_money",10),
        ("market_structure",8),
        ("order_block",8),
        ("liquidity",8),
        ("multi_timeframe",10)

    ]:


        if name in data:

            signal = data[name].get("signal")


            if signal == "BUY":

                buy_score += weight

                reasons.append(
                    name.upper()+" BUY"
                )


            elif signal == "SELL":

                sell_score += weight

                reasons.append(
                    name.upper()+" SELL"
                )


    # -----------------------------
    # Market Filters
    # -----------------------------

    filters = [

        ("global",5),

        ("sector",5),

        ("breadth",5),

        ("option_chain",5)

    ]


    for name, weight in filters:


        if name in data:

            signal = data[name].get("signal")


            if signal == "BUY":

                buy_score += weight

                reasons.append(
                    name.upper()+" SUPPORT"
                )


            elif signal == "SELL":

                sell_score += weight

                reasons.append(
                    name.upper()+" PRESSURE"
                )



    # -----------------------------
    # Final Decision
    # -----------------------------


    if buy_score > sell_score:

        final_signal = "BUY"

        confidence = buy_score


    elif sell_score > buy_score:

        final_signal = "SELL"

        confidence = sell_score


    else:

        final_signal = "NO TRADE"

        confidence = 0



    # Safety Filter

    if confidence < 80:

        final_signal = "NO TRADE"



    return {


        "signal": final_signal,

        "confidence": min(
            confidence,
            100
        ),

        "buy_score": buy_score,

        "sell_score": sell_score,

        "reasons": reasons

    }
