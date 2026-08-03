# ==========================================
# Institutional Trade Engine
# File : sector_strength.py
# Version : 1.0
# ==========================================

import yfinance as yf

# Sector ETF / Index Mapping
SECTORS = {

    "BANK": "^NSEBANK",

    "IT": "^CNXIT",

    "AUTO": "^CNXAUTO",

    "FMCG": "^CNXFMCG",

    "PHARMA": "^CNXPHARMA",

    "METAL": "^CNXMETAL",

    "REALTY": "^CNXREALTY"

}


def get_sector_strength():

    result = {}

    buy_score = 0

    sell_score = 0

    for sector, ticker in SECTORS.items():

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

            prev_close = float(df["Close"].iloc[-2])

            last_close = float(df["Close"].iloc[-1])

            change = ((last_close - prev_close) / prev_close) * 100

            result[sector] = round(change, 2)

            if change > 0:

                buy_score += 1

            else:

                sell_score += 1

        except:

            pass

    if buy_score > sell_score:

        signal = "BUY"

        confidence = round((buy_score / len(SECTORS)) * 100)

    elif sell_score > buy_score:

        signal = "SELL"

        confidence = round((sell_score / len(SECTORS)) * 100)

    else:

        signal = "NEUTRAL"

        confidence = 50

    return {

        "signal": signal,

        "confidence": confidence,

        "sectors": result

    }
