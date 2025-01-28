from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model
import pandas as pd
import tensorflow as tf
from src.stroke_disease_detection.entities.entities import ModelEvaluationConfig




class ModelEvaluation():
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config
    
    def initiate_evaluation(self):
        
        test_data = pd.read_csv(self.config.evaluation_data)
        X = test_data.iloc[:,0:-1]
        Y = test_data.iloc[:,-1]
        le = LabelEncoder()
        Y = le.fit_transform(test_data.iloc[:,-1])
        Y = to_categorical(Y)
        
        
        model = load_model(self.config.model_path)
        loss,accuracy = model.evaluate(X,Y)
        
        # Create a SummaryWriter for validation logs
        val_summary_writer = tf.summary.create_file_writer(logdir="logs/val")
        with val_summary_writer.as_default():
            
            tf.summary.scalar('loss', loss, step=self.config.epoch)
            tf.summary.scalar('accuracy', accuracy, step=self.config.epoch)
         # ... other metrics 

        