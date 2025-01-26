from src.stroke_disease_detection.config.configuration import DataEvaluationConfigurationManager
from src.stroke_disease_detection.components.data_evaluation import DataEvaluation
from Exceptions import CustomException
import sys



class DataEvaluationPipeline():
    def __init__(self):
        pass
    def main(self):
        try:
            config = DataEvaluationConfigurationManager()
            get_data_evaluation_config = config.get_data_evaluation_config()
            data_evaluation = DataEvaluation(config=get_data_evaluation_config)
            data_evaluation.evaluate_data()
        except Exception as e:
            raise CustomException(e,sys)