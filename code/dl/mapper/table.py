from dl.entity.db_engine import DBEngine
from dl.entity.table import Table
from dl.entity.schedule import Schedule
from dl.mapper.itable import ITableMapper


class TableMapper(ITableMapper):
    def __init__(self):
        pass

    def get_all(self):
        tables = DBEngine.get_session().query(Table).all()
        return tables

    def get(self, obj_id):
        return DBEngine.get_session().query(Table).filter(Table.StulID == obj_id).first()

    def add(self, obj):
        if self.get(obj.StulID):
            return False
        DBEngine.get_session().add(obj)
        DBEngine.get_session().commit()
        return True

    def delete(self, obj):
        if not self.get(obj.StulID):
            return False
        DBEngine.get_session().delete(obj)
        DBEngine.get_session().commit()
        return True

    def get_with(self, seats, schedules):
        tables = DBEngine.get_session().query(Table).join(
            schedules, Schedule.StulID == Table.StulID
        ).filter(Table.Pocetmist >= seats).all()
        return tables
