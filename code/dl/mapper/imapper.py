from abc import ABC, abstractstaticmethod

# Interface class

class IMapper(ABC):
    # [@param-return] All objects from specific table in database
    @abstractstaticmethod
    def get_all():
        pass

    # [@param-in] ID of object we want to get from database
    # [@param-return] object from specific table
    @abstractstaticmethod
    def get(objID):
        pass

    # [@param-in] new object for database
    # [@param-return] True at success, False when object is already in database
    @abstractstaticmethod
    def add(obj):
        pass

    # [@param-in] old object for removal
    # [@param-out] True at success, False when object is not in database
    @abstractstaticmethod
    def delete(obj):
        pass
