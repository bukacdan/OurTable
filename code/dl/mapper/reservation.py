from .imapper import IMapper
from dl.entity.reservation import Reservation


class ReservationMapper(IMapper):
    @staticmethod
    def get_all():
        reservations = session.query(Reservation).all()
        return reservations

    @staticmethod
    def get(objID):
        return session.query(Reservation).filter(Reservation.RezervaceID == objID).first()

    @staticmethod
    def add(obj):
        if ReservationMapper.get(obj.RezervaceID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not ReservationMapper.get(obj.RezervaceID):
            return False
        session.delete(obj)
        session.commit()
        return True
