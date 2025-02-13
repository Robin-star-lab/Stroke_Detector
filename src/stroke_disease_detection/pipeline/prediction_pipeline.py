from tensorflow.keras.models import load_model
from pathlib import Path
from src.stroke_disease_detection.utils.common import load_json
import pandas as pd


class PredictionPipeline():
    def __init__(self):
        self.model = load_model(Path("artifacts\model_evaluator\model.keras"))
        self.preprocessor = load_json(Path("artifacts/data_transformation/preprocessor.pkl"))
    def predict(self,input_data):
        input_data = self.preprocessor.transform(input_data)
        prediction = self.model.predict(input_data)
        
        return prediction
    
    
class CustomData():
    def __init__(self,
                 age:int,
                 gender: str,
                 hypertension: bool,
                 heart_disease: bool,
                 ever_married: bool,
                 work_type: str,
                 Residence_type: str,
                 avg_glucose_level: float,
                 bmi: float,
                 smoking_status: str):
        self.age = age
        self.gender = gender
        self.hypertension = hypertension
        self.heart_disease = heart_disease
        self.ever_married = ever_married
        self.work_type = work_type
        self.Residence_type = Residence_type
        self.avg_glucose_level = avg_glucose_level
        self.bmi = bmi
        self.smoking_status = smoking_status
        
    def get_data_asdf(self):
        dataframe = {
            "age":[self.age],
            "gender":[self.gender],
            "hypertension":[self.hypertension],
            "heart_disease":[self.heart_disease],
            "ever_married":[self.ever_married],
            "work_type":[self.work_type],
            "Residence_type":[self.Residence_type],
            "avg_glucose_level":[self.avg_glucose_level],
            "bmi":[self.bmi],
            "smoking_status":[self.smoking_status]
            
        }
        
        df = pd.DataFrame(dataframe)
        return df

        