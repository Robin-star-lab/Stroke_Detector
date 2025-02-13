from flask import Flask,render_template,request
from Exceptions import CustomException
import sys
import numpy as np
import pandas as pd
from src.stroke_disease_detection.pipeline.prediction_pipeline import PredictionPipeline,CustomData

app = Flask(__name__)

@app.route('/',methods=['GET'])
def index():
    return render_template('index.html')
@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        try:
            # Reading inputsgiven by the user
            data = CustomData(
                age = int(request.form.get('age')),
                
                gender = str(request.form.get('gender')),
                hypertension = bool(request.form.get('hypertension')),
                heart_disease = bool(request.form.get('heart_disease')),
                ever_married = bool(request.form.get('ever_married')),
                work_type = str(request.form.get('work_type')),
                Residence_type = str(request.form.get('residence_type')),
                avg_glucose_level = float(request.form.get('avg_glucose_level')),
                bmi = float(request.form.get('bmi')),
                smoking_status = str(request.form.get('smoking_status'))
            )
            
            
            final_data = data.get_data_asdf()
            prediction = PredictionPipeline()
            my_predictions = prediction.predict(final_data)
            

            if isinstance(my_predictions, np.ndarray):
                # Check if it's a NumPy array
                if my_predictions.size == 1:
                    # Check if it has only one element
                     prediction_value = my_predictions.item()  # Extract the value
                else:
                    
                # Handle the case where there are multiple predictions
                # For example, take the first one:
                    prediction_value = my_predictions.flat[0]
            # Or choose another appropriate strategy
            else:
                # If it's not a NumPy array, try to get the first element
                try:
                    
                    prediction_value = my_predictions[0] 
                except (TypeError, IndexError):
                    # Handle potential errors
                    prediction_value = my_predictions # If it's already a single value

                    # Convert to integer AFTER extracting the single value
                    prediction_value = int(prediction_value) 

            return render_template('results.html', my_predictions=prediction_value)
            
        except Exception as e:
            raise CustomException(e,sys)
            

if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True, port = 8080)