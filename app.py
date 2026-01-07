import streamlit as st 
import numpy as np 

st.title("🏏 IPL Score Predictor")

overs = st.slider("Overs Completed: ", min_value = 5.0, max_value = 20.0, step = 0.1)
runs = st.number_input("Current Score: ", min_value = 0, step = 1)

if overs > 0:
    prediction = (runs/overs)* 20
else:
    prediction = 0 

if st.button("Predict Score"):
    st.header(f"Predicted Score: {int(prediction)}")

    if prediction > 200:
        st.balloons()