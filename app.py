import streamlit as st
import config
from datetime import datetime

# -----------------------------------
# Page Config
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

st.caption("AI Based High Confidence Trade Scanner")

st.divider()

# -----------------------------------
# Dummy Live Data (abhi testing)
# -----------------------------------
signal = "NO TRADE"
symbol = "BANKNIFTY"

entry = "--"
sl = "--"
target1 = "--"
target2 = "--"

confidence = 0

status = "Scanning..."

# -----------------------------------
# Signal Box
# -----------------------------------
if signal == "BUY":
    st.success("🟢 BUY")

elif signal == "SELL":
    st.error("🔴 SELL")

else:
    st.warning("⚪ NO TRADE")

# -----------------------------------
# Main Dashboard
# -----------------------------------
col1, col2 = st.columns(2)

with col1:

    st.metric("Symbol", symbol)

    st.metric("Entry", entry)

    st.metric("Stop Loss", sl)

with col2:

    st.metric("Target 1", target1)

    st.metric("Target 2", target2)

    st.metric("Confidence", f"{confidence}%")

st.divider()

st.write("### Trade Status")

st.info(status)

st.divider()

st.write("Last Scan")

st.success(datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

st.caption("Ultra Trade Engine Version 1.0")
