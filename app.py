from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd
import joblib
import os

app = FastAPI()

# Get the directory where the current script is located
base_dir = os.path.dirname(__file__)

# Load the saved model and scaler with error handling
try:
    kmeans_model = joblib.load(os.path.join(base_dir, 'models', 'kmeans_model.pkl'))
    standard_scaler = joblib.load(os.path.join(base_dir, 'models', 'standard_scaler.pkl'))
except FileNotFoundError as e:
    raise HTTPException(status_code=500, detail=f"Model file not found: {e}")

class PredictionRequest(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

# Mount the templates directory
templates = Jinja2Templates(directory=os.path.join(base_dir, "templates"))

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        data = pd.DataFrame([request.dict()])  # Convert request data to DataFrame
        scaled_data = standard_scaler.transform(data)
        cluster = kmeans_model.predict(scaled_data)
        df = pd.read_csv(os.path.join(base_dir, 'models', 'app_data.csv'))

        # Filter the crops based on the predicted cluster
        df2 = df[df['cluster'] == cluster[0]]
        crops = list(df2['Label'].value_counts().keys())

        return JSONResponse(content={"cluster": crops})
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction error: {e}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
