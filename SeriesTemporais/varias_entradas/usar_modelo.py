import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model

# Carregar o modelo treinado e os scalers
model = load_model('varias_entradas\modelo_lstm.h5')
scalers = joblib.load('varias_entradas\scalers.pkl')

# Carregar os dados
df = pd.read_csv('varias_entradas\dados_sensores.csv', parse_dates=['timestamp'], index_col='timestamp')
df = df.sort_index()

# Selecionar a última janela para previsão antes da normalização
window_size = 5
last_window_raw = df[-window_size:]  # Últimos 5 períodos sem normalização
print("Última janela antes da normalização:")
print(last_window_raw)

# Normalizar usando os scalers
for column, scaler in scalers.items():
    df[column] = scaler.transform(df[[column]])

# Selecionar a última janela para previsão após a normalização
last_window = df[-window_size:].values.reshape(1, window_size, 5)

# Exibir a entrada normalizada que será usada para a previsão
#print("Entrada para previsão (última janela normalizada):")
#print(last_window)

# Fazer a previsão
next_prediction = model.predict(last_window)

# Reverter a normalização para os 5 sensores
next_prediction_rescaled = [scalers[column].inverse_transform(next_prediction[:, i].reshape(-1, 1)) for i, column in enumerate(df.columns)]
next_prediction_rescaled = np.hstack(next_prediction_rescaled)

print("Previsão para o próximo período:", next_prediction_rescaled)
