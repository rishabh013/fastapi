from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import UserInput
from models.predict import predict_output, MODEL_VERSION, model
from schema.prediction_response import PredictionResponse

app = FastAPI()

# Any person will be in the home page the below message will be shown
# humman redable message
@app.get('/')
def home():
    return {'message': 'Insurance Premium Prediction API'}

# health check endpoints
# Machine redable message
@app.get('/health')
def health_check():
    return {'status': 'ok',
            'model_version': MODEL_VERSION,
            'model_loaded': model is not None}

@app.post('/predict', response_model= PredictionResponse)
def predict_premium(data: UserInput):

    input_df = {
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }
    try:
        prediction = predict_output(input_df)

        return JSONResponse(status_code=200, content={'response': prediction})
    
    except Exception as e:
        return JSONResponse(status_code=500, content={'error': str(e)})
