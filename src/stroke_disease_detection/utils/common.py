from box import ConfigBox
from ensure import ensure_annotations
import yaml
from typing import List
from pathlib import Path
import logging
from logger import my_logger
import os
import pickle

@ensure_annotations
def read_yaml(filepath:Path)->ConfigBox:
    with open(filepath, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
        
        return ConfigBox(data)
 
@ensure_annotations    
def create_directories(filepath:List):
    for path in filepath:
        if path != "":
            os.makedirs(path,exist_ok=True)
        else:
            my_logger.info("Folder already exists")
            
            
@ensure_annotations
def save_json(preprocessor,filepath):
    with open(filepath,'wb') as f:
        pickle.dump(preprocessor,f)
        
        
    
        