import streamlit as st 
import pandas as pd 
from sklearn.linear_model import LinearRegression 
import numpy as np 
import matplotlib.pyplot as plt

st.title("AI IPL Score Predictor")
st.write("This App Uses Machine Learning to Predict Final Score.")

try:
    df = pd.read_csv('cricket_data.csv')

    
    X = df[['powerplay_runs', 'wickets']]
    y = df['final_score']  

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
    
    pp_runs = st.number_input("Powerplay Runs: ", min_value=0, max_value=100, step=1, value=45)

with col2: 
    
    wickets_lost = st.number_input("Wickets Lost: ", min_value=0, max_value=10, step=1, value=1)

if st.button("Predict Final Score"):
    
    prediction = model.predict([[pp_runs, wickets_lost]])
    final_score = int(prediction[0])

    if final_score < pp_runs:
        final_score = pp_runs
    
    if wickets_lost == 10:
        final_score = pp_runs

    st.header(f"Predicted Final Score: {final_score}")

    if final_score > 200:
        st.balloons()
        st.write("That's a Massive Total!")
    elif final_score < 140:
        st.write("Needs some Acceleration")
    
    st.divider()
    st.subheader("Match Scenario Anaylsis")
    st.write("See how your prediction (Red) compares to past matches (Blue).")

    fig, ax = plt.subplots()

    ax.scatter(df['powerplay_runs'], df['final_score'], color = 'blue', label = 'Historical Matches', alpha = 0.6)

    ax.scatter(pp_runs, final_score, color = 'red', s = 200, label ='Current Prediction', marker = '*')

    ax.set_xlabel('Powerplay Runs')
    ax.set_ylabel('Final Score')
    ax.set_title('Powerplay Runs vs. Final Score')
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)