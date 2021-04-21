from dl.entity.base import Session
from dl.entity.reservation import Reservation
from dl.mapper.ireservation import IReservationMapper


class ReservationMapper(IReservationMapper):
    def __init__(self):
        super().__init__(Reservation)

    def get(self, objID):
        return Session.query(Reservation).filter(Reservation.RezervaceID == objID).first()

    def add(self, obj):
        if self.get(obj.RezervaceID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.RezervaceID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
