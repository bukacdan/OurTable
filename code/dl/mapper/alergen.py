from dl.entity.base import Session
from dl.entity.alergen import Alergen
from dl.mapper.ialergen import IAlergenMapper


class AlergenMapper(IAlergenMapper):
    def __init__(self):
        super().__init__(Alergen)

    def get(self, objID):
        return Session.query(Alergen).filter(Alergen.Cislo == objID).first()

    def add(self, obj):
        if self.get(obj.Cislo):
            return False
        Session.add(obj)
        Session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.Cislo):
            return False
        Session.delete(obj)
        Session.commit()
        return True
