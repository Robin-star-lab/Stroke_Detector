from src.stroke_disease_detection.config.configuration import ModelTrainerConfigurationManager
from src.stroke_disease_detection.components.model_trainer import ModelTrainer
from Exceptions import CustomException
import sys


class ModelTrainerPipeline():
    def __init__(self):
        pass
    def main(self):
        # Training pipeline
        try:
            config = ModelTrainerConfigurationManager()
            get_model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=get_model_trainer_config)
            model_trainer.initiate_model_trainer()
        except Exception as e:
            raise CustomException(e,sys)
            