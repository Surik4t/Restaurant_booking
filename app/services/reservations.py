from app.models.reservation import ReservationModel
from fastapi import HTTPException
from datetime import datetime, timedelta

def get_reservations(session) -> list[ReservationModel]:
    return session.query(ReservationModel).all()


def is_booked(new_reservation, existing_reservation):
    new_start = new_reservation.reservation_time
    new_end = new_reservation.reservation_time + timedelta(minutes=new_reservation.duration_minutes)
    existing_start = existing_reservation.reservation_time
    existing_end = existing_reservation.reservation_time + timedelta(minutes=existing_reservation.duration_minutes)
    return existing_start < new_end and existing_end > new_start


def create_reservation(reservation_data, session):
    reservation = ReservationModel(**dict(reservation_data))
    if reservation.reservation_time < datetime.now() - timedelta(minutes=1):
        raise HTTPException(status_code=400, detail="Invalid reservation date/time.")
    if reservation.duration_minutes <= 0:
        raise HTTPException(status_code=400, detail="Duration can not be equal or less then 0.")
    existing_reservations = session.query(ReservationModel).filter(ReservationModel.table_id == reservation.table_id).all()
    conflict = [is_booked(reservation, existing_reservation) for existing_reservation in existing_reservations]
    if any(conflict):
        raise HTTPException(status_code=400, detail="Table already booked.")

    try:
        session.add(reservation)
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
