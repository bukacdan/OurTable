from .base import Base
from dl.entity.base import Session
from dl.entity.meal import Meal


class MealMapper(Base):
    def __init__(self):
        super().__init__(Meal)

    def get(self, objID):
        return Session.query(Meal).filter(Meal.JidloID == objID).first()

    def add(self, obj):
        if self.get(obj.JidloID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.JidloID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
