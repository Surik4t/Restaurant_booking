from pydantic import BaseModel

class TableSchema(BaseModel):
    name: str
    seats: int
    location: str