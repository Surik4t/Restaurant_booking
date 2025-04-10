from sqlalchemy import create_engine

DB_HOST = 'localhost'
DB_PORT = '5433'
DB_NAME = 'fast_api'
DB_USER = 'admin'
DB_PASSWORD = 'my_super_password'

DATABASE_URL = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL)
