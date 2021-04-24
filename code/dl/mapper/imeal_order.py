from typing import List
from .ibase import IBaseMapper
from dl.entity.meal_order import MealOrder


class IMealOrderMapper(IBaseMapper):
    """
    Interface for MealOrderMapper
    """

    def get_all() -> List[MealOrder]:
        """
        Retrieves all meal orders from database

        Returns
        ----------
        list[MealOrder]
            List of all meal orders from database
        """
        pass

    def get(meal_order_id: int) -> MealOrder:
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

    def add(meal_order: MealOrder) -> bool:
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

    def delete(meal_order: MealOrder) -> bool:
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
