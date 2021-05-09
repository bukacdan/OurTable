from datetime import datetime, timedelta

from typing import List

from dl.mapper.itable import ITableMapper
from dl.entity.table import Table


class TableService:
    """
    Manages table methods
    """

    @staticmethod
    def get_free_tables(since: datetime, count: int, table_mapper: ITableMapper) -> List[Table]:
        """
        Retrieves all free tables in specified time + 2 hours from database

        Parameters
        ----------
        since: datetime
            datetime to filter tables based on their availability
        count: int
            minimal size of tables to retrieve

        Returns
        ----------
        list[Table]
            List of all free tables from database
        """
        until = since + timedelta(hours=2)
        return table_mapper.get_free_tables(count, since, until)
