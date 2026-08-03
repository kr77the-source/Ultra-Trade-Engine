# ==========================================
# Institutional Trade Engine
# File : app.py
# Version : 2.0
# ==========================================

import streamlit as st
from datetime import datetime

import config
import scanner

# ------------------------------------------
# PAGE CONFIG
# ------------------------------------------

st.set_page_config(
    page_title=config.APP_NAME,
    page_icon="📈",
    layout="wide"
)

# ------------------------------------------
# LOAD BEST TRADE
# ------------------------------------------

trade = scanner.get_best_trade()

if trade:

    signal = trade["signal"]
    symbol = trade["symbol"]
    entry = trade["price"]
    stop_loss = round(entry * 0.998, 2)
    target1 = round(entry * 1.004, 2)
    target2 = round(entry * 1.008, 2)
    confidence = trade["confidence"]
    status = "Market Scanned Successfully"

else:

    signal = "NO TRADE"
    symbol = "--"
    entry = "--"
    stop_loss = "--"
    target1 = "--"
    target2 = "--"
    confidence = 0
    status = "No Data"

# ------------------------------------------
# HEADER
# ------------------------------------------

st.title("📈 Institutional Trade Engine")

st.caption("Ultra High Confidence Trade Scanner")

st.divider()

# ------------------------------------------
# SIGNAL
# ------------------------------------------

if signal == "BUY":
    st.success("🟢 BUY")

elif signal == "SELL":
    st.error("🔴 SELL")

else:
    st.warning("⚪ NO TRADE")

# ------------------------------------------
# DASHBOARD
# ------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.metric("Symbol", symbol)
    st.metric("Entry", entry)
    st.metric("Stop Loss", stop_loss)

with col2:

    st.metric("Target 1", target1)
    st.metric("Target 2", target2)
    st.metric("Confidence", f"{confidence}%")

st.divider()

st.subheader("Trade Status")

st.info(status)

st.divider()

st.subheader("Last Scan")

st.success(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

st.divider()

st.caption("Version 2.0")
