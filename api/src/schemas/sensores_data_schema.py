from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class SensorDataResponse(BaseModel):
    id: int  # ID do sensor
    sensor1: float  # Valor do sensor 1
    sensor2: float  # Valor do sensor 2
    sensor3: float  # Valor do sensor 3
    sensor4: float  # Valor do sensor 4
    sensor5: float  # Valor do sensor 5
    date: datetime  # Data e hora

    class Config:
        orm_mode = True  # Permite compatibilidade com objetos SQLAlchemy


class SensorDataCreate(BaseModel):
    sensor1: float
    sensor2: float
    sensor3: float
    sensor4: float
    sensor5: float

    class Config:
        orm_mode = True