from sklearn.datasets import load_diabetes
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import joblib
import json
import os
import numpy as np

# Train the model here
SEED = 42

# Load the diabetes dataset
Xy = load_diabetes(as_frame=True)
X = Xy.frame.drop(columns=["target"])
y = Xy.frame["target"] # acts as a "progression index" (higher = worse)

print(y)

# splitting the data for training and testing the model
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=SEED)

# Standardizing the data
scalar = StandardScaler()
X_train_scaled = scalar.fit_transform(X_train)
X_test_scaled = scalar.transform(X_test)

# Training the model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# Testing the model
y_pred = model.predict(X_test_scaled)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

# Save the artifacts
os.makedirs("model", exist_ok=True)
joblib.dump(scalar, "model/scaler.joblib")
joblib.dump(model, "model/model.joblib")

# Save metrics of model performance and versioning
metrics = {
    "rmse": rmse,
    "model_version": "v0.1"
}

with open("model/metrics.json", "w") as f:
    json.dump(metrics, f)

