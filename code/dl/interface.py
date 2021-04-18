from abc import ABC
from abc import abstractmethod
from typing import List


class Database(ABC):

    @abstractmethod
    def get_tables(self):
        pass

    @abstractmethod
    def add_table(self, spaces: int):
        pass

    @abstractmethod
    def delete_table(self, table_id: int):
        pass

    @abstractmethod
    def get_meals(self):
        pass

    @abstractmethod
    def add_meal(self, price: int, name: str):
        pass

    @abstractmethod
    def delete_meal(self, meal_id: int):
        pass

    @abstractmethod
    def get_reservations(self):
        pass

    @abstractmethod
    def add_reservation(self, since, until, user_id: int, table_ids: List[int]):
        pass

    @abstractmethod
    def delete_reservation(self, reservation_id: int):
        pass

    @abstractmethod
    def add_user(self, email: str, name: str, surname: str, phone_number: str):
        pass

    @abstractmethod
    def add_meal_order(self, meal_id: int, reservation_id: int, count: int):
        pass

    @abstractmethod
    def delete_meal_order(self, order_id: int):
        pass

    @abstractmethod
    def add_menu(self, since: int, until: int, meal_ids: List[int]):
        pass

    @abstractmethod
    def add_allergen(self, number: int, name: str):
        pass

    @abstractmethod
    def add_is_part_of(self, allergen_id: int, meal_id: int):
        pass

    @abstractmethod
    def add_address(self, city: str, postal_code: int, country: str, street: str):
        pass

    @abstractmethod
    def add_schedule(self, table_id: int, since, until, is_available: bool):
        pass
