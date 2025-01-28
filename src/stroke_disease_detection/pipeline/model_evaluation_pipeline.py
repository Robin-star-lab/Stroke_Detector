from Exceptions import CustomException
import sys
from src.stroke_disease_detection.config.configuration import ModelEvaluationConfigManager
from src.stroke_disease_detection.components.model_evaluation import ModelEvaluation



class ModelEvaluationPipeline():
    def __init__(self):
        pass
    def main(self):
        try:
            
            config = ModelEvaluationConfigManager()
            get_model_evalaution = config.get_model_evalaution()
            model_evaluation = ModelEvaluation(config=get_model_evalaution)
            model_evaluation.initiate_evaluation()
        except Exception as e:
            raise CustomException(e,sys)
        