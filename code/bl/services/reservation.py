from datetime import datetime, timedelta
from dl.mapper.itable import ITableMapper
from dl.entity.reservation import Reservation
from dl.mapper.ireservation import IReservationMapper


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
    def add_reservation(self, time: datetime, tableID: int, tableMapper: ITableMapper,
                        reservation_mapper: IReservationMapper) -> bool:
        reservation = Reservation(Datumod=time, Datumdo=time + timedelta(hours=2))
        reservation_mapper.add(reservation, tableMapper, tableID)
        return True
