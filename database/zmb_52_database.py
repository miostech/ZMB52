from sqlalchemy import create_engine, engine
#from core.model.zmb_52_model import ZMB52
from database import connection_database

import datetime

engine = create_engine(connection_database.connection())
connection = engine.connect()


def return_all():
    """
    return all data from database
    :return:
    """
    with engine.connect() as con:
        rs = con.execute("SELECT * FROM MachineAlarms")
        return rs.fetchall()


return_all()
