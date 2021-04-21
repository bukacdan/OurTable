from dl.entity.base import session
from dl.entity.table import Table
from dl.mapper.itable import ITableMapper


class TableMapper(ITableMapper):
    def __init__(self):
        super().__init__(Table)

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
