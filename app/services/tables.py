tables = []

def get_table():
    return tables


def create_table(table):
    tables.append(table)
    return {"message": "Table created."}


def delete_table(table_id):
    try:
        tables.remove(table_id)
    except Exception as e:
        return e
    return {"message": "Table removed."}