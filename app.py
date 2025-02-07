from flask import Flask,render_template,request
from Exceptions import CustomException
import sys
import numpy as np
import pandas as pd
from src.stroke_disease_detection.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        try:
            # Reading inputsgiven by the user
            age = int(request.form.get(['age']))
            gender = str(request.form.get(['gender']))
            hypertension = int(request.form.get(['hypertension']))
            heart_disease = int(request.form.get(['heart_disease']))
            ever_married = str(request.form.get(['ever_married']))
            work_type = str(request.form.get(['work_type']))
            Residence_type = str(request.form.get(['residence_type']))
            avg_glucose_level = float(request.form.get(['avg_glucose_level']))
            bmi = float(request.form.get(['bmi']))
            smoking_status = str(request.form.get(['smoking_status']))
            
            data = [age,gender,hypertension,heart_disease,ever_married,work_type,Residence_type,avg_glucose_level,bmi,smoking_status]
            data = np.array(data).reshape(1,11)
            to_dataframe = pd.DataFrame(data)
            
            obj = PredictionPipeline()
            prediction = obj.predict(to_dataframe)
            
            return render_template('results.html',prediction=str(prediction))
        except Exception as e:
            raise CustomException(e,sys)
            

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 8080)