import pytest
from conftest import test_db_client, mock_db_client
from datetime import datetime, timedelta


def default_reservation():
    reservation = {
        "customer_name": "test_reservation",
        "table_id": 0,
        "reservation_time": str(datetime.now()),
        "duration_minutes": 30
    }
    return reservation


def test_negative_or_0_booking_duration(mock_db_client):
    payload = default_reservation()
    payload["duration_minutes"] = 0
    response = mock_db_client.post("/reservations/reservation", json=payload)
    assert response.status_code == 400

    payload["duration_minutes"] = -1
    response = mock_db_client.post("/reservations/reservation", json=payload)
    assert response.status_code == 400


def test_past_date_booking(mock_db_client):
    payload = default_reservation()
    payload["reservation_time"] = str(datetime.now() - timedelta(hours=1))
    response = mock_db_client.post("/reservations/reservation", json=payload)
    assert response.status_code == 400


@pytest.mark.parametrize(
    ("test_name", "table_id", "time", "duration", "expected"),
    (
            # другой стол
            ("different table", 1, "2050-01-01T12:15:00", 30, 200),

            # полный оверлап
            ("full overlap", 0, "2050-01-01T12:00:00", 60, 400),
            ("full overlap (large)", 0, "2050-01-01T11:30:00", 120, 400),

            # частичные оверлапы
            ("inside existing booking", 0, "2050-01-01T12:15:00", 30, 400),
            ("overlap start", 0, "2050-01-01T11:45:00", 30, 400),
            ("overlap end ", 0, "2050-01-01T12:15:00", 30, 400),
    )
)
def test_reservation_crossing(test_name, test_db_client, table_id, time, duration, expected):
    payload = default_reservation()
    payload["reservation_time"] = "2050-01-01T12:00:00"
    initial_reservation = test_db_client.post("/reservations/reservation", json=payload)
    assert initial_reservation.status_code == 200

    test_reservation = {
        "customer_name": "new_reservation",
        "table_id": table_id,
        "reservation_time": time,
        "duration_minutes": duration
    }

    result = test_db_client.post("/reservations/reservation", json=test_reservation)
    assert result.status_code == expected
