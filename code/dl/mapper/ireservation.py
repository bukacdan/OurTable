from typing import List
from dl.entity.reservation import Reservation
from .ibase import IBaseMapper


class IReservationMapper(IBaseMapper):
    """
    Interface for ReservationMapper
    """

    def get_all() -> List[Reservation]:
        """
        Retrieves all reservations from database

        Returns
        ----------
        list[Reservation]
            List of all reservations from database
        """
        pass

    def get(reservation_id: int) -> Reservation:
        """
        Retrieves a reservation from database

        Parameters
        ----------
        reservation_id: int
            ID of the reservation we want to get

        Returns
        ----------
        Reservation
            Reservation with the specified ID
        """
        pass

    def add(reservation: Reservation) -> bool:
        """
        Adds a reservation to database

        Parameters
        ----------
        reservation: Reservation
            Reservation to add to database

        Returns
        ----------
        bool
            True on success, False when reservation is already in database
        """
        pass

    def delete(reservation: Reservation) -> bool:
        """
        Deletes a reservation from database

        Parameters
        ----------
        reservation: Reservation
            Reservation to delete

        Returns
        ----------
        bool
            True on success, False when reservation is not in database
        """
        pass

