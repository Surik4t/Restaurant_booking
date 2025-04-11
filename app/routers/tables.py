from fastapi import APIRouter
from app.services.tables import get_table, create_table, delete_table

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("/")
def read_tables():
    return get_table()


@router.post("/{table_id}")
def add_table(table_id: int):
    return create_table(table_id)


@router.delete("/{table_id}")
def remove_table(table_id: int):
    return delete_table(table_id)