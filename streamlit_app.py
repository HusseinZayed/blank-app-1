
import streamlit as st
import pickle
import numpy as np

# load pkl file
with open('modell.pkl', 'rb') as file:
    model = pickle.load(file)




# Streamlit App
st.title("Linear Regression Prediction")

# Input features
st.sidebar.header("Input Features")
feature_1 = st.sidebar.number_input("Feature 1", value=1.0)
feature_2 = st.sidebar.number_input("Feature 2", value=2.0)
feature_3 = st.sidebar.number_input("Feature 3", value=3.0)

# Prepare the input data
input_data = np.array([[feature_1, feature_2, feature_3]])

prediction = model.predict(input_data)
    
# Display the prediction
st.write("### Predicted Output")
st.write(prediction[0])
