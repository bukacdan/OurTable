from dl.entity.db_engine import DBEngine
from dl.entity.customer import Customer
from dl.mapper.icustomer import ICustomerMapper


class CustomerMapper(ICustomerMapper):
    def __init__(self):
        pass

    def get_all(self):
        customers = DBEngine.get_session().query(Customer).all()
        return customers

    def get(self, obj_id):
        return DBEngine.get_session().query(Customer).filter(Customer.UzivatelID == obj_id).first()

    def add(self, obj):
        if self.get(obj.UzivatelID):
            return False
        DBEngine.get_session().add(obj)
        DBEngine.get_session().commit()
        return True

    def delete(self, obj):
        if not self.get(obj.UzivatelID):
            return False
        DBEngine.get_session().delete(obj)
        DBEngine.get_session().commit()
        return True
