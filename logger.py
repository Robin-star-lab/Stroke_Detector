import logging
import os
import sys

logs_str = "[ %(asctime)s:%(levelname)s:%(module)s:%(message)s]"

log_dir = 'log'

if log_dir !="":
    os.makedirs(log_dir,exist_ok=True)
    
log_file_path = os.path.join(log_dir,'running.logs')

logging.basicConfig(
    level=logging.INFO,
    format=logs_str,
    handlers=[
        logging.FileHandler(log_file_path, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

my_logger = logging.getLogger('stroke_detection_logger')