from dl.entity.base import session
from dl.entity.menu import Menu
from dl.mapper.imenu import IMenuMapper


class MenuMapper(IMenuMapper):
    def __init__(self):
        super().__init__(Menu)

    def get(self, objID):
        return session.query(Menu).filter(Menu.MenuID == objID).first()

    def add(self, obj):
        if self.get(obj.MenuID):
            return False
        session.add(obj)
        session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.MenuID):
            return False
        session.delete(obj)
        session.commit()
        return True
