import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from agents.investment_advisor_agent import investment_advice
from utils.calculations import calculate_financial_health_score
from utils.net_worth import calculate_net_worth
from ml_models.expense_anomaly import detect_expense_anomaly
from ml_models.savings_predictor import predict_future_savings
from utils.net_worth_history import get_net_worth_history
from utils.pdf_report import generate_pdf_report


st.sidebar.title("Navigation")
st.set_page_config(
    page_title="AI Personal Finance Manager",
    page_icon="💰",
    layout="wide"
)

st.title("💰 AI Personal Finance Manager")

st.success(
    "Welcome to your AI-Powered Financial Platform"
)

page = st.sidebar.radio(
    "Go To",
    [
        "Dashboard",
        "Income & Expenses",
        "AI Investment",
        "Financial Products",
        "Summary Report"
    ]
)
if page != "Dashboard":

    st.info(
        f"{page} module has been created in frontend/pages."
    )

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
# Monthly Summary

st.header("Monthly Summary")

summary_response = requests.get(
    "http://127.0.0.1:8000/monthly-summary"
)

if summary_response.status_code == 200:

    summary_data = summary_response.json()

    st.success(
        f"Income: ₹{summary_data['income']} | "
        f"Expense: ₹{summary_data['expense']} | "
        f"Savings: ₹{summary_data['savings']}"
    )
    # Delete Income

st.header("Delete Income")

income_id = st.number_input(
    "Enter Income ID",
    min_value=1,
    step=1,
    key="delete_income"
)

if st.button("Delete Income"):

    response = requests.delete(
        f"http://127.0.0.1:8000/income/{income_id}"
    )

    if response.status_code == 200:
        st.success("Income Deleted Successfully")
    else:
        st.error("Failed to Delete Income")
        # Delete Expense

st.header("Delete Expense")

expense_id = st.number_input(
    "Enter Expense ID",
    min_value=1,
    step=1,
    key="delete_expense"
)

if st.button("Delete Expense"):

    response = requests.delete(
        f"http://127.0.0.1:8000/expense/{expense_id}"
    )

    if response.status_code == 200:
        st.success("Expense Deleted Successfully")
    else:
        st.error("Failed to Delete Expense")
        # Update Income

st.header("Update Income")

update_income_id = st.number_input(
    "Enter Income ID to Update",
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
        # Update Expense

st.header("Update Expense")

update_expense_id = st.number_input(
    "Enter Expense ID to Update",
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
        # AI Spending Insights

st.header("AI Spending Insights")

expense_percentage = 0

if data["total_income"] > 0:
    expense_percentage = (
        data["total_expense"] / data["total_income"]
    ) * 100

st.info(
    f"Your expenses are {expense_percentage:.2f}% of your income."
)

if expense_percentage < 50:
    st.success("Excellent savings habit. Keep it up!")

elif expense_percentage < 80:
    st.warning("Your expenses are increasing. Monitor spending.")

else:
    st.error("High spending detected. Consider reducing expenses.")


# AI Investment Advisor

st.header("AI Investment Advisor")

advice = investment_advice(
    data["total_income"],
    data["total_expense"]
)

st.info(advice)
# Financial Health Score

st.header("Financial Health Score")

score = calculate_financial_health_score(
    data["total_income"],
    data["total_expense"]
)

st.metric("Score", f"{score}/100")

if score >= 90:
    st.success("Excellent Financial Health")

elif score >= 70:
    st.warning("Good Financial Health")

else:
    st.error("Needs Financial Improvement")
    # Net Worth Tracker

st.header("Net Worth Tracker")

net_worth = calculate_net_worth(
    data["total_income"],
    data["total_expense"]
)

st.metric(
    "Current Net Worth",
    f"₹{net_worth}"
)

if net_worth >= 50000:
    st.success("Strong Financial Position")

elif net_worth >= 10000:
    st.warning("Growing Financial Position")

else:
    st.error("Needs Wealth Building")
    # Expense Anomaly Detection

st.header("Expense Anomaly Detection")

anomaly_result = detect_expense_anomaly(
    data["total_expense"]
)

st.info(anomaly_result)
# Savings Predictor

st.header("AI Savings Predictor")

predicted_savings = predict_future_savings(
    data["total_income"],
    data["total_expense"]
)

st.metric(
    "Predicted Annual Savings",
    f"₹{predicted_savings}"
)
# Net Worth History

st.header("Net Worth History")

history = get_net_worth_history()

history_df = pd.DataFrame({
    "Month": [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May"
    ],
    "Net Worth": history
})

history_chart = px.line(
    history_df,
    x="Month",
    y="Net Worth",
    title="Net Worth Growth"
)

st.plotly_chart(history_chart)
# PDF Report Generator

st.header("PDF Report Generator")

if st.button("Generate PDF Report"):

    pdf_file = generate_pdf_report()

    st.success(
        f"Report Generated: {pdf_file}"
    )