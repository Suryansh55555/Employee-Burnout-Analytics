
import streamlit as st
import joblib
import pandas as pd

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="AI-Powered Employee Burnout Analytics Platform",
    page_icon="",
    layout="wide"
)

# --------------------------------------------------
# LOAD MODEL
# --------------------------------------------------

model = joblib.load("burnout_model.pkl")

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

st.sidebar.title("Project Information")

st.sidebar.markdown("""
### Developed By
Suryansh Varshney

### Project
AI-Powered Employee Burnout Analytics Platform

### Model
Random Forest Regressor

### Performance
- R² Score: 0.893
- MAE: 0.049
- RMSE: 0.064
""")

st.sidebar.markdown("---")

st.sidebar.subheader("Risk Scale")

st.sidebar.success("0.00 – 0.33 : Low Risk")
st.sidebar.warning("0.34 – 0.66 : Medium Risk")
st.sidebar.error("0.67 – 1.00 : High Risk")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("AI-Powered Employee Burnout Analytics Platform")

st.markdown("""
This application predicts employee burnout risk using machine learning
and workforce analytics based on workload, mental fatigue, designation level,
and workplace conditions.
""")

st.markdown("---")

# --------------------------------------------------
# INPUT SECTION
# --------------------------------------------------

st.subheader("Employee Information")

designation_options = {
    "Junior Employee": 1,
    "Associate": 2,
    "Senior Associate": 3,
    "Manager": 4,
    "Senior Manager": 5
}

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

    company_type = st.selectbox(
        "Company Type",
        ["Service", "Product"]
    )

    designation_label = st.selectbox(
        "Designation Level",
        list(designation_options.keys())
    )

with col2:

    wfh = st.selectbox(
        "Work From Home Available",
        ["Yes", "No"]
    )

    resource = st.slider(
        "Workload Level",
        min_value=1,
        max_value=10,
        value=5,
        help="1 = Very Low Workload | 10 = Extremely High Workload"
    )

    fatigue = st.slider(
        "Mental Fatigue Score",
        min_value=0.0,
        max_value=10.0,
        value=5.0,
        help="0 = Relaxed | 10 = Extremely Fatigued"
    )

# --------------------------------------------------
# ENCODING
# --------------------------------------------------

gender_encoded = 1 if gender == "Male" else 0
wfh_encoded = 1 if wfh == "Yes" else 0
company_encoded = 1 if company_type == "Service" else 0

designation = designation_options[designation_label]

# --------------------------------------------------
# PREDICTION BUTTON
# --------------------------------------------------

if st.button("Generate Burnout Assessment"):

    input_data = pd.DataFrame({
        "Gender": [gender_encoded],
        "Company Type": [company_encoded],
        "WFH Setup Available": [wfh_encoded],
        "Designation": [designation],
        "Resource Allocation": [resource],
        "Mental Fatigue Score": [fatigue],
        "join_month": [6],
        "join_day": [15]
    })

    prediction = model.predict(input_data)[0]

    # --------------------------------------------------
    # RISK LEVEL
    # --------------------------------------------------

    if prediction < 0.33:

        risk = "LOW RISK"

        recommendation = """
        - Maintain current workload levels
        - Continue employee engagement initiatives
        - Monitor periodically
        """

    elif prediction < 0.66:

        risk = "MEDIUM RISK"

        recommendation = """
        - Monitor workload distribution
        - Encourage regular breaks
        - Review work-life balance
        - Conduct periodic check-ins
        """

    else:

        risk = "HIGH RISK"

        recommendation = """
        - Reduce workload where possible
        - Encourage leave utilization
        - Conduct wellness check-ins
        - Reassess task allocation
        """

    # --------------------------------------------------
    # METRICS
    # --------------------------------------------------

    st.markdown("---")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Predicted Burn Rate",
            value=f"{prediction:.2f}"
        )

    with col2:
        st.metric(
            label="Mental Fatigue",
            value=f"{fatigue:.1f}/10"
        )

    with col3:
        st.metric(
            label="Workload",
            value=f"{resource}/10"
        )

    # --------------------------------------------------
    # SEVERITY BAR
    # --------------------------------------------------

    st.subheader("Burnout Severity")

    st.progress(float(prediction))

    # --------------------------------------------------
    # RISK ASSESSMENT
    # --------------------------------------------------

    st.subheader("Risk Assessment")

    if prediction < 0.33:
        st.success(risk)

    elif prediction < 0.66:
        st.warning(risk)

    else:
        st.error(risk)

    # --------------------------------------------------
    # RECOMMENDATIONS
    # --------------------------------------------------

    st.subheader("Recommendations")

    st.info(recommendation)

    # --------------------------------------------------
    # KEY DRIVERS
    # --------------------------------------------------

    st.subheader("Key Drivers")

    drivers = []

    if fatigue >= 7:
        drivers.append("High Mental Fatigue Score")

    if resource >= 7:
        drivers.append("Heavy Workload Allocation")

    if wfh == "No":
        drivers.append("No Work-From-Home Support")

    if prediction >= 0.66 and designation >= 4:
        drivers.append("High Responsibility Role")

    if len(drivers) == 0:

        st.success(
            "No major burnout drivers detected."
        )

    else:

        for driver in drivers:
            st.write("•", driver)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Developed by Suryansh Varshney | AI-Powered Employee Burnout Analytics Platform"
)

