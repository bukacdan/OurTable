from .imapper import IMapper
from dl.entity.menu import Menu


class MenuMapper(IMapper):
    @staticmethod
    def get_all():
        menus = session.query(Menu).all()
        return menus

    @staticmethod
    def get(objID):
        return session.query(Menu).filter(Menu.MenuID == objID).first()

    @staticmethod
    def add(obj):
        if MenuMapper.get(obj.MenuID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not MenuMapper.get(obj.MenuID):
            return False
        session.delete(obj)
        session.commit()
        return True
