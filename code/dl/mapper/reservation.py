from dl.entity.db_engine import DBEngine
from dl.entity.reservation import Reservation
from dl.mapper.ireservation import IReservationMapper
from dl.mapper.itable import ITableMapper


class ReservationMapper(IReservationMapper):
    def __init__(self):
        pass

    def get_all(self):
        reservations = DBEngine.get_session().query(Reservation).all()
        return reservations

    def get(self, obj_id: int):
        return DBEngine.get_session().query(Reservation).filter(Reservation.RezervaceID == obj_id).first()

    def add(self, reservation: Reservation, tableMapper: ITableMapper, tableID: int):
        if self.get(reservation.RezervaceID):
            return False
        reservation.stul_collection.append(tableMapper.get(tableID))
        DBEngine.get_session().add(reservation)
        DBEngine.get_session().commit()
        return True

    def delete(self, obj: Reservation):
        if not self.get(obj.RezervaceID):
            return False
        DBEngine.get_session().delete(obj)
        DBEngine.get_session().commit()
        return True
