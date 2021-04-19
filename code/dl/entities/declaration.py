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