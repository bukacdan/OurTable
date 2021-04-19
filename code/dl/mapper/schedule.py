from .imapper import IMapper
from dl.entity.base import Session
from dl.entity.schedule import Schedule


class ScheduleMapper(IMapper):
    @staticmethod
    def get_all():
        schedules = Session.query(Schedule).all()
        return schedules

    @staticmethod
    def get(objID):
        return Session.query(Schedule).filter(Schedule.RozvrhID == objID).first()

    @staticmethod
    def add(obj):
        if ScheduleMapper.get(obj.RozvrhID):
            return False
        Session.add(obj)
        Session.commit()
        return True

    @staticmethod
    def delete(obj):
        if not ScheduleMapper.get(obj.RozvrhID):
            return False
        Session.delete(obj)
        Session.commit()
        return True
