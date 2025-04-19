from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

DATABASE_URL = 'postgresql+psycopg2://admin:my_super_password@localhost:5433/fast_api'

engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

class Base(DeclarativeBase): pass
