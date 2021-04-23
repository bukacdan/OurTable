from typing import List
from dl.entity.alergen import Alergen
from .ibase import IBaseMapper


class IAlergenMapper(IBaseMapper):
    """
    Interface for AlergenMapper
    """

    def get_all() -> List[object]:
        """
        Retrieves all alergens from database

        Returns
        ----------
        list[Alergen]
            List of all alergens from database
        """
        pass

    def get(alergen_ID: int) -> Alergen:
        """
        Retrieves an alergen from database with the specified ID

        Parameters
        ----------
        alergen_ID: int
            ID of the alergen to retrieve

        Returns
        ----------
        Alergen
            Alergen from database with the specified ID
        """
        pass

    def add(alergen: Alergen) -> bool:
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

    def delete(alergen) -> bool:
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
