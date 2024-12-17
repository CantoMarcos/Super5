import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Gerar dados simulados
date_range = pd.date_range(start="2023-01-01", end="2023-01-07 23:00:00", freq='h')
data = {
    "timestamp": date_range,
    "sensor_1": np.random.normal(20, 5, len(date_range)),
    "sensor_2": np.random.normal(50, 10, len(date_range)),
    "sensor_3": np.random.normal(75, 15, len(date_range)),
    "sensor_4": np.random.normal(100, 20, len(date_range)),
    "sensor_5": np.random.normal(150, 25, len(date_range))
}

# Criar DataFrame
df = pd.DataFrame(data)

# Salvar em CSV
df.to_csv('dados_sensores.csv', index=False)
print("Arquivo CSV 'dados_sensores.csv' criado com sucesso!")
