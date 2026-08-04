# ==========================================
# Institutional Trade Engine
# File : dashboard.py
# Version : 7.0
# ==========================================

import streamlit as st


class Dashboard:

    def __init__(self):
        pass


    # ---------------------------------------
    # Market Status
    # ---------------------------------------

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
                "Global Sentiment",
                global_sentiment
            )

        with c3:
            st.metric(
                "India VIX",
                india_vix
            )


    # ---------------------------------------
    # Trade Display
    # ---------------------------------------

    def show_trade(self, trade):

        if not trade:

            st.warning(
                "No Trade Available"
            )

            return


        symbol = trade.get(
            "symbol",
            "UNKNOWN"
        )

        signal = trade.get(
            "signal",
            "WAIT"
        )


        confidence = trade.get(
            "confidence",
            0
        )


        st.header(
            f"{signal} : {symbol}"
        )


        st.success(
            f"Confidence : {confidence}%"
        )


        setup = trade.get(
            "setup",
            {}
        )


        c1, c2, c3 = st.columns(3)


        with c1:

            st.metric(
                "Entry",
                setup.get(
                    "entry",
                    "-"
                )
            )


        with c2:

            st.metric(
                "Stop Loss",
                setup.get(
                    "stop_loss",
                    "-"
                )
            )


        with c3:

            st.metric(
                "Quantity",
                setup.get(
                    "quantity",
                    "-"
                )
            )


        c4, c5 = st.columns(2)


        with c4:

            st.metric(
                "Target 1",
                setup.get(
                    "target_1",
                    "-"
                )
            )


        with c5:

            st.metric(
                "Target 2",
                setup.get(
                    "target_2",
                    "-"
                )
            )


        st.metric(
            "Risk Reward",
            setup.get(
                "risk_reward",
                "-"
            )
        )


        st.subheader(
            "Trade Confirmation"
        )


        reasons = trade.get(
            "reasons",
            []
        )


        if reasons:

            for reason in reasons:

                st.write(
                    "✅",
                    reason
                )

        else:

            st.write(
                "No confirmation details available"
            )


    # ---------------------------------------
    # No Trade
    # ---------------------------------------

    def show_no_trade(
        self,
        reason
    ):

        st.error(
            "NO TRADE"
        )

        st.write(
            reason
        )


    # ---------------------------------------
    # Performance
    # ---------------------------------------

    def show_performance(
        self,
        stats
    ):

        st.subheader(
            "Performance"
        )


        if not stats:

            st.info(
                "No performance data"
            )

            return


        c1, c2, c3, c4 = st.columns(4)


        with c1:

            st.metric(
                "Trades",
                stats.get(
                    "total_trades",
                    0
                )
            )


        with c2:

            st.metric(
                "Win Rate",
                f"{stats.get('win_rate',0)}%"
            )


        with c3:

            st.metric(
                "Profit Factor",
                stats.get(
                    "profit_factor",
                    0
                )
            )


        with c4:

            st.metric(
                "PnL",
                stats.get(
                    "total_pnl",
                    0
                )
            )
