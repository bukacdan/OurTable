from typing import List
from dl.entity.address import Address
from .ibase import IBaseMapper


class IAddressMapper(IBaseMapper):
    """
    Interface for AddressMapper
    """

    def get_all() -> List[Address]:
        """
        Retrieves all addresses from database

        Returns
        ----------
        list[Address]
            All addresses from database
        """
        pass

    def get(address_ID: int) -> Address:
        """
        Retrieves an address from database

        Parameters
        ----------
        address_ID: int
            ID of the address to retrieve

        Returns
        ----------
        Address
            Address from database with the specified ID
        """
        pass

    def add(address: Address) -> bool:
        """
        Adds an address to database

        Parameters
        ----------
        address: Address
            Address to add to database

        Returns
        ----------
        bool
            True on success, False when address is already in database
        """
        pass

    def delete(address: Address) -> bool:
        """
        Deletes an address from database

        Parameters
        ----------
        address: Address
            Address to delete from database

        Returns
        ----------
        bool
            True on success, False when address is not in database
        """
        pass
