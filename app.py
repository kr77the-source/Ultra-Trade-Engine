# ==========================================
# Institutional Trade Engine
# File : app.py (Streamlit Version)
# ==========================================

import streamlit as st
import config
from engine import TradingEngine

# Page Config
st.set_page_config(page_title=config.APP_NAME, layout="wide")

def main():
    st.title(f"📊 {config.APP_NAME}")
    st.sidebar.header("Configuration")
    st.sidebar.text(f"Version: {config.VERSION}")
    st.sidebar.text(f"Symbol: {config.DEFAULT_SYMBOL}")
    st.sidebar.text(f"Live Mode: {config.LIVE_MODE}")

    # Initialize Engine
    engine = TradingEngine()

    if st.button("Run Analysis Cycle"):
        with st.spinner("Fetching market data and running analysis..."):
            price, df = engine.run_cycle()
            
            st.success(f"Analysis completed successfully for {config.DEFAULT_SYMBOL}!")
            st.metric(label="Current Price", value=f"₹{price}")
            
            st.subheader("Historical / Market Data")
            st.dataframe(df.tail(10))
    else:
        st.info("Click the button above to execute a trade analysis cycle.")

if __name__ == "__main__":
    main()
