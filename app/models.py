from pydantic import BaseModel

class PredictionRequest(BaseModel):
    age: int
    years_on_the_job  : int
    nb_previous_loans : float
    avg_amount_loans_previous: float
    flag_own_car: float


class PredictionResponse(BaseModel):
    prediction: float