from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase

class Table(DeclarativeBase):
    __tablename__ = "tables"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    seats = Column(Integer)
    location = Column(String)