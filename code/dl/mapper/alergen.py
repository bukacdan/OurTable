from dl.entity.db_engine import DBEngine
from dl.entity.alergen import Alergen
from dl.mapper.ialergen import IAlergenMapper


class AlergenMapper(IAlergenMapper):
    def __init__(self):
        pass

    def get_all(self):
        alergens = DBEngine.get_session().query(Alergen).all()
        return alergens

    def get(self, obj_id):
        return DBEngine.get_session().query(Alergen).filter(Alergen.Cislo == obj_id).first()

    def add(self, obj):
        if self.get(obj.Cislo):
            return False
        DBEngine.get_session().add(obj)
        DBEngine.get_session().commit()
        return True

    def delete(self, obj):
        if not self.get(obj.Cislo):
            return False
        DBEngine.get_session().delete(obj)
        DBEngine.get_session().commit()
        return True
