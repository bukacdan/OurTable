from dl.entity.base import session
from dl.entity.customer import Customer
from dl.mapper.icustomer import ICustomerMapper


class CustomerMapper(ICustomerMapper):
    def __init__(self):
        super().__init__(Customer)

    def get(self, objID):
        return session.query(Customer).filter(Customer.UzivatelID == objID).first()

    def add(self, obj):
        if self.get(obj.UzivatelID):
            return False
        session.add(obj)
        session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.UzivatelID):
            return False
        session.delete(obj)
        session.commit()
        return True
