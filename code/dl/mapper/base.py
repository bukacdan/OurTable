from .ibase import IBaseMapper
from dl.entity.base import session


class BaseMapper(IBaseMapper):
    def __init__(self, item):
        self.item = item

    def get_all(self):
        items = session.query(self.item).all()
        return items
