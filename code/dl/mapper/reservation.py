from dl.entity.base import session
from dl.entity.reservation import Reservation
from dl.mapper.ireservation import IReservationMapper


class ReservationMapper(IReservationMapper):
    def __init__(self):
        pass

    def get_all(self):
        reservations = session.query(Reservation).all()
        return reservations

    def get(self, objID):
        return session.query(Reservation).filter(Reservation.RezervaceID == objID).first()

    def add(self, obj):
        if self.get(obj.RezervaceID):
            return False
        session.add(obj)
        session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.RezervaceID):
            return False
        session.delete(obj)
        session.commit()
        return True

    @staticmethod
    def tmp_add (time, tableID):
        reservation = Reservation (Datumdo = time + datetime.timedelta(hours = 2), Datumod = time)
        reservation.StulID.append(tableID)
        session.add(reservation)
        session.commit()
        return True