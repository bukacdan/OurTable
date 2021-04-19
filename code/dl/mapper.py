from sqlalchemy import create_engine, MetaData, Table, func
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

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
Food = Base.classes.Jidlo
Menu = Base.classes.Menu
FoodOrder = Base.classes.ObjednavkaJidla
Reservation = Base.classes.Rezervace
Schedule = Base.classes.Rozvrh
Tabl = Base.classes.Stul
Customer = Base.classes.Uzivatel
IsPartOf = Base.classes.je_soucasti
Contains = Base.classes.obsahuje
IsReserved = Base.classes.je_zarezervovan
LivesAt = Base.classes.prebyva_na_adrese



def get_tables():
    tables = []
    for t in Base.metadata.tables.keys():
        tables.append(t)
    return tables

## add functions ##
# These functions are missing some utility,
# it is not recomended to use outside db.py
# will be private -> TODO make private ( __* )

def add_address ( city, psc, state, street ):
    session.add ( Address ( Mesto = city, Psc = psc, Stat = state, Ulice = street ) )
    session.commit()
    return

def add_alergen ( name ):
    session.add ( Alergen ( Nazev = name ) )
    session.commit()
    return

def add_food ( price, name ):
    session.add ( Food ( Cena = price, Nazev = name ) )
    session.commit()
    return

def add_menu ( until, since ):
    session.add ( Menu ( Platnostdo = until, Platnostod = since ) )
    session.commit()
    return

def add_foodorder ( count ):
    session.add ( FoodOrder ( Pocet = count ) )
    session.commit()
    return
# if function is not private, check for cutomer id
def add_reservation ( until, since, customerID ):
    session.add ( Reservation ( Datumdo = until, Datumod = since, UzivatelID = customerID ) )
    session.commit()
    return

def add_schedule ( until, since, avaiable, tableID ):
    session.add ( Schedule ( Datumdo = until, Datumod = since, Jedostupny = avaiable, StulID = tableID ) )
    session.commit()
    return

def add_table ( space ):
    session.add ( Tabl ( Pocetmist = space ) )
    session.commit()
    return

def add_customer ( email, name, surname, phonenumber ):
    session.add ( Customer ( Email = email, Jmeno = name, Prijmeni = surname, Telefon = phonenumber ) )
    session.commit()
    return

def add_ispartof ( foodID, alergenNumber ):
    session.add ( IsPartOf ( JidloID = foodID, Cislo = alergenNumber ) )
    session.commit()
    return

def add_contains ( menuID, foodID ):
    session.add ( Contains ( MenuID = menuID, JidloID = foodID ) )
    session.commit()
    return

def add_isreserved ( reservationID, tableID ):
    session.add ( IsReserved ( RezervaceID = reservationID, StulID = tableID ) )
    session.commit()
    return
def add_livesat ( addressID, customerID ):
    session.add ( LivesAt ( AdresaID = addressID, UzivatelID = customerID ) )
    session.commit()
    return

## Delete functions ##    
# These functions are missing some utility,
# it is not recomended to use outside db.py
# will be private -> TODO make private ( __* )

def delete_address ( id ):
    address = session.query ( Address ).filter ( Address.AdresaID == id ).first()
    if address is None:
        return False
    session.delete ( address )
    session.commit()
    return True

def delete_alergen ( id ):
    alergen = session.query ( Alergen ).filter ( Alergen.Cislo == id ).first()
    if alergen is None:
        return False
    session.delete ( alergen )
    session.commit()
    return True

def delete_food ( id ):
    food = session.query ( Food ).filter ( Food.JidloID == id ).first()
    if food is None:
        return False
    session.delete ( food  )
    session.commit()
    return True

def delete_menu  ( id ):
    menu = session.query ( Menu ).filter ( Menu.MenuID == id ).first()
    if menu is None:
        return False
    session.delete ( menu )
    session.commit()
    return True

def delete_foodorder ( id ):
    foodorder = session.query ( FoodOrder ).filter ( FoodOrder.ObjednavkaJidlaID == id ).first()
    if foodorder is None:
        return False
    session.delete ( foodorder )
    session.commit()
    return True

def delete_reservation ( id ):
    reservation = session.query ( Reservation ).filter ( Reservation.RezervaceID == id ).first()
    if reservation is None:
        return False
    session.delete ( reservation )
    session.commit()
    return True

def delete_schedule ( id ):
    schedule = session.query ( Schedule ).filter ( Schedule.RozvrhID == id ).first()
    if schedule is None:
        return False
    session.delete ( schedule )
    session.commit()
    return True

def delete_table ( id ):
    table = session.query ( Tabl ).filter ( Tabl.StulID == id ).first()
    if table is None:
        return False
    session.delete ( table )
    session.commit()
    return True

def delete_customer ( id ):
    customer = session.query ( Customer ).filter ( Customer.UzivatelID == id ).first()
    if customer is None:
        return False
    session.delete ( customer )
    session.commit()
    return True

def delete_ispartof ( id ):
    ispartof = session.query ( IsPartOf ).filter ( IsPartOf.Je_SoucastiID == id ).first()
    if ispartof is None:
        return False
    session.delete ( ispartof )
    session.commit()
    return True

def delete_contains ( id ):
    contains = session.query ( Contains ).filter ( Contains.ObsahujeID == id ).first()
    if contains is None:
        return False
    session.delete ( contains )
    session.commit()
    return True

def delete_isreserved ( id ):
    isreserved = session.query ( IsReserved ).filter ( IsReserved.Je_zarezervovanID == id ).first()
    if isreserved is None:
        return False
    session.delete ( isreserved )
    session.commit()
    return True

def delete_livesat ( id ):
    livesat = session.query ( LivesAt ).filter ( LivesAt.Prebyva_na_adreseID == id ).first()
    if livesat is None:
        return False
    session.delete ( livesat )
    session.commit()
    return True

## Tests ##

#TEST ONLY ON NEW DATABASE
def try_all():
    add_address ( "Praha", 15000, "CZ", "Londynska" )

    add_alergen ( "roztoci" )

    add_food ( 129, "Svickova" )

    add_menu ( "12.01.2020", "06.01.2020" )

    add_foodorder ( 10 )

    add_customer ( "jd@gmail.com", "John", "Doe", "111" )

    #Why date?
    add_reservation ( "12.01.2020", "06.01.2020", 1 )

    add_table ( 5 )

    add_schedule ( "12.01.2020", "06.01.2020", True, 1 )

    add_ispartof ( 1, 1 )

    add_contains ( 1, 1 )

    add_isreserved ( 1, 1 )
    
    add_livesat ( 1, 1 )

    delete_livesat ( 1 )
    delete_isreserved ( 1 )
    delete_contains ( 1 )
    delete_ispartof ( 1 )
    delete_schedule ( 1 )
    delete_table ( 1 )
    delete_reservation ( 1 )
    delete_customer ( 1 )
    delete_foodorder ( 1 )
    delete_menu ( 1 )
    delete_food ( 1 )
    delete_alergen ( 1 )
    delete_address ( 1 )

    return

def delete_in_wrong_order():
    add_address ( "Praha", 15000, "CZ", "Londynska" )
    add_customer ( "jd@gmail.com", "John", "Doe", "111" )
    idAdd = session.query ( func.max ( Address.AdresaID ) ).scalar()
    idCustomer = session.query ( func.max ( Customer.UzivatelID ) ).scalar()

    add_livesat ( idAdd, idCustomer )
    delete_address ( idAdd )
    return

## ##

try_all()