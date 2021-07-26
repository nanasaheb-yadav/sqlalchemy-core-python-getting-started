from sqlalchemy import create_engine
from sqlalchemy import *
engine = create_engine('sqlite:///heroes.db')
connection = engine.connect()

"""query = "SELECT * FROM Heroes;"
result = connection.execute(query)
result = result.fetchall()
print(result)
"""
metadata = MetaData()
heroes_table = Table('heroes', metadata,
                     Column('hero_id', Integer, nullable=False, primary_key=True),
                     Column('name', String(20), nullable=False, unique=True))

from sqlalchemy.sql import select

query = select([heroes_table])
result = connection.execute(query)
print(result.fetchall())
