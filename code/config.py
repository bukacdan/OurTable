from dl.mapper.address import AddressMapper
from dl.mapper.alergen import AlergenMapper
from dl.mapper.customer import CustomerMapper
from dl.mapper.meal import MealMapper
from dl.mapper.meal_order import MealOrderMapper
from dl.mapper.menu import MenuMapper
from dl.mapper.reservation import ReservationMapper
from dl.mapper.schedule import ScheduleMapper
from dl.mapper.table import TableMapper

from dl.mapper.iaddress import IAddressMapper
from dl.mapper.ialergen import IAlergen
from dl.mapper.icustomer import ICustomer
from dl.mapper.imeal import IMealMapper
from dl.mapper.imeal_order import IMealOrderMapper
from dl.mapper.imenu import IMenuMapper
from dl.mapper.ireservation import IReservationMapper
from dl.mapper.ischedule import IScheduleMapper
from dl.mapper.itable import ITableMapper

from injector import singleton


def configure(binder):
    binder.bind(IAddressMapper, to=AddressMapper, scope=singleton)
    binder.bind(IAlergenMapper, to=AlergenMapper, scope=singleton)
    binder.bind(ICustomerMapper, to=CustomerMapper, scope=singleton)
    binder.bind(IMealMapperMapper, to=MealMapper, scope=singleton)
    binder.bind(IMealOrderMapper, to=MealOrderMapper, scope=singleton)
    binder.bind(IMenuMapper, to=MenuMapper, scope=singleton)
    binder.bind(IReservationMapper, to=ReservationMapper, scope=singleton)
    binder.bind(IScheduleMapper, to=ScheduleMapper, scope=singleton)
    binder.bind(ITableMapper, to=TableMapper, scope=singleton)
