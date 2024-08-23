
import streamlit as st
import pickle

# load pkl file
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


# Check the number of features the model expects
n_features = model.n_features_in_

# Streamlit App
st.title("Linear Regression Prediction")

# Input features
st.sidebar.header("Input Features")
feature_1 = st.sidebar.number_input("Feature 1", value=1.0)
feature_2 = st.sidebar.number_input("Feature 2", value=2.0)
feature_3 = st.sidebar.number_input("Feature 3", value=3.0)

# Prepare the input data
input_data = np.array([[feature_1, feature_2, feature_3]])

# Check if the input data has the correct number of features
if input_data.shape[1] != n_features:
    st.error(f"The model expects {n_features} features, but received {input_data.shape[1]} features.")
else:
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display the prediction
    st.write("### Predicted Output")
    st.write(prediction[0])
