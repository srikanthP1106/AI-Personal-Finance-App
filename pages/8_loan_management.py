import streamlit as st

st.title("Loan Management")

loan_amount = st.number_input(
    "Loan Amount (₹)",
    min_value=1000,
    value=500000
)

interest_rate = st.number_input(
    "Interest Rate (%)",
    min_value=1.0,
    value=9.0
)

loan_years = st.number_input(
    "Loan Tenure (Years)",
    min_value=1,
    value=10
)

monthly_rate = interest_rate / 12 / 100

months = loan_years * 12

emi = (
    loan_amount * monthly_rate *
    ((1 + monthly_rate) ** months)
) / (
    ((1 + monthly_rate) ** months) - 1
)

total_payment = emi * months

total_interest = total_payment - loan_amount

st.metric(
    "Monthly EMI",
    f"₹{emi:,.0f}"
)

st.metric(
    "Total Interest",
    f"₹{total_interest:,.0f}"
)

st.metric(
    "Total Payment",
    f"₹{total_payment:,.0f}"
)
st.markdown("---")

st.caption(
    "Developed by Srikanth Paruchuri | AI Personal Finance Manager | 2026"
)