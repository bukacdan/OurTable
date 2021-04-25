from dl.entity.db_engine import DBEngine
from dl.entity.schedule import Schedule
from dl.mapper.ischedule import IScheduleMapper


class ScheduleMapper(IScheduleMapper):
    def __init__(self):
        pass

    def get_all(self):
        schedules = DBEngine.get_session().query(Schedule).all()
        return schedules

    def get(self, obj_id):
        return DBEngine.get_session().query(Schedule).filter(Schedule.RozvrhID == obj_id).first()

    def add(self, obj):
        if self.get(obj.RozvrhID):
            return False
        DBEngine.get_session().add(obj)
        DBEngine.get_session().commit()
        return True

    def delete(self, obj):
        if not self.get(obj.RozvrhID):
            return False
        DBEngine.get_session().delete(obj)
        DBEngine.get_session().commit()
        return True

    def filter_on_date(self, since, until, availability):
        #schedules = DBEngine.get_session().query(Schedule).filter(
        #    Schedule.Datumod <= since,
        #    Schedule.Datumdo >= until,
        #    Schedule.Jedostupny == availability).all()
        alls = DBEngine().get_session().query(Schedule).all()
        schedules = []
        for s in alls:
            if s.Datumdo <= since and s.Datumod >= until and s.Jedostupny == availability:
                schedules.add(s)

        return schedules
