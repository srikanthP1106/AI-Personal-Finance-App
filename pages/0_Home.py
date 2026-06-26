import streamlit as st

st.set_page_config(
    page_title="AI Personal Finance Manager",
    page_icon="💰",
    layout="wide"
)
st.sidebar.image(
    "https://img.icons8.com/fluency/96/money-bag.png",
    width=80
)

st.sidebar.title("AI Finance Manager")

st.sidebar.success("Navigation")

# ---------------- HEADER ----------------

st.markdown("""
<h1 style='text-align:center;color:#2E86C1;'>
💰 AI Personal Finance Manager
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center;color:gray;'>
Smart • Secure • AI Powered Personal Finance Solution
</h4>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------- HERO ----------------

st.success("🚀 Welcome to your AI-Powered Financial Platform")

st.write("")

col1, col2 = st.columns([2, 1])

with col1:

    st.markdown("""
### 📌 About the Project

AI Personal Finance Manager is an intelligent financial application
that helps users manage their daily finances with Artificial Intelligence.

### Key Features

- 💵 Income Management
- 💸 Expense Tracking
- 🤖 AI Investment Advisor
- 📈 Financial Health Score
- 📊 Summary Reports
- 💳 Credit Card Management
- 🏦 Loan Management
- 🛡 Insurance Planner
- 📄 PDF Report Generator
- 📈 Stock Market Analysis
""")

with col2:

    st.info("""
### 🎯 Project Goal

✔ Track Income

✔ Track Expenses

✔ Improve Savings

✔ AI Financial Advice

✔ Better Investment Planning

✔ Wealth Growth
""")

st.markdown("---")

# ---------------- FEATURE CARDS ----------------

st.header("🚀 Available Modules")

c1, c2, c3 = st.columns(3)

with c1:

    st.success("""
### 💵 Income & Expenses

✔ Add Income

✔ Add Expenses

✔ Update Records

✔ Delete Records
""")

    st.success("""
### 🤖 AI Advisor

✔ Investment Suggestions

✔ Financial Health Score

✔ Savings Prediction
""")

with c2:

    st.info("""
### 📈 Analytics

✔ Dashboard

✔ Charts

✔ Net Worth

✔ Monthly Summary
""")

    st.info("""
### 📄 Reports

✔ PDF Report

✔ Financial Summary

✔ Expense Analysis
""")

with c3:

    st.warning("""
### 🏦 Financial Tools

✔ EMI Calculator

✔ SIP Calculator

✔ FD Calculator

✔ Loan Planner
""")

    st.warning("""
### 🌐 Extra Modules

✔ Stock Market

✔ Insurance Planner

✔ Credit Card Manager
""")

st.markdown("---")

# ---------------- WHY CHOOSE ----------------

st.header("⭐ Why Choose AI Personal Finance Manager?")

a, b, c, d = st.columns(4)

a.metric("🤖 AI Powered", "100%")
b.metric("🔒 Secure", "Yes")
c.metric("⚡ Fast", "High")
d.metric("📈 Smart Finance", "Enabled")

st.markdown("---")

# ---------------- FOOTER ----------------

st.success("✅ Project Status : Successfully Running")

st.caption("Developed using Python • FastAPI • Streamlit • SQLite • Machine Learning")
st.markdown("---")

st.caption(
    "Developed by Srikanth Paruchuri | AI Personal Finance Manager | 2026"
)