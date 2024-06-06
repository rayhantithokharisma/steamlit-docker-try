import streamlit as st
import joblib

# Load the saved model
model = joblib.load('iris_model.pkl')

# Define feature names
feature_names = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

# Streamlit app
st.title('Iris Flower Classification')
st.write('Please enter the following information:')

# Get input feature values from the user
input_features = []
for feature_name in feature_names:
    value = st.number_input(f'Enter {feature_name}', step=0.1)
    input_features.append(value)

if st.button('Submit'):
    # Make a prediction
    prediction = model.predict([input_features])[0]

    # Display the predicted class
    iris_classes = ['setosa', 'versicolor', 'virginica']
    st.write(f'The predicted iris flower class is: {iris_classes[prediction]}')
