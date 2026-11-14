"""
Entrena una red neuronal (MLPRegressor) con datos atmosféricos sintéticos.
IMPORTANTE: el modelo es demostrativo y usa presión de referencia estándar
P0=1013.25 hPa. Para uso real debe calibrarse con mediciones del lugar.
"""
import os
import joblib
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

SEED = 42
P0_HPA = 1013.25
G = 9.80665
M = 0.0289644
R = 8.3144598

def make_dataset(n=60000, seed=SEED):
    rng = np.random.default_rng(seed)
    # Alturas de 0 a 3000 m; temperaturas locales plausibles.
    altitude = rng.uniform(0, 3000, n)
    temp_c = rng.uniform(-5, 35, n)
    # Ecuación hipsométrica simplificada. La temperatura ingresada es
    # la temperatura local; se usa como aproximación de temperatura media
    # de la columna de aire.
    temp_k = temp_c + 273.15
    pressure = P0_HPA * np.exp(-(G * M * altitude) / (R * temp_k))
    # Pequeña variación instrumental para evitar datos artificialmente perfectos.
    temp_measured = temp_c + rng.normal(0, 0.25, n)
    pressure_measured = pressure + rng.normal(0, 0.35, n)
    X = np.column_stack([temp_measured, pressure_measured])
    y = altitude
    return X, y

def main():
    X, y = make_dataset()
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=SEED
    )
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("rna", MLPRegressor(
            hidden_layer_sizes=(32, 16),
            activation="relu",
            solver="adam",
            learning_rate_init=0.001,
            max_iter=500,
            early_stopping=True,
            validation_fraction=0.15,
            n_iter_no_change=20,
            random_state=SEED
        ))
    ])
    model.fit(X_train, y_train)
    pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, pred)
    rmse = np.sqrt(mean_squared_error(y_test, pred))
    r2 = r2_score(y_test, pred)

    os.makedirs("model", exist_ok=True)
    joblib.dump(model, "model/drone_altitude_rna.joblib")
    with open("model/metrics.txt", "w", encoding="utf-8") as f:
        f.write(f"MAE: {mae:.2f} m\nRMSE: {rmse:.2f} m\nR2: {r2:.4f}\n")
        f.write(f"Iteraciones: {model.named_steps['rna'].n_iter_}\n")
    print("Modelo guardado en model/drone_altitude_rna.joblib")
    print(f"MAE: {mae:.2f} m | RMSE: {rmse:.2f} m | R²: {r2:.4f}")
    print("Datos de entrenamiento: sintéticos; referencia P0=1013.25 hPa.")

if __name__ == "__main__":
    main()
