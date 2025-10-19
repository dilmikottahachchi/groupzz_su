from fastapi import FastAPI
from sklearn.datasets import load_diabetes
import joblib
import json
import numpy as np
from pydantic import BaseModel

app = FastAPI()

# Use the trained scalar and model from the training script
scalar = joblib.load("model/scaler.joblib")
model = joblib.load("model/model.joblib")
with open("model/metrics.json") as f:
    metrics = json.load(f)

FEATURES = ["age", "sex", "bmi", "bp", "s1", "s2", "s3", "s4", "s5", "s6"]

class PredictRequest(BaseModel):
    age: float
    sex: float
    bmi: float
    bp: float
    s1: float
    s2: float
    s3: float
    s4: float
    s5: float
    s6: float

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "model_version": "v0.1"
    }

# To predict if the patient needed follow ups
@app.post("/predict")
async def predict(input: PredictRequest):
    try:
        X = np.array([[getattr(input, feat) for feat in FEATURES]])
        X_scaled = scalar.transform(X)
        pred = model.predict(X_scaled)[0]
        return {"prediction": float(pred)}
    except Exception as e:
        return {"status": "error", "details": str(e)}