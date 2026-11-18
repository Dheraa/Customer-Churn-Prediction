
import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("models/customer_churn_model.pkl")

st.set_page_config(page_title="Customer Churn Predictor", page_icon="📊")

st.title("Customer Churn Prediction")
st.write("Predict whether a customer is likely to leave a business.")

# Customer inputs
tenure = st.slider("Customer Tenure (Months)", 0, 72, 12)

contract = st.selectbox(
    "Contract Type",
    ["Month-to-month", "One year", "Two year"]
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0,
    value=70.0
)

# Prediction
if st.button("Predict Customer Churn"):
    customer = pd.DataFrame([{
        "tenure": tenure,
        "Contract": contract,
        "MonthlyCharges": monthly_charges
    }])

    prediction = model.predict(customer)[0]
    churn_probability = model.predict_proba(customer)[0][
        list(model.classes_).index("Yes")
    ]

    if prediction == "Yes":
        st.error("Customer is likely to leave.")
    else:
        st.success("Customer is likely to stay.")

    st.metric(
        "Probability of Churning",
        f"{churn_probability:.2%}"
    )
