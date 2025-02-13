from sklearn.model_selection import train_test_split
import sys
from Exceptions import CustomException
import numpy as np
import pandas as pd
import os
from src.stroke_disease_detection.entities.entities import DataTransformationConfig
from imblearn.over_sampling import SMOTE
from sklearn.compose import ColumnTransformer
from sklearn.impute import  SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from src.stroke_disease_detection.utils.common import read_yaml, create_directories,save_json



class DataTransformation():
    def __init__(self,config:DataTransformationConfig):
        self.config = config
        
    def get_transform_data(self):
        transform_data = self.config.data_directory
        folder_path = self.config.transform_data_path
        data = pd.read_csv(transform_data)
        data = data.drop(columns='id',axis=1)
        
        data['stroke'] = data['stroke'].replace({"No":'None-stroke',"yes":'stroke'})
        data[['hypertension','heart_disease']]=data[['hypertension','heart_disease']].replace({0:'No',1:'Yes'})
    
        X = data.drop(columns='stroke',axis=1)
        Y = data['stroke']
        
        numerical_columns = X.select_dtypes(exclude='object').columns
        categorical_columns = X.select_dtypes(include='object').columns
        
        x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=0.3,random_state=42)
        
        # Define the transformers separately first
        categorical_pipeline = Pipeline([
            
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('encoder', OneHotEncoder(handle_unknown='ignore')),
            ('scaler', StandardScaler(with_mean=False))
            ])

        numerical_pipeline = Pipeline([
            ('imputer', SimpleImputer(strategy='median')),
            ('scaler', StandardScaler())
            ])

         # Create the final preprocessor
        preprocessor = ColumnTransformer([
            ('categorical', categorical_pipeline, categorical_columns),
            ('numerical', numerical_pipeline, numerical_columns)
            ])

        
        # Add this before saving the preprocessor
        os.makedirs(self.config.preprocessor_path, exist_ok=True)

        
        
        
        preprocessor.fit(x_train)
        
        save_json(preprocessor,os.path.join(self.config.preprocessor_path,'preprocessor.pkl'))

        x_train_transformed = preprocessor.transform(x_train)
        
        smote = SMOTE(sampling_strategy='auto')
        x_train_balanced, y_train_balanced = smote.fit_resample(x_train_transformed, y_train)
        x_test_transformed = preprocessor.transform(x_test)
        x_test_balanced, y_test_balanced = smote.fit_resample(x_test_transformed, y_test)
        
        scaled_train_df = pd.DataFrame(x_train_balanced,columns = preprocessor.get_feature_names_out())
        scaled_test_df = pd.DataFrame(x_test_balanced,columns = preprocessor.get_feature_names_out())
        
        scaled_train_array = np.c_[scaled_train_df,np.array(y_train_balanced)]
        scaled_test_array = np.c_[scaled_test_df,np.array(y_test_balanced)]
        
        scaled_train = pd.DataFrame(scaled_train_array)
        scaled_test = pd.DataFrame(scaled_test_array)
        
        scaled_train.to_csv(os.path.join(folder_path,'train_data.csv'),index=False)
        scaled_test.to_csv(os.path.join(folder_path,'test_data.csv'),index=False)

        