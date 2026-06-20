import streamlit as st

st.title("Insurance Planner")

age = st.number_input(
    "Enter Your Age",
    min_value=18,
    max_value=100,
    value=25
)

annual_income = st.number_input(
    "Enter Annual Income (₹)",
    min_value=10000,
    value=500000
)

recommended_cover = annual_income * 10

st.header("Insurance Recommendation")

st.metric(
    "Recommended Life Cover",
    f"₹{recommended_cover:,.0f}"
)

if age < 30:
    st.success(
        "Young age detected. Premiums will be lower."
    )

elif age < 50:
    st.warning(
        "Consider adequate family protection."
    )

else:
    st.error(
        "Insurance becomes more expensive with age."
    )