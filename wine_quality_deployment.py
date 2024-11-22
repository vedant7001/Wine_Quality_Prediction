# -- coding: utf-8 --

"""

Created on Tue Jun 18 00:49:07 2024



@author: VEDANT

"""



import numpy as np

import pickle

import streamlit as st



# Load the saved model

wine_model = pickle.load(open('wine_model.sav', 'rb'))

# Sidebar for navigation

with st.sidebar:

    selected = st.selectbox('Wine Quality Prediction System',

                            ['Wine Quality Prediction'],

                            index=0)



# Wine Quality Prediction Page

if selected == 'Wine Quality Prediction':



    # Page title

    st.title('Wine Quality Prediction using ML')



    # Input data from the user

    col1, col2, col3 = st.columns(3)



    with col1:

        fixed_acidity = st.text_input('Fixed Acidity')

    

    with col2:

        volatile_acidity = st.text_input('Volatile Acidity')

    

    with col3:

        citric_acid = st.text_input('Citric Acid')

    

    with col1:

        residual_sugar = st.text_input('Residual Sugar')

    

    with col2:

        chlorides = st.text_input('Chlorides')

    

    with col3:

        free_sulfur_dioxide = st.text_input('Free Sulfur Dioxide')

    

    with col1:

        total_sulfur_dioxide = st.text_input('Total Sulfur Dioxide')

    

    with col2:

        density = st.text_input('Density')

    

    with col3:

        pH = st.text_input('pH')

    

    with col1:

        sulphates = st.text_input('Sulphates')

    

    with col2:

        alcohol = st.text_input('Alcohol')



    # Code for prediction

    quality_prediction = ''



    # Create a button for prediction

    if st.button('Check Wine Quality'):

        try:

            # Convert input data to numpy array

            input_data = np.array([[fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,

                                    free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]]).astype(float)

            

            # Predict using the loaded model

            prediction = loaded_model.predict(input_data)

            

            # Interpret the prediction

            if prediction[0] == 1:

                quality_prediction = 'The wine is of good quality!'

            else:

                quality_prediction = 'The wine is of lower quality.'

        except Exception as e:

            st.error(f"Error in prediction: {e}")

    

    # Display the prediction result

    st.success(quality_prediction)

