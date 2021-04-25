from dl.entity.db_engine import DBEngine
from dl.entity.meal_order import MealOrder
from dl.mapper.imeal_order import IMealOrderMapper


class MealOrderMapper(IMealOrderMapper):
    def __init__(self):
        pass

    def get_all(self):
        mealorders = DBEngine.get_session().query(MealOrder).all()
        return mealorders

    def get(self, obj_id: int):
        return DBEngine.get_session().query(MealOrder).filter(MealOrder.Objednavka_jidlaID == obj_id).first()

    def add(self, obj: MealOrder):
        if self.get(obj.Objednavka_jidlaID):
            return False
        DBEngine.get_session().add(obj)
        DBEngine.get_session().commit()
        return True

    def delete(self, obj: MealOrder):
        if not self.get(obj.Objednavka_jidlaID):
            return False
        DBEngine.get_session().delete(obj)
        DBEngine.get_session().commit()
        return True
