import streamlit as st 
import pandas as pd 
from sklearn.linear_model import LinearRegression 
import numpy as np 

st.title("AI IPL Score Predictor")
st.write("This App Uses Machine Learning to Predict Final Score.")

try:
    df = pd.read_csv('cricket_data.csv')

    # FIX 1: Use the correct column names from your CSV screenshot
    X = df[['powerplay_runs', 'wickets']]
    y = df['final_score']  # Changed from 'total_score' to 'final_score'

    model = LinearRegression()
    model.fit(X,y)

    st.success("Model Successfully Trained on Data!")

except FileNotFoundError:
    st.error("Error: cricket_data.csv not found. Please put it in the same folder.")
    st.stop()
except KeyError:
    st.error("⚠️ Error: CSV columns don't match. Make sure your CSV has 'powerplay_runs', 'wickets', and 'final_score'.")
    st.stop()

col1 , col2 = st.columns(2)

with col1:
    # FIX 2: Renamed variable to 'pp_runs' to avoid confusion
    pp_runs = st.number_input("Powerplay Runs: ", min_value=0, max_value=100, step=1, value=45)

with col2: 
    # FIX 3: Renamed variable to 'wickets_lost'
    wickets_lost = st.number_input("Wickets Lost: ", min_value=0, max_value=10, step=1, value=1)

if st.button("Predict Final Score"):
    # FIX 4: Use the actual variables created above
    prediction = model.predict([[pp_runs, wickets_lost]])
    final_score = int(prediction[0])

    st.header(f"Predicted Final Score: {final_score}")

    if final_score > 200:
        st.balloons()
        st.write("That's a Massive Total!")
    elif final_score < 140:
        st.write("Needs some Acceleration")