import streamlit as st
import requests

st.title("Summary Report")

response = requests.get(
    "http://127.0.0.1:8000/balance"
)

if response.status_code == 200:

    data = response.json()

    st.header("Financial Overview")

    st.metric(
        "Total Income",
        f"₹{data['total_income']}"
    )

    st.metric(
        "Total Expense",
        f"₹{data['total_expense']}"
    )

    st.metric(
        "Balance",
        f"₹{data['balance']}"
    )