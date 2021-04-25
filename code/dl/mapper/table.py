from dl.entity.db_engine import DBEngine
from dl.entity.table import Table
from dl.entity.schedule import Schedule
from dl.mapper.itable import ITableMapper
from datetime import datetime, timedelta


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
        #tables = []
        tables = DBEngine.get_session().query(Table).join(schedules, Schedule.StulID == Table.StulID).filter(Table.Pocetmist >= seats).all()
        #for t,s in DBEngine().get_session().query(Table, schedules).filter (Table.StulID == Schedule.StulID).all():
         #   tables.add(t)
        #for i in schedules:
        #    print(1)
        return tables

    @staticmethod
    def tbl(since, count):
        newsince = since + timedelta(hours=2)
        schedules = DBEngine.get_session().query(Schedule)
        tables = DBEngine.get_session().query(Table).join(
            Schedule, Schedule.StulID == Table.StulID).filter(
                Schedule.Datumod >= since,
                Schedule.Datumdo <= newsince,
                Schedule.Jedostupny == True,
                Table.Pocetmist >= count
        ).all()
        return tables
