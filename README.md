### fraud_detection_portal/README.md

# Fraud Detection Portal with Explainable AI

## Description
An interactive web application to predict and explain credit card fraud using an XGBoost model and SHAP values.

## Run Instructions
1. Clone repo and download `creditcard.csv` into `data/` folder.
2. Train model: `python backend/model/train_model.py`
3. Start services: `docker-compose up --build`

## Tech Stack
- Streamlit (frontend)
- FastAPI (backend)
- PostgreSQL (database)
- SHAP + XGBoost (AI model)
- Docker (deployment)

## API Endpoint
- `POST /predict` — Accepts transaction features, returns prediction and SHAP explanation.

## Data Source
[Credit Card Fraud Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)


