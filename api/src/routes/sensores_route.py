from fastapi import APIRouter, Depends, HTTPException, status
from ..middleware.utils_db import get_session
from sqlalchemy.ext.asyncio import AsyncSession
from ..schemas import sensores_data_schema
from ..controllers import sensor_data_controller

router = APIRouter(tags=["sensores"], prefix="/sensores")

@router.get("/get_all_sensor_data", response_model=list[sensores_data_schema.SensorDataResponse])
async def get_all_sensor_data(db: AsyncSession = Depends(get_session)):
    """
    Get all sensor from the database
    """
    return await sensor_data_controller.get_all_sensor_data(db)


@router.post("/create_sensor_data", response_model=sensores_data_schema.SensorDataResponse, status_code=status.HTTP_201_CREATED)
async def create_sensor_data(sensor: sensores_data_schema.SensorDataCreate, db: AsyncSession = Depends(get_session)):
    """
    Create new sensor data entry in the database
    """
    return await sensor_data_controller.create_sensor_data(sensor, db)