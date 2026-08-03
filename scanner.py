# ==========================================
# Institutional Trade Engine
# File : scanner.py
# Version : 1.0
# ==========================================

import database
import live_data


def scan_market():

    results = []

    for name, info in database.WATCHLIST.items():

        try:

            data = live_data.get_live_price(info["ticker"])

            if data is None:
                continue

            results.append({

                "symbol": name,

                "ticker": info["ticker"],

                "price": data["close"],

                "high": data["high"],

                "low": data["low"],

                "volume": data["volume"],

                "signal": "NO TRADE",

                "confidence": 0

            })

        except Exception as e:

            print(name, e)

    return results


def get_best_trade():

    market = scan_market()

    if len(market) == 0:

        return None

    return market[0]
