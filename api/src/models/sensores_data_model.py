from sqlalchemy import Column, Integer, Float, DateTime
from src.config.config_db import Base  # Certifique-se de importar corretamente o Base

class SensorData(Base):
    __tablename__ = "sensor_data"  # Nome atualizado da tabela

    id = Column(Integer, primary_key=True, autoincrement=True)  # Chave primária
    sensor1 = Column(Float, nullable=False)  # Valor do sensor 1
    sensor2 = Column(Float, nullable=False)  # Valor do sensor 2
    sensor3 = Column(Float, nullable=False)  # Valor do sensor 3
    sensor4 = Column(Float, nullable=False)  # Valor do sensor 4
    sensor5 = Column(Float, nullable=False)  # Valor do sensor 5
    date = Column(DateTime, nullable=False)  # Data e hora
