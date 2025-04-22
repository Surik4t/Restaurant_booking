from pydantic import BaseModel
from datetime import datetime

class Reservation(BaseModel):
    customer_name: str
    table_id: int
    reservation_time: datetime
    duration_minutes: int