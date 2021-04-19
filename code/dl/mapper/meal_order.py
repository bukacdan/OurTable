from .imapper import IMapper
from dl.entity.base import Session
from dl.entity.mealorder import MealOrder


class MealOrderMapper(IMapper):
    @staticmethod
    def get_all():
        mealorders = Session.query(MealOrder).all()
        return mealorders

    @staticmethod
    def get(objID):
        return Session.query(MealOrder).filter(MealOrder.Objednavka_jidlaID == objID).first()

    @staticmethod
    def add(obj):
        if MealOrderMapper.get(obj.Objednavka_jidlaID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not MealOrderMapper.get(obj.Objednavka_jidlaID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
