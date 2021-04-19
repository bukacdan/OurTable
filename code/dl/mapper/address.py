from .imapper import IMapper
from dl.entity.base import Session
from dl.entity.address import Address


class AddressMapper(IMapper):
    @staticmethod
    def get_all():
        addresses = Session.query(Address).all()
        return addresses

    @staticmethod
    def get(objID):
        return Session.query(Address).filter(Address.AdresaID == objID).first()

    @staticmethod
    def add(obj):
        if AddressMapper.get(obj.AdresaID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not AddressMapper.get(obj.AdresaID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
