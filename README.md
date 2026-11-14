## 🚀 Aplicación en línea

Puedes probar Drone Altitude AI directamente desde el navegador:

👉 [Abrir Drone Altitude AI](https://drone-altitude-ai.onrender.com)

**Nota:** La aplicación está alojada en Render mediante el plan gratuito.
Si permanece inactiva durante aproximadamente 15 minutos, puede tardar
50 segundos o más en responder cuando se vuelva a abrir.

> **Alcance:** prototipo demostrativo. El modelo inicial se entrena con datos sintéticos generados por una aproximación atmosférica; no está calibrado con vuelos ni mediciones reales. No debe utilizarse para navegación o control de un dron real.

## 📌 Objetivo

Desarrollar una aplicación que reciba temperatura y presión atmosférica, procese esos datos mediante una RNA y muestre una altura estimada en metros.

##  ¿Cómo funciona?

El proyecto se divide en dos partes:

1. **Entrenamiento (`train_model.py`):** genera un conjunto de datos sintéticos, entrena la RNA y guarda el modelo.
2. **Aplicación web (`app.py` + `templates/index.html`):** presenta un formulario para ingresar temperatura y presión. El navegador envía los valores al servidor Flask, que consulta el modelo y devuelve la altura estimada.

### Variables del modelo

| Tipo | Variable | Unidad |
|---|---|---|
| Entrada 1 | Temperatura atmosférica | °C |
| Entrada 2 | Presión atmosférica | hPa |
| Salida | Altura estimada | m |

### Red neuronal

Se utiliza `MLPRegressor` de **scikit-learn**, una red neuronal artificial de tipo perceptrón multicapa para regresión.

- Capas ocultas: 32 y 16 neuronas.
- Función de activación: ReLU.
- Optimizador: Adam.
- Normalización de entradas: `StandardScaler`.
- División de datos: 80 % entrenamiento y 20 % prueba.
- Semilla aleatoria: 42 para facilitar la reproducibilidad.

### Datos y consideraciones

El conjunto de entrenamiento se genera de forma sintética para alturas entre 0 y 3000 metros y temperaturas entre -5 y 35 °C. La presión se aproxima usando una relación atmosférica simplificada con presión de referencia estándar de **1013.25 hPa**. Se agrega una pequeña variación aleatoria para simular ruido de medición.

La temperatura ingresada se utiliza como aproximación de la temperatura media de la columna de aire. En condiciones reales, la presión de referencia local cambia con el clima y la temperatura varía con la altitud. Por eso, las predicciones actuales sirven para demostrar el flujo de una RNA, pero no garantizan precisión en un entorno real.

Para una validación experimental, se deben reemplazar los datos sintéticos por registros sincronizados de temperatura, presión y altura real, y calibrar el sistema con mediciones del lugar y momento del ensayo.

##  Estructura del proyecto

```text
drone-altitude-ai/
├── app.py
├── train_model.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── model/
    ├── drone_altitude_rna.joblib   # se genera al entrenar
    └── metrics.txt                 # métricas generadas al entrenar
```

La carpeta `model/` y sus archivos se crean automáticamente al ejecutar el entrenamiento.

## ⚙️ Requisitos

- Windows 10/11.
- Python 3.10, 3.11 o 3.12.
- Conexión a internet para instalar las dependencias.

##  Instalación y ejecución en Windows

### 1. Descargar el proyecto

Descarga el repositorio como ZIP desde GitHub y descomprímelo. También puedes clonarlo si tienes Git instalado.

### 2. Abrir la terminal en la carpeta

En el Explorador de archivos, abre la carpeta `drone-altitude-ai`, escribe `cmd` en la barra de direcciones y presiona Enter.

### 3. Crear y activar un entorno virtual

```bash
py -m venv .venv
.venv\Scripts\activate
```

### 4. Instalar dependencias

```bash
py -m pip install --upgrade pip
pip install -r requirements.txt
```

### 5. Entrenar la RNA

```bash
py train_model.py
```

Al finalizar, se crea el archivo `model/drone_altitude_rna.joblib` y se guardan las métricas de evaluación en `model/metrics.txt`. La terminal muestra MAE, RMSE y R² calculados sobre el conjunto de prueba sintético.

### 6. Iniciar la aplicación web

```bash
py app.py
```

### 7. Abrir el simulador

En el navegador, visita:

```text
http://127.0.0.1:5000
```

Introduce la temperatura y la presión atmosférica y pulsa **CALCULAR ALTURA ESTIMADA**.

Para detener el servidor, vuelve a la terminal y presiona `Ctrl + C`.

##  Evaluación del modelo

Durante el entrenamiento se calculan tres métricas:

- **MAE:** error absoluto medio, expresado en metros.
- **RMSE:** raíz del error cuadrático medio, expresada en metros.
- **R²:** coeficiente de determinación.

Los valores que aparecen corresponden a una prueba con datos sintéticos. No deben interpretarse como una medida de precisión en vuelos reales.

## Tecnologías utilizadas

- Python
- NumPy y Pandas
- scikit-learn
- Joblib
- Flask
- HTML y CSS
- JavaScript

## 👤 Autor

**Daniel Madrid Giraldo**  
Proyecto académico – Ingeniería de Software


