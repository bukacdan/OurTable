from .imapper import IMapper
from dl.entity.mealorder import MealOrder


class MealOrderMapper(IMapper):
    @staticmethod
    def get_all():
        mealorders = session.query(MealOrder).all()
        return mealorders

    @staticmethod
    def get(objID):
        return session.query(MealOrder).filter(MealOrder.Objednavka_jidlaID == objID).first()

    @staticmethod
    def add(obj):
        if MealOrderMapper.get(obj.Objednavka_jidlaID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not MealOrderMapper.get(obj.Objednavka_jidlaID):
            return False
        session.delete(obj)
        session.commit()
        return True
