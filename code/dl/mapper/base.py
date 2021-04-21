from .ibase import IBaseMapper
from dl.entity.base import Session


class BaseMapper(IBaseMapper):
    def __init__(self, item):
        self.item = item

    def get_all(self):
        items = Session.query(self.item).all()
        return items
