from app.models.reservation import ReservationModel
from fastapi import HTTPException


def get_reservations(session) -> list[ReservationModel]:
    return session.query(ReservationModel).all()


def create_reservation(reservation, session):
    reservation_model = ReservationModel(**dict(reservation))
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