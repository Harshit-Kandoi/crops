from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd
import joblib

app = FastAPI()

# Load the saved model and scaler
kmeans_model = joblib.load('models/kmeans_model')
standard_scaler = joblib.load('models/standard_scaler')

class PredictionRequest(BaseModel):
    N: float
    P: float
    K: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float  # Add rainfall to the request model

# Mount the templates directory
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict")
def predict(request: PredictionRequest):
    data = pd.DataFrame([request.model_dump()])  # Use model_dump instead of dict
    scaled_data = standard_scaler.transform(data)
    cluster = kmeans_model.predict(scaled_data)
    df = pd.read_csv('./models/app_data.csv')
    # print(cluster)
    # print(type(cluster))
    # print(df)
    df2 = df[df['cluster']==cluster[0]]
    crops = list(df2['Label'].value_counts().keys())
    # print(crops)
    # return crops
    return JSONResponse(content={"cluster": crops})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
