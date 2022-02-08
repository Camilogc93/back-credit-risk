from models import PredictionRequest
from utils import get_model, transform_to_dataframe
from pydantic import BaseModel
from pandas import DataFrame
import aporia
import uuid
model = get_model()

###### Initiate Aporia ######
aporia.init(token="0f1dd74d2344ea2d2eb52f793bce3c46e1dfb88b0d497e863e0ae20845b98bb0", 
            environment="local-dev", 
            verbose=True)



###### Report Version Schema ######
apr_model_version = "Credit-risk-v1"
# apr_model_type = "binary"
# apr_features_schema = {
#     "age": "numeric",
#     "years_on_the_job": "numeric",
#     "nb_previous_loans": "numeric",
#     "avg_amount_loans_previous": "numeric",
#     "flag_own_car": "numeric",
# }

# apr_predictions_schema = {
#     "prediction": "numeric",
   
# }
# apr_model = aporia.create_model_version(
#     model_id="credit-risk-i2aw",
#     model_version=apr_model_version,
#     model_type=apr_model_type,
#     features=apr_features_schema,
#     predictions=apr_predictions_schema
# )



def get_prediction(request: PredictionRequest):
   # print('request')
   # print(request)
    data_to_predict,dictionary = transform_to_dataframe(request)
    prediction = model.predict(data_to_predict)[0]
   # print(prediction)
    output= {'prediction':prediction}
 
    
    new_dict={
    "age": dictionary["age"][0],
    "years_on_the_job":  dictionary["years_on_the_job"][0],
    "nb_previous_loans": dictionary["nb_previous_loans"][0],
    "avg_amount_loans_previous": dictionary["avg_amount_loans_previous"][0],
    "flag_own_car": dictionary["flag_own_car"][0],
}
    
    apr_model = aporia.Model('credit-risk-i2aw',apr_model_version)
    apr_prediction_id = "pred_1337"

    apr_model.log_prediction(
    id=str(uuid.uuid4()),
    features=new_dict,
    predictions=output,
                                    )

    apr_model.flush()


    #print(prediction)
    return prediction

