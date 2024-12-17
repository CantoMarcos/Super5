import numpy as np
import pandas as pd
import joblib
from tensorflow.keras.models import load_model
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Carregar os dados e o scaler
df = pd.read_csv('dados_pm.csv', parse_dates=['date'], index_col='date')
data = df[['median']]
scaler = joblib.load('scaler.pkl')

# Normalizar os dados
data_normalized = scaler.transform(data)

# Preparar os dados de teste
window_size = 10
X, y = [], []
for i in range(window_size, len(data_normalized)):
    X.append(data_normalized[i-window_size:i, 0])
    y.append(data_normalized[i, 0])

X, y = np.array(X), np.array(y)
X = X.reshape((X.shape[0], X.shape[1], 1))

# Carregar o modelo treinado
model = load_model('modelo_lstm_umaentrada.h5')

# Dividir em conjunto de teste
test_size = int(len(X) * 0.8)
X_test, y_test = X[test_size:], y[test_size:]

# Fazer previsões
predictions = model.predict(X_test)

# Reverter a normalização
predictions_rescaled = scaler.inverse_transform(predictions)
y_test_rescaled = scaler.inverse_transform(y_test.reshape(-1, 1))

# Calcular o RMSE
rmse = np.sqrt(mean_squared_error(y_test_rescaled, predictions_rescaled))
print(f'Erro médio quadrado (RMSE): {rmse}')

# Visualizar previsões vs valores reais
plt.plot(y_test_rescaled, label="Valor Real (Median)")
plt.plot(predictions_rescaled, label="Previsão (Median)")
plt.xlabel("Tempo")
plt.ylabel("Valor")
plt.legend()
plt.show()
