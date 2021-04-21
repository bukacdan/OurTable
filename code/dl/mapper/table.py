from .imapper import IMapper
from dl.entity.base import session
from dl.entity.table import Table
from dl.entity.schedule import Schedule
from datetime import timedelta
from sqlalchemy import or_


class TableMapper(IMapper):
    @staticmethod
    def get_all():
        tables = session.query(Table).all()
        return tables

    @staticmethod
    def get_all_free(since, count):
        newsince = since + timedelta(hours=2)
        schedules = session.query(Schedule)

        tables = session.query(Table).join(
            Schedule, Schedule.StulID == Table.StulID).filter(
                Schedule.Datumod >= since,
                Schedule.Datumdo <= newsince,
                Schedule.Jedostupny == True,
                Table.Pocetmist >= count
        ).all()
        return tables

    @staticmethod
    def get(objID):
        return session.query(Table).filter(Table.StulID == objID).first()

    @staticmethod
    def add(obj):
        if TableMapper.get(obj.StulID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not TableMapper.get(obj.StulID):
            return False
        session.delete(obj)
        session.commit()
        return True
