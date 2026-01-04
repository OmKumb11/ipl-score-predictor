import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression

data = pd.read_csv('cricket_data.csv')

X = data[['powerplay_runs', 'wickets']]
Y = data['final_score']

model = LinearRegression()
model.fit(X,Y)

print("IPL Score Predictor 2.0")
user_in = float(input("Enter the Number of Runs Scored in Powerplay (6 Overs):  "))
wickets = float(input("Wickets lost: "))
prediction = model.predict([[user_in,wickets]])

print(f"Predicted Final Score: {int(prediction[0])}")
