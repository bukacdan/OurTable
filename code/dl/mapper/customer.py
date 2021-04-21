from .base import Base
from dl.entity.base import Session
from dl.entity.customer import Customer


class CustomerMapper(Base):
    def __init__(self):
        super().__init__(Customer)

    def get(self, objID):
        return Session.query(Customer).filter(Customer.UzivatelID == objID).first()

    def add(self, obj):
        if self.get(obj.UzivatelID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.UzivatelID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
