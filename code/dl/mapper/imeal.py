from typing import List
from .ibase import IBaseMapper
from dl.entity.meal import Meal
from abc import abstractmethod


class IMealMapper(IBaseMapper):
    """
    Interface for MealMapper
    """

    @abstractmethod
    def get_all(self) -> List[Meal]:
        """
        Retrieves all meals from database

        Returns
        ----------
        list[Meal]
            List of all meals from database
        """
        pass

    @abstractmethod
    def get(self, meal_id: int) -> Meal:
        """
        Retrieves a meal from database

        Parameters
        ----------
        meal_id: int
            ID of the meal we want to get

        Returns
        ----------
        Meal
            Meal with the specified ID
        """
        pass

    @abstractmethod
    def add(self, meal: Meal) -> bool:
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

    @abstractmethod
    def delete(self, meal: Meal) -> bool:
        """
        Deletes a meal from database

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
