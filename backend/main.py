### fraud_detection_portal/backend/main.py

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import shap
import psycopg2
from backend.database.db import insert_prediction

app = FastAPI()

model = joblib.load("backend/model/fraud_model.pkl")
explainer = shap.Explainer(model)

class Transaction(BaseModel):
    features: list

@app.post("/predict")
def predict(transaction: Transaction):
    data = pd.DataFrame([transaction.features])
    prediction = model.predict(data)[0]
    shap_values = explainer(data)
    explanation = shap_values.values.tolist()[0]
    insert_prediction(transaction.features, int(prediction), explanation)
    return {"prediction": int(prediction), "explanation": explanation}