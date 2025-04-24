from app.models.reservation import ReservationModel
from fastapi import HTTPException
from datetime import datetime

def get_reservations(session) -> list[ReservationModel]:
    return session.query(ReservationModel).all()


def create_reservation(reservation, session):
    reservation_model = ReservationModel(**dict(reservation))
    if reservation_model.reservation_time < datetime.now():
        raise HTTPException(status_code=400, detail="Invalid reservation date/time.")
    if reservation_model.duration_minutes <= 0:
        raise HTTPException(status_code=400, detail="Duration can not be equal or less then 0.")
    try:
        session.add(reservation_model)
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Table booked."}


def delete_reservation(reservation_id, session):
    try:
        reservation = session.query(ReservationModel).filter(ReservationModel.id == reservation_id).one()
        session.delete(reservation)
        session.commit()
    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    return {"message": "Reservation removed."}