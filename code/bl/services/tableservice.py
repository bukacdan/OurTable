from datetime import datetime, timedelta

from typing import List

from dl.mapper.itable import ITableMapper
from dl.mapper.ischedule import IScheduleMapper

from dl.entity.table import Table


class TableService:
    """
    Manages table methods
    """

    def get_free_tables(self, since: datetime, count: int, table_mapper: ITableMapper, schedule_mapper: IScheduleMapper) -> List[Table]:
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
        tables = table_mapper.tbl(since, count)
        return tables



        #newsince = since + timedelta(hours=2)
        #schedules = schedule_mapper.filter_on_date(since, newsince, True)
        #schedules = schedule_mapper.get_all()
        #if not schedules:
        #    return []
        #tables = table_mapper.get_with(count, schedules)
        #return tables
