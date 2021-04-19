from .imapper import IMapper
from dl.entity.base import Session
from dl.entity.meal import Meal


class MealMapper(IMapper):
    @staticmethod
    def get_all():
        meals = Session.query(Meal).all()
        return meals

    @staticmethod
    def get(objID):
        return Session.query(Meal).filter(Meal.JidloID == objID).first()

    @staticmethod
    def add(obj):
        if MealMapper.get(obj.JidloID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not MealMapper.get(obj.JidloID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
