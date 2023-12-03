# fastapi_app.py
from fastapi import FastAPI, HTTPException
import onnxruntime
from pydantic import BaseModel
import pandas as pd
import numpy as np
import pickle
from fastapi.requests import Request
from fastapi.responses import JSONResponse
app = FastAPI()

# Load the ONNX model and preprocessing transformers
onnx_model = onnxruntime.InferenceSession("models/best_model.onnx")
with open("models/preprocessing_transformations.pkl", "rb") as f:
    scaler = pickle.load(f)





# Define input schema using Pydantic
class InputData(BaseModel):
    bedrooms: float
    bathrooms: float
    sqft_living: float
    sqft_lot: float
    floors: float
    waterfront: float
    view: float
    condition: float
    grade: float
    sqft_above: float
    sqft_basement: float
    yr_built: float
    yr_renovated: float
    zipcode: float
    lat: float
    long: float
    sqft_living15: float
    sqft_lot15: float

# Define prediction endpoint
@app.post("/predict", response_model=dict)
def predict(data: InputData):
    # Preprocess input data
    input_data = pd.DataFrame([data.dict()])
    # Convert input data types to float
    input_data = input_data.astype(float)
    input_data_scaled = scaler.transform(input_data)
    
    # Convert input to numpy array
    # Convert input to numpy array with dtype=np.float32
    input_array = np.array(input_data_scaled, dtype=np.float32)

    

# Make prediction using ONNX model
    result = onnx_model.run(None, {"float_input": input_array})

# Extract the prediction
    prediction = result[0][0][0]
    print(prediction)   
    


    # Return the prediction as a dictionary
    return JSONResponse(content={"prediction": float(prediction)})

if __name__ == "__main__":
    import uvicorn


    uvicorn.run("app:app", port=8000, reload=True)