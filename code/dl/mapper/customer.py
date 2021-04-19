from .imapper import IMapper
from dl.entity.customer import Customer


class CustomerMapper(IMapper):
    @staticmethod
    def get_all():
        customers = session.query(Customer).all()
        return customers

    @staticmethod
    def get(objID):
        return session.query(Customer).filter(Customer.UzivatelID == objID).first()

    @staticmethod
    def add(obj):
        if CustomerMapper.get(obj.UzivatelID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not CustomerMapper.get(obj.UzivatelID):
            return False
        session.delete(obj)
        session.commit()
        return True
