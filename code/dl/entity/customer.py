from .db_engine import DBEngine


# This is not a global parameter, but an automatically created class
Customer = DBEngine.get_base().classes.Uzivatel
