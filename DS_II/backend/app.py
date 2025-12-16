from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("../ml/model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    temp = data["temp"]
    hum = data["hum"]

    prediction = model.predict(np.array([[temp, hum]]))[0]

    status = "FAKE DATA 🚨" if prediction == -1 else "NORMAL DATA ✅"

    return jsonify({
        "temperature": temp,
        "humidity": hum,
        "status": status
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
