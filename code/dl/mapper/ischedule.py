from typing import List
from abc import abstractmethod
from dl.entity.schedule import Schedule
from .ibase import IBaseMapper

from datetime import datetime


class IScheduleMapper(IBaseMapper):
    """
    Interface for ScheduleMapper
    """

    @abstractmethod
    def get_all(self) -> List[Schedule]:
        """
        Retrieves all schedules from database

        Returns
        ----------
        list[Schedule]
            List of all schedules from database
        """
        pass

    @abstractmethod
    def get(self, schedule_id: int) -> Schedule:
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

    @abstractmethod
    def add(self, schedule: Schedule) -> bool:
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

    @abstractmethod
    def delete(self, schedule: Schedule) -> bool:
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

    @abstractmethod
    def filter_on_date(self, since: datetime, until: datetime, availability: bool) -> List[Schedule]:
        """
        Filters based on time interval and availability

        Parameters
        ----------
        since: datetime
            bottom interval boundary
        until: datetime
            upper interval boundary
        availability: boolean
            tables availability

        Returns
        ---------
        List of tables fulfiling criteriea;
        """
