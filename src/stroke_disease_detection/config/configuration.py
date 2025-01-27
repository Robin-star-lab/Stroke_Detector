
from src.constants import *
from src.stroke_disease_detection.entities.entities import DataIngestionConfig,DataEvaluationConfig,DataTransformationConfig
from src.stroke_disease_detection.utils.common import read_yaml,create_directories


class ConfigurationManager:
    def __init__(self, 
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        
        create_directories([self.config.Artifacts_root])
    
    def data_ingestion_config(self)->DataIngestionConfig:
        config = self.config.data_ingestion
        
        create_directories([config.root_url])
        get_data_ingestion_config = DataIngestionConfig(
            root_url = config.root_url,
            source_url = config.source_url,
            local_data_path = config.local_data_path,
            unzip_data = config.unzip_data,
            test_data = config.test_data,
            train_data = config.train_data
        )
        
        return get_data_ingestion_config



class DataEvaluationConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.schema = read_yaml(schema_file_path)
        
        create_directories([self.config.Artifacts_root])
    
    def get_data_evaluation_config(self)->DataEvaluationConfig:
        config = self.config.data_evaluation
        schema = self.schema
        
        create_directories([config.root_url])
        data_evaluation_config = DataEvaluationConfig(
            root_url=config.root_url,
            data_directory=config.data_directory,
            validation_status=config.validation_status,
            all_schema=schema.COLUMNS
        )
        
        return data_evaluation_config
    
    
    

class DataTransformationConfigurationManager():
    def __init__(self,
                 config_fie_path = CONFIG_FILE_PATH):
        self.config = read_yaml(config_fie_path)
        
        create_directories([self.config.Artifacts_root])
    
    def get_data_transformation_config(self)->DataTransformationConfig:
        config = self.config.data_transformation
        
        create_directories([config.root_url])
        data_transformation_config = DataTransformationConfig(
            root_url = config.root_url,
            data_directory = config.data_directory,
            transform_data_path = config.transform_data_path,
            preprocessor_path = config.preprocessor_path
        )
        
        return data_transformation_config
    
        