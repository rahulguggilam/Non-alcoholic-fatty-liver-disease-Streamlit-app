import streamlit as st
import pickle
import numpy as np

# Load the pickled model
with open('Liver_project.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

st.title("Liver Disease Prediction")

# Define input fields for features
age = st.number_input("Age", 1, 100)
gender = st.radio("Gender", ["Male", "Female"])
total_bilirubin = st.number_input("Total Bilirubin", min_value=0.0)
alkaline_phosphatase = st.number_input(
    "Alkaline Phosphatase", min_value=0.0)
alamine_aminotransferase = st.number_input(
    "Alamine Aminotransferase", min_value=0.0)
aspartate_aminotransferase = st.number_input(
    "Aspartate Aminotransferase", min_value=0.0)
total_proteins = st.number_input("Total Proteins", min_value=0.0)
albumin = st.number_input("Albumin", min_value=0.0)
albumin_globulin_ratio = st.number_input(
    "Albumin/Globulin Ratio", min_value=0.0)

# Create a dictionary with user input
user_input = {
    "Age": age,
    "Gender": 1 if gender == "Male" else 0,  # Encode gender as 0 or 1
    "Total_Bilirubin": total_bilirubin,
    "Alkaline_Phosphatase": alkaline_phosphatase,
    "Alamine_Aminotransferase": alamine_aminotransferase,
    "Aspartate_Aminotransferase": aspartate_aminotransferase,
    "Total_Protiens": total_proteins,
    "Albumin": albumin,
    "Albumin_and_Globulin_Ratio": albumin_globulin_ratio
}

# Perform prediction when a button is clicked
if st.button("Predict"):
    # Prepare the input data in the format expected by the model
    input_data = np.array([user_input[feature]
                          for feature in user_input]).reshape(1, -1)

    # Make a prediction using the loaded model
    prediction = model.predict(input_data)

    # Display the prediction
    if prediction[0] == 1:
        st.error("Liver Disease")
        st.snow()
    else:
        st.success("No Liver Disease")
        st.balloons()
