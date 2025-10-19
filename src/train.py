from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import json

# load data
Xy = load_diabetes(as_frame=True)
X = Xy.frame.drop(columns=["target"])
y = Xy.frame["target"]

# split data
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# training model
model = LinearRegression()
model.fit(X_train_scaled, y_train)

# make predictions
y_pred = model.predict(X_test_scaled)

# calculate metrics
metrics = {
    "rmse": mean_squared_error(y_test, y_pred, squared=False),
    "r2": r2_score(y_test, y_pred)
}

# save artifacts
joblib.dump(scaler, "model/scaler.joblib")
joblib.dump(model, "model/model.joblib")
with open("model/metrics.json", "w") as f:
    json.dump(metrics, f, indent=2)
