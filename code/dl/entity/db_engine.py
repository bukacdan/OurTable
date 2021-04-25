from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base


class DBEngine():
    '''
    Class encapsulating SQLAlchemy database engine

    This class is a singleton.
    '''
    db_destination = 'postgresql://postgres:postgres@localhost:5432/our_table'
    engine = None
    session = None
    base = None
    valid = False

    @classmethod
    def get_engine(cls):
        '''Retrieve database engine'''
        if not cls.valid:
            cls.__init()
        return cls.engine

    @classmethod
    def get_session(cls):
        '''Retrieve database session'''
        if not cls.valid:
            cls.__init()
        return cls.session

    @classmethod
    def get_base(cls):
        '''Retrieve database base object'''
        if not cls.valid:
            cls.__init()
        return cls.base

    @classmethod
    def __init(cls):
        '''Initialize singleton'''
        cls.__init_engine()
        cls.__init_session()
        cls.__init_base()
        cls.valid = True

    @classmethod
    def __init_engine(cls):
        '''Initialize database engine'''
        cls.engine = create_engine(cls.db_destination)
        cls.connection = cls.engine.connect()

    @classmethod
    def __init_session(cls):
        '''Initialize database session'''
        Session = sessionmaker(bind=cls.engine)
        cls.session = Session()

    @classmethod
    def __init_base(cls):
        '''Initialize database base object'''
        cls.base = automap_base(bind=cls.engine)
        cls.base.prepare(cls.engine, reflect=True)
