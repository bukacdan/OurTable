from entities.declaration import session

from entities.alergen import Alergen
from entities.address import Address
from entities.customer import Customer
from entities.meal import Meal as Meal
from entities.mealorder import MealOrder
from entities.menu import Menu as Menu
from entities.reservation import Reservation
from entities.schedule import Schedule
from entities.tbl import Tbl

from abc import ABC, abstractstaticmethod


# Interfaces classess #

class IDbTableMapper(ABC):

    # [@param-return] All objects from specific table in database
    @abstractstaticmethod
    def get_all():
        pass

    # [@param-in] ID of object we want to get from database
    # [@param-return] object from specific table
    @abstractstaticmethod
    def get(objID):
        pass

    # [@param-in] new object for database
    # [@param-return] True at success, False when object is already in database
    @abstractstaticmethod
    def add(obj):
        pass

    # [@param-in] old object for removal
    # [@param-out] True at success, False when object is not in database
    @abstractstaticmethod
    def delete(obj):
        pass


# Concrete classes #

class MealMapper(IDbTableMapper):

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


class AddressMapper(IDbTableMapper):

    @staticmethod
    def get_all():
        addresses = session.query(Address).all()
        return addresses

    @staticmethod
    def get(objID):
        return session.query(Address).filter(Address.AdresaID == objID).first()

    @staticmethod
    def add(obj):
        if AddressMapper.get(obj.AdresaID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not AddressMapper.get(obj.AdresaID):
            return False
        session.delete(obj)
        session.commit()
        return True


class AlergenMapper(IDbTableMapper):

    @staticmethod
    def get_all():
        alergens = session.query(Alergen).all()
        return alergens

    @staticmethod
    def get(objID):
        return session.query(Alergen).filter(Alergen.Cislo == objID).first()

    @staticmethod
    def add(obj):
        if AlergenMapper.get(obj.Cislo):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not AlergenMapper.get(obj.Cislo):
            return False
        session.delete(obj)
        session.commit()
        return True


class CustomerMapper(IDbTableMapper):

    @staticmethod
    def get_all():
        customers = session.query(Customer).all()
        return customers

    @staticmethod
    def get(objID):
        return session.query(Customer).filter(Customer.UzivatelID == objID).first()

    @staticmethod
    def add(obj):
        if CustomerMapper.get(obj.UzivatelID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not CustomerMapper.get(obj.UzivatelID):
            return False
        session.delete(obj)
        session.commit()
        return True


class MealOrderMapper(IDbTableMapper):

    @staticmethod
    def get_all():
        mealorders = session.query(MealOrder).all()
        return mealorders

    @staticmethod
    def get(objID):
        return session.query(MealOrder).filter(MealOrder.Objednavka_jidlaID == objID).first()

    @staticmethod
    def add(obj):
        if MealOrderMapper.get(obj.Objednavka_jidlaID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not MealOrderMapper.get(obj.Objednavka_jidlaID):
            return False
        session.delete(obj)
        session.commit()
        return True


class MenuMapper(IDbTableMapper):

    @staticmethod
    def get_all():
        menus = session.query(Menu).all()
        return menus

    @staticmethod
    def get(objID):
        return session.query(Menu).filter(Menu.MenuID == objID).first()

    @staticmethod
    def add(obj):
        if MenuMapper.get(obj.MenuID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not MenuMapper.get(obj.MenuID):
            return False
        session.delete(obj)
        session.commit()
        return True


class ReservationMapper(IDbTableMapper):

    @staticmethod
    def get_all():
        reservations = session.query(Reservation).all()
        return reservations

    @staticmethod
    def get(objID):
        return session.query(Reservation).filter(Reservation.RezervaceID == objID).first()

    @staticmethod
    def add(obj):
        if ReservationMapper.get(obj.RezervaceID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not ReservationMapper.get(obj.RezervaceID):
            return False
        session.delete(obj)
        session.commit()
        return True


class ScheduleMapper(IDbTableMapper):

    @staticmethod
    def get_all():
        schedules = session.query(Schedule).all()
        return schedules

    @staticmethod
    def get(objID):
        return session.query(Schedule).filter(Schedule.RozvrhID == objID).first()

    @staticmethod
    def add(obj):
        if ScheduleMapper.get(obj.RozvrhID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not ScheduleMapper.get(obj.RozvrhID):
            return False
        session.delete(obj)
        session.commit()
        return True


class TblMapper(IDbTableMapper):

    @staticmethod
    def get_all():
        tbls = session.query(Tbl).all()
        return tbls

    @staticmethod
    def get(objID):
        return session.query(Tbl).filter(Tbl.StulID == objID).first()

    @staticmethod
    def add(obj):
        if TblMapper.get(obj.StulID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not TblMapper.get(obj.StulID):
            return False
        session.delete(obj)
        session.commit()
        return True
