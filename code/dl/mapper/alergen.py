from .imapper import IMapper
from dl.entity.base import Session
from dl.entity.alergen import Alergen


class AlergenMapper(IMapper):
    @staticmethod
    def get_all():
        alergens = Session.query(Alergen).all()
        return alergens

    @staticmethod
    def get(objID):
        return Session.query(Alergen).filter(Alergen.Cislo == objID).first()

    @staticmethod
    def add(obj):
        if AlergenMapper.get(obj.Cislo):
            return False
        Session.add(obj)
        Session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not AlergenMapper.get(obj.Cislo):
            return False
        Session.delete(obj)
        Session.commit()
        return True
