# ==========================================
# Institutional Trade Engine
# File : market_breadth.py
# Version : 1.0
# ==========================================

import yfinance as yf
import database


def get_market_breadth():

    advance = 0
    decline = 0
    unchanged = 0

    details = {}

    for symbol, info in database.WATCHLIST.items():

        try:

            df = yf.download(
                info["ticker"],
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

            details[symbol] = round(change, 2)

            if change > 0.20:
                advance += 1

            elif change < -0.20:
                decline += 1

            else:
                unchanged += 1

        except Exception:

            continue

    total = advance + decline + unchanged

    if total == 0:

        return {

            "signal": "NO DATA",

            "confidence": 0,

            "advance": 0,

            "decline": 0,

            "unchanged": 0,

            "ratio": 0

        }

    ratio = round(advance / max(decline, 1), 2)

    signal = "NEUTRAL"
    confidence = 50

    if ratio >= 2:

        signal = "BUY"
        confidence = 90

    elif ratio <= 0.50:

        signal = "SELL"
        confidence = 90

    return {

        "signal": signal,

        "confidence": confidence,

        "advance": advance,

        "decline": decline,

        "unchanged": unchanged,

        "ratio": ratio,

        "details": details

    }
