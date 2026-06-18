import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("Personal Finance Manager")

# Income Section

st.header("Add Income")

amount = st.number_input(
    "Enter Income Amount",
    min_value=0.0
)

source = st.text_input(
    "Enter Income Source"
)

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


# Dashboard Section

st.header("Dashboard")

response = requests.get(
    "http://127.0.0.1:8000/balance"
)

if response.status_code == 200:

    data = response.json()

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Income", f"₹{data['total_income']}")
    col2.metric("Total Expense", f"₹{data['total_expense']}")
    col3.metric("Balance", f"₹{data['balance']}")

    st.write("Income Records :", data["income_count"])
    st.write("Expense Records :", data["expense_count"])


# Income History

st.header("Income History")

income_response = requests.get(
    "http://127.0.0.1:8000/income"
)

if income_response.status_code == 200:

    income_data = income_response.json()

    income_df = pd.DataFrame(
        income_data,
        columns=["ID", "Amount", "Source", "Created At"]
    )

    st.dataframe(income_df)


# Expense History

st.header("Expense History")

expense_response = requests.get(
    "http://127.0.0.1:8000/expense"
)

if expense_response.status_code == 200:

    expense_data = expense_response.json()

    expense_df = pd.DataFrame(
        expense_data,
        columns=["ID", "Amount", "Category", "Created At"]
    )

    st.dataframe(expense_df)


# Charts

st.header("Financial Charts")

chart_data = pd.DataFrame({
    "Category": ["Income", "Expense"],
    "Amount": [
        data["total_income"],
        data["total_expense"]
    ]
})

fig = px.pie(
    chart_data,
    names="Category",
    values="Amount",
    title="Income vs Expense"
)

st.plotly_chart(fig)
bar_data = pd.DataFrame({
    "Type": ["Income", "Expense", "Balance"],
    "Amount": [
        data["total_income"],
        data["total_expense"],
        data["balance"]
    ]
})

bar_fig = px.bar(
    bar_data,
    x="Type",
    y="Amount",
    title="Income Expense Balance"
)

st.plotly_chart(bar_fig)