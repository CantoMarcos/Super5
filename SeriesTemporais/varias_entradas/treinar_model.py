import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import joblib

# Passo 1: Carregar e normalizar os dados
df = pd.read_csv('dados_sensores.csv', parse_dates=['timestamp'], index_col='timestamp')
df = df.sort_index()

# Normalizar cada coluna de sensor e salvar os scalers
scalers = {}
for column in df.columns:
    scaler = MinMaxScaler(feature_range=(0, 1))
    df[column] = scaler.fit_transform(df[[column]])
    scalers[column] = scaler

# Salvar os scalers para uso posterior
joblib.dump(scalers, 'scalers.pkl')

# Passo 2: Criar janelas de dados
window_size = 5
X, y = [], []
for i in range(window_size, len(df)):
    X.append(df.iloc[i-window_size:i].values)
    y.append(df.iloc[i].values)

X, y = np.array(X), np.array(y)

# Dividir em conjuntos de treino e teste
train_size = int(len(X) * 0.8)
X_train, y_train = X[:train_size], y[:train_size]

# Passo 3: Criar e treinar o modelo
model = Sequential()
model.add(LSTM(units=50, activation='relu', input_shape=(window_size, X.shape[2])))
model.add(Dense(5))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(X_train, y_train, epochs=100, batch_size=32, verbose=1)

# Salvar o modelo treinado
model.save('modelo_lstm.h5')
print("Modelo treinado e salvo com sucesso.")
