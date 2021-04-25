from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base


class DBEngine():
    db_string = 'postgresql://postgres:postgres@localhost:5432/our_table'
    engine = None
    session = None
    base = None
    valid = False

    @classmethod
    def get_engine(cls):
        if not cls.valid:
            cls.__init()
        return cls.engine

    @classmethod
    def get_session(cls):
        if not cls.valid:
            cls.__init()
        return cls.session

    @classmethod
    def get_base(cls):
        if not cls.valid:
            cls.__init()
        return cls.base

    @classmethod
    def __init(cls):
        cls.__init_engine()
        cls.__init_session()
        cls.__init_base()

    @classmethod
    def __init_engine(cls):
        cls.engine = create_engine(cls.db_string)
        cls.connection = cls.engine.connect()

    @classmethod
    def __init_session(cls):
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    @classmethod
    def __init_base(cls):
        cls.base = automap_base(bind=cls.engine)
        cls.base.prepare(cls.engine, reflect=True)
