from dl.mapper.address import AddressMapper
from dl.mapper.alergen import AlergenMapper
from dl.mapper.customer import CustomerMapper
from dl.mapper.meal import MealMapper
from dl.mapper.meal_order import MealOrderMapper
from dl.mapper.menu import MenuMapper
from dl.mapper.reservation import ReservationMapper
from dl.mapper.schedule import ScheduleMapper
from dl.mapper.table import TableMapper

from dl.mapper.iaddress import IAddress
from dl.mapper.ialergen import IAlergen
from dl.mapper.icustomer import ICustomer
from dl.mapper.imeal import IMeal
from dl.mapper.imeal_order import IMealOrder
from dl.mapper.imenu import IMenu
from dl.mapper.ireservation import IReservation
from dl.mapper.ischedule import ISchedule
from dl.mapper.itable import ITable

from injector import singleton


def configure(binder):
    binder.bind(IAddress, to=AddressMapper, scope=singleton)
    binder.bind(IAlergen, to=AlergenMapper, scope=singleton)
    binder.bind(ICustomer, to=CustomerMapper, scope=singleton)
    binder.bind(IMeal, to=MealMapper, scope=singleton)
    binder.bind(IMealOrder, to=MealOrderMapper, scope=singleton)
    binder.bind(IMenu, to=MenuMapper, scope=singleton)
    binder.bind(IReservation, to=ReservationMapper, scope=singleton)
    binder.bind(ISchedule, to=ScheduleMapper, scope=singleton)
    binder.bind(ITable, to=TableMapper, scope=singleton)
