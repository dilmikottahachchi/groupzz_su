# Diabetes Follow-up Prediction API
## Project Overview
A machine learning service as part of the MAIO course that helps predict diabetes progression to determind it the patients need follow-up care.

## Getting Started
### Build and Train Locally
```bash
python src/train.py
```

### Run API locally
```bash
fastapi dev .\src\main.py
```

## API Definition
### Predict
POST `/predict`

```bash
curl --location --request POST 'http://127.0.0.1:8000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{"age": 0.02, "sex": -0.044, "bmi": 0.06, "bp": -0.03, "s1": -0.02, "s2": 0.03, "s3": -0.02, "s4": 0.02, "s5": 0.02, "s6": -0.001}'
```

Returns:

```json
{ "prediction": "123" }
```

### Health check

GET `/health`

```bash
curl --location --request GET 'http://127.0.0.1:8000/health' \
--header 'Content-Type: application/json'
```

Returns:

```json
{ "status": "ok", "model_version": "v0.1" }
```

### Docker

Build:

```bash
docker build -t diabetes-triage-ml:v0.1 .
```

Run:

```bash
docker run -p 8000:8000 diabetes-triage-ml:v0.1
```