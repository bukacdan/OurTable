from dl.entity.base import session
from dl.entity.table import Table
from dl.mapper.itable import ITableMapper
from dl.mapper.schedule import Schedule
import datetime


class TableMapper(ITableMapper):
    def __init__(self):
        pass

    def get_all(self):
        tables = session.query(Table).all()
        return tables

    def get(self, objID):
        return session.query(Table).filter(Table.StulID == objID).first()

    def add(self, obj):
        if self.get(obj.StulID):
            return False
        session.add(obj)
        session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.StulID):
            return False
        session.delete(obj)
        session.commit()
        return True

    def get_all_free(self, since, count):
        newsince = since + datetime.timedelta(hours = 2)
        schedules = session.query(Schedule).filter(datetime.fromisoformat(Schedule.Datumdo) >= newsince, Schedule.Dotumod <= since)

        tables = Table.join(schedules, Table.StulID  == schedules.StulID)
        return tables
