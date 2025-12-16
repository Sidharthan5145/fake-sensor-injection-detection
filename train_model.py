import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

df = pd.read_csv("../data/sensor_data.csv")

X = df[["temperature", "humidity"]]

model = IsolationForest(contamination=0.1, random_state=42)
model.fit(X)

joblib.dump(model, "model.pkl")

print("Model trained and saved")
