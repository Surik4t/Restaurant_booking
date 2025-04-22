from fastapi import APIRouter
from app.schemas.reservations import Reservation
from app.services.reservations import get_reservations, create_reservation, delete_reservation

router = APIRouter(prefix="/reservations", tags=["reservations"])

@router.get("/")
def read_tables():
    return get_reservations()


@router.post("/reservation")
def add_table(reservation: Reservation):
    return create_reservation(reservation)


@router.delete("/{reservation_id}")
def remove_table(reservation_id: int):
    return delete_reservation(reservation_id)