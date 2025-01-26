import logging
import os
from pathlib import Path


project_name = "stroke_disease_detection"
list_of_files = [
    "src/__init__.py",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/config/__init__.py"
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/entities/__init__.py",
    f"src/{project_name}/entities/entities.py",
    "Resources/trials.ipynb",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py"
]
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s : %(module)s : %(message)s]"
)

for filepath in list_of_files:
    filepath = Path(filepath)
    
    file_dir,file_name = os.path.split(filepath)
    
    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Directory {file_dir} created")
    else:
        logging.info(f"Directory {file_dir} already exists")
        
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath))==0:
            with open(filepath,'w') as f:
                pass
            logging.info(f"Created file: {file_name}")
    else:
            logging.info(f"File {file_name} already exists")