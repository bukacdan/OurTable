from .imapper import IMapper
from dl.entity.base import Session
from dl.entity.customer import Customer


class CustomerMapper(IMapper):
    @staticmethod
    def get_all():
        customers = Session.query(Customer).all()
        return customers

    @staticmethod
    def get(objID):
        return Session.query(Customer).filter(Customer.UzivatelID == objID).first()

    @staticmethod
    def add(obj):
        if CustomerMapper.get(obj.UzivatelID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not CustomerMapper.get(obj.UzivatelID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
