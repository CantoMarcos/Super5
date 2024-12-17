
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from src.middleware.utils_environment import get_environment_config

config = get_environment_config()

DATABASE_DIALECT = 'mysql+aiomysql'
DATABASE_USER = config.get('DATABASE_USER')
DATABASE_PASSWORD = config.get('DATABASE_PASSWORD')
DATABASE_HOST = config.get('DATABASE_HOST')
DATABASE_NAME = config.get('DATABASE_NAME')
TEST_DATABASE_NAME = config.get('TEST_DATABASE_NAME')

ECHO = False if config.get('ECHO', "False") == 'False' else True

DATABASE_URL = f'{DATABASE_DIALECT}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{DATABASE_NAME}'
TEST_DATABASE_URL = f'{DATABASE_DIALECT}://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}/{TEST_DATABASE_NAME}'
    
engine = create_async_engine(DATABASE_URL, echo=ECHO)
test_engine = create_async_engine(TEST_DATABASE_URL, echo=False)

async_session  = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
test_async_session = sessionmaker(test_engine, class_=AsyncSession, expire_on_commit=False)

origins = [
    "*" # Temporary. Just to Test the frontend
]

Base = declarative_base()
