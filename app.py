import streamlit as st
import config
import database
from datetime import datetime

# -----------------------------------
# Page Configuration
# -----------------------------------

st.set_page_config(
    page_title=config.APP_NAME,
    page_icon="📈",
    layout="wide"
)

# -----------------------------------
# Header
# -----------------------------------

st.title("📈 Institutional Trade Engine")

st.caption("Ultra High Confidence AI Trade Scanner")

st.divider()

# -----------------------------------
# Dummy Data (Next Step me Live Data aayega)
# -----------------------------------

signal = "NO TRADE"

symbol = "BANKNIFTY"

entry = "--"

stop_loss = "--"

target1 = "--"

target2 = "--"

confidence = 0

status = "Scanning Market..."

# -----------------------------------
# Trade Signal
# -----------------------------------

if signal == "BUY":
    st.success("🟢 BUY")

elif signal == "SELL":
    st.error("🔴 SELL")

else:
    st.warning("⚪ NO TRADE")

# -----------------------------------
# Dashboard
# -----------------------------------

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

# -----------------------------------
# Status
# -----------------------------------

st.subheader("Trade Status")

st.info(status)

st.divider()

# -----------------------------------
# Watchlist
# -----------------------------------

st.subheader("Watchlist")

for stock in database.WATCHLIST:
    st.write("✅", stock)

st.divider()

# -----------------------------------
# Last Scan
# -----------------------------------

st.subheader("Last Scan")

st.success(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

st.divider()

st.caption("Institutional Trade Engine v1.0")
