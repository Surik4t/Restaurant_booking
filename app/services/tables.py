from app.models.table import Table
from database import engine
from fastapi import HTTPException

tables = []

def get_tables():
    return tables


def get_table(table_id):
    if table_id not in tables:
        raise HTTPException(status_code=404, detail="Table not found.")
    return tables[table_id]

def create_table(table):
    tables.append(table)
    return {"message": "Table created."}


def delete_table(table_id):
    if table_id not in tables:
        raise HTTPException(status_code=404, detail="Table not found.")
    tables.remove(table_id)
    return {"message": "Table removed."}