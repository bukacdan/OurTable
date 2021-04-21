from .imapper import IMapper
from dl.entity.base import session
from dl.entity.table import Table


class TableMapper(IMapper):
    @staticmethod
    def get_all():
        tables = session.query(Table).all()
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

    @staticmethod
    def get_all_free(since, count):
        newsince = since + datetime.timedelta(hours = 2)
        schedules = session.query(Schedule).filter(datetime.fromisoformat(Schedule.Datumdo) >= newsince, Schedule.Dotumod <= since) 

        tables = Table.join(schedules, Table.StulID  == schedules.StulID)
        return tables