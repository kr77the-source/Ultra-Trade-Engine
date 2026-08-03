import streamlit as st
from datetime import datetime

import config
import database
import live_data

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title=config.APP_NAME,
    page_icon="📈",
    layout="wide"
)

# ==========================================
# LOAD LIVE DATA
# ==========================================

data = live_data.get_live_price("^NSEBANK")

if data:

    signal = "NO TRADE"

    symbol = "BANKNIFTY"

    entry = data["close"]

    stop_loss = round(entry - 100, 2)

    target1 = round(entry + 200, 2)

    target2 = round(entry + 400, 2)

    confidence = 10

    status = "Scanning Market..."

else:

    signal = "NO TRADE"

    symbol = "BANKNIFTY"

    entry = "--"

    stop_loss = "--"

    target1 = "--"

    target2 = "--"

    confidence = 0

    status = "Market Data Not Available"

# ==========================================
# HEADER
# ==========================================

st.title("📈 Institutional Trade Engine")

st.caption("Ultra High Confidence AI Trade Scanner")

st.divider()

# ==========================================
# SIGNAL
# ==========================================

if signal == "BUY":

    st.success("🟢 BUY")

elif signal == "SELL":

    st.error("🔴 SELL")

else:

    st.warning("⚪ NO TRADE")

# ==========================================
# DASHBOARD
# ==========================================

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

# ==========================================
# TRADE STATUS
# ==========================================

st.subheader("Trade Status")

st.info(status)

st.divider()

# ==========================================
# WATCHLIST
# ==========================================

st.subheader("Watchlist")

for stock in database.WATCHLIST:

    st.write("✅", stock)

st.divider()

# ==========================================
# LAST SCAN
# ==========================================

st.subheader("Last Scan")

st.success(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

st.divider()

st.caption("Institutional Trade Engine Version 1.0")
