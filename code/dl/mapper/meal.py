from dl.entity.db_engine import DBEngine
from dl.entity.meal import Meal
from dl.mapper.imeal import IMealMapper


class MealMapper(IMealMapper):
    def __init__(self):
        pass

    def get_all(self):
        meals = DBEngine.get_session().query(Meal).all()
        return meals

    def get(self, obj_id: int):
        return DBEngine.get_session().query(Meal).filter(Meal.JidloID == obj_id).first()

    def add(self, obj: Meal):
        if self.get(obj.JidloID):
            return False
        DBEngine.get_session().add(obj)
        DBEngine.get_session().commit()
        return True

    def delete(self, obj: Meal):
        if not self.get(obj.JidloID):
            return False
        DBEngine.get_session().delete(obj)
        DBEngine.get_session().commit()
        return True
