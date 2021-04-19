from .imapper import IMapper
from dl.entity.meal import Meal


class MealMapper(IMapper):
    @staticmethod
    def get_all():
        meals = session.query(Meal).all()
        return meals

    @staticmethod
    def get(objID):
        return session.query(Meal).filter(Meal.JidloID == objID).first()

    @staticmethod
    def add(obj):
        if MealMapper.get(obj.JidloID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not MealMapper.get(obj.JidloID):
            return False
        session.delete(obj)
        session.commit()
        return True
