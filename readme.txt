https://medical-insurance-cost-prediction-8dk4bj5po9xfzjrjgz6bmc.streamlit.app/
Overview
Predicting medical insurance charges using the Medical Cost Dataset.
The project focuses on improving a baseline Linear Regression model through feature engineering based on exploratory data
analysis (EDA).
Data Insights & Engineering
The Interaction Effect: EDA showed that BMI doesn't increase costs linearly for everyone; its impact is significantly
amplified for smokers.
Custom Feature: Engineered an interaction term: bmi_smoker = bmi * smoker_yes.
Result: This single addition raised the R^2 score from 0.78 to 0.86, capturing the variance that the baseline model missed.
Model ComparisonModelR2 
ScoreLinear Regression (Baseline)0.783
Linear Regression (Optimized)
0.865Random Forest Regressor0.865
Note: I opted for the Optimized Linear Regression as the final model because it provides the same predictive
power as Random Forest but with much better interpretability and lower computational overhead.
Key Tools
Analysis: **Pandas, Seaborn, Matplotlib**.
ML: **Scikit-learn** (LinearRegression, RandomForestRegressor).
Interactive Web App
Deployment: Deployed a real-time predictor using Streamlit.
Functionality: The app accepts user metrics (Age, BMI, Smoking status) and applies the same feature
engineering logic (bmi_smoker) to output a cost estimate.

Usage: Run streamlit run app.py to launch the local interface.
