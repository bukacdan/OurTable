from sqlalchemy import create_engine, MetaData, Table, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

from abc import ABC, abstractmethod

import psycopg2
db_string = 'postgresql://postgres:postgres@localhost:5432/our_table'

engine = create_engine ( db_string )
connection = engine.connect()
metadata = MetaData()
Session = sessionmaker ( bind = engine )
session = Session()

Base = automap_base( bind = engine )
Base.prepare ( engine, reflect = True )

Address = Base.classes.Adresa
Alergen = Base.classes.Alergen
Meal = Base.classes.Jidlo
Menu = Base.classes.Menu
Mealrder = Base.classes.ObjednavkaJidla
Reservation = Base.classes.Rezervace
Schedule = Base.classes.Rozvrh
Tabl = Base.classes.Stul
Customer = Base.classes.Uzivatel
IsPartOf = Base.classes.je_soucasti
Contains = Base.classes.obsahuje
IsReserved = Base.classes.je_zarezervovan
LivesAt = Base.classes.prebyva_na_adrese

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

