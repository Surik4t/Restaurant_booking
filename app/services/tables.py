from app.models.table import Table
from database import session
from fastapi import HTTPException


def get_tables() -> list[Table]:
    tables = [table for table in session.query(Table)]
    return tables


def create_table(table):
    table_model = Table(**dict(table))
    with session:
        try:
            session.add(table_model)
            session.commit()
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Table created."}


def delete_table(table_id):
    try:
        table = session.query(Table).filter(Table.id==table_id).one()
        session.delete(table)
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Table removed."}