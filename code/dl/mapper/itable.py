from typing import List, Any
from dl.entity.table import Table
from .ibase import IBaseMapper
from abc import abstractmethod
from datetime import datetime

from dl.entity.schedule import Schedule


class ITableMapper(IBaseMapper):
    """
    Interface for TableMapper
    """

    @abstractmethod
    def get_all(self) -> List[Table]:
        """
        Retrieves all tables from database

        Returns
        ----------
        list[Table]
            List of all tables from database
        """
        pass

    @abstractmethod
    def get(self, table_id: int) -> Table:
        """
        Retrieves a table from database

        Parameters
        ----------
        table_id: int
            ID of the table we want to get

        Returns
        ----------
        Table
            Table with the specified ID
        """
        pass

    @abstractmethod
    def add(self, table: Table) -> bool:
        """
        Adds a table to database

        Parameters
        ----------
        table: Table
            Table to add to database

        Returns
        ----------
        bool
            True on success, False when table is already in database
        """
        pass

    @abstractmethod
    def delete(self, table: Table) -> bool:
        """
        Deletes a table from database

        Parameters
        ----------
        table: Table
            Table to delete

        Returns
        ----------
        bool
            True on success, False when table is not in database
        """
        pass

    @abstractmethod
    def get_free_tables(self, seats: int, since: datetime, until: datetime):
        """
        Get free table for a given interval

        Parameters
        ----------
        seats: int
            minimal number of seats
        since: datetime
            date from
        until: datetime
            date to

        Returns
        ---------
        Table satisfying given parameters
        """
        pass
