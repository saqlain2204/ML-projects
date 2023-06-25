import streamlit as st
import numpy as np
import pandas as pd
import pickle


# Loading the saved model
with open('titanic_model', 'rb') as file:
    model = pickle.load(file)

# Creating a function for prediction

def titanic_prediction(input_data, name):
    
    # Converting the input into a numpy array
    data_as_array = np.asarray(input_data).reshape(1, -1)
    prediction=model.predict(data_as_array)

    if(prediction[0]==0):
        return f"The passenger {name} has not survided."
    else:
        return f"The passenger {name} has survived."
    
def main():

    # Title for the web page
    st.title("Titanic survival prediction")

    # Getting user data
    # name,Pclass,age,parch,fare,gender

    name=st.text_input("Enter the passenger name")
    Pclass=st.text_input("Enter the Passenger Class")
    age=st.text_input("Enter the Passenger Age")
    parch=st.text_input("Enter the Passenger Arch")
    fare=st.text_input("Enter the Passenger Fare")
    gender=st.text_input("Enter the Passenger Gender")
    if(gender.lower()=='male'):
        gender=1
    else:
        gender=0
    
    # Button to predict

    pred=''
    if st.button('Predict'):
        pred = titanic_prediction([Pclass, age, parch, fare, gender], name)     
    st.success(pred)


if __name__ == '__main__':
    main()