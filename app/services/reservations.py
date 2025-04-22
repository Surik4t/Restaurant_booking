from app.models.reservation import Reservation
from datetime import datetime
from database import session
from fastapi import HTTPException

tables = []

def get_reservations() -> list[Reservation]:
    reservations = [reservation for reservation in session.query(Reservation)]
    return reservations


def create_reservation(reservation):
    reservation_model = Reservation(**dict(reservation))
    with session:
        try:
            session.add(reservation_model)
            session.commit()
        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Table booked."}


def delete_reservation(reservation_id):
    try:
        reservation = session.query(Reservation).filter(Reservation.id==reservation_id).one()
        session.delete(reservation)
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Reservation removed."}