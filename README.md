# AI-Powered Employee Burnout Analytics Platform

Developed by: Suryansh Varshney

## Project Overview

This machine learning application predicts employee burnout risk using workforce analytics and behavioral indicators such as:

* Mental Fatigue Score
* Resource Allocation
* Designation Level
* Work From Home Availability
* Company Type
* Gender

The project combines machine learning, explainable AI, and interactive deployment to assist HR teams in identifying burnout risks and supporting employee wellbeing initiatives.

---

## Problem Statement

Employee burnout can negatively impact productivity, retention, and overall workplace wellbeing.

This project aims to predict burnout risk using historical employee data and provide actionable recommendations to HR professionals.

---

## Dataset

Employee Burnout Analysis Dataset

Features include:

* Gender
* Company Type
* WFH Setup Available
* Designation
* Resource Allocation
* Mental Fatigue Score
* Burn Rate

---

## Machine Learning Workflow

1. Data Cleaning
2. Missing Value Treatment
3. Feature Engineering
4. Exploratory Data Analysis
5. Linear Regression
6. Random Forest Regression
7. Feature Importance Analysis
8. SHAP Explainability
9. Streamlit Deployment

---

## Model Performance

| Model                    | R² Score |
| ------------------------ | -------: |
| Linear Regression        |    0.868 |
| Random Forest Regression |    0.893 |

Random Forest was selected as the final model.

---

## Key Findings

* Mental Fatigue Score was the strongest burnout predictor.
* Resource Allocation significantly influenced burnout risk.
* Employees with Work-From-Home availability showed lower burnout levels.
* Designation level contributed moderately to burnout prediction.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* SHAP
* Streamlit
* Matplotlib
* Seaborn

---

## Deployment

Streamlit Application:

https://employee-burnout-analytics.streamlit.app/

---

## Author

Suryansh Varshney
