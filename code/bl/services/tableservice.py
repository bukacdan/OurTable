import datetime
from dl.mapper.itable import ITableMapper
from dl.mapper.ischedule import IScheduleMapper

class TableService:
    """
    Manages table methods
    """

    def get_free_tables(self, since: datetime, count: int, tableMapper: ITableMapper, scheduleMapper: IScheduleMapper) -> List[Table]:
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
        newsince = since + timedelta(hours = 2)
        schedules = scheduleMapper.filter_on_date(since, newsince, True)
        tables = tableMapper.join_with(count, schedules)
        return tables