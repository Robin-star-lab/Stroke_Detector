from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.models import load_model
import pandas as pd
import tensorflow as tf
from src.stroke_disease_detection.utils.common import read_yaml,create_directories
import os
from src.stroke_disease_detection.entities.entities import ModelEvaluationConfig




class ModelEvaluation():
    def __init__(self, config:ModelEvaluationConfig):
        self.config = config
    
    def initiate_evaluation(self):
        
        test_data = pd.read_csv(self.config.evaluation_data)
        path = self.config.model_name
        if path != "":
            os.makedirs(path,exist_ok=True)
        
        X = test_data.iloc[:,0:-1]
        
        le = LabelEncoder()
        Y = le.fit_transform(test_data.iloc[:,-1])
        Y = to_categorical(Y)
        
        
        model = load_model(self.config.model_path)
        model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
        model.fit(X, Y,self.config.batch_size,self.config.epoch,verbose=2)
        loss,accuracy = model.evaluate(X,Y)
        
        # save evaluated model
        model.save(os.path.join(self.config.model_name,'model.keras'))
        
        
        
        
        # Trian the model
       