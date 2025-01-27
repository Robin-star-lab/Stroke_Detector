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
    