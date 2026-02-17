import streamlit as st

st.title("Insurance Claim Prediction")

st.header("Enter Customer Details")

# Numeric inputs
age = st.number_input(
    "Enter Age",
    min_value=18,
    max_value=100,
    value=30
)

annual_income = st.number_input(
    "Enter Annual Income",
    min_value=0,
    value=50000
)

claim_amount = st.number_input(
    "Enter Claim Amount",
    min_value=0,
    value=10000
)

# Categorical inputs
gender = st.selectbox(
    "Select Gender",
    ["Male", "Female"]
)

employment_status = st.selectbox(
    "Select Employment Status",
    ["Employed", "Unemployed", "Self-employed"]
)

policy_type = st.selectbox(
    "Select Policy Type",
    ["Basic", "Premium", "Gold"]
)

fraud_risk = st.selectbox(
    "Select Fraud Risk",
    ["Low", "Medium", "High"]
)

# Show entered values
st.subheader("User Input Summary")

st.write("Age:", age)
st.write("Annual Income:", annual_income)
st.write("Claim Amount:", claim_amount)
st.write("Gender:", gender)
st.write("Employment Status:", employment_status)
st.write("Policy Type:", policy_type)
st.write("Fraud Risk:", fraud_risk)
