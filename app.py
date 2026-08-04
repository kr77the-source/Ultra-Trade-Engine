# ==========================================
# Institutional Trade Engine
# File : app.py
# Version : 6.0 Final
# ==========================================

import streamlit as st
import time

from engine import TradeEngine
from dashboard import Dashboard
from performance import get_statistics

# ------------------------------------------
# PAGE CONFIG
# ------------------------------------------

st.set_page_config(

    page_title="Institutional AI Trade Engine",

    page_icon="📈",

    layout="wide"

)

# ------------------------------------------
# OBJECTS
# ------------------------------------------

engine = TradeEngine()

ui = Dashboard()

# ------------------------------------------
# HEADER
# ------------------------------------------

st.title("📈 Institutional AI Trade Engine")

st.caption(
    "Professional Intraday Trading Dashboard"
)

# ------------------------------------------
# SIDEBAR
# ------------------------------------------

st.sidebar.header("Controls")

refresh = st.sidebar.slider(

    "Auto Refresh (Seconds)",

    10,

    300,

    60

)

capital = st.sidebar.number_input(

    "Capital",

    value=500000

)

scan = st.sidebar.button(

    "🔍 Scan Market"

)

# ------------------------------------------
# SCAN
# ------------------------------------------

if scan:

    with st.spinner("Scanning Market..."):

        result = engine.run()

        st.session_state["result"] = result

# ------------------------------------------
# DISPLAY
# ------------------------------------------

if "result" in st.session_state:

    result = st.session_state["result"]

    if result["status"] == "TRADE APPROVED":

        trade = result["trade"]

        ui.show_market_status(

            "Bullish"

            if trade["signal"] == "BUY"

            else "Bearish",

            "Positive",

            "Normal"

        )

        ui.show_trade(trade)

    else:

        ui.show_no_trade(

            result["reason"]

        )

# ------------------------------------------
# PERFORMANCE
# ------------------------------------------

stats = get_statistics()

ui.show_performance(stats)

# ------------------------------------------
# FOOTER
# ------------------------------------------

st.divider()

st.caption(

    "Institutional AI Engine Version 6"

)

# ------------------------------------------
# AUTO REFRESH
# ------------------------------------------

if st.sidebar.checkbox(

    "Enable Auto Refresh"

):

    time.sleep(refresh)

    st.rerun()
