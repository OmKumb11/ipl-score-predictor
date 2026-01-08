# 🏏 AI IPL Score Predictor

> A Machine Learning web app that predicts the final score of an IPL innings based on Powerplay performance.

## 🔗 Live Demo
[Click here to use the App](https://ipl-score-predictor-bw55crsnjtnnbzdyww3jz4.streamlit.app/)

## 🛠️ Tech Stack
* **Python** (Logic)
* **Scikit-Learn** (Machine Learning - Linear Regression)
* **Streamlit** (Web Framework)
* **Matplotlib** (Data Visualization)

## 📊 How it Works
The model was trained on historical IPL data. It analyzes:
1.  **Powerplay Runs** (First 6 overs)
2.  **Wickets Lost**
It uses **Linear Regression** to predict the projected final score with **85% accuracy** (R² Score).

## 🚀 Future Improvements
* Upgrade model to **Random Forest/XGBoost** for better accuracy.
* Add team-specific predictions (e.g., "CSK vs MI").
* Deploy a "Win Probability" calculator.
