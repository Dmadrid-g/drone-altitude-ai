PROYECTO: DRONE ALTITUDE AI
==========================

CONTENIDO
- train_model.py: genera datos sintéticos y entrena la RNA.
- app.py: servidor local que recibe temperatura/presión y consulta el modelo.
- templates/index.html: interfaz web.
- requirements.txt: dependencias de Python.

REQUISITOS
- Windows 10/11
- Python 3.10, 3.11 o 3.12
- Conexión a internet para instalar dependencias la primera vez.

PASOS EN WINDOWS
1. Descomprime la carpeta.
2. Abre la carpeta drone_altitude_ai.
3. En el Explorador de archivos, haz clic en la barra de dirección, escribe cmd y pulsa Enter.
4. Ejecuta estos comandos, uno por uno:

   py -m venv .venv
   .venv\Scripts\activate
   py -m pip install --upgrade pip
   pip install -r requirements.txt
   py train_model.py
   py app.py

5. Cuando aparezca que Flask está ejecutándose, abre en Chrome:
   http://127.0.0.1:5000

6. Introduce temperatura y presión y pulsa CALCULAR ALTURA ESTIMADA.

PARA VOLVER A ABRIR
Abre CMD dentro de la carpeta y ejecuta:
   .venv\Scripts\activate
   py app.py
Luego abre http://127.0.0.1:5000

IMPORTANTE SOBRE EL MODELO
La RNA es un perceptrón multicapa (MLP) entrenado con datos atmosféricos
sintéticos generados mediante una aproximación de la ecuación hipsométrica.
Se fija una presión de referencia P0=1013.25 hPa. La temperatura local
se usa como aproximación de la temperatura media de la columna de aire.
Por ello, es un prototipo académico demostrativo, no un modelo calibrado
con vuelos ni mediciones reales. En la atmósfera real, la presión al nivel
del mar cambia con el clima y la temperatura media de la columna de aire
no es necesariamente igual a la temperatura medida junto al dron.
Para resultados experimentales fiables, sustituye los datos sintéticos
por mediciones sincronizadas de presión, temperatura y altura real,
y calibra la presión de referencia para el lugar y momento del ensayo.

El entrenamiento imprime MAE, RMSE y R² sobre un conjunto de prueba.
Esos indicadores evalúan el ajuste a los datos sintéticos, no garantizan
la precisión en un vuelo real.
