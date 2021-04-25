from typing import List
from .ibase import IBaseMapper
from dl.entity.meal_order import MealOrder
from abc import abstractmethod


class IMealOrderMapper(IBaseMapper):
    """
    Interface for MealOrderMapper
    """

    @abstractmethod
    def get_all(self) -> List[MealOrder]:
        """
        Retrieves all meal orders from database

        Returns
        ----------
        list[MealOrder]
            List of all meal orders from database
        """
        pass

    @abstractmethod
    def get(self, meal_order_id: int) -> MealOrder:
        """
        Retrieves a meal order from database

        Parameters
        ----------
        meal_order_id: int
            ID of the meal order we want to get

        Returns
        ----------
        MealOrder
            Meal order with the specified ID
        """
        pass

    @abstractmethod
    def add(self, meal_order: MealOrder) -> bool:
        """
        Adds a meal order to database

        Parameters
        ----------
        meal_order: MealOrder
            Meal order to add to database

        Returns
        ----------
        bool
            True on success, False when meal order is already in database
        """
        pass

    @abstractmethod
    def delete(self, meal_order: MealOrder) -> bool:
        """
        Deletes a meal order from database

        Parameters
        ----------
        meal_order: MealOrder
            Meal order to delete

        Returns
        ----------
        bool
            True on success, False when meal order is not in database
        """
        pass
