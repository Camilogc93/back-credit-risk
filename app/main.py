from fastapi import FastAPI
from views import get_prediction
from models import PredictionResponse, PredictionRequest


app = FastAPI()

@app.post('/prediction')
def make_model_prediction(request: PredictionRequest):
    
    response=get_prediction(request)
    #response=response.astype(int)
    #print(type(response))
    response= PredictionResponse(prediction=response)
    return response