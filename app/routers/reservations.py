from fastapi import APIRouter
from database import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from app.schemas.reservations import ReservationSchema
from app.services.reservations import get_reservations, create_reservation, delete_reservation

router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.get("/")
def read_tables(session: Session = Depends(get_db)):
    return get_reservations(session)


@router.post("/reservation")
def add_table(reservation: ReservationSchema, session: Session = Depends(get_db)):
    return create_reservation(reservation, session)


@router.delete("/{reservation_id}")
def remove_table(reservation_id: int, session: Session = Depends(get_db)):
    return delete_reservation(reservation_id, session)