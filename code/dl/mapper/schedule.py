from .imapper import IMapper
from dl.entity.base import session
from dl.entity.schedule import Schedule


class ScheduleMapper(IMapper):
    @staticmethod
    def get_all():
        schedules = session.query(Schedule).all()
        return schedules

    @staticmethod
    def get(objID):
        return session.query(Schedule).filter(Schedule.RozvrhID == objID).first()

    @staticmethod
    def add(obj):
        if ScheduleMapper.get(obj.RozvrhID):
            return False
        session.add(obj)
        session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not ScheduleMapper.get(obj.RozvrhID):
            return False
        session.delete(obj)
        session.commit()
        return True
