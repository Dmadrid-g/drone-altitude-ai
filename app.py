import os
import joblib
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
MODEL_PATH = os.path.join("model", "drone_altitude_rna.joblib")
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "No se encontró el modelo. Ejecuta primero: python train_model.py"}), 500
    data = request.get_json(silent=True) or {}
    try:
        temperature = float(data["temperature"])
        pressure = float(data["pressure"])
    except (KeyError, TypeError, ValueError):
        return jsonify({"error": "Ingresa valores numéricos válidos."}), 400

    if not (-30 <= temperature <= 60):
        return jsonify({"error": "La temperatura debe estar entre -30 y 60 °C."}), 400
    if not (650 <= pressure <= 1050):
        return jsonify({"error": "La presión debe estar entre 650 y 1050 hPa."}), 400

    altitude = float(model.predict(np.array([[temperature, pressure]]))[0])
    altitude = max(0.0, altitude)
    return jsonify({"altitude": round(altitude, 2)})

if __name__ == "__main__":
    if model is None:
        raise SystemExit("Primero ejecuta: python train_model.py")
    app.run(host="127.0.0.1", port=5000, debug=True)
