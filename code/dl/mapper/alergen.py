from dl.entity.base import session
from dl.entity.alergen import Alergen
from dl.mapper.ialergen import IAlergenMapper


class AlergenMapper(IAlergenMapper):
    def __init__(self):
        pass

    def get_all(self):
        alergens = session.query(Alergen).all()
        return alergens

    def get(self, objID):
        return session.query(Alergen).filter(Alergen.Cislo == objID).first()

    def add(self, obj):
        if self.get(obj.Cislo):
            return False
        session.add(obj)
        session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.Cislo):
            return False
        session.delete(obj)
        session.commit()
        return True
