from typing import List
from dl.entity.schedule import Schedule
from .ibase import IBaseMapper


class IScheduleMapper(IBaseMapper):
    """
    Interface for ScheduleMapper
    """

    def get_all() -> List[Schedule]:
        """
        Retrieves all schedules from database

        Returns
        ----------
        list[Schedule]
            List of all schedules from database
        """
        pass

    def get(schedule_id: int) -> Schedule:
        """
        Retrieves a schedule from database

        Parameters
        ----------
        schedule_id: int
            ID of the schedule we want to get

        Returns
        ----------
        Schedule
            Schedule with the specified ID
        """
        pass

    def add(schedule: Schedule) -> bool:
        """
        Adds a schedule to database

        Parameters
        ----------
        schedule: Schedule
            Schedule to add to database

        Returns
        ----------
        bool
            True on success, False when schedule is already in database
        """
        pass

    def delete(schedule: Schedule) -> bool:
        """
        Deletes a schedule from database

        Parameters
        ----------
        schedule: Schedule
            Schedule to delete

        Returns
        ----------
        bool
            True on success, False when schedule is not in database
        """
        pass

