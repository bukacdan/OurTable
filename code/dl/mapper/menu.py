from dl.entity.db_engine import DBEngine
from dl.entity.menu import Menu
from dl.mapper.imenu import IMenuMapper


class MenuMapper(IMenuMapper):
    def __init__(self):
        pass

    def get_all(self):
        menus = DBEngine.get_session().query(Menu).all()
        return menus

    def get(self, obj_id):
        return DBEngine.get_session().query(Menu).filter(Menu.MenuID == obj_id).first()

    def add(self, obj):
        if self.get(obj.MenuID):
            return False
        DBEngine.get_session().add(obj)
        DBEngine.get_session().commit()
        return True

    def delete(self, obj):
        if not self.get(obj.MenuID):
            return False
        DBEngine.get_session().delete(obj)
        DBEngine.get_session().commit()
        return True
