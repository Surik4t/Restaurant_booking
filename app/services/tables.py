from app.models.table import TableModel
from fastapi import HTTPException


def get_tables(session) -> list[TableModel]:
    return session.query(TableModel).all()


def create_table(table, session):
    table_data = table.dict()
    table_model = TableModel(**table_data)
    try:
        session.add(table_model)
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Table created."}


def delete_table(table_id: int, session):
    try:
        table = session.query(TableModel).filter(TableModel.id == table_id).one()
        session.delete(table)
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Table removed."}