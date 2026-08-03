# ==========================================
# Institutional Trade Engine
# File : global_market.py
# Version : 1.0
# ==========================================

import yfinance as yf


GLOBAL_MARKETS = {

    "DOW": "^DJI",

    "NASDAQ": "^IXIC",

    "S&P500": "^GSPC",

    "NIKKEI": "^N225",

    "HANGSENG": "^HSI",

    "SHANGHAI": "000001.SS"

}


def get_market_sentiment():

    buy_score = 0
    sell_score = 0

    result = {}

    for name, ticker in GLOBAL_MARKETS.items():

        try:

            df = yf.download(
                ticker,
                period="2d",
                interval="1d",
                progress=False,
                auto_adjust=False
            )

            if len(df) < 2:
                continue

            previous_close = float(df["Close"].iloc[-2])

            current_close = float(df["Close"].iloc[-1])

            change = ((current_close - previous_close) / previous_close) * 100

            result[name] = round(change, 2)

            if change > 0:
                buy_score += 1

            else:
                sell_score += 1

        except Exception:

            pass

    if buy_score > sell_score:

        signal = "BUY"

        confidence = round((buy_score / len(GLOBAL_MARKETS)) * 100)

    elif sell_score > buy_score:

        signal = "SELL"

        confidence = round((sell_score / len(GLOBAL_MARKETS)) * 100)

    else:

        signal = "NEUTRAL"

        confidence = 50

    return {

        "signal": signal,

        "confidence": confidence,

        "markets": result

    }
