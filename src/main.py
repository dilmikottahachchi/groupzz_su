from fastapi import FastAPI

app = FastAPI()


@app.get("/predict")
async def root():
    return {"message": "Hello World"}

    
@app.get("/health")
async def root():
    return {"message": "Hello World"}