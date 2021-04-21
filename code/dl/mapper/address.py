from dl.entity.base import session
from dl.entity.address import Address
from dl.mapper.iaddress import IAddressMapper


class AddressMapper(IAddressMapper):
    def __init__(self):
        pass

    def get_all(self):
        addresses = session.query(Address).all()
        return addresses

    def get(self, objID):
        return session.query(Address).filter(Address.AdresaID == objID).first()

    def add(self, obj):
        if self.get(obj.AdresaID):
            return False
        session.add(obj)
        session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.AdresaID):
            return False
        session.delete(obj)
        session.commit()
        return True
