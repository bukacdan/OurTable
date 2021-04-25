from dl.entity.db_engine import DBEngine
from dl.entity.address import Address
from dl.mapper.iaddress import IAddressMapper


class AddressMapper(IAddressMapper):
    def __init__(self):
        pass

    def get_all(self):
        addresses = DBEngine.get_session().query(Address).all()
        return addresses

    def get(self, obj_id: int):
        return DBEngine.get_session().query(Address).filter(Address.AdresaID == obj_id).first()

    def add(self, obj: Address):
        if self.get(obj.AdresaID):
            return False
        DBEngine.get_session().add(obj)
        DBEngine.get_session().commit()
        return True

    def delete(self, obj: Address):
        if not self.get(obj.AdresaID):
            return False
        DBEngine.get_session().delete(obj)
        DBEngine.get_session().commit()
        return True
