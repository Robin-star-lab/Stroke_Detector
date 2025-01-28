from src.stroke_disease_detection.entities.entities import ModelTrainerConfig
import tensorflow as tf
from tensorflow import keras
from Exceptions import CustomException
import sys
import os
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd
from src.stroke_disease_detection.utils.common import read_yaml,create_directories





class ModelTrainer():
    def __init__(self, config: ModelTrainerConfig):
        self.config = config
        
    def initiate_model_trainer(self):
        train_data = self.config.train_data_path
        data = pd.read_csv(train_data)
        X = data.iloc[:,0:-1]
        le = LabelEncoder()
        Y = le.fit_transform(data.iloc[:,-1])
        Y = to_categorical(Y)
        # Split the data
        x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=42)
        # Initialize the model
        model = Sequential([
            Dense(64,activation='relu'),
            Dense(64, activation='relu'),
            Dense(2,activation='softmax')
        ])
        
        model.compile(loss='binary_crossentropy', optimizer='adam',metrics=['accuracy'])
        # Trian the model
        model.fit(x_train, y_train,self.config.batch_size,self.config.epoch,verbose=2)
        # Evaluate the model
        model.save(os.path.join(self.config.model_name,'model.h5'))