import streamlit as st

st.title("Stock Market")

st.success("Stock Market Module Working")

stock_name = st.text_input(
    "Enter Stock Name",
    "RELIANCE"
)

st.metric(
    "Current Price",
    "₹1500"
)

st.metric(
    "Daily Change",
    "+2.5%"
)