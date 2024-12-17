from src.config.config_db import async_session, test_async_session
from sqlalchemy.ext.asyncio import AsyncSession
import sys

# Dependency
async def get_session() -> AsyncSession: # type: ignore
    """ Open the database connection and return an AsyncSession """
    async with async_session() as session:
        yield session

async def open_connection_and_exec_sql(sql: str):
    if 'pytest' in sys.modules: #Code running in pytest
        async with test_async_session() as db:
            return await exec_sql(sql, db)
    else: 
        async with async_session() as db:
            return await exec_sql(sql, db)

async def exec_sql(sql: str, db: AsyncSession):
    response = await db.execute(sql)
    return response.all()
