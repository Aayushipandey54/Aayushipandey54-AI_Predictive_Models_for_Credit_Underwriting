import streamlit as st
import joblib
import pandas as pd


# Load the pre-trained model
model = joblib.load("model.joblib")

# App Title
st.title("Loan Approval Prediction")
st.write("Provide the required details below to predict loan approval.")

# User Input Fields
gender = st.selectbox("Gender:", ['Male', 'Female'])
married = st.selectbox("Marital Status:", ['Yes', 'No'])
dependents = st.selectbox("Number of Dependents:", ['0', '1', '2', '3+'])
education = st.selectbox("Education Level:", ['Graduate', 'Not Graduate'])
self_employed = st.selectbox("Self Employed:", ['No', 'Yes'])
applicant_income = st.number_input("Applicant's Annual Income (e.g., 50000):", min_value=0)
coapplicant_income = st.number_input("Coapplicant's Annual Income (e.g., 50000):", min_value=0)
loan_amount = st.number_input("Loan Amount (e.g., 50000):", min_value=0)
loan_amount_term = st.number_input("Loan Term (in months, e.g., 360):", min_value=0)
credit_history = st.selectbox("Credit History:", ['Yes', 'No'])
property_area = st.selectbox("Property Area:", ['Urban', 'Semiurban', 'Rural'])

# Predict Button
if st.button("Predict Loan Approval"):
    # Create user input data as a DataFrame
    user_data = pd.DataFrame({
        'Gender': [1 if gender == 'Male' else 0],
        'Married': [1 if married == 'Yes' else 0],
        'Dependents': [0 if dependents == '0' else (1 if dependents == '1' else (2 if dependents == '2' else 3))],
        'Education': [0 if education == 'Graduate' else 1],
        'Self_Employed': [1 if self_employed == 'Yes' else 0],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount / 1000],  # Scaling loan amount to match model input
        'Loan_Amount_Term': [loan_amount_term],
        'Credit_History': [1 if credit_history == 'Yes' else 0],
        'Property_Area': [2 if property_area == 'Urban' else (1 if property_area == 'Semiurban' else 0)]
    })

    # Make the prediction
    prediction = model.predict(user_data)

    # Display Result
    if prediction[0] == 1:
        st.success("Congratulations! Your loan is likely to be approved.")
    else:
        st.error("Unfortunately, your loan is likely to be rejected.")
