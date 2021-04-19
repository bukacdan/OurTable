from .imapper import IMapper
from dl.entity.address import Address


class AddressMapper(IMapper):
    @staticmethod
    def get_all():
        addresses = session.query(Address).all()
        return addresses

    @staticmethod
    def get(objID):
        return session.query(Address).filter(Address.AdresaID == objID).first()

    @staticmethod
    def add(obj):
        if AddressMapper.get(obj.AdresaID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not AddressMapper.get(obj.AdresaID):
            return False
        session.delete(obj)
        session.commit()
        return True
