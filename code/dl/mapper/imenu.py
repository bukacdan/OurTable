from typing import List
from dl.entity.menu import Menu
from .ibase import IBaseMapper


class IMenuMapper(IBaseMapper):
    """
    Interface for MenuMapper
    """

    def get_all() -> List[Menu]:
        """
        Retrieves all menus from database

        Returns
        ----------
        list[Menu]
            List of all menus from database
        """
        pass

    def get(menu_ID: int) -> Menu:
        """
        Retrieves a menu from database

        Parameters
        ----------
        menu_ID: int
            ID of the menu we want to get

        Returns
        ----------
        Menu
            Menu with the specified ID
        """
        pass

    def add(menu: Menu) -> bool:
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

    def delete(menu: Menu) -> bool:
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

