### fraud_detection_portal/backend/model/train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
import shap
import joblib

# Load dataset
data = pd.read_csv('data/creditcard.csv')
X = data.drop('Class', axis=1)
y = data['Class']

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42)

# Train model
model = XGBClassifier(use_label_encoder=False, eval_metric='logloss')
model.fit(X_train, y_train)

# SHAP
explainer = shap.Explainer(model)
shap_values = explainer(X_test[:100])

# Save
joblib.dump(model, 'backend/model/fraud_model.pkl')
joblib.dump(shap_values, 'backend/model/shap_values.pkl')