from .base import Base
from dl.entity.base import Session
from dl.entity.table import Table


class TableMapper(Base):
    def __init__(self):
        super().__init__(Table)

    def get(self, objID):
        return Session.query(Table).filter(Table.StulID == objID).first()

    def add(self, obj):
        if self.get(obj.StulID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.StulID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
