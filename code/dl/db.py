from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

import psycopg2
db_string = 'postgresql://postgres:postgres@localhost:5432/our_table'

engine = create_engine ( db_string )
connection = engine.connect()
metadata = MetaData()
Session = sessionmaker ( bind = engine )
session = Session()

Base = automap_base()
Base.prepare ( engine, reflect = True )

Address = Base.classes.Adresa
Alergen = Base.classes.Alergen
Food = Base.classes.Jidlo
Menu = Base.classes.Menu
FoodOrder = Base.classes.ObjednavkaJidla
Reservation = Base.classes.Rezervace
Schedule = Base.classes.Rozvrh
Tabl = Base.classes.Stul
Customer = Base.classes.Uzivatel


def get_tables():
    tables = []
    for t in engine.table_names():
        tables.append(t)
    return tables

def add ( src ):
    session.add( src )
    session.commit()

def add_address ( city, psc, state, street ):
    new_address = Address ( Mesto = city, Psc = psc, Stat = state, Ulice = street )
    session.add ( new_address )
    session.commit()
    return

def add_alergen ( name ):
    new_alergen = Alergen ( Nazev = name )
    session.add ( new_alergen )
    session.commit()
    return


def delete_address ( id ):
    old_addres = session.query ( Address ).filter ( Address.AdresaID == id ).first()
    if old_addres == None:
        return
    session.delete ( old_addres )
    session.commit()
    return

delete_address (50)
result = session.query(Address).all()
for r in result:
    print( r.AdresaID )
for c in Base.classes:
    print ( c )
for i in get_tables():
    print ( i )