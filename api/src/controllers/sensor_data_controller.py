from ..repository import sensor_data_repository
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas.sensores_data_schema import SensorDataCreate, SensorDataResponse
from fastapi import HTTPException, status
from datetime import datetime



async def get_all_sensor_data(db: AsyncSession):
    try:
        return await sensor_data_repository.get_all_sensor_data(db)
    except Exception as ex:
        raise ex
    
async def create_sensor_data(sensor: SensorDataCreate, db: AsyncSession) -> SensorDataResponse:
    """
    Controller to handle creation of new sensor data
    """
    try:
        # Adiciona a data automaticamente no controlador
        sensor_data = sensor.dict()
        sensor_data["date"] = datetime.utcnow()

        created_sensor = await sensor_data_repository.create_sensor_data(sensor_data, db)
        return created_sensor
    except SQLAlchemyError as e:
        await db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while creating sensor data"
        ) from e