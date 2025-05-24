### fraud_detection_portal/frontend/app.py

import streamlit as st
import requests

st.title("Fraud Detection Portal with Explainable AI")

features = st.text_input("Enter 30 transaction features, comma-separated:")
if st.button("Predict"):
    try:
        feature_list = [float(x.strip()) for x in features.split(',')]
        response = requests.post("http://backend:8000/predict", json={"features": feature_list})
        result = response.json()
        st.write(f"Prediction: {'Fraud' if result['prediction'] == 1 else 'Not Fraud'}")
        st.write("SHAP Explanation:")
        st.json(result['explanation'])
    except Exception as e:
        st.error(f"Error: {e}")