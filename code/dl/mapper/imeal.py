from typing import List
from .ibase import IBaseMapper
from dl.entity.meal import Meal


class IMealMapper(IBaseMapper):
    """
    Interface for MealMapper
    """

    def get_all() -> List[Meal]:
        """
        Retrieves all meals from database

        Returns
        ----------
        list[Meal]
            List of all meals from database
        """
        pass

    def get(meal_ID: int) -> Meal:
        """
        Retrieves a meal from database

        Parameters
        ----------
        meal_ID: int
            ID of the meal we want to get

        Returns
        ----------
        Meal
            Meal with the specified ID
        """
        pass

    def add(meal: Meal) -> bool:
        """
        Adds a meal to database

        Parameters
        ----------
        meal: Meal
            Meal to add to database

        Returns
        ----------
        bool
            True on success, False when meal is already in database
        """
        pass

    def delete(meal: Meal) -> bool:
        """
        Deletes a meal from the database

        Parameters
        ----------
        meal: Meal
            Meal to delete

        Returns
        ----------
        bool
            True on success, False when meal is not in database
        """
        pass
