# ==========================================
# Institutional Trade Engine
# File : app.py
# Version : 4.0
# ==========================================

import streamlit as st
import scanner
import time


# -----------------------------
# Page Config
# -----------------------------

st.set_page_config(

    page_title="Institutional Trade Engine",

    page_icon="📈",

    layout="wide"

)


# -----------------------------
# Title
# -----------------------------

st.title(
    "📈 Institutional AI Trade Engine"
)


st.caption(
    "Multi Strategy + Smart Money + Global Market Scanner"
)



# -----------------------------
# Refresh Button
# -----------------------------

if st.button("🔄 Scan Market"):

    with st.spinner(
        "Scanning Market..."
    ):

        trade = scanner.get_best_trade()


        st.session_state["trade"] = trade



# -----------------------------
# Display Result
# -----------------------------


if "trade" in st.session_state:


    trade = st.session_state["trade"]


    if trade is None:


        st.warning(
            "No High Confidence Trade Found"
        )


    else:


        signal = trade["signal"]


        confidence = trade["confidence"]



        # Signal Box

        if signal == "BUY":

            st.success(
                f"🟢 BUY SIGNAL\n\nConfidence : {confidence}%"
            )


        elif signal == "SELL":

            st.error(
                f"🔴 SELL SIGNAL\n\nConfidence : {confidence}%"
            )


        else:

            st.info(
                "⚪ NO TRADE"
            )



        st.divider()


        # Details

        col1,col2,col3 = st.columns(3)


        with col1:

            st.metric(

                "Symbol",

                trade["symbol"]

            )


        with col2:

            st.metric(

                "Confidence",

                f"{confidence}%"

            )


        with col3:

            st.metric(

                "Signal",

                signal

            )



        st.divider()



        # Trade Setup

        setup = trade.get(
            "setup"
        )


        if setup:


            st.subheader(
                "Trade Levels"
            )


            c1,c2,c3,c4 = st.columns(4)


            with c1:

                st.metric(

                    "Entry",

                    setup.get(
                        "entry"
                    )

                )


            with c2:

                st.metric(

                    "Stop Loss",

                    setup.get(
                        "stop_loss"
                    )

                )


            with c3:

                st.metric(

                    "Target 1",

                    setup.get(
                        "target_1"
                    )

                )


            with c4:

                st.metric(

                    "Target 2",

                    setup.get(
                        "target_2"
                    )

                )



            st.write(

                "Quantity:",

                setup.get(
                    "quantity"
                )

            )



        st.divider()



        # Reasons

        st.subheader(
            "Confirmation"
        )


        for reason in trade["reasons"]:

            st.write(
                "✅",
                reason
            )



else:


    st.info(
        "Click Scan Market to find setup"
    )



# Auto refresh option

st.sidebar.title(
    "Settings"
)


auto = st.sidebar.checkbox(
    "Auto Refresh"
)


if auto:

    time.sleep(60)

    st.rerun()
