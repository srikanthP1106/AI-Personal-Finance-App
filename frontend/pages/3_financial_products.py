import streamlit as st

st.title("Financial Products")

st.header("SIP Calculator")

monthly_investment = st.number_input(
    "Monthly SIP Amount",
    min_value=500,
    value=1000
)

years = st.number_input(
    "Investment Years",
    min_value=1,
    value=5
)

expected_return = st.number_input(
    "Expected Return (%)",
    min_value=1.0,
    value=12.0
)

estimated_value = (
    monthly_investment * 12 * years
) * (1 + expected_return / 100)

st.metric(
    "Estimated Value",
    f"₹{estimated_value:,.0f}"
)