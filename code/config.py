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

from injector import singleton

# TODO: change this
SECRET_KEY = b'\xda\xf3nN7\x7f;\xef\x9a\xb1FX\x8c\xf4\x91\xe4'


def configure(binder):
    binder.bind(Address, to=AddressMapper, scope=singleton)
    binder.bind(Alergen, to=AlergenMapper, scope=singleton)
    binder.bind(Customer, to=CustomerMapper, scope=singleton)
    binder.bind(Meal, to=MealMapper, scope=singleton)
    binder.bind(Menu, to=MenuMapper, scope=singleton)
    binder.bind(Reservation, to=ReservationMapper, scope=singleton)
    binder.bind(Schedule, to=ScheduleMapper, scope=singleton)
    binder.bind(Table, to=TableMapper, scope=singleton)
