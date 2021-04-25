from typing import List
from dl.entity.alergen import Alergen
from .ibase import IBaseMapper
from abc import abstractmethod


class IAlergenMapper(IBaseMapper):
    """
    Interface for AlergenMapper
    """

    @abstractmethod
    def get_all(self) -> List[object]:
        """
        Retrieves all alergens from database

        Returns
        ----------
        list[Alergen]
            List of all alergens from database
        """
        pass

    @abstractmethod
    def get(self, alergen_id: int) -> Alergen:
        """
        Retrieves an alergen from database with the specified ID

        Parameters
        ----------
        alergen_id: int
            ID of the alergen to retrieve

        Returns
        ----------
        Alergen
            Alergen from database with the specified ID
        """
        pass

    @abstractmethod
    def add(self, alergen: Alergen) -> bool:
        """
        Adds an alergen to database

        Parameters
        ----------
        alergen: Alergen
            Alergen to add to database

        Returns
        ----------
        bool
             True on success, False when alergen is already in database
        """
        pass

    @abstractmethod
    def delete(self, alergen) -> bool:
        """
        Deletes an alergen from database

        Parameters
        ----------
        alergen: Alergen
            Alergen to remove from database

        Returns
        ----------
        bool
            True on success, False when alergen is not in database
        """
        pass
