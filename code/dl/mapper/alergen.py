from .imapper import IMapper
from dl.entity.base import session
from dl.entity.alergen import Alergen


class AlergenMapper(IMapper):
    @staticmethod
    def get_all():
        alergens = session.query(Alergen).all()
        return alergens

    @staticmethod
    def get(objID):
        return session.query(Alergen).filter(Alergen.Cislo == objID).first()

    @staticmethod
    def add(obj):
        if AlergenMapper.get(obj.Cislo):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not AlergenMapper.get(obj.Cislo):
            return False
        session.delete(obj)
        session.commit()
        return True
