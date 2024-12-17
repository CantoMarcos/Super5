import pandas as pd
import numpy as np
import joblib
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# Carregar dados e scalers
df = pd.read_csv('dados_sensores.csv', parse_dates=['timestamp'], index_col='timestamp')
df = df.sort_index()
scalers = joblib.load('scalers.pkl')

# Normalizar os dados usando os scalers
for column, scaler in scalers.items():
    df[column] = scaler.transform(df[[column]])

# Preparar os dados de teste
window_size = 5
X, y = [], []
for i in range(window_size, len(df)):
    X.append(df.iloc[i-window_size:i].values)
    y.append(df.iloc[i].values)

X, y = np.array(X), np.array(y)

# Carregar o modelo treinado
model = load_model('modelo_lstm.h5')

# Dividir em conjunto de teste
test_size = int(len(X) * 0.8)
X_test, y_test = X[test_size:], y[test_size:]

# Fazer previsões
predictions = model.predict(X_test)

# Reverter a normalização
predictions_rescaled = []
y_test_rescaled = []
for i, column in enumerate(df.columns):
    scaler = scalers[column]
    predictions_rescaled.append(scaler.inverse_transform(predictions[:, i].reshape(-1, 1)))
    y_test_rescaled.append(scaler.inverse_transform(y_test[:, i].reshape(-1, 1)))

predictions_rescaled = np.hstack(predictions_rescaled)
y_test_rescaled = np.hstack(y_test_rescaled)

# Calcular o erro RMSE para cada sensor
for i, column in enumerate(df.columns):
    rmse = np.sqrt(mean_squared_error(y_test_rescaled[:, i], predictions_rescaled[:, i]))
    print(f'RMSE para {column}: {rmse}')


# Selecionar um sensor para visualização (por exemplo, sensor_1)
sensor_index = 0  # índice para o primeiro sensor (sensor_1)

# Visualizar os valores reais vs. previsões para o sensor selecionado
plt.figure(figsize=(10, 5))
plt.plot(y_test_rescaled[:, sensor_index], label="Valor Real - Sensor 1")
plt.plot(predictions_rescaled[:, sensor_index], label="Previsão - Sensor 1")
plt.xlabel("Tempo")
plt.ylabel("Valor")
plt.title("Previsão vs Valor Real para Sensor 1")
plt.legend()
plt.show()