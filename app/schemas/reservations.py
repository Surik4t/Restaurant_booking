from pydantic import BaseModel
from datetime import datetime

class ReservationSchema(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int