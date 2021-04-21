from typing import List

from .database_interface import DatabaseInterface

from dl.entity.address import Address
from dl.entity.alergen import Alergen
from dl.entity.customer import Customer
from dl.entity.meal import Meal
from dl.entity.meal_order import MealOrder
from dl.entity.menu import Menu
from dl.entity.reservation import Reservation
from dl.entity.schedule import Schedule
from dl.entity.table import Table

from dl.mapper.address import AddressMapper
from dl.mapper.alergen import AlergenMapper
from dl.mapper.customer import CustomerMapper
from dl.mapper.meal import MealMapper
from dl.mapper.meal_order import MealOrderMapper
from dl.mapper.menu import MenuMapper
from dl.mapper.reservation import ReservationMapper
from dl.mapper.schedule import ScheduleMapper
from dl.mapper.table import TableMapper

from dl.entity.base import session


class PostgreSQLDatabase(DatabaseInterface):
    def get_tables(self):
        return TableMapper.get_all()

    def add_table(self, spaces: int):
        table = Table()
        print('id: ', table.StulID)
        table.Pocetmist = spaces
        return TableMapper.add(table)

    def delete_table(self, table_id: int):
        table = TableMapper.get(table_id)
        if not table:
            return False
        return TableMapper.delete(table)

    def get_meals(self):
        return MealMapper.get_all()

    def add_meal(self, price: int, name: str):
        meal = Meal()
        meal.Cena = price
        meal.Nazev = name
        return MealMapper.add(meal)

    def delete_meal(self, meal_id: int):
        meal = MealMapper.get(meal_id)
        if not meal:
            return False
        return MealMapper.delece(meal)

    def get_reservations(self):
        return ReservationMapper.get_all()

    def add_reservation(self, since, until, user_id: int, table_ids: List[int]):
        reservation = Reservation()
        reservation.Datumod = since
        reservation.Datumdo = until
        reservation.UzivatelID = user_id
        return ReservationMapper.add(reservation)

    def delete_reservation(self, reservation_id: int):
        reservation = ReservationMapper.get(reservation_id)
        if not reservation:
            return False
        return ReservationMapper.delete(reservation)

    def add_user(self, email: str, name: str, surname: str, phone_number: str):
        customer = Customer()
        customer.Email = email
        customer.Jmeno = name
        customer.Prijmeni = surname
        customer.Telefon = phone_number
        return CustomerMapper.add(customer)

    def add_meal_order(self, meal_id: int, reservation_id: int, count: int):
        order = MealOrder()
        order.JidloID = meal_id
        # TODO je soucasti

    def delete_meal_order(self, order_id: int):
        order = MealOrderMapper.get(order_id)
        if not order:
            return False
        return CustomerMapper.delete(order)

    def add_menu(self, since: int, until: int, meal_ids: List[int]):
        menu = Menu()
        menu.Platnostod = since
        menu.Platnostdo = until
        # TODO obsahuje
        return MealMapper.add(menu)

    def add_allergen(self, number: int, name: str):
        allergen = Alergen()
        allergen.Cislo = number
        allergen.Nazev = name
        return AlergenMapper.add(allergen)

    def add_is_part_of(self, allergen_id: int, meal_id: int):
        # TODO missing mapper
        pass

    def add_address(self, city: str, postal_code: int, country: str, street: str):
        address = Address()
        address.Mesto = city
        address.Psc = postal_code
        address.Stat = country
        address.Ulice = street
        return AddressMapper.add(address)

    def add_schedule(self, table_id: int, since, until, is_available: bool):
        schedule = Schedule()
        schedule.StulID = table_id
        schedule.Datumod = since
        schedule.Datumdo = until
        schedule.Jedostupny = is_available
        return ScheduleMapper.add(schedule)
