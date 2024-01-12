import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np

# loading the saved models

diabetes_model = pickle.load(open('./Liverrandom.pkl', 'rb'))
# sidebar for navigation


def diabetes_prediction(input_data):
    # changing the input data to numpy
    input_data_as_numpy_array = np.asarray(input_data)
    # reshape the array as we are predicting
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    prediction = diabetes_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0] == 1):
        return 'The person has  disease'
    else:
        return 'The person doesn\'t have disease'
# diagnosis = diabetes_prediction ([Pregnancies, Glucose, Blood Pressure, SkinThickness, Insul


with st.sidebar:

    selected = option_menu('Liver Disease Prediction System',

                           ['Liver Prediction'],
                           icons=['activity'],
                           default_index=0)


# Diabetes Prediction Page
if (selected == 'Liver Prediction'):

    # page title
    st.title('Liver Disease Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.text_input('Age')

    with col2:
        Gender = st.text_input('Gender(enter male for 0 and female for 1)')

    with col3:
        Total_bilirubin = st.text_input('Total_bilirubin')

    with col1:
        Alkaline_Phosphotase = st.text_input('Alkaline_Phosphotase')

    with col2:
        Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')

    with col3:
        Aspartate_Aminotransferase = st.text_input(
            'Aspartate_Aminotransferase')

    with col1:
        Total_Protiens = st.text_input('Total_Protiens')

    with col2:
        Albumin = st.text_input('Albumin')

    with col3:
        Albumin_and_Globulin_Ratio = st.text_input(
            'Albumin_and_Globulin_Ratio')

    # code for Prediction
diab_diagnosis = ''

# creating a button for Prediction
if st.button('Liver Test Result'):
    # Convert string input values to numeric values
    Age = int(Age)
    Gender = float(Gender)
    Total_bilirubin = float(Total_bilirubin)
    Alkaline_Phosphotase = float(Alkaline_Phosphotase)
    Alamine_Aminotransferase = float(Alamine_Aminotransferase)
    Aspartate_Aminotransferase = float(Aspartate_Aminotransferase)
    Total_Protiens = float(Total_Protiens)
    Albumin = float(Albumin)
    Albumin_and_Globulin_Ratio = float(Albumin_and_Globulin_Ratio)

    # Make prediction
    diab_prediction = diabetes_prediction([[Age, Gender, Total_bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase,
                                          Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])
    print(diab_prediction)
    if diab_prediction == 'The person has disease':
        diab_diagnosis = 'The person has liver disease'
    else:
        diab_diagnosis = 'The person has no liver disease'

    if diab_diagnosis == 'The person has liver disease':
        title = "diab_diagnosis"

        st.title(title)

        st.success(f"Success: {title}")

        # st.error(diab_diagnosis)

    else:
        # st.success(diab_diagnosis)
        title = diab_diagnosis

        st.title(title)

        st.success(f"Success: {title}")

    #st.success("Prediction:", diab_prediction)
