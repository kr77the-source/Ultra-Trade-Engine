# ==========================================
# Institutional Trade Engine
# File : dashboard.py
# Version : 6.0
# ==========================================

import streamlit as st


class Dashboard:

    def __init__(self):
        pass

    def show_market_status(

        self,

        market_bias,

        global_sentiment,

        india_vix

    ):

        st.subheader("Market Overview")

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Market Bias",
                market_bias
            )

        with c2:
            st.metric(
                "Global",
                global_sentiment
            )

        with c3:
            st.metric(
                "India VIX",
                india_vix
            )


    def show_trade(self, trade):

        if trade is None:

            st.warning(
                "No Trade Available"
            )

            return


        setup = trade["setup"]


        st.header(

            f"{trade['signal']} : {trade['symbol']}"

        )


        st.success(

            f"Confidence : {trade['confidence']}%"

        )


        c1, c2, c3 = st.columns(3)

        with c1:

            st.metric(

                "Entry",

                setup["entry"]

            )

        with c2:

            st.metric(

                "Stop Loss",

                setup["stop_loss"]

            )

        with c3:

            st.metric(

                "Quantity",

                setup["quantity"]

            )


        c4, c5 = st.columns(2)

        with c4:

            st.metric(

                "Target 1",

                setup["target_1"]

            )

        with c5:

            st.metric(

                "Target 2",

                setup["target_2"]

            )


        st.metric(

            "Risk Reward",

            setup["risk_reward"]

        )


        st.subheader("Trade Confirmation")


        for reason in trade["reasons"]:

            st.write(

                "✅",

                reason

            )


    def show_no_trade(self, reason):

        st.error(

            "NO TRADE"

        )

        st.write(

            reason

        )


    def show_performance(self, stats):

        st.subheader(

            "Performance"

        )


        a, b, c, d = st.columns(4)


        with a:

            st.metric(

                "Trades",

                stats["total_trades"]

            )


        with b:

            st.metric(

                "Win Rate",

                f"{stats['win_rate']}%"

            )


        with c:

            st.metric(

                "Profit Factor",

                stats["profit_factor"]

            )


        with d:

            st.metric(

                "PnL",

                stats["total_pnl"]

            )
