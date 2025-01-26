from src.stroke_disease_detection.config.configuration import ConfigurationManager
from src.stroke_disease_detection.components.data_ingestion import DataIngestion
import sys
from Exceptions import CustomException



# Ingestion pipeline
class DataIngestionPipeline():
    def __init__(self):
        pass
    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            data_ingestion.load_data()
            data_ingestion.extract_data()
        except Exception as e:
            raise CustomException(e,sys)