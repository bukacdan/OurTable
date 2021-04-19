from .imapper import IMapper
from dl.entity.base import Session
from dl.entity.table import Table


class TableMapper(IMapper):
    @staticmethod
    def get_all():
        tables = Session.query(Table).all()
        return tables

    @staticmethod
    def get(objID):
        return Session.query(Table).filter(Table.StulID == objID).first()

    @staticmethod
    def add(obj):
        if TableMapper.get(obj.StulID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not TableMapper.get(obj.StulID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
