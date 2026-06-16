import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# Set page configuration
st.set_page_config(page_title="Heart Disease Prediction", layout="wide", page_icon=":heart:")

# Determine the path for the model
# In Colab, the model is saved in /content/saved_models/heart_disease_model.sav
# When run via Streamlit locally, it will be in saved_models/heart_disease_model.sav
model_path = 'saved_models/heart_disease_model.sav'
if not os.path.exists(model_path):
    # This handles the case where Streamlit might be run from the root, not /content/
    # Adjust if your deployment strategy changes
    model_path = '/content/saved_models/heart_disease_model.sav'

# Loading the saved model
try:
    loaded_model = pickle.load(open(model_path, 'rb'))
except FileNotFoundError:
    st.error(f"Model file not found at {model_path}. Please ensure the model is saved correctly.")
    st.stop() # Stop execution if model is not found

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Heart Disease Prediction System',
                           ['Home'],
                           icons=['house'],
                           default_index=0)

# Home Page
if selected == 'Home':
    st.title('Heart Disease Prediction using Machine Learning')

    # Getting input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.selectbox('Sex', options=[0, 1], format_func=lambda x: 'Female' if x == 0 else 'Male')
    with col3:
        cp = st.text_input('Chest Pain Type (0-3)')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure (mm Hg)')
    with col2:
        chol = st.text_input('Cholesterol (mg/dl)')
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Results (0-2)')
    with col2:
        thalach = st.text_input('Maximum Heart Rate Achieved')
    with col3:
        exang = st.selectbox('Exercise Induced Angina', options=[0, 1], format_func=lambda x: 'No' if x == 0 else 'Yes')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise relative to rest')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment (0-2)')
    with col3:
        ca = st.text_input('Number of major vessels (0-4) colored by fluoroscopy')
    with col1:
        thal = st.text_input('Thalassemia (0-3)')

    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            # Convert all inputs to appropriate numerical types
            input_data = [float(age), float(sex), float(cp), float(trestbps), float(chol),
                          float(fbs), float(restecg), float(thalach), float(exang),
                          float(oldpeak), float(slope), float(ca), float(thal)]

            # Change the input data to a numpy array
            input_data_as_numpy_array = np.asarray(input_data)

            # Reshape the numpy array as we are predicting for only one instance
            input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

            prediction = loaded_model.predict(input_data_reshaped)

            if prediction[0] == 0:
                heart_diagnosis = 'The person does not have Heart Disease'
            else:
                heart_diagnosis = 'The person has Heart Disease'
        except ValueError:
            heart_diagnosis = 'Please enter valid numerical values for all inputs.'
        except Exception as e:
            heart_diagnosis = f'An error occurred: {e}'

    st.success(heart_diagnosis)
