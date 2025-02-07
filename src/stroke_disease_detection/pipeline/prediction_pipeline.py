from tensorflow.keras.models import load_model
from pathlib import Path
from src.stroke_disease_detection.utils.common import load_json


class PredictionPipeline():
    def __init__(self):
        self.model = load_model(Path("artifacts\model_trainer\model.keras"))
        self.preprocessor = load_json(Path("artifacts\data_transformation\preprocessor.pkl"))
    def predict(self,input_data):
        input_data = self.preprocessor.transform(input_data)
        prediction = self.model.predict(input_data)
        
        return prediction
    

        