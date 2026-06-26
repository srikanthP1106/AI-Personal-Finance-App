import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.title("💵 Income & Expenses")

st.markdown("---")

# -----------------------------
# ADD INCOME
# -----------------------------

st.header("➕ Add Income")

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

st.markdown("---")

# -----------------------------
# ADD EXPENSE
# -----------------------------

st.header("➖ Add Expense")

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

st.markdown("---")

# -----------------------------
# DASHBOARD
# -----------------------------

st.header("📊 Dashboard")

response = requests.get(
    "http://127.0.0.1:8000/balance"
)

if response.status_code == 200:

    data = response.json()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Income",
        f"₹{data['total_income']}"
    )

    col2.metric(
        "Total Expense",
        f"₹{data['total_expense']}"
    )

    col3.metric(
        "Balance",
        f"₹{data['balance']}"
    )

    st.write(
        f"Income Records : {data['income_count']}"
    )

    st.write(
        f"Expense Records : {data['expense_count']}"
    )

st.markdown("---")

# -----------------------------
# INCOME HISTORY
# -----------------------------

st.header("📜 Income History")

income_response = requests.get(
    "http://127.0.0.1:8000/income"
)

if income_response.status_code == 200:

    income_df = pd.DataFrame(
        income_response.json(),
        columns=[
            "ID",
            "Amount",
            "Source",
            "Created At"
        ]
    )

    st.dataframe(
        income_df,
        use_container_width=True
    )

st.markdown("---")

# -----------------------------
# EXPENSE HISTORY
# -----------------------------

st.header("📜 Expense History")

expense_response = requests.get(
    "http://127.0.0.1:8000/expense"
)

if expense_response.status_code == 200:

    expense_df = pd.DataFrame(
        expense_response.json(),
        columns=[
            "ID",
            "Amount",
            "Category",
            "Created At"
        ]
    )

    st.dataframe(
        expense_df,
        use_container_width=True
    )
    st.markdown("---")

# -----------------------------
# UPDATE INCOME
# -----------------------------

st.header("✏️ Update Income")

update_income_id = st.number_input(
    "Enter Income ID",
    min_value=1,
    step=1,
    key="update_income_id"
)

new_income_amount = st.number_input(
    "Enter New Income Amount",
    min_value=0.0,
    key="new_income_amount"
)

new_income_source = st.text_input(
    "Enter New Income Source",
    key="new_income_source"
)

if st.button("Update Income"):

    response = requests.put(
        f"http://127.0.0.1:8000/income/{update_income_id}",
        params={
            "amount": new_income_amount,
            "source": new_income_source
        }
    )

    if response.status_code == 200:
        st.success("Income Updated Successfully")
    else:
        st.error("Failed to Update Income")


st.markdown("---")

# -----------------------------
# DELETE INCOME
# -----------------------------

st.header("🗑 Delete Income")

delete_income_id = st.number_input(
    "Enter Income ID to Delete",
    min_value=1,
    step=1,
    key="delete_income"
)

if st.button("Delete Income"):

    response = requests.delete(
        f"http://127.0.0.1:8000/income/{delete_income_id}"
    )

    if response.status_code == 200:
        st.success("Income Deleted Successfully")
    else:
        st.error("Failed to Delete Income")


st.markdown("---")

# -----------------------------
# UPDATE EXPENSE
# -----------------------------

st.header("✏️ Update Expense")

update_expense_id = st.number_input(
    "Enter Expense ID",
    min_value=1,
    step=1,
    key="update_expense_id"
)

new_expense_amount = st.number_input(
    "Enter New Expense Amount",
    min_value=0.0,
    key="new_expense_amount"
)

new_expense_category = st.text_input(
    "Enter New Expense Category",
    key="new_expense_category"
)

if st.button("Update Expense"):

    response = requests.put(
        f"http://127.0.0.1:8000/expense/{update_expense_id}",
        params={
            "amount": new_expense_amount,
            "category": new_expense_category
        }
    )

    if response.status_code == 200:
        st.success("Expense Updated Successfully")
    else:
        st.error("Failed to Update Expense")


st.markdown("---")

# -----------------------------
# DELETE EXPENSE
# -----------------------------

st.header("🗑 Delete Expense")

delete_expense_id = st.number_input(
    "Enter Expense ID to Delete",
    min_value=1,
    step=1,
    key="delete_expense"
)

if st.button("Delete Expense"):

    response = requests.delete(
        f"http://127.0.0.1:8000/expense/{delete_expense_id}"
    )

    if response.status_code == 200:
        st.success("Expense Deleted Successfully")
    else:
        st.error("Failed to Delete Expense")
        st.markdown("---")

st.caption(
    "Developed by Srikanth Paruchuri | AI Personal Finance Manager | 2026"
)