import requests
from app.routers.tables import add_table, delete_table

def test_add_table_endpoint_test():
    payload = {
        "name": "test_table",
        "seats": 2,
        "location": "Somewhere over the rainbow"
    }

    response = add_table(payload)
    assert response["status_code"] == 200