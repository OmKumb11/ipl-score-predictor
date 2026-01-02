import pandas as pd
import numpy as np 
from sklearn.linear_model import LinearRegression

data = pd.read_csv('cricket_data.csv')

X = data[['powerplay_runs']]
Y = data['final_score']

model = LinearRegression()
model.fit(X,Y)

print("IPL Score Predictor")
user_in = int(input("Enter the Number of Runs Scored in Powerplay (6 Overs):  "))

prediction = model.predict([[user_in]])

print(f"Predicted Final Score: {int(prediction[0])}")
