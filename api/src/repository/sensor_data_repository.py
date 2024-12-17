from sqlalchemy import select
from ..models import sensores_data_model
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas.sensores_data_schema import SensorDataCreate
from ..models.sensores_data_model import SensorData

model = sensores_data_model.SensorData

async def get_all_sensor_data(db: AsyncSession):
    response = await db.execute(select(model))
    return response.scalars().all()


async def create_sensor_data(sensor_data: dict, db: AsyncSession) -> SensorData:
    """
    Insert new sensor data into the database
    """
    new_sensor = SensorData(
        sensor1=sensor_data["sensor1"],
        sensor2=sensor_data["sensor2"],
        sensor3=sensor_data["sensor3"],
        sensor4=sensor_data["sensor4"],
        sensor5=sensor_data["sensor5"],
        date=sensor_data["date"],  # A data já foi adicionada no controlador
    )
    db.add(new_sensor)
    await db.commit()
    await db.refresh(new_sensor)
    return new_sensor