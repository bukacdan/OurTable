from dl.entity.db_engine import DBEngine
from dl.entity.reservation import Reservation
from dl.mapper.ireservation import IReservationMapper


class ReservationMapper(IReservationMapper):
    def __init__(self):
        pass

    def get_all(self):
        reservations = DBEngine.get_session().query(Reservation).all()
        return reservations

    def get(self, obj_id):
        return DBEngine.get_session().query(Reservation).filter(Reservation.RezervaceID == obj_id).first()

    def add(self, obj):
        if self.get(obj.RezervaceID):
            return False
        DBEngine.get_session().add(obj)
        DBEngine.get_session().commit()
        return True

    def delete(self, obj):
        if not self.get(obj.RezervaceID):
            return False
        DBEngine.get_session().delete(obj)
        DBEngine.get_session().commit()
        return True

    @staticmethod
    def tmp_add (time, tableID):
        reservation = Reservation (Datumdo = time + datetime.timedelta(hours = 2), Datumod = time)
        reservation.StulID.append(tableID)
        DBEngine.get_session().add(reservation)
        DBEngine.get_session().commit()
        return True
