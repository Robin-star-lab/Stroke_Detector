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