from dl.entity.base import Session
from dl.entity.address import Address
from dl.mapper.iaddress import IAddressMapper


class AddressMapper(IAddressMapper):
    def __init__(self):
        super().__init__(Address)

    def get(self, objID):
        return Session.query(Address).filter(Address.AdresaID == objID).first()

    def add(self, obj):
        if self.get(obj.AdresaID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.AdresaID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
