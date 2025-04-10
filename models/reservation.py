from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import DeclarativeBase


class Reservation(DeclarativeBase):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    table_id = Column(Integer, ForeignKey("tables.id"))
    reservation_time = Column(DateTime)
    duration_minutes = Column(Integer)