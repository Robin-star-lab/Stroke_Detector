from src.stroke_disease_detection.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.stroke_disease_detection.pipeline.data_evaluation_pipeline import DataEvaluationPipeline
from logger import my_logger
stage_name = "Data Ingestion Stage"

if __name__=='__main__':
    obj = DataIngestionPipeline()
    obj.main()
    
    my_logger.info(f"======{stage_name}======Successfully Completed.")
    
    
    
if __name__ == '__main__':
    pipeline = DataEvaluationPipeline()
    pipeline.main()
    
    my_logger.info(f"======{stage_name}======Successfully Completed.")
    