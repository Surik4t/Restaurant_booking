from conftest import client
from datetime import datetime, timedelta


def default_reservation():
    reservation = {
        "customer_name": "test_reservation",
        "table_id": 0,
        "reservation_time": str(datetime.now()),
        "duration_minutes": 60
    }
    return reservation


def test_get_tables():
    response = client.get("/reservations")
    assert response.status_code == 200


def test_negative_or_0_booking_duration():
    payload = default_reservation()
    payload["duration_minutes"] = 0
    response = client.post("/reservations/reservation", json=payload)
    assert response.status_code == 400

    payload["duration_minutes"] = -1
    response = client.post("/reservations/reservation", json=payload)
    assert response.status_code == 400


def test_past_date_booking():
    payload = default_reservation()
    payload["reservation_time"] = str(datetime.now() - timedelta(hours=1))
    response = client.post("/reservations/reservation", json=payload)
    assert response.status_code == 400


def test_reservation_crossing():
    payload = default_reservation()
    payload["reservation_time"] = str(datetime(year=2000, month=1, day=1, hour=12, minute=0, second=0))
    first_reservation = client.post("/reservations/reservation", json=payload)
    assert first_reservation.status_code == 200

    same_reservation = client.post("/reservations/reservation", json=payload)
    assert same_reservation.status_code == 400