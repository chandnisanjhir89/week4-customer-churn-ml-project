import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("best_model.pkl")

st.title("Customer Churn Prediction System")

st.write("Enter customer details below:")

Age = st.number_input("Age", min_value=18, max_value=100)

Tenure = st.number_input("Tenure")

Usage_Frequency = st.number_input("Usage Frequency")

Support_Calls = st.number_input("Support Calls")

Payment_Delay = st.number_input("Payment Delay")

Subscription_Type = st.selectbox(
    "Subscription Type",
    [0, 1, 2]
)

Contract_Length = st.selectbox(
    "Contract Length",
    [0, 1, 2]
)

Total_Spend = st.number_input("Total Spend")

Last_Interaction = st.number_input("Last Interaction")

gender = st.selectbox(
    "Gender",
    [0, 1]
)

spend_per_month = Total_Spend / (Tenure + 1)

if st.button("Predict Churn"):

    input_data = pd.DataFrame(
        [[
            Age,
            Tenure,
            Usage_Frequency,
            Support_Calls,
            Payment_Delay,
            Subscription_Type,
            Contract_Length,
            Total_Spend,
            Last_Interaction,
            gender,
            spend_per_month
        ]],
        columns=[
            "Age",
            "Tenure",
            "Usage Frequency",
            "Support Calls",
            "Payment Delay",
            "Subscription Type",
            "Contract Length",
            "Total Spend",
            "Last Interaction",
            "gender",
            "spend_per_month"
        ]
    )

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer is likely to Churn")
    else:
        st.success("Customer is likely to Stay")
