from src.stroke_disease_detection.config.configuration import DataTransformationConfigurationManager
from src.stroke_disease_detection.components.data_transformation import DataTransformation
from Exceptions import CustomException
import sys



class DataTransformationPipeline():
    def __init__(self):
        pass
    def main(self):
        try:
            config = DataTransformationConfigurationManager()
            get_data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(config=get_data_transformation_config)
            data_transformation.get_transform_data()
        except Exception as e:
            raise CustomException(e,sys)