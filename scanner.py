# ==========================================
# Institutional Trade Engine
# File : scanner.py
# Version : 4.0
# ==========================================


import database
import live_data
import indicators

import strategy_pdh
import strategy_orb
import strategy_vwap
import strategy_ema
import strategy_cpr

import supertrend
import smart_money
import market_structure
import order_block
import liquidity_grab
import multi_timeframe

import global_market
import sector_strength
import market_breadth
import option_chain

import ai_score_engine
import trade_setup


def scan_symbol(symbol, info):

    try:

        ticker = info["ticker"]


        # -----------------------------
        # Live Price
        # -----------------------------

        live = live_data.get_live_price(
            ticker
        )

        if live is None:

            return None



        # -----------------------------
        # Market Data
        # -----------------------------

        df = live_data.get_candles(
            ticker
        )


        if df is None:

            return None



        current = df.iloc[-1]

        previous = df.iloc[-2]



        # -----------------------------
        # Strategies
        # -----------------------------

        pdh = strategy_pdh.pdh_strategy(
            current,
            previous,
            live
        )


        ema_data = indicators.get_ema(
            ticker
        )


        ema = strategy_ema.ema_strategy(

            live["close"],

            ema_data["ema20"],

            ema_data["ema50"]

        )


        vwap_value = indicators.get_vwap(
            ticker
        )


        vwap = strategy_vwap.vwap_strategy(

            current,

            vwap_value

        )


        cpr_data = indicators.get_cpr(
            ticker
        )


        cpr = strategy_cpr.cpr_strategy(

            live["close"],

            cpr_data["pivot"],

            cpr_data["tc"],

            cpr_data["bc"]

        )


        # ORB placeholder
        orb = {

            "signal":"NEUTRAL"

        }


        # -----------------------------
        # Advanced Filters
        # -----------------------------


        st = supertrend.calculate_supertrend(
            df
        )


        sm = smart_money.detect_smart_money(
            ticker
        )


        ms = market_structure.detect_market_structure(
            df
        )


        ob = order_block.detect_order_block(
            df
        )


        lg = liquidity_grab.detect_liquidity_grab(
            df
        )


        mtf = multi_timeframe.multi_timeframe_analysis(
            ticker
        )


        # -----------------------------
        # External Filters
        # -----------------------------

        global_data = global_market.get_market_sentiment()

        sector_data = sector_strength.get_sector_strength()

        breadth_data = market_breadth.get_market_breadth()


        option_data = option_chain.option_chain_signal(

            100000,

            120000,

            5000,

            9000

        )


        # -----------------------------
        # AI Score
        # -----------------------------


        ai = ai_score_engine.calculate_ai_score({

            "pdh":pdh,

            "orb":orb,

            "vwap":vwap,

            "ema":ema,

            "cpr":cpr,

            "supertrend":st,

            "smart_money":sm,

            "market_structure":ms,

            "order_block":ob,

            "liquidity":lg,

            "multi_timeframe":mtf,

            "global":global_data,

            "sector":sector_data,

            "breadth":breadth_data,

            "option_chain":option_data

        })



        # -----------------------------
        # Trade Setup
        # -----------------------------


        atr = indicators.get_atr(
            ticker
        )


        setup = trade_setup.create_trade_setup(

            ai["signal"],

            live["close"],

            atr,

            500000

        )


        return {

            "symbol":symbol,

            "signal":ai["signal"],

            "confidence":ai["confidence"],

            "setup":setup,

            "reasons":ai["reasons"]

        }


    except Exception as e:

        print(
            symbol,
            e
        )

        return None



def scan_market():

    results=[]


    for symbol,info in database.WATCHLIST.items():

        result = scan_symbol(
            symbol,
            info
        )


        if result:

            results.append(result)


    return results



def get_best_trade():

    trades = scan_market()


    if len(trades)==0:

        return None


    trades.sort(

        key=lambda x:x["confidence"],

        reverse=True

    )


    return trades[0]
