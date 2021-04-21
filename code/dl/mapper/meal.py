from dl.entity.base import session
from dl.entity.meal import Meal
from dl.mapper.imeal import IMealMapper


class MealMapper(IMealMapper):
    def __init__(self):
        super().__init__(Meal)

    def get(self, objID):
        return session.query(Meal).filter(Meal.JidloID == objID).first()

    def add(self, obj):
        if self.get(obj.JidloID):
            return False
        session.add(obj)
        session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.JidloID):
            return False
        session.delete(obj)
        session.commit()
        return True
