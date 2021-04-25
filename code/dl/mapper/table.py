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

    def get(self, obj_id):
        return session.query(Table).filter(Table.StulID == obj_id).first()

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

    def get_with(self, seats, schedules):
        tables = session.query(Table).join(
            schedules, schedule.StulID == Table.StulID
        ).filter(Table.Pocetmist >= seats).all()
        return tables
