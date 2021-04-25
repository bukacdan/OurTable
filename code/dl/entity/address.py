from .db_engine import DBEngine


# This is not a global parameter, but an automatically created class
Address = DBEngine.get_base().classes.Adresa
