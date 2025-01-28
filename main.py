from src.stroke_disease_detection.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.stroke_disease_detection.pipeline.data_evaluation_pipeline import DataEvaluationPipeline
from src.stroke_disease_detection.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.stroke_disease_detection.pipeline.model_trainer_pipeline import ModelTrainerPipeline
from src.stroke_disease_detection.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline
from Exceptions import CustomException
import sys
from logger import my_logger
stage_name = "Data Ingestion Stage"

if __name__=='__main__':
    obj = DataIngestionPipeline()
    obj.main()
    
    my_logger.info(f"======{stage_name}======Successfully Completed.")
    
    
stage_name = "Data Evaluation Stage"  
if __name__ == '__main__':
    pipeline = DataEvaluationPipeline()
    pipeline.main()
    
    my_logger.info(f"======{stage_name}======Successfully Completed.")
    
    
stage_name = "Data Transformation Stage"
if __name__ == '__main__':
    pipeline  = DataTransformationPipeline()
    pipeline.main()
        
    my_logger.info(f"======{stage_name}======Successfully Completed.")
    
    
stage_name = 'Model Training Stage'
if __name__ == '__main__':
    pipeline = ModelTrainerPipeline()
    pipeline.main()
    
    my_logger.info(f"======{stage_name}======Successfully Completed.")
    
    
stage_name = 'Model Evaluation Stage'
if __name__ == '__main__':
    pipeline = ModelEvaluationPipeline()
    pipeline.main()
    
    my_logger.info(f"======{stage_name}======Successfully Completed.")
    