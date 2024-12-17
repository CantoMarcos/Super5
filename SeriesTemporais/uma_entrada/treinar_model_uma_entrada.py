import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib

# Carregar os dados
df = pd.read_csv('dados_pm.csv', parse_dates=['date'], index_col='date')
data = df[['median']]

# Normalizar os dados
scaler = MinMaxScaler(feature_range=(0, 1))
data_normalized = scaler.fit_transform(data)

# Salvar o scaler
joblib.dump(scaler, 'scaler.pkl')

# Criar janelas de tempo
window_size = 5
X, y = [], []
for i in range(window_size, len(data_normalized)):
    X.append(data_normalized[i-window_size:i, 0])
    y.append(data_normalized[i, 0])

X, y = np.array(X), np.array(y)
X = X.reshape((X.shape[0], X.shape[1], 1))

# Dividir em conjuntos de treino e teste
train_size = int(len(X) * 0.8)
X_train, y_train = X[:train_size], y[:train_size]

# Criar e treinar o modelo
model = Sequential()
model.add(LSTM(units=50, activation='relu', input_shape=(window_size, 1)))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)

# Salvar o modelo treinado
model.save('modelo_lstm_umaentrada.h5')
print("Modelo treinado e salvo com sucesso.")
