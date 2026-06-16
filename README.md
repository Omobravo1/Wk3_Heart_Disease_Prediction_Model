# Heart Disease Prediction System

This repository contains a machine learning model and a Streamlit web application designed to predict the presence of heart disease based on various health parameters.

## Project Description

This project aims to provide a simple, interactive tool for predicting heart disease. The model is trained on a dataset containing medical attributes and uses Logistic Regression for classification. The Streamlit application allows users to input their health data and receive an instant prediction.

## Features

*   **Machine Learning Model:** A Logistic Regression model trained to predict heart disease.
*   **Streamlit Web Application:** An interactive user interface for making predictions.
*   **Data Preprocessing:** Handles data loading, initial exploration, and splitting into training and test sets.
*   **Model Evaluation:** Provides accuracy metrics for the trained model.

## Setup Instructions

To set up and run this project locally, follow these steps:

### 1. Clone the Repository

git clone <your-repository-url>
cd heart-disease-prediction

### 2. Create a Virtual Environment (Recommended)

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

### 3. Install Dependencies

Install the required Python packages using `pip`:

pip install -r requirements.txt

**Note:** If you don't have a `requirements.txt` file, you can create one from your Colab notebook using:

pip freeze > requirements.txt

### 4. Prepare the Model and Data

Ensure that the `heart_disease_model.sav` file (the trained model) and `heart_gtigwd.csv` (your dataset) are in the correct directories (e.g., in a `saved_models` directory for the model, and the root for the data as per the `app.py`).

## How to Run the Streamlit Application

Once the setup is complete, you can run the Streamlit application:

streamlit run app.py
```

This command will open the Streamlit application in your web browser. If it doesn't open automatically, navigate to `http://localhost:8501`.

## Model Performance

The Logistic Regression model achieved the following accuracy:

*   **Accuracy on Training Data:** 85.24%

## Usage

1.  **Input Data:** On the Streamlit app, enter the requested health parameters (Age, Sex, Chest Pain Type, etc.).
2.  **Get Prediction:** Click the "Heart Disease Test Result" button.
3.  **View Result:** The application will display whether the person is predicted to have heart disease or not.

## Technologies Used

*   **Python**
*   **Pandas**
*   **NumPy**
*   **Scikit-learn**
*   **Streamlit**
*   **Pyngrok** (for public URL in Colab environment)

## Dataset

The model was trained on the `heart_gtigwd.csv` dataset. (You may want to add more details about the dataset if publicly available, e.g., source, features explanation).