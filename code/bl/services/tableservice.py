import datetime
from dl.mapper.table import TableMapper
from dl.mapper.schedule import ScheduleMapper

class TableService:
    def get_free_tables(self, since, count):
        allTables = TableMapper.get_all()
        allSchedules = ScheduleMapper.get_all()
        newsince = since + datetime.timedelta(hours = 2)

        schedules = allSchedules.filter(datetime.fromisoformat(Schedule.Datumdo) >= newsince, Schedule.Dotumod <= since)
        tables = allTables.join(schedules, allTables.StulID  == schedules.StulID)
    
        return tables