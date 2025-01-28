from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig():
    root_url:Path
    source_url:str
    local_data_path:Path
    unzip_data:Path
    test_data:Path
    train_data:Path
    
@dataclass
class DataEvaluationConfig():
    root_url: Path
    data_directory: Path
    validation_status: str
    all_schema: str


@dataclass
class DataTransformationConfig():
    root_url: Path
    data_directory: Path
    transform_data_path: Path
    preprocessor_path: Path
    


@dataclass
class ModelTrainerConfig():
    # configuration for model trainer
    root_url: Path
    train_data_path: Path
    trained_model: Path
    parameters: dict
    epoch: int
    batch_size: int
    model_name: str
    
    

@dataclass
class ModelEvaluationConfig():
    root_url: Path
    evaluation_data: Path
    model_path: Path
    parameters: dict
    epoch: int
    batch_size: int