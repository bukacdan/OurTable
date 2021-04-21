from dl.entity.base import session
from dl.entity.schedule import Schedule
from dl.mapper.ischedule import IScheduleMapper


class ScheduleMapper(IScheduleMapper):
    def __init__(self):
        super().__init__(Schedule)

    def get(self, objID):
        return session.query(Schedule).filter(Schedule.RozvrhID == objID).first()

    def add(self, obj):
        if self.get(obj.RozvrhID):
            return False
        session.add(obj)
        session.commit()
        return True

    def delete(self, obj):
        if not self.get(obj.RozvrhID):
            return False
        session.delete(obj)
        session.commit()
        return True
