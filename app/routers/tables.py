from fastapi import APIRouter
from app.schemas.tables import Table
from app.services.tables import get_table, create_table, delete_table

router = APIRouter(prefix="/tables", tags=["tables"])

@router.get("/")
def read_tables():
    return get_table()


@router.get("/{table_id}")
def read_table():
    return


@router.post("/table")
def add_table(table: Table):
    return create_table(table)


@router.delete("/{table_id}")
def remove_table(table_id: int):
    return delete_table(table_id)