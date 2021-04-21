from dl.entity.base import Session
from dl.entity.menu import Menu
from dl.mapper.imenu import IMenuMapper


class MenuMapper(IMenuMapper):
    def __init__(self):
        super().__init__(Menu)

    def get(self, objID):
        return Session.query(Menu).filter(Menu.MenuID == objID).first()

    def add(self, obj):
        if self.get(obj.MenuID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.MenuID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
