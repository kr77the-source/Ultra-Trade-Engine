import streamlit as st
import config

st.set_page_config(
    page_title=config.APP_NAME,
    layout="wide"
)

st.title("Institutional Trade Engine")

st.success("Application Started Successfully")

st.write("Market Scan will start after 09:30 AM")
