from pydantic import BaseModel

class Table(BaseModel):
    name: str
    seats: int
    location: str