import streamlit as st

st.title("Credit Card Manager")

credit_limit = st.number_input(
    "Credit Limit (₹)",
    min_value=10000,
    value=100000
)

outstanding = st.number_input(
    "Outstanding Amount (₹)",
    min_value=0,
    value=20000
)

available_limit = credit_limit - outstanding

st.metric(
    "Available Credit",
    f"₹{available_limit:,.0f}"
)

utilization = (outstanding / credit_limit) * 100

st.metric(
    "Credit Utilization",
    f"{utilization:.2f}%"
)

if utilization < 30:
    st.success("Healthy Credit Usage")

elif utilization < 70:
    st.warning("Moderate Credit Usage")

else:
    st.error("High Credit Utilization")