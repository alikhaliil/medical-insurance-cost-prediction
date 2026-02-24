import streamlit as st
import pandas as pd
import joblib

model = joblib.load('insurance_model.pkl')

st.title("Insurance Premium Predictor 🏥")

age = st.number_input("Age", 18, 100, 25)
bmi = st.number_input("BMI", 10.0, 60.0, 25.0)
children = st.number_input("Number of Children", 0, 10, 0)

sex = st.selectbox("Sex", ["female", "male"])
smoker = st.selectbox("Smoker?", ["no", "yes"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

sex_male = 1 if sex == "male" else 0
smoker_yes = 1 if smoker == "yes" else 0

reg_nw = 1 if region == "northwest" else 0
reg_se = 1 if region == "southeast" else 0
reg_sw = 1 if region == "southwest" else 0

bmi_smoker = bmi * smoker_yes

input_data = pd.DataFrame([[
    age, bmi, children, sex_male, smoker_yes, 
    reg_nw, reg_se, reg_sw, bmi_smoker
]], columns=[
    'age', 'bmi', 'children', 'sex_male', 'smoker_yes', 
    'region_northwest', 'region_southeast', 'region_southwest', 'bmi_smoker'
])

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success(f"Estimated Cost: ${prediction[0]:,.2f}")