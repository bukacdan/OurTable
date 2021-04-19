from .imapper import IMapper
from dl.entity.base import Session
from dl.entity.reservation import Reservation


class ReservationMapper(IMapper):
    @staticmethod
    def get_all():
        reservations = Session.query(Reservation).all()
        return reservations

    @staticmethod
    def get(objID):
        return Session.query(Reservation).filter(Reservation.RezervaceID == objID).first()

    @staticmethod
    def add(obj):
        if ReservationMapper.get(obj.RezervaceID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not ReservationMapper.get(obj.RezervaceID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
