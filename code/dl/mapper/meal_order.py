from dl.entity.base import session
from dl.entity.meal_order import MealOrder
from dl.mapper.imeal_order import IMealOrderMapper


class MealOrderMapper(IMealOrderMapper):
    def __init__(self):
        super().__init__(MealOrder)

    def get(self, objID):
        return session.query(MealOrder).filter(MealOrder.Objednavka_jidlaID == objID).first()

    def add(self, obj):
        if self.get(obj.Objednavka_jidlaID):
            return False
        session.add(obj)
        session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.Objednavka_jidlaID):
            return False
        session.delete(obj)
        session.commit()
        return True
