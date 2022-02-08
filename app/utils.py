from joblib import load

from pydantic import BaseModel
from pandas import DataFrame
import os 
from io import BytesIO,StringIO
from dvc import api



def get_model():

    
   #print(model)

    model = load('model/model_risk.joblib')
    return model


def transform_to_dataframe(class_model: BaseModel):
    transition_dictionary = {key:[value] for key, value in class_model.dict().items()}
    data_frame = DataFrame(transition_dictionary)
    return data_frame,transition_dictionary


