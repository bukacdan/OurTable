from typing import List
from dl.entity.table import Table
from .ibase import IBaseMapper
from abc import abstractmethod


class ITableMapper(IBaseMapper):
    """
    Interface for TableMapper
    """

    def get_all() -> List[Table]:
        """
        Retrieves all tables from database

        Returns
        ----------
        list[Table]
            List of all tables from database
        """
        pass

    def get(table_id: int) -> Table:
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

    def add(table: Table) -> bool:
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

    def delete(table: Table) -> bool:
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

