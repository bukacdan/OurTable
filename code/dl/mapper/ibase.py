from abc import ABC, abstractmethod

# Interface class

class IBase(ABC):
    # [@param-return] All objects from specific table in database
    @abstractmethod
    def get_all():
        pass

    # [@param-in] ID of object we want to get from database
    # [@param-return] object from specific table
    @abstractmethod
    def get(objID):
        pass

    # [@param-in] new object for database
    # [@param-return] True at success, False when object is already in database
    @abstractmethod
    def add(obj):
        pass

    # [@param-in] old object for removal
    # [@param-out] True at success, False when object is not in database
    @abstractmethod
    def delete(obj):
        pass
