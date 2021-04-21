from .base import Base
from dl.entity.base import Session
from dl.entity.meal_order import MealOrder


class MealOrderMapper(Base):
    def __init__(self):
        super().__init__(MealOrder)

    def get(self, objID):
        return Session.query(MealOrder).filter(MealOrder.Objednavka_jidlaID == objID).first()

    def add(self, obj):
        if self.get(obj.Objednavka_jidlaID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.Objednavka_jidlaID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
