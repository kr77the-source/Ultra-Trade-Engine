# ==========================================
# Institutional Trade Engine
# File : scanner.py
# Version : 2.0
# ==========================================

import database
import live_data
import strategy_pdh
import yfinance as yf


def get_last_two_candles(symbol):

    try:

        df = yf.download(
            symbol,
            period="2d",
            interval="5m",
            progress=False,
            auto_adjust=False
        )

        if len(df) < 3:
            return None, None

        previous = df.iloc[-2]

        current = df.iloc[-1]

        prev = {

            "open": float(previous["Open"]),
            "high": float(previous["High"]),
            "low": float(previous["Low"]),
            "close": float(previous["Close"]),
            "volume": float(previous["Volume"])

        }

        curr = {

            "open": float(current["Open"]),
            "high": float(current["High"]),
            "low": float(current["Low"]),
            "close": float(current["Close"]),
            "volume": float(current["Volume"])

        }

        return prev, curr

    except Exception as e:

        print(e)

        return None, None


def scan_market():

    trades = []

    for name, info in database.WATCHLIST.items():

        try:

            live = live_data.get_live_price(info["ticker"])

            prev_day = live_data.get_previous_day(info["ticker"])

            previous, current = get_last_two_candles(info["ticker"])

            if (
                live is None
                or prev_day is None
                or previous is None
                or current is None
            ):
                continue

            result = strategy_pdh.pdh_strategy(
                current,
                previous,
                prev_day
            )

            trades.append({

                "symbol": name,

                "price": live["close"],

                "signal": result["signal"],

                "confidence": result["confidence"]

            })

        except Exception as e:

            print(name, e)

    return trades


def get_best_trade():

    market = scan_market()

    if len(market) == 0:
        return None

    market.sort(
        key=lambda x: x["confidence"],
        reverse=True
    )

    return market[0]
