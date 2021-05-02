from typing import List
from abc import abstractmethod
from dl.entity.reservation import Reservation
from .itable import ITableMapper
from .ibase import IBaseMapper


class IReservationMapper(IBaseMapper):
    """
    Interface for ReservationMapper
    """

    @abstractmethod
    def get_all(self) -> List[Reservation]:
        """
        Retrieves all reservations from database

        Returns
        ----------
        list[Reservation]
            List of all reservations from database
        """
        pass

    @abstractmethod
    def get(self, reservation_id: int) -> Reservation:
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

    @abstractmethod
    def add(self, reservation: Reservation, tableMapper: ITableMapper, tableID: int) -> bool:
        """
        Adds a reservation to database

        Parameters
        ----------
        reservation: Reservation
            Reservation to add to database
        tableMapper: ITableMapper
            TableMapper to be injected
        tableID: int
            ID of the table to be reserved

        Returns
        ----------
        bool
            True on success, False when reservation is already in database
        """
        pass

    @abstractmethod
    def delete(self, reservation: Reservation) -> bool:
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
