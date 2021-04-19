from .imapper import IMapper
from dl.entity.table import Table


class TableMapper(IMapper):
    @staticmethod
    def get_all():
        tbls = session.query(Tbl).all()
        return tbls

    @staticmethod
    def get(objID):
        return session.query(Tbl).filter(Tbl.StulID == objID).first()

    @staticmethod
    def add(obj):
        if TblMapper.get(obj.StulID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not TblMapper.get(obj.StulID):
            return False
        session.delete(obj)
        session.commit()
        return True
