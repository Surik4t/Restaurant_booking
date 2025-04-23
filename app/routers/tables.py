from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from app.schemas.tables import TableSchema
from app.services.tables import get_tables, create_table, delete_table

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("/")
def read_tables(session: Session = Depends(get_db)):
    return get_tables(session)


@router.post("/table")
def add_table(table: TableSchema, session: Session = Depends(get_db)):
    return create_table(table, session)


@router.delete("/{table_id}")
def remove_table(table_id: int, session: Session = Depends(get_db)):
    return delete_table(table_id, session)