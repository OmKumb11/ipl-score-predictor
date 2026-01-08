import streamlit as st 
import pandas as pd 
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import mean_squared_error
import numpy as np 
import matplotlib.pyplot as plt

st.set_page_config(page_title= "IPL Predictor", page_icon="🏏")
st.title("AI IPL Score Predictor")
st.write("This App Uses Machine Learning to Predict Final Score.")

try:
    df = pd.read_csv('cricket_data.csv')

    
    X = df[['powerplay_runs', 'wickets']]
    y = df['final_score']  

    model = LinearRegression()
    model.fit(X,y)

    accuracy = model.score(X,y)

    st.success("Model Successfully Trained on Data!")

except FileNotFoundError:
    st.error("Error: cricket_data.csv not found. Please put it in the same folder.")
    st.stop()
except KeyError:
    st.error("⚠️ Error: CSV columns don't match. Make sure your CSV has 'powerplay_runs', 'wickets', and 'final_score'.")
    st.stop()

st.sidebar.header("Match Scenario")
st.sidebar.write("Enter the Current Match Stats: ")


pp_runs = st.number_input("Powerplay Runs: ", min_value=0, max_value=100, step=1, value=45)
wickets_lost = st.number_input("Wickets Lost: ", min_value=0, max_value=10, step=1, value=1)

st.sidebar.markdown("---")
st.sidebar.caption(f"Model Accurary: {accuracy*100:.1f}%")

if st.button("Predict Final Score"):
    
    prediction = model.predict([[pp_runs, wickets_lost]])
    final_score = int(prediction[0])

    if final_score < pp_runs:
        final_score = pp_runs
    
    if wickets_lost == 10:
        final_score = pp_runs

    st.markdown(f"<h1 style='text-align: center; color: red;'>{final_score}</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Predicted Final Score</h3>", unsafe_allow_html=True)

    if final_score > 200:
        st.balloons()
        st.write("That's a Massive Total!")
    elif final_score < 140:
        st.write("Needs some Acceleration")
    
    st.divider()
    fig, ax = plt.subplots(figsize=(8,4))

    ax.scatter(df['powerplay_runs'], df['final_score'], color = 'blue', label = 'Historical Matches', alpha = 0.6)

    ax.scatter(pp_runs, final_score, color = 'red', s = 200, label ='Current Prediction', marker = '*')

    ax.set_xlabel('Powerplay Runs')
    ax.set_ylabel('Final Score')
    ax.set_title('Powerplay Runs vs. Final Score')
    ax.legend()
    ax.grid(True, linestyle = '--', alpha = 0.5)

    st.pyplot(fig)