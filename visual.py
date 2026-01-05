import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data = pd.read_csv('cricket_data.csv')
X = data[['powerplay_runs']]
y = data['final_score']

model = LinearRegression()
model.fit(X, y)

plt.scatter(X, y, color='blue', label='Actual Matches') 
plt.plot(X, model.predict(X), color='red', label='AI Prediction Line') 


plt.xlabel('Powerplay Runs')
plt.ylabel('Final Score')
plt.title('Cricket AI: The Best Fit Line')
plt.legend()
plt.show()