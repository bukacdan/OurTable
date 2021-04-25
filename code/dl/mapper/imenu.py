from typing import List
from dl.entity.menu import Menu
from .ibase import IBaseMapper
from abc import abstractmethod


class IMenuMapper(IBaseMapper):
    """
    Interface for MenuMapper
    """

    @abstractmethod
    def get_all(self) -> List[Menu]:
        """
        Retrieves all menus from database

        Returns
        ----------
        list[Menu]
            List of all menus from database
        """
        pass

    @abstractmethod
    def get(self, menu_id: int) -> Menu:
        """
        Retrieves a menu from database

        Parameters
        ----------
        menu_id: int
            ID of the menu we want to get

        Returns
        ----------
        Menu
            Menu with the specified ID
        """
        pass

    @abstractmethod
    def add(self, menu: Menu) -> bool:
        """
        Adds a menu to database

        Parameters
        ----------
        menu: Menu
            Menu to add to database

        Returns
        ----------
        bool
            True on success, False when menu is already in database
        """
        pass

    @abstractmethod
    def delete(self, menu: Menu) -> bool:
        """
        Deletes a menu from database

        Parameters
        ----------
        menu: Menu
            Menu to delete

        Returns
        ----------
        bool
            True on success, False when menu is not in database
        """
        pass
