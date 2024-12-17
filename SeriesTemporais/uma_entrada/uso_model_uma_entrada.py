import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

# Carregar o modelo e o scaler
model = load_model('uma_entrada\modelo_lstm_umaentrada.h5')
scaler = joblib.load('uma_entrada\scaler.pkl')

# Carregar os dados
df = pd.read_csv('uma_entrada\dados_pm.csv', parse_dates=['date'], index_col='date')
data = df[['median']]

# Normalizar os dados
data_normalized = scaler.transform(data)

# Selecionar a última janela para previsão
window_size = 5
last_window = data_normalized[-window_size:].reshape(1, window_size, 1)

# Fazer previsões para os próximos 5 períodos
future_predictions = []
for _ in range(5):
    # Fazer a previsão para o próximo período
    next_prediction = model.predict(last_window)
    
    # Adicionar a previsão (revertida) à lista de previsões futuras
    next_prediction_rescaled = scaler.inverse_transform(next_prediction)
    future_predictions.append(next_prediction_rescaled[0][0])
    
    # Atualizar a janela de entrada para a próxima previsão
    last_window = np.append(last_window[:, 1:, :], next_prediction.reshape(1, 1, 1), axis=1)

# Convertendo a lista de np.float32 para float
future_predictions = [float(pred) for pred in future_predictions]
print("Previsões para os próximos 5 períodos (Median):", future_predictions)

