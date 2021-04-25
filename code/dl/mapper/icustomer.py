from typing import List
from dl.entity.customer import Customer
from .ibase import IBaseMapper
from abc import abstractmethod


class ICustomerMapper(IBaseMapper):
    """
    Interface for customer mapper
    """

    @abstractmethod
    def get_all(self) -> List[Customer]:
        """
        Retrieves all customers from database

        Returns
        ----------
        list[Customer]
            List of all customers from database
        """
        pass

    @abstractmethod
    def get(self, customer_id: int) -> Customer:
        """
        Retrieves a customer from database with the specified ID

        Parameters
        ----------
        customer_id: int
            ID of the customer to retrieve

        Returns
        ----------
        Customer
            Customer from database with the specified ID
        """
        pass

    @abstractmethod
    def add(self, customer: Customer) -> bool:
        """
        Adds a customer to database

        Parameters
        ----------
        customer: Customer
            Customer to add to database

        Returns
        ----------
        bool
            True on success, False when customer is already in database
        """
        pass

    @abstractmethod
    def delete(self, customer: Customer) -> bool:
        """
        Deletes a customer from database

        Parameters
        ----------
        customer: Customer
            Customer to remove from database

        Returns
        ----------
        bool
            True on success, False when customer is not in database
        """
        pass
