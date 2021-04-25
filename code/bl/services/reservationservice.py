from datetime import datetime, timedelta
from dl.mapper.ireservation import IReservationMapper
from dl.entity.reservation import Reservation

class ReservationService:
    """
    Adds new reservation to database for 2 hours

    Parameters
    ----------
    time: datetime
        start of reservation
    tableID: int
        ID of reserved table

    Returns
    ----------
    bool
        True at success, False when reservation fails
    """
    def add_reservation(self, time: datetime, tableID: int, reservationMapper: IReservationMapper) -> bool:
        reservation = Reservation (Datumdo = time + timedelta(hours = 2), Datumod = time)
        reservation.Rezervace.stul_collection.append(tableID)
        return reservationMapper.add(reservation)