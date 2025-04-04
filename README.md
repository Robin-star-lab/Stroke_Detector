# Stroke Detection Machine Learning Application

This repository contains an end-to-end machine learning application designed to predict the likelihood of a stroke based on various patient health parameters. The model is built with dynamic training parameters, allowing for fine-tuning to achieve optimal prediction performance.

## Table of Contents

- Introduction
- Features
- Installation
- Usage
- Model Details
- Dynamic Parameter Tuning
- Dataset
- Evaluation
- Contributing
- License
- Contact

## Introduction

Stroke is a serious medical condition requiring immediate attention. This application aims to provide a rapid and accessible tool for preliminary stroke risk assessment. By leveraging machine learning, it analyzes patient data to predict the probability of a stroke, assisting medical professionals in early detection and intervention.

## Features

- **End-to-End Prediction:** Processes input data and delivers a stroke prediction output.
- **Dynamic Training Parameters:** Allows for flexible model tuning and optimization.
- **User-Friendly Interface (If applicable):** [A CLI UI is implimented.Though hosted locally]
- **Data Preprocessing:** Handles missing values, categorical encoding, and feature scaling.
- **Model Persistence:** Saves and loads trained models for future use.
- **Comprehensive Evaluation Metrics:** Provides insights into model performance.

## Installation

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/Robin-star-lab/Stroke-Detector.git]
    cd Stroke-Detector
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    conda create -n stroke
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application (adjust as needed):**

    ```bash
    python main.py  # Or whatever your main script is called.
    ```

2.  **Input patient data as  through the UI.**

3.  **Receive the stroke prediction output.**

   * **Example Input format(If applicable):**
     * age: 67
     * hypertension: 0
     * heart_disease: 1
     * avg_glucose_level: 228.69
     * bmi: 36.6
     * gender: Male
     * ever_married: Yes
     * work_type: Private
     * Residence_type: Urban
     * smoking_status: formerly smoked

4.  **Prediction Output:**
    * Probability of Stroke: 0.85 (Example)
    * Prediction: High stroke risk

## Model Details

-   **Model Architecture:** [Deep learning with 3 layers of neural network.As the dataset used in training is small]
-   **Key Libraries:** tensorflow, pandas, numpy, etc.
-   **Feature Engineering:** Data transformation pipeline with,onehotencoder,simpleimpute and standard scaler

## Dynamic Parameter Tuning

The application allows for dynamic tuning of the following training parameters:

All parameters can be fine-tuned inside params.yaml file.
My UI is made by the front-end person.Who is in the contributors list.