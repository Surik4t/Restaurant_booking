from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from database import Base


class ReservationModel(Base):
    __tablename__ = "reservations"

    id = Column(Integer, primary_key=True)
    customer_name = Column(String)
    table_id = Column(Integer, ForeignKey("tables.id"))
    reservation_time = Column(DateTime)
    duration_minutes = Column(Integer)