# ==========================================
# Institutional Trade Engine
# File : scanner.py
# Version : 3.0
# ==========================================

import database
import live_data

import global_market
import sector_strength
import market_breadth
import option_chain
import news_filter

import trade_filter


def scan_market():

    trades = []

    # --------------------------------------
    # Global Filters
    # --------------------------------------

    global_result = global_market.get_market_sentiment()

    sector_result = sector_strength.get_sector_strength()

    breadth_result = market_breadth.get_market_breadth()

    news_result = news_filter.check_news("")

    # --------------------------------------
    # Scan Symbols
    # --------------------------------------

    for symbol, info in database.WATCHLIST.items():

        try:

            live = live_data.get_live_price(info["ticker"])

            if live is None:
                continue

            # --------------------------------------
            # Temporary Strategy
            # (Next Version will use PDH + ORB + EMA)
            # --------------------------------------

            strategy_signal = "NO TRADE"
            strategy_confidence = 60

            # Bullish Example
            if live["close"] > live["open"]:

                strategy_signal = "BUY"

                strategy_confidence = 80

            # Bearish Example
            elif live["close"] < live["open"]:

                strategy_signal = "SELL"

                strategy_confidence = 80

            # --------------------------------------
            # Temporary Option Chain
            # --------------------------------------

            option_result = option_chain.option_chain_signal(

                call_oi=100000,

                put_oi=130000,

                call_change=5000,

                put_change=12000

            )

            # --------------------------------------
            # Final Validation
            # --------------------------------------

            final = trade_filter.validate_trade(

                strategy_signal,

                strategy_confidence,

                global_result["signal"],

                sector_result["signal"],

                breadth_result["signal"],

                option_result["signal"],

                news_result["allow_trade"]

            )

            trades.append({

                "symbol": symbol,

                "price": live["close"],

                "signal": final["signal"],

                "confidence": final["confidence"],

                "reasons": final["reasons"]

            })

        except Exception as e:

            print(symbol, e)

    return trades


def get_best_trade():

    trades = scan_market()

    if len(trades) == 0:

        return None

    trades.sort(

        key=lambda x: x["confidence"],

        reverse=True

    )

    return trades[0]
