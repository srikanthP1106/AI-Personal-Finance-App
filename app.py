import streamlit as st
import requests

st.title("Personal Finance Manager")

# Income Section

st.header("Add Income")

amount = st.number_input("Enter Income Amount", min_value=0.0)

source = st.text_input("Enter Income Source")

if st.button("Add Income"):

    response = requests.post(
        "http://127.0.0.1:8000/income",
        params={
            "amount": amount,
            "source": source
        }
    )

    if response.status_code == 200:
        st.success("Income Added Successfully")
    else:
        st.error("Failed to Add Income")


# Expense Section

st.header("Add Expense")

expense_amount = st.number_input(
    "Enter Expense Amount",
    min_value=0.0,
    key="expense_amount"
)

category = st.text_input(
    "Enter Expense Category",
    key="category"
)

if st.button("Add Expense"):

    response = requests.post(
        "http://127.0.0.1:8000/expense",
        params={
            "amount": expense_amount,
            "category": category
        }
    )

    if response.status_code == 200:
        st.success("Expense Added Successfully")
    else:
        st.error("Failed to Add Expense")