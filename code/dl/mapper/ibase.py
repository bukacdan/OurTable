from abc import ABC, abstractmethod
from typing import List


class IBaseMapper(ABC):
    """
    Base interface for all data mappers
    """

    @abstractmethod
    def get_all() -> List[object]:
        """
        Retrieves all objects from specific table

        Returns
        ----------
        list[object]
            All objects from specific table in database
        """
        pass

    @abstractmethod
    def get(objID: int) -> object:
        """
        Retrieves an object from specific table with the specified ID

        Parameters
        ----------
        objID: int
            ID of object we want to get from database

        Returns
        ----------
        object
            object from specific table
        """
        pass

    @abstractmethod
    def add(obj) -> bool:
        """
        Add an object to the database

        Parameters
        ----------
        obj:
            New object for database

        Returns
        ----------
        bool
            True on success, False when object is already in database
        """
        pass

    @abstractmethod
    def delete(obj) -> bool:
        """
        Deletes an object from the database

        Parameters
        ----------
        obj: object
            Old object for removal

        Returns
        ----------
        bool
            True on success, False when object is not in database
        """
        pass
