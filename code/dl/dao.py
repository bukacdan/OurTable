from sqlalchemy import create_engine, MetaData, Table, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base
from entities import Address, Alergen, Customer, Meal, Menu, MealOrder, Reservation, Schedule, Tbl
from entities.declaration import session

from abc import ABC, abstractmethod

import psycopg2



class IMealDAO(ABC):

    @abstractmethod
    def get_meals(self):
        pass

    def add_meal(self):
        pass

    def delete_meal(self):
        pass


## Concrete classes ##

class MealDAO(IMealDAO):

    @classmethod
    def get_meals(self):
        mealList = []
        meals = session.query(Meal).all()
        for m in meals:
            mealList.append((m.Cena, m.Nazev))
        
        return mealList

    @classmethod
    def add_meal(self, price, name):
        meal = session.query(Meal).filter(Meal.Cena == price, Meal.Nazev == name).first()
        if meal is not None:
            return False
        session.add(Meal(Cena = price, Nazev = name))
        session.commit()
        return True

    @classmethod
    def delete_meal(self, id):
        meal = session.query(Meal).filter(Meal.JidloID == id).first()
        if meal is None:
            return False
        session.delete(meal)
        session.commit()
        return True

