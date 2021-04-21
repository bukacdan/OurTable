from .ibase import IBase
from dl.entity.base import Session


class Base(IBase):
    def __init__(self, item):
        self.item = item

    def get_all(self):
        items = Session.query(self.item).all()
        return items
