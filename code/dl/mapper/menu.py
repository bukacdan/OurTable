from .imapper import IMapper
from dl.entity.base import Session
from dl.entity.menu import Menu


class MenuMapper(IMapper):
    @staticmethod
    def get_all():
        menus = Session.query(Menu).all()
        return menus

    @staticmethod
    def get(objID):
        return Session.query(Menu).filter(Menu.MenuID == objID).first()

    @staticmethod
    def add(obj):
        if MenuMapper.get(obj.MenuID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not MenuMapper.get(obj.MenuID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
