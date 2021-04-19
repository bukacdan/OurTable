from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.automap import automap_base

db_string = 'postgresql://postgres:postgres@localhost:5432/our_table'
engine = create_engine(db_string)
connection = engine.connect()

Session = sessionmaker(bind=engine)
session = Session()
Base = automap_base(bind=engine)
Base.prepare(engine, reflect=True)
