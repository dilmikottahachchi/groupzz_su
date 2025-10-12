from fastapi import FastAPI
from sklearn.datasets import load_diabetes

app = FastAPI()

# Health check endpoint
@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "model_version": "0.1.0"
    }

# To predict if the patient needed follow ups
@app.get("/predict")
async def predict():
    # Load the diabetes dataset
    Xy = load_diabetes(as_frame=True)
    X = Xy.frame.drop(columns=["target"])
    y = Xy.frame["target"] # acts as a "progression index" (higher = worse)

    return { "age": 0.02, "sex": -0.044, "bmi": 0.06, "bp": -0.03, "s1": -0.02, "s2": 0.03, "s3": -0.02, "s4": 0.02, "s5": 0.02, "s6": -0.001 }